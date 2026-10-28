---
status: verified-guide
last_verified: 2026-10-28
audience: human-and-ai
sensitivity: internal
evidence_basis:
  - ../README.md
  - ../dataset/buahsafe_jambu_kristal_dataset_final.csv
  - ../dataset/holdout_fruits.json
  - ../pipeline_jambu_kristal_ml.py
  - ../BuahSafe_Jambu_Kristal_ML_Pipeline_Utama.ipynb
  - ../models/buahsafe_svm_model.joblib
  - ../BuahSafe_AS7265x_ML_Extensively_Explanatory_Colab.ipynb
---

# Research and Evidence Guide

## Role of this repository

This repository serves as the central machine learning research, data science, and spectral modeling hub for the **BuahSafe** project. It documents the transition from early proof-of-concept pipeline architecture (Phase 1) to direct empirical validation and calibrated model artifacts on the primary guava (*Psidium guajava L.*) transmission dataset (Phase 2).

## Evidence chain

```text
Phase 1: Proof-of-Concept Feasibility
secondary coffee reflectance dataset
  -> explanatory Jupyter notebook (AS7265x 18-channel physics feasibility)
  -> baseline and tuned classifiers, importance analysis

Phase 2: Primary Guava Research & Validation (Current Production State)
primary guava optical transmission dataset (60 fruits, 180 scans, halogen lamp)
  -> dataset schema with stable fruit_id and destructive ground truth labels
  -> leakage-free GroupKFold cross-validation (LeaveOneGroupOut by fruit_id)
  -> 13-fruit locked holdout test set (holdout_fruits.json)
  -> 6-channel NIR model training (nm730, nm760, nm810, nm860, nm900, nm940)
  -> SVM RBF calibrated model (buahsafe_svm_model.joblib)
  -> 100% anomaly recall on holdout set (zero false negatives)
  -> real-time conveyor integration in buahsafe-web-capture & buahsafe-client
```

## Current findings and boundaries

1. **Guava Primary Models:**
   - The primary SVM model trained on 6-channel NIR transmission data (`nm730` through `nm940`) achieves 100% recall on the locked 13-fruit holdout set (zero damaged fruit classified as normal).
   - Random Forest feature importance identifies Red-Edge (730 nm) and near-infrared absorption bands (760–940 nm) as dominant discriminators of internal tissue breakdown and larval cavity moisture.
2. **Preliminary Coffee Study:**
   - The tuned SVM on secondary coffee reflectance reached 75% accuracy and demonstrated that restricting to 4 channels degraded F1-score relative to 18 channels. This confirmed instrument capability prior to guava hardware acquisition.
3. **Methodological Invariants:**
   - Evaluation MUST split by physical `fruit_id`, not by individual repeated scan lines.
   - The business-critical metric is **Anomaly Recall**; false negatives (damaged fruit escaping to premium market) must be minimized to zero.

## Reproduction procedure

1. Environment: Python 3.10+ with `scikit-learn==1.9.0`, `pandas`, `numpy`, `joblib`.
2. Execute automated evaluation:
   ```bash
   python pipeline_jambu_kristal_ml.py
   ```
3. Inspect model coefficients and decision trees:
   ```bash
   python models/baca_dan_oprek_model.py
   ```
4. Run interactive notebook:
   `BuahSafe_Jambu_Kristal_ML_Pipeline_Utama.ipynb`.
