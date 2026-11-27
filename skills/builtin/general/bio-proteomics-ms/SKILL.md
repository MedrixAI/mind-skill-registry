---
name: bio-proteomics-ms
description: Assess and analyze quantitative mass-spectrometry proteomics data with sample-aware quality control and differential protein abundance analysis. Use for bottom-up LC-MS/MS protein or peptide quantification, including label-free, DIA, DDA or isobaric-label experiments.
license: Apache-2.0
metadata:
  mind.id: ai.medrix.skill.builtin.bio-proteomics-ms
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.tags: '["bioinformatics", "proteomics", "mass-spectrometry"]'
---

# Quantitative proteomics by mass spectrometry

Plan or conduct a reproducible, sample-aware analysis of bottom-up LC-MS/MS proteomics. This instruction-only skill does not itself run software and its output is research evidence, not clinical validation. Distinguish protein abundance from RNA expression, protein activity, absolute concentration and causality.

## Establish inputs and design

Collect the scientific question, organism, independent biological replicates, sample identifiers, groups, paired/repeated measurements, batches, run order, covariates and desired contrast. Distinguish biological from technical replicates. Confirm acquisition (DDA, DIA or targeted), quantification (label-free, TMT/iTRAQ or other), fractionation, multiplex/channel and reference design where relevant. Preserve the original files.

Identify whether inputs are raw spectra, search-engine results, peptide/precursor tables, protein groups, normalized intensities or ratios; they are not interchangeable. Check exact sample-to-column mapping, units and log scale, zero and missing-value conventions, duplicate IDs and metadata alignment. Record instrument, acquisition and search/quantification software and versions, sequence database/version, search settings and provenance when available. Do not claim identification confidence from a quantitative matrix alone. If raw files require unavailable licensed software, a search database or unresolved settings, explain what is missing rather than inventing results.

## Identification and quality control

1. Review search and quantification summaries, target-decoy and identification false discovery rate (FDR) controls and their level (PSM, peptide and protein/group) when available; do not equate identification FDR with differential-abundance FDR. Report unavailable evidence and do not imply a threshold was verified without supporting files.
2. Examine decoys, known contaminants and site-only entries where applicable, documenting flags and exclusions. Describe protein-group inference, shared peptides, isoforms and ambiguous identifiers rather than presenting every group as a uniquely identified protein. Preserve accession mapping and annotation versions.
3. Inspect per-sample identification counts, intensity distributions, missingness by sample, protein and condition, sample correlations/PCA, technical replicates and available run or pooled-QC metrics. Evaluate run order and batch. Identify candidate outliers with evidence; do not silently remove samples or correct a fully confounded batch and treatment.
4. For multiplex data, inspect channel mapping, reference and batch structure and available interference/ratio-compression evidence; for DIA/DDA respect the search tool's reporting and protein-group conventions. Record what cannot be assessed.

## Quantification and inference

1. Choose filtering and normalization appropriate to the measurement and design; establish whether inputs are already normalized or log-transformed and avoid repeating transformations. Record excluded features and samples, assumptions, parameters and diagnostics before and after normalization. Normalization is not guaranteed to remove all technical bias.
2. Investigate missingness before selecting a method. Missingness may be abundance-dependent or have other causes; zero is not automatically a measured zero or a missing value. Avoid blind zero-filling or a universal imputation rule. Use a suitable method that accounts for missingness, or disclose assumptions, imputation uncertainty and sensitivity analyses; do not report unsupported effects when a contrast is not estimable.
3. Use an established available method appropriate to the input level and experimental design. Define the contrast, biological replication, covariates and pairing before testing. Distinguish a peptide-level model from a protein-group model, account for repeated observations where applicable, and check estimability, model diagnostics and warnings. If replication or a defensible design is missing, restrict output to descriptive analysis and say why.
4. Report effect estimates with direction and uncertainty, raw and multiple-testing-adjusted p-values, correction method, tested feature universe, filtering and missing-value treatment. Identification confidence and statistical differential abundance are separate claims. Do not apply RNA-seq count models to continuous protein intensities without a justified compatible method. Keep nonsignificant and missing results visible.
5. If pathway enrichment is requested, use appropriately mapped and actually tested proteins as the background, report ambiguous mappings and versioned gene sets, and avoid inferring pathway activation from an unsigned enrichment alone. Only create plots and files after execution, and preserve raw inputs and reproducibility information.

## Deliverables and boundaries

Provide a design and provenance summary, QC findings and exclusions, software versions and parameters, protein/peptide results with accession mappings, diagnostics, limitations and paths to actual artifacts. State precisely which steps ran and which could not run. Avoid clinical, biomarker or mechanistic claims without independent validation. Never invent a tool call, output or confidence assessment. Do not download data, install tools, transmit private data or overwrite inputs without the applicable user authorization.

Methodological references: https://pubmed.ncbi.nlm.nih.gov/30473739/ (missing data and peptide-to-protein inference); https://pubmed.ncbi.nlm.nih.gov/34432947/ (batch diagnostics and correction); https://pubmed.ncbi.nlm.nih.gov/25827922/ (peptide-based and summarized analyses and imputation effects).
