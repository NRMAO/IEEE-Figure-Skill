# Figure preflight profiles

ieee-baseline.json is a configurable screening profile based on public IEEE Author Center guidance. It is not an official universal IEEE rule set and does not replace the target journal/conference's current instructions.

To create a venue-specific profile:

1. Copy ieee-baseline.json to a new file named for the target journal or conference.
2. Check the target venue's current author instructions.
3. Update accepted formats, dimensions, resolution, font guidance, and other settings that the venue explicitly specifies.
4. Keep the official source URL and the date you verified the requirements.
5. Run the preflight tool with --profile path/to/venue-profile.json.

The color-distance, grayscale-luminance, text-contrast, and minimum-font thresholds in the baseline are screening heuristics, not IEEE-mandated acceptance thresholds.
