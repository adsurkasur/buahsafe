# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.1.0] - 2026-10-28
### Added
- Dataset primer transmisi optik/NIR 18-kanal pada 60 buah jambu kristal (`dataset/buahsafe_jambu_kristal_dataset_final.csv`).
- Locked holdout test set 13 buah (`dataset/holdout_fruits.json`).
- Artefak model machine learning terlatih untuk Jambu Kristal: SVM RBF 6-kanal produksi, Random Forest explainability, dan Logistic Regression (`models/*.joblib`).
- Skrip mandiri pembongkaran matematis dan koefisien model (`models/baca_dan_oprek_model.py`).
- Skrip evaluasi otomatis model dengan Leave-One-Fruit-Out CV (`pipeline_jambu_kristal_ml.py`).
- Notebook analisis spektrum transmisi utama jambu kristal (`BuahSafe_Jambu_Kristal_ML_Pipeline_Utama.ipynb`).
- Sinkronisasi dokumentasi ekosistem BuahSafe (koneksi ke backend `buahsafe-web-capture`, frontend `buahsafe-client`, dan deployment produksi Vercel / Cloudflare).

## [1.0.0] - 2026-09-16
### Added
- Modular logging protocol (`logs/` directory with activity, decision, and changelog files).
- Mandatory `AGENTS.md` guidelines for AI agents and contributors.
- Preliminary Proof-of-Concept study and explanatory notebook on AS7265x secondary coffee dataset.
