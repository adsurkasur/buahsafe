"""
Skrip Inspeksi & Oprek Model BuahSafe (.joblib)
----------------------------------------------
Skrip ini menunjukkan cara:
1. Memuat (load) model .joblib untuk prediksi data baru (inferensi).
2. Membongkar / mengoprek 'isi otak' ketiga model (Explainability).
"""
from pathlib import Path
import joblib
import numpy as np

MODEL_DIR = Path(__file__).resolve().parent

# Contoh 1 pindaian sensor AS7265x (6 kanal: 730, 760, 810, 860, 900, 940 nm)
# Contoh data buah normal dan anomali
sample_normal = np.array([[28.5, 29.1, 75.2, 78.4, 88.6, 76.2]])
sample_anomali = np.array([[19.2, 18.7, 35.1, 38.0, 48.3, 44.1]])

print("=" * 60)
print("1. MEMBONGKAR MODEL LOGISTIC REGRESSION (Paling Explainable)")
print("=" * 60)
lr_data = joblib.load(MODEL_DIR / "buahsafe_lr_model.joblib")
lr_pipe = lr_data["pipeline"]
channels = lr_data["channels"]
coefs = lr_pipe.named_steps["clf"].coef_[0]

print("Koefisien tiap panjang gelombang (Log-Odds Anomali):")
for ch, w in zip(channels, coefs):
    arah = "Menaikkan risiko anomali (+)" if w > 0 else "Mengindikasikan buah normal (-)"
    print(f"  - {ch}: {w:+.4f} ({arah})")

prob_anomali = lr_pipe.predict_proba(sample_anomali)[0][1]
print(f"Prediksi buah uji anomali: Probabilitas={prob_anomali:.2%} -> "
      f"{'ANOMALI' if prob_anomali >= 0.35 else 'NORMAL'}")

print("\n" + "=" * 60)
print("2. MEMBONGKAR MODEL RANDOM FOREST (Tingkat Kepentingan Fitur)")
print("=" * 60)
rf_data = joblib.load(MODEL_DIR / "buahsafe_rf_model.joblib")
rf_pipe = rf_data["pipeline"]
rf_clf = rf_pipe.named_steps["clf"]
importances = rf_clf.feature_importances_

print("Ranking Feature Importance (Pengaruh kanal memisahkan buah busuk):")
sorted_idx = np.argsort(importances)[::-1]
for idx in sorted_idx:
    print(f"  - {channels[idx]}: {importances[idx]*100:.2f}%")

print(f"Total pohon keputusan dalam hutan: {len(rf_clf.estimators_)} pohon.")
print("Contoh aturan di Pohon ke-0 (cabang atas):")
from sklearn.tree import export_text
tree_rules = export_text(rf_clf.estimators_[0], feature_names=channels, max_depth=2)
print(tree_rules)

print("=" * 60)
print("3. MEMBONGKAR MODEL SVM (RBF) - Model Terpilih Produksi")
print("=" * 60)
svm_data = joblib.load(MODEL_DIR / "buahsafe_svm_model.joblib")
svm_pipe = svm_data["pipeline"]
svm_clf = svm_pipe.named_steps["clf"]

print(f"Jumlah Support Vectors penentu batas: {svm_clf.n_support_} "
      f"(Kelas 0 / Normal: {svm_clf.n_support_[0]}, Kelas 1 / Anomali: {svm_clf.n_support_[1]})")
print(f"Ambang Batas Keputusan (Threshold) Produksi: {svm_data.get('threshold', 0.35)}")

prob_svm = svm_pipe.predict_proba(sample_anomali)[0][1]
print(f"Prediksi buah uji anomali dengan SVM: Probabilitas={prob_svm:.2%} -> "
      f"{'ANOMALI' if prob_svm >= svm_data.get('threshold', 0.35) else 'NORMAL'}")
