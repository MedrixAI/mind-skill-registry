---
name: bio-wgs-somatic
description: Assess tumor-normal whole-genome sequencing and research-grade somatic SNV/small-indel calls from the available FASTQ, alignment, or VCF stage. Use for cancer WGS quality review, matched-normal calling plans, and evidence-limited variant reports; not inherited variant analysis or clinical diagnosis.
license: Apache-2.0
metadata:
  mind.id: ai.medrix.skill.builtin.bio-wgs-somatic
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.tags: '["bioinformatics","genomics","wgs","somatic-variants","cancer"]'
---

# Tumor-normal WGS somatic short-variant analysis

Analyze a defined cancer research question using the actual data stage supplied. A VCF-stage review does not imply raw reads were aligned or somatic variants were recalled. Distinguish a tumor-normal pair from tumor-only data; absence in an unmatched normal or population reference does not establish that a variant is somatic. Structural variants, copy-number changes, mutational signatures and clinical actionability require separate methods.

## Inputs and readiness

Record tumor and matched-normal sample IDs, pairing evidence, tissue and collection context, assay/platform, read depth, tumor purity and ploidy estimates when available, contamination, consent and data-use scope, file checksums, reference assembly/FASTA, caller/filter versions, panel-of-normals and germline-resource versions, and callable regions. Keep individual genomes and patient variants inside the authorized environment. If only a VCF is supplied, mark BAM/FASTQ coverage and caller steps unverified.

## Workflow

1. Verify sample identity, tumor-normal pairing, file format and reference build. For reads/alignments, inspect per-sample quality, mapping, duplicate rate, coverage breadth, contamination, cross-sample identity and callable tumor/normal overlap. A low-frequency event cannot be judged without coverage and assay context.
2. For authorized raw-read analysis, use a version-pinned tumor-normal workflow and document alignment, recalibration, caller, panel of normals, germline filter, artifact filters and matched-normal genotype evidence. A tumor-only route must be explicitly identified and its lower somatic specificity explained. Do not silently mix WGS and exome or panel assay denominators.
3. At VCF stage, inspect contigs, sample columns, FILTER values, SNV/indel classes, depth, tumor/normal allele counts and variant allele fractions, orientation/context artifacts, strand bias and contamination flags. Separate raw, filtered and high-confidence calls; `FILTER=.` is unfiltered rather than PASS.
4. If a version-matched reference truth set and confident-region BED exist, benchmark only the supported variant classes inside those regions with a representation-aware comparator. Report precision/recall only when the actual query callset, comparator, normalization and region denominator are verified. A truth-set-only QC is not a caller benchmark.
5. Produce a reproducible report with executed versus inherited steps, reference and tool versions, QC exclusions, variant summaries, selected research findings with evidence and uncertainty, file checksums and limitations. Do not promote an automated annotation to a diagnosis or treatment recommendation.

Workflow reference: https://nf-co.re/sarek/latest/docs/usage . The [SEQC2 HCC1395/HCC1395BL study](https://pmc.ncbi.nlm.nih.gov/articles/PMC8532138/) provides a real WGS tumor-normal benchmark; its v1.2.1 truth VCFs and high-confidence BED are suitable for checking VCF-stage handling, not proof that a local caller was run.

## Worked example: SEQC2 reference VCF review

Example request: “Review the public SEQC2 HCC1395 somatic SNV and indel reference VCFs against their high-confidence BED. Check variant classes and FILTER fields, and explain which upstream tumor-normal steps remain untested.”

Use the fixed [NCBI SEQC2 release v1.2.1](https://ftp.ncbi.nlm.nih.gov/ReferenceSamples/seqc/Somatic_Mutation_WG/release/v1.2.1/), including its README, SNV VCF, indel VCF and BED, plus one original [WGS BWA/MuTect2 tumor-normal callset](https://ftp.ncbi.nlm.nih.gov/ReferenceSamples/seqc/Somatic_Mutation_WG/analysis/SNVs/vcfs/WGS/WGS_EA_1.bwa.muTect2.vcf.gz). In a local VCF-stage test, the truth had 39,447 SNVs and 1,625 indels; the two-sample callset had 382,025 records, of which 106,828 were `PASS`. The truth uses `PASS;HighConf` and `PASS;MedConf` labels, so inspect source-specific FILTER semantics instead of treating only literal `PASS` as valid. Within the BED, exact allele matching found 37,139 overlapping SNVs and 1,318 overlapping indels. This representation-sensitive overlap is not a formal som.py precision/recall result; raw WGS processing and clinical interpretation were not rerun. Recompute if release or callset changes.
