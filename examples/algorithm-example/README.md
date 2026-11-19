# HBM SSEC RS decoder flow example

The Mermaid source (\`ssec_decoder_flow.mmd\`) and rendered SVG/PDF/PNG (\`ssec_decoder_flow.*\`)
summarize the RS(19,17) single-symbol error-correction approach described by Kwon et al.,
IEEE TVLSI 2026, Figures 4–6. The flow shows the restricted comparison-based error-location
search and limited-set constant multiplication for error magnitude.

This is an original summary, not a reproduction of the paper's figure. The source paper does not
make all implementation-specific no-error, invalid-syndrome, or bypass behavior explicit in the
shown flow. Confirm those cases against the complete RTL/specification before treating this as a
complete decoder specification.
