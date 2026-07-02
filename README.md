# BuahSafe Preliminary Machine Learning Study
## Extremely Explanatory Notebook for Non-AI Readers

Repositori ini berisi penelitian pendahuluan dan **pipeline pemodelan Machine Learning (ML)** untuk proyek **BuahSafe**. Notebook yang disediakan dirancang sangat komunikatif dan informatif (*Extensively Explanatory*) sehingga dapat dipahami oleh pembaca non-teknis atau non-praktisi AI.

---

## 🎯 Tujuan & Konteks Bisnis

Dalam pengembangan sistem **BuahSafe**, perangkat keras direncanakan menggunakan sensor spektroskopi inframerah dekat/visual optik 18-kanal (**AS7265x**). 

Penelitian dalam repositori ini memanfaatkan dataset sekunder reflektansi biji kopi sangrai yang diukur menggunakan sensor AS7265x sebagai **sarana latihan dan pembuktian konsep (*Proof of Concept*) pipeline analisis spektral**. Pipeline ini mencakup:
- Audit dan pembersihan data sensor spektroskopi.
- **Normalisasi nama file dataset** dan penanganan otomatis pengunduhan langsung dari jaringan **IPFS Pinata** tanpa kendala pemblokiran HTTP (`403 Forbidden`).
- Pelatihan model klasifikasi (*Logistic Regression*, *Support Vector Machine*, *Random Forest*).
- *Hyperparameter tuning* dan *feature selection benchmark*.
- Analisis regresi nilai *Agtron*.

> [!NOTE]
> Karena objek biologis dataset latihan ini adalah kopi (bukan buah jambu kristal), model yang dihasilkan di sini merupakan **pipeline pendahuluan**. Saat dataset primer BuahSafe tersedia, seluruh alur kerja ini dapat langsung diterapkan dengan mengganti dataset dan targetnya.

---

## 📂 Struktur Repositori

```text
buahsafe/
├── BuahSafe_AS7265x_ML_Extensively_Explanatory_Colab.ipynb  # Notebook utama penelitian
├── Reflectance intensity dataset...csv                     # Dataset lokal (opsional/fallback)
├── .gitignore                                              # Pengaturan pengabaian file Git
└── README.md                                               # Dokumentasi proyek
```

---

## 🚀 Cara Menjalankan Secara Lokal

Untuk memastikan pengujian berjalan terisolasi dan tidak mencemari instalasi Python global Anda, disarankan menggunakan *Virtual Environment*.

### 1. Buat dan Aktifkan Virtual Environment
Di sistem operasi **Windows (PowerShell)**:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Pasang Dependensi
Pasang pustaka yang dibutuhkan di dalam virtual environment:
```powershell
pip install numpy pandas matplotlib scikit-learn joblib jupyter
```

### 3. Jalankan Jupyter Notebook
Buka notebook interaktif:
```powershell
jupyter notebook BuahSafe_AS7265x_ML_Extensively_Explanatory_Colab.ipynb
```

---

## ☁️ Menjalankan di Google Colab

Notebook ini kompatibel langsung dengan **Google Colab**. Anda cukup mengunggah file `BuahSafe_AS7265x_ML_Extensively_Explanatory_Colab.ipynb` ke Colab atau membukanya langsung melalui integrasi GitHub Google Colab. Notebook secara otomatis akan mengunduh dataset yang dibutuhkan dari jaringan IPFS.

---

## 🔧 Fitur Unggulan Pipeline

1. **Anti-Bot Blocking (403 Forbidden Prevention):** Unduhan dataset dari gateway IPFS Pinata (`purple-given-lark-169.mypinata.cloud`) menggunakan *User-Agent* peramban modern sehingga bebas dari pemblokiran *Cloudflare/Pinata*.
2. **Normalisasi Nama Dataset Otomatis:** Apabila file dataset diunduh secara manual atau memiliki nama CID mentah (`bafkreieqtfnas62ufy5j5mevga7clt4fmokbnrovbtodv6zsbt7gurnfai`), sistem secara otomatis mendeteksi dan merubah namanya sesuai standar pipeline sebelum pemodelan dimulai.
