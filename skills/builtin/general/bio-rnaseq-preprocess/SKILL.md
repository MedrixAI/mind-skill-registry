---
name: bio-rnaseq-preprocess
description: Check and process bulk RNA-seq FASTQ reads into reproducible gene or transcript quantification with sample-level QC. Use when raw bulk RNA-seq reads need a count matrix before differential expression; use bio-bulk-rnaseq for an already verified count matrix.
license: Apache-2.0
metadata:
  mind.id: ai.medrix.skill.builtin.bio-rnaseq-preprocess
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.tags: '["bioinformatics","rna-seq","fastq","quality-control","quantification"]'
---

# Bulk RNA-seq read processing

Turn raw bulk RNA-seq reads into checked quantification for downstream analysis. Do not route single-cell barcoded data here; use the single-cell workflows. This skill ends at a gene/transcript count matrix and QC package; differential-expression testing belongs to `bio-bulk-rnaseq`.

## Inputs and readiness

Collect the question, organism, assay/library protocol, FASTQ pairs and checksums, sample sheet with biological sample IDs and technical lanes, read layout, strandedness, spike-ins, reference FASTA/transcriptome and annotation release, and available compute/storage. Verify sample identities and paired-read matching before processing. Preserve raw files. If reference, metadata, an authorized execution environment or enough capacity is missing, return a concrete unexecuted plan and do not fabricate counts.

## Workflow

1. Validate FASTQ structure and sample sheet: unique biological IDs, lane aggregation rule, paired-end consistency, read counts, length and quality profiles, adapter content and truncation. Record checksum and file provenance.
2. Choose a version-pinned, documented workflow appropriate for the library (for example nf-core/rnaseq with STAR/Salmon) and record reference and annotation checksums. Confirm strandedness from protocol or a supported inference; flag disagreement rather than silently switching settings.
3. Run authorized trimming, alignment or pseudoalignment, and gene/transcript quantification in an isolated work directory. Record commands, container digest or software versions, parameters, resource use and failed steps. Do not treat transcript TPM as raw gene counts.
4. Review sample-level and aggregated QC: read survival, mapping/assignment, rRNA and duplication where measured, gene-body or transcript coverage, inferred strandedness, library complexity and outlying samples. Avoid universal thresholds; justify any exclusion using assay context. Do not infer a biological result from QC alone.
5. Export a count matrix with stable feature IDs, a reconciled sample sheet, per-sample QC, MultiQC or equivalent, reference/annotation provenance, retained/excluded sample decisions and execution log. Verify matrix dimensions, nonnegative counts and exact sample-column correspondence. Pass only compatible counts and design metadata to `bio-bulk-rnaseq`.

Pipeline and sample-sheet reference: https://nf-co.re/rnaseq/usage . The skill guides execution through available authorized tools; it does not itself supply aligners, references or compute.

## Worked example: GSE110004 read processing

Example request: “Process the public GSE110004 bulk RNA-seq FASTQs for `SRR6357070`, `SRR6357072`, and `SRR6357076`; verify pairing and strandedness, quantify expression, and provide a checked matrix and sample QC.”

The [nf-core test-datasets `rnaseq` branch](https://github.com/nf-core/test-datasets/tree/9dd6d014f560e182047992834a8d267214fbccd1/testdata/GSE110004) supplies the real paired reads; its [sample sheet](https://github.com/nf-core/test-datasets/blob/9dd6d014f560e182047992834a8d267214fbccd1/samplesheet/samplesheet_test.csv) records reverse strandedness. In a local test with Salmon 1.4.0 and that branch's deliberately reduced yeast reference, each run had 50,000 read pairs; mapping rates were 78.094%, 78.580%, and 79.990%. Quantification produced 125 transcript rows and 124 GTF-mapped gene rows; `Gfp_transgene_gene` lacked a GTF mapping. These subset counts demonstrate processing, not differential expression or whole-transcriptome coverage. Recheck read identity, reference and results when using another release or full dataset.
