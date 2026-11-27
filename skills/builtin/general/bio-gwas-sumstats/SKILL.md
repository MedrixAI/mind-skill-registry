---
name: bio-gwas-sumstats
description: Inspect and analyze human GWAS summary statistics for a defined trait, including allele harmonization checks, locus evidence and cautious gene prioritization. Use when supplied a full summary-statistics file or a public study accession; not for individual-level genotypes.
license: Apache-2.0
metadata:
  mind.id: ai.medrix.skill.builtin.bio-gwas-sumstats
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.tags: '["bioinformatics","genomics","gwas","summary-statistics"]'
---

# GWAS summary-statistics analysis

Use aggregate association results to answer a specified trait or target question. A significant variant is evidence of locus association, not proof that the nearest gene is causal. This skill does not analyze individual-level genotypes or make clinical risk predictions.

## Inputs and boundaries

Identify the phenotype and definition, study accession/publication, ancestry and cohort, sample size, case/control counts when applicable, genome assembly, summary-statistics format, effect and other allele definitions, effect scale (beta or odds ratio), standard error, p-value, frequency, and data-use terms. Inspect the actual header and metadata before choosing column mappings. Do not infer missing alleles or build from rsIDs alone. Keep controlled-access data within its authorized compute environment; do not send variant-level user data to a public service.

For a public study, record the exact accession, source URL, retrieval date, release/version and file checksum. Prefer a harmonized GWAS-SSF file when available, but still inspect its metadata and harmonization status. If only curated lead hits are available, state that full summary-statistics analyses cannot be performed.

## Workflow

1. Verify that the input is a real genome-wide summary-statistics table. Check required columns, row count, duplicate variants, malformed chromosomes/positions, impossible frequencies or p-values, missing effect sizes, and whether p=0 represents underflow. Record exclusions rather than silently dropping rows.
2. Verify build and allele orientation against the declared reference. Treat A/T and C/G palindromic variants as ambiguous when frequency cannot resolve orientation. Normalize effect direction before combining studies or comparing eQTL/pQTL results. Stop the affected comparison if build or effect allele cannot be reconciled.
3. Inspect genome-wide signal and calibration with QQ and Manhattan plots, reported genomic inflation or LD-score diagnostics when available, and study design limitations. Do not interpret inflation as confounding without considering polygenicity and sample size.
4. Define locus windows or LD-based clumps and the multiple-testing threshold before prioritizing signals. Keep independent lead variants, full locus context, uncertainty and ancestry-specific LD assumptions visible. A nearest-gene label is only positional annotation.
5. If appropriate data and tools exist, add fine-mapping, colocalization with molecular QTL, functional annotation and independent replication as separate evidence layers. Do not claim colocalization, causality, or transferability from overlap alone.
6. Produce a source-linked report with QC exclusions, trait/cohort context, assembly, harmonization decisions, significant and null loci, candidate-gene rationale, alternative genes, limitations, exact commands/versions, and output paths. Label any unexecuted stage explicitly.

Reference formats and harmonization: https://www.ebi.ac.uk/gwas/docs/methods/summary-statistics/ . Execute calculations only with authorized tools and sufficient input; the skill text itself is not a statistical pipeline.

## Worked example: BMI summary statistics

Example request: “Analyze the public Locke et al. BMI GWAS summary statistics. Check the full table, show a QQ and Manhattan plot, identify significant signals, and explain which follow-up evidence is still needed before naming causal genes.”

Use `bmi.tsv.gz` from the [SUMSTATS repository](https://github.com/jinghuazhao/SUMSTATS/blob/5b03f1cb92d35019aea583a5305bcddee405c27e/bmi.tsv.gz) together with that repository's README column definitions. It is a derived GRCh37 table without a header or complete GWAS-SSF metadata; confirm those facts before parsing. In a local test of this exact file, 2,612,310 unique valid variant rows remained after 615 duplicate rows; 57,452 rows lacked allele frequency, and 1,859 had p <= 5e-8. A 500 kb distance rule yielded 77 representative regions, **not** LD-independent loci. Report `rs1558902` as a leading A/T association while flagging its ambiguous orientation for cross-study comparison. Do not infer a causal gene from proximity alone. Recompute all numbers if the source file changes.
