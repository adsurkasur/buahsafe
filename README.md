# BuahSafe — Machine Learning Research & Spectral Analysis Core

> **Status Ekosistem (Pembaruan Oktober 2026):**
> Penelitian di repositori ini telah berhasil ditransisikan dari studi pendahuluan (*Proof of Concept*) ke **validasi nyata pada dataset primer Jambu Kristal (*Psidium guajava L.*)**, pengujian perangkat keras konveyor otomatis, serta *deployment* penuh ke backend dan web frontend produksi.
>
> 🌐 **Layanan Live:**
> - **Aplikasi Web Kios & Analitik:** [https://buahsafe.vercel.app](https://buahsafe.vercel.app)
> - **Backend API Server (HP t530 via Cloudflare Tunnel):** [https://buahsafe-api.adsurkasur.my.id](https://buahsafe-api.adsurkasur.my.id)
>
> 🔗 **Repositori Terkait:**
> - **Backend & Conveyor Daemon:** [adsurkasur/buahsafe-web-capture](https://github.com/adsurkasur/buahsafe-web-capture)
> - **Frontend Web Client:** [adsurkasur/buahsafe-client](https://github.com/adsurkasur/buahsafe-client)
> - **Superproject & Dokumen Output (Laporan Akhir, HAKI, Jurnal):** [adsurkasur/managed-projects-handoff](https://github.com/adsurkasur/managed-projects-handoff/tree/main/BuahSafe)

---

## 🎯 Ringkasan Ekosistem & Peta Proyek

```text
[ Sensor Optik AS7265x (18-Ch) + Lampu Halogen ]
                   │
                   ▼ (Transmisi Spektroskopi NIR 410-940 nm)
[ Dataset Primer Jambu Kristal (dataset/) ] ──► [ Pipeline ML & Model (models/) ]
                                                              │
                                            ┌─────────────────┴─────────────────┐
                                            ▼                                   ▼
                            [ Backend & Konveyor Daemon ]            [ Frontend Web Kios ]
                            (buahsafe-web-capture)                   (buahsafe-client)
                            Flask + SQLite + ESP32 WiFi              React 19 + TanStack + Tailwind
                            Server: HP t530 Mini PC                  Hosting: Vercel Production
```

Repositori ini berfungsi sebagai **pusat penelitian data sains, eksplorasi spektrum, dan repositori model machine learning** untuk mendeteksi kerusakan internal (busuk atau ulat larva lalat buah *Bactrocera carambolae*) pada jambu kristal secara non-destruktif.

---

## 🔬 Dataset Primer Jambu Kristal (`dataset/`)

Telah tersedia dataset primer transmisi optik/NIR hasil pengukuran 60 buah jambu kristal segar:

* **File Dataset:** [`dataset/buahsafe_jambu_kristal_dataset_final.csv`](dataset/buahsafe_jambu_kristal_dataset_final.csv)
* **Holdout Set Terkunci:** [`dataset/holdout_fruits.json`](dataset/holdout_fruits.json) (13 buah independen untuk evaluasi akhir).
* **Karakteristik:**
  * 60 buah independen (30 Normal, 30 Anomali).
  * 180 baris data (3 sudut rotasi per buah pada rotasi 120°).
  * 18 panjang gelombang (410, 435, 460, 485, 510, 535, 560, 585, 610, 645, 680, 705, 730, 760, 810, 860, 900, 940 nm).
  * Validasi tanah destruktif (*ground truth*) belah buah fisik.

Detail spesifikasi dan kamus data tersedia di [`dataset/README.md`](dataset/README.md).

---

## 📦 Model Machine Learning Terlatih (`models/`)

Model machine learning telah dilatih dan diuji menggunakan pemisahan bebas kebocoran data (`GroupKFold` by `fruit_id`):

1. **`buahsafe_svm_model.joblib` (Model Utama Produksi):**
   * Kernel: RBF (`C=10.0, gamma=0.1`) dengan `StandardScaler`.
   * Input: 6 kanal NIR (`nm730`, `nm760`, `nm810`, `nm860`, `nm900`, `nm940`).
   * **Recall Anomali:** 100% pada holdout set (Zero False Negatives / tidak ada buah rusak yang lolos).
2. **`buahsafe_rf_model.joblib` (Model Explainability / Pohon Keputusan):**
   * Memberikan peringkat *Feature Importance*: panjang gelombang 730 nm (Red-edge) dan 760–940 nm (NIR) mendominasi daya pisah kualitas.
3. **`buahsafe_lr_model.joblib` (Model Regresi Logistik Baseline):**
   * Memberikan koefisien log-odds linear untuk interpretasi arah korelasi per kanal.

Untuk membongkar jeroan matematis dan bobot model, jalankan:
```bash
python models/baca_dan_oprek_model.py
```

---

## 🚀 Menjalankan Pipeline Evaluasi & Notebook

### 1. Eksekusi Skrip Pipeline Otomatis:
```bash
python pipeline_jambu_kristal_ml.py
```
Skrip ini akan memuat dataset primer, menjalankan validasi silang `LeaveOneGroupOut` bebas *data leakage*, mengevaluasi performa pada 13 buah *holdout set*, dan mencetak laporan klasifikasi serta matriks konfusi.

### 2. Notebook Analisis & Eksplorasi:
* **Notebook Utama Jambu Kristal:** [`BuahSafe_Jambu_Kristal_ML_Pipeline_Utama.ipynb`](BuahSafe_Jambu_Kristal_ML_Pipeline_Utama.ipynb)
  *(Eksplorasi kurva transmisi normal vs anomali, pemisahan GroupKFold, pelatihan SVM, dan metrik evaluasi).*
* **Notebook Studi Pendahuluan:** [`BuahSafe_AS7265x_ML_Extensively_Explanatory_Colab.ipynb`](BuahSafe_AS7265x_ML_Extensively_Explanatory_Colab.ipynb)
  *(Studi kelayakan spektral sensor AS7265x pada sampel sekunder dengan penjelasan 15 pertanyaan refleksi).*

---

## 📖 Kamus Istilah Spektroskopi & Machine Learning

* **Spektroskopi Transmisi:** Metode melewatkan cahaya dari satu sisi objek menembus seluruh volume daging buah menuju sensor di sisi seberang, menangkap kerusakan internal yang tertutup kulit luar.
* **Near-Infrared (NIR):** Cahaya inframerah dekat (700–1100 nm) yang memiliki daya penetrasi tinggi ke dalam jaringan sel tumbuhan basah.
* **Red-Edge (730 nm):** Daerah transisi tajam antara absorpsi klorofil dan hamburan internal seluler; sangat sensitif terhadap *internal browning* dan kerusakan sel akibat aktivitas makan larva.
* **Overtone Air (940 nm):** Panjang gelombang serapan ikatan O-H molekul air. Jaringan busuk berair memiliki serapan transmisi yang jauh lebih drastis.
* **GroupKFold (Bebas Leakage):** Metode validasi silang di mana seluruh pindaian rotasi dari satu buah fisik yang sama diisolasi dalam satu fold agar model tidak 'menghafal' sidik jari buah yang sama.
* **Zero False Negatives:** Target utama QC BuahSafe; memastikan probabilitas meloloskan buah berulat/busuk ke pasar komersial ditekan hingga nol demi menjaga reputasi merek mitra.

---

## 📚 Panduan Riset & Integritas Bukti

Panduan kepatuhan bukti ilmiah dan batas klaim penelitian dapat dibaca di [`docs/RESEARCH_AND_EVIDENCE_GUIDE.md`](docs/RESEARCH_AND_EVIDENCE_GUIDE.md).
