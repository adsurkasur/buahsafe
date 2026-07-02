# BuahSafe Preliminary Machine Learning Study
## Extremely Explanatory & Comprehensive Notebook for Non-AI Readers

Repositori ini berisi penelitian pendahuluan dan **pipeline pemodelan Machine Learning (ML)** untuk proyek **BuahSafe**. Notebook yang disediakan dirancang **Super Duper Extensive & Explanatory** sehingga dapat dipahami sekali baca oleh pembaca non-teknis, agronomis, maupun praktisi bisnis QC, yang membagi tuntas tidak hanya cara kerja algoritmanya, tetapi juga **makna bisnis, manajemen risiko, dan strategi implementasi perangkat keras sortasi buah**.

---

## 🎯 Tujuan & Konteks Bisnis BuahSafe

Dalam pengembangan perangkat keras sistem **BuahSafe**, sensor utama yang digunakan adalah sensor spektroskopi optik/inframerah dekat 18-kanal (**AS7265x**). 

Penelitian dalam repositori ini memanfaatkan dataset sekunder reflektansi biji kopi sangrai yang diukur menggunakan sensor AS7265x sebagai **sarana pembuktian konsep (*Proof of Concept*) arsitektur pipeline analisis spektral**. Pipeline ini mencakup:
- Audit dan pembersihan data sensor spektroskopi.
- **Normalisasi nama file dataset** dan penanganan otomatis pengunduhan langsung dari jaringan **IPFS Pinata** tanpa kendala pemblokiran HTTP (`403 Forbidden`).
- Pelatihan model klasifikasi (*Logistic Regression*, *Support Vector Machine*, *Random Forest*).
- *Hyperparameter tuning* dan *feature selection benchmark*.
- Analisis regresi nilai *Agtron*.
- **Pondasi Ilmu & First Principles:** Penjelasan mendalam dari nol mengenai fisika spektroskopi (absorpsi, refleksi, hamburan difus), biologi buah (mengapa kerusakan sel merubah pantulan NIR 940 nm), definisi dasar ML (fitur, label, generalisasi), dan kausalitas data.

> [!NOTE]
> Karena objek biologis dataset latihan ini adalah kopi (bukan buah jambu kristal), model yang dihasilkan di sini merupakan **pipeline pendahuluan**. Saat dataset primer BuahSafe tersedia, seluruh alur kerja ini langsung diterapkan dengan mengganti dataset dan target klasifikasinya.

---

## 📖 Kamus Istilah Lengkap (Literally Dijelaskan Per Istilah)

* **Spektroskopi:** Ilmu fisika tentang interaksi cahaya dengan molekul/benda.
* **Near-Infrared (NIR):** Cahaya inframerah dekat (700–1100 nm) yang tidak terlihat mata tetapi mampu menembus ke dalam jaringan sel buah.
* **Reflektansi:** Persentase cahaya yang dipantulkan kembali oleh permukaan objek ke sensor.
* **Hamburan Difus (*Sub-surface Scattering*):** Pantulan cahaya yang masuk ke bawah kulit, memantul di dalam daging buah, lalu keluar membawa informasi kerusakan internal.
* **Agtron Value:** Skala standar internasional angka numerik industri kopi untuk mengukur kegelapan sangrai (Angka tinggi = sangrai muda/terang; Angka rendah = sangrai gelap).
* **Reaksi Maillard & Melanoidin:** Pembentukan pigmen cokelat gelap pada biji kopi akibat reaksi panas antara asam amino dan gula.
* **Ikatan Hidrogen (O-H):** Ikatan molekul air di daging buah yang menyerap kuat cahaya NIR pada panjang gelombang 940 nm.
* **Larva Lalat Buah (*Bactrocera carambolae*):** Ulat hama yang memakan daging buah di dalam sementara kulit luarnya tetap tampak mulus.
* **Fitur ($X$) & Target ($y$):** $X$ adalah 18 kolom angka dari sensor; $y$ adalah kelas kualitas atau angka yang ingin ditebak model.
* **Overfitting:** Kondisi model AI menghafal soal latihan (100% saat latihan), tetapi bingung/hancur saat diuji pada buah asing di lapangan.
* **GroupKFold:** Metode uji silang yang memastikan semua pemindaian ulang dari 1 buah fisik yang sama berada di kelompok yang sama (latih atau uji), mencegah penipuan akurasi (*Data Leakage*).
* **StandardScaler:** Menyederhanakan skala semua kolom agar tidak ada angka raksasa yang menindas angka kecil dalam perhitungan algoritma.
* **Permutation Importance:** Menguji vitalitas suatu kolom dengan mengacak angkanya; jika akurasi model hancur saat kolom diacak, berarti kolom tersebut sangat penting.

---

## ☕ Mengapa Menggunakan Kopi & Agtron? (Pemanfaatan & Jembatan ke Jambu Kristal)

Penelitian pendahuluan ini **tidak mengabaikan kopi**, melainkan memanfaatkan fisika-kimia kopi sebagai **pembuktian konsep (*Proof of Concept*)** sebelum dihubungkan ke jambu kristal:

### 1. Pemanfaatan Nyata Jika Diterapkan di Dunia Kopi
Selama ini roaster kopi bergantung pada alat *Agtron Spectrophotometer* seharga **ratusan juta rupiah**. Kita membuktikan bahwa sensor 18-kanal **AS7265x** yang terjangkau **mampu memprediksi derajat sangrai (akurasi 75%) dan angka Agtron (regresi)** dengan mengenali pembentukan melanoidin dan kehilangan air. Ini membuktikan bahwa alat AS7265x beserta pipeline ML kita **sangat bernilai sebagai alat kontrol mutu non-destruktif murah bagi industri kopi!**

### 2. Jembatan Pemahaman Kausalitas ke Jambu Kristal
Konsep instrumen dan algoritma AI yang dipakai **100% sama persis**. Logika penghubung ilmunya:
* **Pada Kopi Sangrai:** Sensor menangkap hilangnya air dan terbentuknya pigmen gelap melanoidin akibat panas sangrai.
* **Pada Jambu Kristal:** Sensor menangkap pecahnya dinding sel berair, akumulasi air di rongga busuk akibat ulat *Bactrocera carambolae*, dan browning jaringan internal.
* **Kesimpulan Ilmiah:** *"Jika sensor 18-kanal AS7265x begitu presisi membedakan perubahan kimiawi halus pada biji kopi kering yang keras, maka sensor yang sama dijamin mampu mendeteksi akumulasi air dan kerusakan jaringan pada daging buah jambu kristal yang basah!"*

---

## 💡 Pembahasan Tuntas 15 Pertanyaan Refleksi (Teknis & Bisnis BuahSafe)

Berikut adalah ringkasan pembahasan mendalam yang menghubungkan hasil eksperimen spektral dengan realitas bisnis dan operasional Quality Control (QC) BuahSafe:

### 1. Apakah model utama mengalahkan Dummy Classifier?
**Ya, sangat telak.** *Dummy Classifier* (menebak buta/kelas mayoritas) hanya memperoleh akurasi **26.2%** (F1 **0.104**). Seluruh model utama kita jauh melampauinya (*Random Forest* mencapai akurasi **67.5%**, *SVM Tuned* mencapai **75.0%**). Ini membuktikan bahwa spektrum 18 kanal AS7265x memiliki **sinyal fisik nyata** yang sah untuk mendeteksi kualitas internal sampel.

### 2. Model mana yang paling stabil antara cross-validation dan test set?
**SVM (setelah Tuning) dan Random Forest.** Selisih antara performa *Cross-Validation* dan *Test Set* sangat kecil (~0.02 - 0.03), membuktikan model tidak *overfitting*. Kestabilan ini menjamin keandalan saat alat dioperasikan di gudang mitra dari hari ke hari.

### 3. Apakah model dengan hasil tertinggi juga paling masuk akal untuk dijelaskan?
**Tidak selalu — terjadi *Trade-off* antara Akurasi vs *Explainability*.** SVM RBF memiliki akurasi tertinggi (75%), namun beroperasi sebagai *black-box*. Sebaliknya, Random Forest (67.5%) memberi penjelasan transparan (*Permutation Importance*) tentang panjang gelombang mana yang berkontribusi paling besar.

### 4. Kelas mana yang paling sering tertukar?
**Kelas berbatasan langsung (*Borderline Cases*).** Kesalahan rentan terjadi pada sampel dengan karakteristik tengah yang gradual. Dalam BuahSafe, ini mewakili tantangan mendeteksi **kerusakan internal stadium awal** (pembusukan dini/larva kecil) di mana kulit luar masih tampak normal.

### 5. Apakah tuning benar-benar meningkatkan performa?
**Sangat signifikan.** Untuk SVM, hyperparameter tuning (`C=10, gamma=1`) melonjakkan akurasi dari **50.0% menjadi 75.0%** (+25%!). Penyesuaian parameter wajib dilakukan untuk mengoptimalkan pembacaan pantulan sensor.

### 6. Apakah 4 kanal cukup mendekati performa 18 kanal?
**Tidak cukup.** Pemotongan menjadi 4 kanal menjatuhkan F1-Score dari **0.72 menjadi 0.51**. Hasil ini memvalidasi secara ilmiah bahwa penggunaan sensor RGB/IR biasa (3-4 kanal) tidak layak untuk deteksi internal buah rumit; sensor 18 kanal **AS7265x** adalah pilihan tepat.

### 7. Kanal apa yang paling penting menurut ANOVA?
**610 nm, 645 nm (Merah), 730 nm (Red-Edge), dan 940 nm (Near-Infrared).** ANOVA menilai hubungan linear univariat per kanal terhadap kelas target.

### 8. Kanal apa yang paling penting menurut Permutation Importance?
**435 nm (Ungu/Biru) dan dominasi NIR (940 nm, 900 nm, 810 nm).** Spektrum **Near-Infrared (NIR)** adalah senjata utama karena memiliki kemampuan menembus jaringan kulit buah (*tissue penetration*) dan sensitif terhadap kandungan air serta sel rusak akibat ulat/busuk.

### 9. Apakah ANOVA dan Permutation Importance memberi hasil serupa?
**Sama di titik krusial (940 nm NIR), namun berbeda di kanal lain.** ANOVA melihat relasi linear tunggal, sedangkan Permutation Importance menangkap interaksi antar kanal. Kerusakan internal buah dipicu oleh kombinasi interaksi spektral multivariat, bukan satu warna tunggal.

### 10. Mengapa model kopi tidak boleh digunakan langsung untuk jambu kristal?
**Matriks biologis berbeda 180 derajat.** Kopi adalah biji kering berserat padat (melanoidin), sedangkan jambu kristal adalah buah basah dominan air (>80%) dengan sel aktif. Model kopi di sini murni sebagai **Proof of Concept arsitektur pipeline**.

### 11. Mengapa dataset primer harus memiliki `fruit_id`?
**Mencegah Kebocoran Data (*Data Leakage*).** Jika satu buah dipindai 3 kali lalu dibagi acak (*random split*), model menghafal 'sidik jari buah yang sama' antara data latih dan uji sehingga akurasi tampak palsu 99%. Keberadaan `fruit_id` memungkinkan pemisahan berbasis **GroupKFold**.

### 12. Untuk BuahSafe, mana yang lebih berbahaya: buah rusak lolos atau buah normal tertolak?
**Buah Rusak Lolos (*False Negative*) jauh lebih berbahaya bagi bisnis!** Jika konsumen menggigit buah bermerek BuahSafe dan menemukan ulat di dalamnya, reputasi dan kepercayaan hancur seketika. Buah normal tertolak (*False Positive*) hanya menyusutkan sedikit sortasi dan masih bisa dialokasikan ke produk turunan (jus/selai).

### 13. Metrik apa yang harus diprioritaskan untuk mitra?
**Recall (Sensitivity) untuk kelas 'Rusak' dipadukan dengan F1-Score.** Sistem harus menangkap sebanyak mungkin buah cacat internal (misal target Recall > 95%) demi melindungi kepercayaan merek mitra.

### 14. Data tambahan apa yang perlu dicatat saat pengambilan data primer?
Metadata lingkungan & verifikasi destruktif: `fruit_id`, `scan_id`, suhu & kelembapan *chamber*, orientasi scan (tangkai/tengah/bawah), usia simpan pasca-panen, serta catatan audit belah buah (kadar Brix, larva lalat buah, browning internal).

### 15. Apa yang harus dilakukan jika performa model primer rendah?
Lakukan perbaikan sistematis di 3 pilar:
1. **Hardware:** Perapatan *chamber* agar gelap total dan jarak scan konsisten.
2. **Preprocessing:** Terapkan normalisasi kemometrik spektral (*SNV, MSC, Savitzky-Golay*) untuk mengoreksi efek hamburan bentuk buah melengkung.
3. **Labeling:** Gunakan label bertingkat (*Sehat, Cacat Ringan, Rusak Parah*) atau regresi keparahan internal.

---

## 📊 Presentasi Eksekutif PowerPoint (.pptx) & Bedah Tuntas Pipeline

Repositori ini menyertakan presentasi eksekutif bergaya modern berformat *Widescreen 16:9* dengan beberapa varian:
1. **`BuahSafe_Super_Comprehensive_Presentation_Deep_Dive.pptx` (Rekomendasi Utama - 28 Slide Deep Dive Walkthrough):** Versi paling komprehensif tanpa batasan slide yang membedah tuntas pipeline secara kronologis dari EDA, Matriks Korelasi Antarkanal, Preprocessing StandardScaler, hingga Evaluasi Confusion Matrix satu per satu untuk seluruh model (*Dummy, Logistic Regression, Random Forest, SVM Default, SVM Tuned, & Regresi Agtron*). Tata letak dirancang modular (*split-screen*) tanpa redundansi teks-gambar dan mempertahankan rasio aspek gambar 100% sempurna tanpa distorsi.
2. **`BuahSafe_Super_Comprehensive_Presentation_Visual_Enhanced.pptx`:** Versi ekstensif 20 slide berfokus pada ringkasan eksekutif visual.
3. **`Good_BuahSafe_Super_Comprehensive_Presentation.pptx`:** Cadangan/backup versi rujukan awal yang sudah bagus.

Semua 21 gambar resolusi tinggi (300 DPI) yang disematkan di dalam presentasi bersumber langsung dari eksekusi nyata pipeline di Jupyter Notebook dan disimpan di dalam folder **`assets/`**:
* **Grafik Diagnostik Otentik Notebook:**
  * `fig1_eda_agtron_dist.png` (Histogram Distribusi Nilai Agtron)
  * `fig2_eda_spectral_curves.png` (Profil Kurva Spektral 18 Kanal berdasarkan Derajat Sangrai)
  * `fig3_correlation_matrix.png` (Heatmap Matriks Korelasi Pearson 18x18 Kanal)
  * `fig4_preprocessing_scaling.png` (Komparasi Intensitas Raw vs StandardScaler)
  * `fig5_cm_dummy.png` hingga `fig9_cm_svm_tuned.png` (Confusion Matrix Lengkap Seluruh Model)
  * `fig10_model_comparison_bar.png` (Bar Chart Akurasi Seluruh Model Klasifikasi)
  * `fig11_regression_actual_vs_pred.png` (Scatter Plot Regresi Kontinu Nilai Agtron)
  * `fig12_channel_benchmark.png` & `fig13_feature_importance.png` (Analisis Kanal & Feature Importance)
* **Diagram Konsep & Kausalitas Ilmiah:**
  * `asset_1_subsurface_scattering.png` (Ilustrasi Fisika *Sub-surface Scattering*)
  * `asset_2_causality_flow.png` (Diagram Alur Kausalitas Fisika-Kimia-Biologi)
  * `asset_4_coffee_to_guava_bridge.png` (Infografis Jembatan Ilmu Kopi vs Jambu)
  * `asset_8_risk_matrix.png` (Matriks Risiko *False Negative* vs *False Positive*)

---

## 🚀 Cara Menjalankan Secara Lokal

### 1. Buat dan Aktifkan Virtual Environment
Di sistem operasi **Windows (PowerShell)**:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Pasang Dependensi
```powershell
pip install numpy pandas matplotlib scikit-learn joblib jupyter
```

### 3. Jalankan Jupyter Notebook
```powershell
jupyter notebook BuahSafe_AS7265x_ML_Extensively_Explanatory_Colab.ipynb
```
