---
name: bio-dataset-discovery
description: Find and assess public biomedical datasets. Use when a user seeks GEO or BioProject studies by disease, organism, tissue, assay, or sample design.
license: MIT
metadata:
  mind.id: ai.medrix.skill.builtin.bio-dataset-discovery
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.tags: '["bioinformatics", "dataset", "discovery"]'
  mind.upstream.repo: https://github.com/ssinder/bioinformatics-agent-skills
  mind.upstream.commit: 42cf1a9c2381b25047dae98ca944ee7b52781ed8
  mind.upstream.path: skills/bioproject-search
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://github.com/ssinder/bioinformatics-agent-skills/blob/42cf1a9c2381b25047dae98ca944ee7b52781ed8/LICENSE", "https://github.com/ssinder/bioinformatics-agent-skills/blob/42cf1a9c2381b25047dae98ca944ee7b52781ed8/skills/bioproject-search/SKILL.md"]'
---

# Biomedical dataset discovery

Find candidate public studies and report traceable evidence for whether they fit a research question. Do not claim to have downloaded, inspected, or validated data that were not actually accessed.

## Inputs and boundaries

Clarify organism, disease or condition, tissue, assay or modality, required experimental groups, sample and donor requirements, data level, access constraints and desired output. If the user has not specified them, make uncertainty explicit and ask the most important questions. Respect the user's data and do not send private samples, identifiers, or credentials to external services. Use only authorized search or browsing tools; if unavailable, explain the limitation and provide reproducible search terms, not fabricated results.

## Workflow

1. Choose sources appropriate to the question, such as GEO for expression studies or BioProject for project-level metadata. Distinguish study, sample, experiment and raw-read identifiers; an accession alone does not establish sample or file availability.
2. Build organism, disease, tissue and assay synonyms, record each query, source and date, and distinguish exact filters from approximations. Do not assume full coverage of any database or privately controlled datasets.
3. Screen retrieved records against explicit eligibility criteria. For each candidate capture accession, title, organism, tissue, modality, samples and donors where documented, groups, relevant metadata, public/restricted status, data levels, license/access terms when discoverable, and a direct source link. Mark unknown fields unknown.
4. Cross-check sample-level and supplementary-file records before asserting that a specific matrix, comparison, cell type or raw file exists. Flag single-donor or group/batch-confounded designs, unclear counts and duplicate or reprocessed versions. Do not infer biological replicates from cell counts.
5. Return a ranked evidence table with why each candidate fits, exclusions, uncertainty, query date and source links. Differentiate public metadata from actual raw-data availability. Suggest QC as a separate next step; do not claim dataset quality has been established from a search result alone.

For BioProject records, official NCBI E-utilities can supply project metadata if a suitable authorized connector is available; obey service limits and policies. Do not silently install clients or disclose user files to any external endpoint.
