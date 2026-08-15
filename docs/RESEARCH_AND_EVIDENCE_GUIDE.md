---
status: verified-guide
last_verified: 2026-08-15
audience: human-and-ai
sensitivity: internal
evidence_basis:
  - ../README.md
  - ../BuahSafe_AS7265x_ML_Extensively_Explanatory_Colab.ipynb
  - ../buahsafe_learning_outputs/
---

# Research and Evidence Guide

## Role of this repository

This repository is the preliminary spectral-machine-learning workstream for BuahSafe. It demonstrates an end-to-end analysis pipeline using AS7265x measurements from roasted coffee beans. It is not the operational acquisition application and does not contain a validated model for guava.

## Evidence chain

```text
secondary coffee reflectance dataset
  -> explanatory Jupyter notebook
  -> data audit and preprocessing
  -> baseline and tuned classifiers
  -> Agtron regression
  -> channel-selection and importance analysis
  -> result tables/models/figures
  -> presentation variants
```

The local `buahsafe_learning_outputs/` directory contains derived `.joblib`, CSV, and metadata outputs and is intentionally ignored by Git. A new maintainer should regenerate or archive these outputs with a notebook/source commit and environment record before treating them as reproducible release evidence.

## Current findings and boundaries

The README reports that tuned SVM reached 75% accuracy on the coffee task and that restricting the model to four channels reduced performance relative to 18 channels. These are repository-reported results tied to the secondary coffee dataset. Verify them from the notebook and result files before reusing exact values.

Do not state:

- that the coffee model detects guava damage;
- that a four-channel device can never work for another dataset;
- that AS7265x performance on coffee guarantees a particular guava accuracy;
- that a random scan-level split is adequate for repeated scans from the same fruit.

## Transition to primary guava research

Required minimum schema:

- stable `fruit_id` for one physical guava;
- stable `scan_id` or scan number;
- 18 calibrated channel values;
- scan position/orientation;
- distance and illumination/chamber configuration;
- sensor settings and firmware/software version;
- storage age, temperature, and humidity when available;
- destructive ground truth and severity label;
- optional Brix, larva, browning, or other recorded findings.

Evaluation must split by physical `fruit_id`, not by individual scan. The business-critical error is a damaged fruit classified as acceptable, so report damaged-class recall and false negatives alongside aggregate metrics.

## Reproduction procedure

1. Create a clean Python environment.
2. Install the packages listed in the root README.
3. Run the notebook from top to bottom without manual hidden state.
4. Save environment/package versions and the source dataset hash.
5. Compare regenerated result tables to `buahsafe_learning_outputs/`.
6. Record any nondeterminism, warnings, or failed download fallback.

## Definition of done for a new experiment

- input dataset and schema are documented and hashed;
- grouping and temporal/biological leakage controls are explicit;
- preprocessing is fit only on training folds;
- baselines and final models use identical splits;
- metrics include class-specific errors and uncertainty across folds;
- model file, code commit, environment, and result table are linked;
- claims are limited to the evaluated population and protocol.
