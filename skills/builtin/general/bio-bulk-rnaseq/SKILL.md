---
name: bio-bulk-rnaseq
description: Assess and analyze bulk RNA-seq count data with a reproducible sample-aware differential-expression workflow. Use when comparing gene expression between biological groups from a count matrix or verified quantification.
license: MIT
metadata:
  mind.id: ai.medrix.skill.builtin.bio-bulk-rnaseq
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.tags: '["bioinformatics", "rna-seq", "differential-expression"]'
  mind.upstream.repo: https://github.com/ssinder/bioinformatics-agent-skills
  mind.upstream.commit: 42cf1a9c2381b25047dae98ca944ee7b52781ed8
  mind.upstream.path: skills/bulk-rnaseq
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://github.com/ssinder/bioinformatics-agent-skills/blob/42cf1a9c2381b25047dae98ca944ee7b52781ed8/LICENSE", "https://github.com/ssinder/bioinformatics-agent-skills/blob/42cf1a9c2381b25047dae98ca944ee7b52781ed8/skills/bulk-rnaseq/SKILL.md"]'
---

# Bulk RNA-seq analysis

Plan or conduct differential expression from suitable bulk RNA-seq data, reporting evidence, diagnostics and uncertainty. This skill does not execute software by itself and does not imply clinical validity.

## Before analysis

Ask for the question, organism and annotation, raw counts or quantified input and its provenance, sample identifiers, biological replicates, group labels, batch, paired/repeated design and desired contrast. Check that metadata align exactly with columns, identifiers are valid, counts are appropriate for the chosen method and data have not been incorrectly transformed or rounded. Clarify whether files are raw reads, transcript estimates, gene counts or normalized values; choose a documented workflow for that input rather than treating them as interchangeable.

Use a validated, available environment and an appropriate established method such as DESeq2, edgeR or PyDESeq2 after checking version and input requirements. Do not install tools, download references, send samples externally or overwrite files without authorization. If required software, raw inputs, biological replication or a defensible model are missing, provide an explicitly unexecuted plan and stop unsupported inference.

## Workflow

1. Inspect matrix dimensions, duplicate or unmapped genes, missing and invalid values, sample metadata, sequencing/quantification quality evidence and sample-level distributions. Record genome build and annotation versions if known.
2. Assess independent biological replicates, technical replicates, pairing, covariates and group/batch confounding. If treatment and batch are completely confounded, state that their effects cannot be separated. When groups contain different donors, distinguish an unpaired design with adequate independent donors per group from one donor per group, which cannot support population-level inference.
3. Define filtering, normalization, model formula and contrast before testing; preserve the raw input. Check library sizes, low-count handling, exploratory sample relationships and model diagnostics using an appropriate method for the design. Record all choices and versions.
4. If prerequisites are met, perform differential expression with the selected validated tool. Report estimated effects, uncertainty, raw and adjusted p-values, the correction method, tested gene universe and relevant filtering. Handle missing statistics explicitly; do not silently replace missing adjusted p-values with zero or claim significance based only on a fold-change cutoff.
5. Produce reproducible tables and plots only if execution actually occurred. Interpret results as associations under the design, acknowledge confounders and power limits, and retain all results including nonsignificant findings. Pass a documented tested-gene universe to any downstream enrichment analysis.

Output the sample/design and QC summary, exact contrast, method/version/parameters, results with provenance, diagnostics, limitations, and reproducible artifact paths when available.
