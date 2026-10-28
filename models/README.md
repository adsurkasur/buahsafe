# Model Machine Learning BuahSafe (Jambu Kristal)

Direktori ini berisi model machine learning yang telah dilatih dan divalidasi pada dataset transmisi spektral NIR jambu kristal (*Psidium guajava L.*), beserta skrip inspeksi dan *explainability* mandiri.

---

## 📦 Berkas Model Terlatih (`.joblib`)

1. **`buahsafe_svm_model.joblib` (Model Utama Produksi)**
   - **Arsitektur:** Pipeline `StandardScaler` + `SVC(kernel='rbf', C=10.0, gamma=0.1, probability=True)`.
   - **Fitur Masukan:** 6 kanal NIR utama (`nm730`, `nm760`, `nm810`, `nm860`, `nm900`, `nm940`).
   - **Akurasi Validasi Silang (GroupKFold):** 96.7%
   - **Akurasi Holdout Test Set (13 buah):** 100% (Recall Anomali 100%, 0 False Negative).
   - **Penggunaan:** Dipakai langsung di backend server BuahSafe (`buahsafe-web-capture/models/`).

2. **`buahsafe_rf_model.joblib` (Model Pohon Keputusan / Explainability)**
   - **Arsitektur:** `RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)`.
   - **Fitur Masukan:** 6 kanal NIR utama.
   - **Kegunaan:** Menghitung *Feature Importance* (panjang gelombang paling dominan) dan mengekstrak aturan percabangan logika IF-ELSE untuk pembaca non-AI.
   - **Kanal Dominan:** `nm730` (Red-edge) dan `nm760` menyumbang >50% bobot pemisahan.

3. **`buahsafe_lr_model.joblib` (Model Linear Baseline & Log-Odds)**
   - **Arsitektur:** Pipeline `StandardScaler` + `LogisticRegression(C=1.0, max_iter=1000)`.
   - **Fitur Masukan:** 6 kanal NIR utama.
   - **Kegunaan:** Memberikan pembobotan linear koefisien odds ratio yang langsung dapat dibaca arah polaritasnya (+/-).

---

## 🔍 Skrip Inspeksi & Bongkar Model (`baca_dan_oprek_model.py`)

Skrip ini dapat dijalankan langsung di terminal tanpa ketergantungan framework web untuk membongkar jeroan matematis ketiga model di atas:

```bash
python models/baca_dan_oprek_model.py
```

Skrip akan menampilkan:
1. Verifikasi kelengkapan berkas model `.joblib`.
2. Pembongkaran koefisien regresi logistik (Log-Odds dan Odds Ratio per kanal).
3. Peringkat *Feature Importance* Random Forest (panjang gelombang terpenting).
4. Rekonstruksi pohon keputusan IF-ELSE hierarkis pertama.
5. Parameter Support Vectors dan intercept hyperplane model SVM.
6. Uji inferensi mandiri pada sampel transmisi buah holdout (`AMAN_017` vs `BOSOK_004`).
