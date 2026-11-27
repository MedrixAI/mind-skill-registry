---
name: bio-gwas-cohort
description: Plan and analyze individual-level genotype plus phenotype data for a cohort GWAS with sample/variant QC, relatedness or population-structure control, association testing and reproducible summary statistics. Use when authorized cohort-level genotypes and real phenotype metadata are available; not for summary-statistics-only input.
license: Apache-2.0
metadata:
  mind.id: ai.medrix.skill.builtin.bio-gwas-cohort
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.tags: '["bioinformatics","genomics","gwas","cohort","genotype-phenotype"]'
---

# Individual-level cohort GWAS

Connect authorized individual genotypes to a defined phenotype and statistical design. Genome-wide association is not a causal-gene claim. Do not substitute simulated phenotypes for a requested real-trait analysis or use population labels as disease outcomes.

## Inputs and data boundary

Record organism, trait definition/units, ascertainment and cohort, consent/data-use terms, genotype format and file checksums, sample IDs and phenotype/covariate tables, genome build, genotyping/imputation platform, sex/karyotype information when relevant, family structure and anticipated sample size. Keep person-level genotype/phenotype data in the approved compute environment; export aggregate results only when permitted. Refuse a join with ambiguous sample IDs or consent scope.

## Workflow

1. Check genotype/phenotype ID matching, duplicates, missing outcomes, trait distribution, case-control balance or quantitative range, covariates and batch structure. Predefine exclusion rules and report every exclusion.
2. Perform sample QC appropriate to the data: call rate, reported versus genetic sex where applicable, heterozygosity, relatedness/duplicates, ancestry or population structure and batch effects. Choose unrelated analysis or an appropriate mixed model for relatives; do not discard family structure without documenting it.
3. Perform variant QC: missingness, allele frequency, imputation INFO where relevant, allele/build checks and context-aware Hardy-Weinberg checks. Apply filters before the association scan and keep counts at each step. HWE assumptions differ for case-control, inbred and family-based designs.
4. Define the phenotype transformation and model before testing. Use linear, logistic, mixed or other suitable association methods with specified covariates, relatedness/ancestry controls and software versions. Explain whether the effective sample size and power support the intended claim.
5. Inspect QQ/Manhattan plots, calibration, top loci, genotype clusters where available and sensitivity analyses. Apply an appropriate multiple-testing threshold. Separate distance-based windows from LD-independent signals, and seek replication and functional evidence before prioritizing genes.
6. Deliver a source-linked report with sample/variant attrition, design and covariates, model diagnostics, results with effect allele/build/effect size/SE/p value, limitations and reproducible commands. Hand off an authorized, checked aggregate table to `bio-gwas-sumstats` for downstream locus analysis.

Method reference: https://www.cog-genomics.org/plink/2.0/ . The [GEMMA manual](https://github.com/genetics-statistics/GEMMA/blob/master/doc/manual.tex) documents mixed-model analysis of related heterogeneous-stock mice with real CD8 and mean corpuscular hemoglobin phenotypes.

## Worked example: real mouse CD8 phenotype

Example request: “Using GEMMA's public heterogeneous-stock mouse genotype and CD8 phenotype files, verify genotype/phenotype alignment, account for relatedness, run a quantitative-trait association scan, and report sample counts and limitations.”

Use the [GEMMA `mouse_hs1940` example at a fixed commit](https://github.com/genetics-statistics/GEMMA/tree/ce5e778cc36c40a2fa82f3dafe66403bb0e3a185/example), including `.bed/.bim/.fam`, phenotype and annotation files. Its documented CD8 and MCH measures came from real mice, but phenotypes were adjusted and quantile normalized by the source study; one included binary trait was constructed for demonstration. In a local GEMMA 0.98.5 run using the quantitative CD8 column and a kinship-based linear mixed model, 1,410 of 1,940 mice across 85 families had usable CD8 values, and 10,768 of 12,226 markers were tested. At Bonferroni `0.05/10,768`, 27 rows passed; 1,668 tested markers had unusable positions, leaving 18 significant rows with valid positions for plotting. The most significant located row was `rs13482968` on mouse chromosome 17 (`p=6.45e-15`). These source genotypes were already family-mean-imputed, so raw genotype call-rate QC cannot be reconstructed. This validates a nonhuman cohort workflow, not human clinical GWAS or independent locus discovery.
