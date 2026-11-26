---
name: bio-wgs-germline
description: Assess human whole-genome germline sequencing quality and short-variant calls, from FASTQ/BAM/gVCF/VCF at the available stage through a reproducible research-grade variant report. Use for inherited SNVs and small indels; not tumor somatic calling or clinical diagnosis.
license: Apache-2.0
metadata:
  mind.id: ai.medrix.skill.builtin.bio-wgs-germline
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.tags: '["bioinformatics","genomics","wgs","germline-variants"]'
---

# WGS germline short-variant analysis

Investigate inherited SNVs and small indels from human whole-genome sequencing. Select the entry point that matches the files supplied. A VCF does not prove that read alignment or variant calling was rerun. Structural variants, repeat expansions, mitochondrial calls and tumor mutations require separate methods and are outside this skill's default claim.

## Inputs and boundaries

Record research question, consent and data-use scope, sample identifiers and pedigree if relevant, sequencing platform/read layout, file type and checksums, reference assembly and exact FASTA, sex/karyotype metadata if available, known-sites resources, callable regions, and software/container versions. Individual genomes are sensitive; keep raw reads and genotypes in the authorized environment. Do not paste individual variant lists into external services without explicit data-use permission. Do not make a pathogenicity or diagnosis claim from automated annotation alone.

## Workflow

1. Verify file identity, format and reference compatibility. For FASTQ/BAM, inspect read quality, alignment rate, duplicates, coverage breadth/depth, contamination and sample identity where the necessary data exist. For VCF-only input, report these upstream metrics as unavailable unless provided; do not backfill them from the VCF.
2. If authorized raw-read compute is available, use a version-pinned preprocessing and germline caller workflow appropriate for the sample set. For a cohort, retain per-sample gVCFs and joint-genotyping provenance; for a single sample, use a documented single-sample route. Apply filtering appropriate to cohort size and available truth resources. Do not claim VQSR was run when prerequisites are absent.
3. Inspect VCF syntax, assembly/contig dictionary, normalization, sample names, genotype missingness, depth and allele-balance distributions, filter status, Ti/Tv and indel summaries, sex-chromosome handling and callable-region denominators. Distinguish a filtered call from a confirmed negative result.
4. Annotate research-relevant variants only with versioned, licensed references. Keep original and normalized coordinates, transcript accession, effect prediction, population frequency, evidence source and conflicting annotations. Separate variant discovery quality from biological or clinical interpretation.
5. Produce a reproducible QC and variant report: input stage, executed versus inherited steps, assembly/reference hashes, methods and versions, per-sample metrics, variant counts by class/filter, callable limits, selected findings with evidence and uncertainty, files and checksums. If an input or tool is absent, stop the affected stage and report what remains unverified.

Germline short-variant workflow reference: https://gatk.broadinstitute.org/hc/en-us/articles/360035535932-Germline-short-variant-discovery-SNPs-Indels . Benchmark suitable outputs against a version-matched truth set and confident regions such as NIST GIAB HG002 when available; report precision/recall only within those regions.

## Worked example: HG002 chr21 VCF-stage QC

Example request: “Assess the public HG002 chr21 bcftools callset against the GRCh38 GIAB v4.2 truth VCF and confident-region BED. Summarize variant QC and state exactly which benchmark claims the inputs support.”

Use the pinned [nf-core variantbenchmarking test data](https://github.com/nf-core/test-datasets/tree/b32e4cd1df4a49d3ad84cd85d1f764e9ae50cacf/testdata/hg38) and verify the VCF/BED filenames, reference build and checksums. In a local VCF-stage test, the callset contained 87,327 records with `FILTER=.` throughout; the truth contained 55,210 `PASS` records. Within the supplied confident intervals, 45,513 exact `(chromosome, position, REF, ALT)` allele keys overlapped. This is an exploratory representation-sensitive comparison, **not** a haplotype-aware precision/recall result. Report upstream FASTQ, alignment, coverage and variant-calling stages as inherited or untested, and do not turn chr21 evidence into a whole-genome quality claim.
