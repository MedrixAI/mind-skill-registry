---
name: bio-figure-builder
description: Design and generate traceable biomedical figures from supplied measurements or analysis results. Use for single-cell embeddings, volcano plots, heatmaps, pathway figures, or other research charts with verifiable data and annotations.
license: MIT
metadata:
  mind.id: ai.medrix.skill.builtin.bio-figure-builder
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.tags: '["bioinformatics", "visualization", "figures"]'
  mind.upstream.repo: https://github.com/GPTomics/bioSkills
  mind.upstream.commit: d91ed3d563019e649dc854c56ccd62551359488a
  mind.upstream.path: data-visualization/volcano-and-ma-plots
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://github.com/GPTomics/bioSkills/blob/d91ed3d563019e649dc854c56ccd62551359488a/LICENSE", "https://github.com/GPTomics/bioSkills/blob/d91ed3d563019e649dc854c56ccd62551359488a/data-visualization/volcano-and-ma-plots/SKILL.md"]'
---

# Biomedical figure builder

Produce or specify a scientific figure grounded in user-supplied data and a verified analysis. Choose the chart from the question and data, not the desired visual style. Do not invent observations, statistics, axes or biological conclusions.

## Inputs and safeguards

Ask for the question, data and provenance, observation/replicate unit, groups, axis units, statistical columns or analysis results, chart format and audience. Check sample and feature alignment, missing values, duplicates, scales, reference versions and permissions. Confirm whether an embedding, differential-expression table or pathway results are already computed. If inputs or an authorized plotting environment are missing, offer a labeled design specification rather than claiming a figure was generated. Do not silently install software, transmit data or overwrite source files.

## Figure selection and validation

1. For single-cell embeddings, verify coordinates, cell labels and sample metadata share barcodes. State that proximity and visual separation in UMAP/t-SNE are exploratory; show sample/donor composition where needed and do not infer significance from the plot.
2. For a volcano plot, require an effect-size column and a documented raw or adjusted p-value column; label which is plotted, define thresholds and record the comparison direction. Treat missing p-values explicitly, never replace them with zero; handle exact zeros or underflow with a disclosed plotting floor. Show whether fold changes are shrunk and avoid inferring significance from effect size alone.
3. For heatmaps, document input transformation, scaling, clustering method, feature selection and sample identity; do not imply distances across independently scaled rows are directly comparable. For pathway plots, include tested background, adjusted significance and supporting genes from the actual analysis.
4. Generate accessible labels, units, legends and readable colors; state the number and kind of biological replicates when available. Record data source, software versions, code/parameters, filters and output file paths. Verify that the plotted table matches the figure and that its caption accurately describes the statistical method and uncertainty.
5. Export a suitable editable/vector and/or raster artifact only when actually generated. If evidence or plot data are incomplete, state the exact gap. Never manufacture p-values, replicate numbers, cell labels, data or figure outputs.
