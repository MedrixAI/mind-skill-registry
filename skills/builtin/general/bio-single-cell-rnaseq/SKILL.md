---
name: bio-single-cell-rnaseq
description: Plan and, when authorized tools and inputs exist, analyze single-cell RNA-seq data from quality-controlled counts to clustering and cautious cell annotation. Use for exploratory single-cell analysis or sample-aware comparisons.
license: MIT
metadata:
  mind.id: ai.medrix.skill.builtin.bio-single-cell-rnaseq
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.tags: '["bioinformatics", "single-cell", "transcriptomics"]'
  mind.upstream.repo: https://github.com/ssinder/bioinformatics-agent-skills
  mind.upstream.commit: 42cf1a9c2381b25047dae98ca944ee7b52781ed8
  mind.upstream.path: skills/single-cell-rnaseq
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://github.com/ssinder/bioinformatics-agent-skills/blob/42cf1a9c2381b25047dae98ca944ee7b52781ed8/LICENSE", "https://github.com/ssinder/bioinformatics-agent-skills/blob/42cf1a9c2381b25047dae98ca944ee7b52781ed8/skills/single-cell-rnaseq/SKILL.md"]'
---

# Single-cell RNA-seq analysis

Guide a reproducible analysis from quality-controlled count data to exploratory cell populations. This workflow is for research, not clinical diagnosis. Do not represent visual clusters as confirmed cell identities or causal findings.

## Inputs and readiness

Obtain the scientific question, organism, tissue, assay, raw-count identity, matrix format, sample/donor/group/batch metadata, prior QC decisions, and output requirements. Distinguish cells, samples and biological replicates. Run the single-cell QC workflow first if the needed inputs or QC have not been checked. Record missing information and stop analyses whose assumptions cannot be assessed. If a compatible authorized Python/R environment and libraries are absent, provide a plan and dependencies rather than claiming execution. Do not install packages, upload data, or modify originals without authorization.

## Workflow

1. Validate cell/feature axes, sample alignment and raw count provenance. Preserve an immutable count layer; record software and reference versions, input identity and random seeds. Check sample structure, group/donor/batch overlap, dataset size and whether the intended operation fits available memory.
2. Review sample-level QC, doublets and ambient-RNA concerns; report choices and cells retained per sample. Avoid automatic universal mitochondrial cutoffs and prevent a zero-count barcode from being reported as 0% mitochondrial fraction.
3. Select normalization, variable-feature selection and dimensionality reduction based on assay and question. Document input layer, method and parameters. Compare sample/batch distributions before considering integration; explain what biological variation might be lost. If group and batch are completely confounded, do not claim integration can separate their effects. When groups contain different donors, assess the number of independent donors per group and use an appropriate unpaired or paired design; one donor per group cannot support population-level inference.
4. Build neighbors and clusters with documented method, parameters and seed; report sensitivity and composition by sample/donor. UMAP/t-SNE is exploratory and is not evidence of differential abundance or mechanistic causality.
5. Propose cell labels using marker evidence, organism, tissue and relevant reference versions. Include competing labels and ambiguous clusters; distinguish observed expression from inferred identity. Avoid using one marker alone as definitive proof.
6. For between-group expression, require independently replicated donors/samples and a suitable sample-aware design such as pseudobulk where appropriate; specify contrasts, covariates, group sizes and multiple-testing correction. If replication or design is insufficient, block inferential claims and report the limitation.
7. Return QC summary, method and versions, sample composition, candidate labels with evidence and uncertainty, plots and data tables only if actually produced, and a reproducibility record. Explicitly distinguish exploratory outputs from tested conclusions.
