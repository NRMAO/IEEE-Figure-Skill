"""Browser-backed SVG text geometry checks using Chromium via Playwright."""
from __future__ import annotations

from pathlib import Path
from typing import Any


JS_INSPECT = r"""
(targetWidthIn) => {
  const svg = document.querySelector('svg');
  if (!svg) return {error: 'No root <svg> element found.'};
  const vb = svg.viewBox && svg.viewBox.baseVal;
  if (!vb || !vb.width || !vb.height) {
    return {error: 'SVG has no usable viewBox; reliable transformed text-boundary checks are unavailable.'};
  }
  const rootScreen = svg.getScreenCTM();
  if (!rootScreen) return {error: 'Could not obtain the root SVG transformation matrix.'};
  const screenToRoot = rootScreen.inverse();
  const texts = Array.from(svg.querySelectorAll('text'));
  const items = [];
  for (const el of texts) {
    const style = getComputedStyle(el);
    if (style.display === 'none' || style.visibility === 'hidden') continue;
    const content = (el.textContent || '').replace(/\s+/g, ' ').trim();
    if (!content) continue;
    let b;
    let m;
    try {
      b = el.getBBox();
      m = el.getScreenCTM();
    } catch (e) { continue; }
    if (!m) continue;
    const corners = [
      [b.x, b.y], [b.x + b.width, b.y],
      [b.x, b.y + b.height], [b.x + b.width, b.y + b.height]
    ].map(([x, y]) => {
      const screen = new DOMPoint(x, y).matrixTransform(m);
      return screen.matrixTransform(screenToRoot);
    });
    const xs = corners.map(p => p.x);
    const ys = corners.map(p => p.y);
    const fontPx = parseFloat(style.fontSize) || 0;
    const fontPt = targetWidthIn ? fontPx * 72 * targetWidthIn / vb.width : null;
    items.push({
      text: content,
      x1: Math.min(...xs), y1: Math.min(...ys),
      x2: Math.max(...xs), y2: Math.max(...ys),
      font_size_css_px: fontPx,
      font_size_pt_at_target_width: fontPt
    });
  }
  return {
    viewBox: {x: vb.x, y: vb.y, width: vb.width, height: vb.height},
    textCount: items.length,
    texts: items
  };
}
"""


def inspect_svg_text(path: str | Path, target_width_in: float | None = None) -> dict[str, Any]:
    """Return text bounding boxes in root SVG viewBox coordinates.

    This is a rendered-browser check, not a static XML guess. It still cannot guarantee
    identical layout in every publisher's rendering engine or with unavailable web fonts.
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:  # pragma: no cover - environment dependent
        raise RuntimeError("Playwright is not installed. Install with: pip install -e '.[browser]' and playwright install chromium") from exc

    svg_text = Path(path).read_text(encoding="utf-8-sig")
    start = svg_text.find("<svg")
    end = svg_text.rfind("</svg>")
    if start < 0 or end < 0:
        raise ValueError("Could not locate a complete <svg>...</svg> root element.")
    markup = svg_text[start : end + len("</svg>")]
    html = "<!doctype html><html><head><meta charset='utf-8'><style>html,body{margin:0;padding:0;background:#fff}svg{display:block}</style></head><body>" + markup + "</body></html>"

    with sync_playwright() as p:
        launch_args: dict[str, Any] = {"headless": True}
        system_chromium = Path("/usr/bin/chromium")
        if system_chromium.exists():
            launch_args["executable_path"] = str(system_chromium)
            launch_args["args"] = ["--no-sandbox"]
        browser = p.chromium.launch(**launch_args)
        try:
            page = browser.new_page(viewport={"width": 1800, "height": 1400}, device_scale_factor=1)
            page.set_content(html, wait_until="load")
            page.evaluate("() => document.fonts.ready")
            return page.evaluate(JS_INSPECT, target_width_in)
        finally:
            browser.close()
