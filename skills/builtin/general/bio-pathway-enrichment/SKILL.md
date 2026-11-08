---
name: bio-pathway-enrichment
description: Interpret a gene list or ranked gene results through pathway and gene-set enrichment with explicit background, identifier mapping, and multiple-testing controls. Use for GO or pathway analysis of biological data.
license: MIT
metadata:
  mind.id: ai.medrix.skill.builtin.bio-pathway-enrichment
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.tags: '["bioinformatics", "pathway", "enrichment"]'
  mind.upstream.repo: https://github.com/GPTomics/bioSkills
  mind.upstream.commit: d91ed3d563019e649dc854c56ccd62551359488a
  mind.upstream.path: pathway-analysis/go-enrichment
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://github.com/GPTomics/bioSkills/blob/d91ed3d563019e649dc854c56ccd62551359488a/LICENSE", "https://github.com/GPTomics/bioSkills/blob/d91ed3d563019e649dc854c56ccd62551359488a/pathway-analysis/go-enrichment/SKILL.md"]'
---

# Gene-set and pathway enrichment

Compare a gene list or ranked results against a defined gene-set collection and report interpretable, traceable research evidence. Enrichment does not establish pathway activation, causality or clinical significance by itself.

## Inputs and checks

Ask for organism, gene identifiers and annotation version, whether input is a selected gene list or a ranked genome-wide result, how genes were selected, a defensible tested-gene background for over-representation analysis (ORA), the gene-set resource and version, and desired output. Verify mapping and duplicates, record input/mapped/unmapped counts and ambiguous mappings, and ensure the selected genes are consistent with the declared background. Never silently use the whole genome as the background when a study-specific tested universe is needed. If the background is missing or cannot be justified, block the ORA significance claim and request it.

## Workflow

1. Determine whether the question calls for ORA of a selected list or a ranked gene-set method. Do not interchange their assumptions or invent ranks. Define the eligible genes and handle ties, duplicate IDs and missing values transparently.
2. Match species, identifier namespace, version and gene-set provenance; record category (for example GO biological process versus molecular function). Explain loss of genes during mapping and assess whether it is material.
3. Use an authorized, available and version-checked implementation. Record method, universe size, gene-set size filters, database version and multiple-testing method; require correct p-value interpretation. Gene length or other selection biases may require method-specific treatment; state when those assumptions are not assessed.
4. Report term, overlap, adjusted significance, supporting genes and the tested background. Describe overlapping or hierarchical terms and avoid presenting redundant terms as independent discoveries. For ranked methods, report the enrichment direction only as supported by the chosen ranking and method.
5. Interpret findings as hypotheses, link to source records and distinguish enrichment of annotations from direct pathway activity or causal evidence. Include missing inputs, ambiguous mappings and limitations. Do not make up data or output tables when computation was not performed.

If relevant data, libraries, databases or network access are unavailable, give a reproducible plan and missing requirements. Do not silently install software, upload a user gene list, or use a remote API without authorization.
