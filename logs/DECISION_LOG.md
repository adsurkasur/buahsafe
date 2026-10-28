# Decision Log (Architecture Decision Records)

### [DEC-002] Integrasi Dataset Primer Jambu Kristal dan Model Produksi ke Core Research Repo
- **Date**: 2026-10-28
- **Status**: Accepted
- **Context**: Repositori `buahsafe` semula hanya mendokumentasikan studi pendahuluan (Proof-of-Concept pada dataset sekunder AS7265x). Dengan rampungnya akuisisi dataset primer transmisi optik 60 buah jambu kristal, kalibrasi model SVM 6-kanal, dan implementasi konveyor lapangan, repositori riset ini perlu diselaraskan agar menjadi sumber kebenaran (*single source of truth*) data sains BuahSafe.
- **Decision**: 
  1. Menjadikan dataset transmisi halogen 18-kanal 60 buah (`dataset/buahsafe_jambu_kristal_dataset_final.csv`) sebagai dataset primer resmi di repositori.
  2. Menyediakan pipeline evaluasi standar `pipeline_jambu_kristal_ml.py` dan notebook interaktif `BuahSafe_Jambu_Kristal_ML_Pipeline_Utama.ipynb`.
  3. Memasukkan model terkalibrasi (`models/*.joblib`) serta skrip inspeksi bobot model `models/baca_dan_oprek_model.py`.
- **Consequences**: Pembaca riset, penguji, dan agronomis dapat langsung mengevaluasi pipeline model jambu kristal nyata tanpa ambiguitas pemisahan antara studi awal dan implementasi final.

### [DEC-001] Adoption of Modular Logging Protocol
- **Date**: 2026-09-16
- **Status**: Accepted
- **Context**: Standardizing change tracking, observability, and auditability across all managed projects for AI agents and human contributors.
- **Decision**: Mandate `logs/ACTIVITY_LOG.md`, `logs/DECISION_LOG.md`, and `logs/CHANGELOG.md` updates across all repositories.
- **Consequences**: Consistent history, reduced context loss during multi-agent handoffs.
