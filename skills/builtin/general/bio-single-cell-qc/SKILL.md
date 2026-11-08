---
name: bio-single-cell-qc
description: Inspect single-cell RNA-seq data and sample metadata for analysis readiness. Use when a user provides a count matrix, AnnData, 10x files, or a QC summary and asks about data quality, cell filtering, or sample-level limitations.
license: MIT
metadata:
  mind.id: ai.medrix.skill.builtin.bio-single-cell-qc
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.tags: '["bioinformatics", "single-cell", "quality-control"]'
  mind.upstream.repo: https://github.com/GPTomics/bioSkills
  mind.upstream.commit: d91ed3d563019e649dc854c56ccd62551359488a
  mind.upstream.path: single-cell/preprocessing
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://github.com/GPTomics/bioSkills/blob/d91ed3d563019e649dc854c56ccd62551359488a/LICENSE", "https://github.com/GPTomics/bioSkills/blob/d91ed3d563019e649dc854c56ccd62551359488a/single-cell/preprocessing/SKILL.md"]'
---

# Single-cell RNA-seq data readiness and quality control

Assess whether the supplied data can support the stated analysis and produce an auditable QC report. This skill covers data intake and QC decisions; it does not promise cell-type annotation, differential expression, or a clinical conclusion.

## Inputs and boundaries

Ask for the research question, organism, tissue, assay, input files, sample and donor identifiers, group and batch metadata, and whether the matrix contains raw counts or transformed values. Ask which output and filtering actions are desired. A 10x matrix, h5ad, tabular matrix, or existing QC summary may be assessed only when the available tools can read it. If inputs or metadata are absent, report the missing information and limit the conclusion; do not invent values or assume that cells are independent biological replicates.

Use an authorized analysis environment when one is available. Check library availability and versions before suggesting runnable code; do not silently install software, transfer data, or alter the original input. If execution is unavailable, provide a clearly labeled assessment plan rather than claiming metrics were calculated. Work with a copy and preserve raw counts when filtering is requested.

## Workflow

1. **Inventory and integrity.** Record file names and format, matrix dimensions and orientation, identifier namespaces, organism/reference if known, and whether counts are raw, normalized, log-transformed or unknown. Check sample-to-cell and feature alignment, duplicate identifiers, missing metadata, negative/non-finite values, zero-count cells and whether the data are sparse. Flag fractional values as a reason to verify count provenance; do not assume they are raw UMI counts. Do not apply count-based methods to transformed data as if they were raw counts.
2. **Design and provenance.** Record biological replicate/donor, sample, group, tissue, assay and batch, and identify whether group is confounded with batch or donor. Report missing mappings and unequal sample composition. A cell count is not the number of independent donors. If group and batch are completely confounded, state that their effects cannot be separated; batch correction cannot recover that missing experimental information. If each group has only one donor or lacks independent donor replication, do not infer a population-level group effect. Different donors in different groups can support an unpaired comparison when there are sufficient independent donors per group.
3. **Compute or review QC metrics.** When raw counts and a compatible environment are available, summarize per-cell total counts, detected genes and mitochondrial fraction, and per-gene detection rates, separately by sample. Identify mitochondrial genes using the correct organism and annotation; if identifiers cannot be mapped or a barcode has zero total counts, mark its fraction unavailable rather than zero. Report distributions and before/after counts, not just a single aggregate.
4. **Assess potential artifacts.** Review low-quality and unusually high-count/high-feature cells as possible artifacts or doublets; note ambient RNA, dissociation stress and batch effects as possibilities, not confirmed diagnoses. High mitochondrial fractions can reflect tissue biology or stress; do not use one universal cutoff. Mention doublet or ambient-RNA tools only when their inputs, assumptions and runtime dependencies are available.
5. **Recommend filters.** Choose thresholds from sample-specific distributions, tissue and study context. Show the number and percentage of cells and genes affected per sample, including samples or populations that could be disproportionately removed. If available information cannot justify a threshold, provide candidate checks and ask for confirmation rather than silently filtering. Filtering is optional and must not overwrite source data.
6. **Report readiness.** Give pass / caution / blocked for each check, with evidence, sample-level counts, missing inputs, decisions and limitations. List proposed next steps and, if executed, software versions, input identity, parameters and output paths. Distinguish calculated results from suggested future analyses. Do not claim an actual analysis was performed without execution evidence.

## Output

Provide an input inventory, sample/design summary, QC metrics and plots when actually generated, findings by sample, proposed thresholds and anticipated losses, unresolved risks, and a reproducibility record. If raw counts, sample metadata or the analysis environment are missing, state exactly which conclusions are blocked.

## Scientific references

- Heumos et al. (2023), Best practices for single-cell analysis across modalities, DOI: 10.1038/s41576-023-00586-w.
- Osorio and Cai (2021), Systematic determination of mitochondrial proportion in human and mouse tissues, DOI: 10.1093/bioinformatics/btaa751.
