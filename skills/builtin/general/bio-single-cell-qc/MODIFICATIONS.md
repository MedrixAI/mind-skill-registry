# Modifications from upstream

Source: GPTomics/bioSkills, `single-cell/preprocessing`, commit `d91ed3d563019e649dc854c56ccd62551359488a` (MIT).

This is a curated, substantially rewritten subset focused on input intake, sample-level quality control and readiness reporting. It draws on the upstream emphasis on tissue-aware mitochondrial QC, sample-specific thresholds, ambient RNA and doublets. It deliberately omits upstream normalization, feature selection, Scanpy/Seurat code examples, bundled scripts, and links to other upstream skill packages: those are outside this pilot's scope and are not supplied. It adds explicit checks for input provenance, biological replicates, raw-count identity, execution evidence, and safe treatment of original data. Registry metadata and this notice are added for Mind integration.

The upstream MIT copyright and license are retained in `LICENSE`. This adaptation has not been validated on a biological dataset or reviewed for production scientific use.
