# Dataset Primer Spektroskopi NIR Jambu Kristal (BuahSafe)

Dataset ini merupakan dataset primer transmisi optik/NIR 18-kanal (*Near-Infrared*) yang diakuisisi langsung dari buah jambu kristal (*Psidium guajava L.*) segar untuk membedakan antara buah berkualitas **Normal** (sehat/layak jual) dan **Anomali** (terserang larva lalat buah *Bactrocera carambolae* / pembusukan internal tersembunyi).

---

## 📊 Ringkasan Spesifikasi Dataset

| Parameter | Spesifikasi |
|---|---|
| **Jumlah Buah Fisik** | 60 buah independen (`fruit_id`: 30 Normal, 30 Anomali) |
| **Jumlah Pindaian (*Scans*)** | 180 baris (3 pindaian per buah pada rotasi 120°) |
| **Sensor Optik** | Triad AS7265x (AS72651, AS72652, AS72653) — 18 kanal spektral |
| **Rentang Panjang Gelombang** | 410 nm hingga 940 nm (410, 435, 460, 485, 510, 535, 560, 585, 610, 645, 680, 705, 730, 760, 810, 860, 900, 940 nm) |
| **Mode Pengukuran** | **Transmisi Optik Langsung** (Lampu halogen 12V 20W di satu sisi, sensor di sisi seberang) |
| **Ground Truth Destruktif** | Uji belah fisik setelah pindaian non-destruktif selesai |
| **Kanal Model Produksi** | 6 kanal utama: `nm730`, `nm760`, `nm810`, `nm860`, `nm900`, `nm940` |
| **Holdout Test Set Terkunci** | 13 buah independen (`ml/holdout_fruits.json`), tidak pernah disentuh saat pelatihan model |

---

## 🔬 Struktur Kolom (`buahsafe_jambu_kristal_dataset_final.csv`)

| Nama Kolom | Tipe Data | Deskripsi |
|---|---|---|
| `fruit_id` | String | Pengenal unik buah fisik (mis. `AMAN_001` s.d. `AMAN_030`, `BOSOK_001` s.d. `BOSOK_030`). Digunakan untuk pengelompokan `GroupKFold` agar tidak terjadi kebocoran data (*data leakage*). |
| `scan_no` | Integer | Nomor pindaian rotasi (1, 2, atau 3). |
| `nm410` s.d. `nm940` | Float | Intensitas cahaya transmisi mentah yang diterima fotodioda sensor AS7265x pada panjang gelombang terkait. |
| `temp_c` | Float | Suhu ambien ruang sortasi saat pengukuran (°C). |
| `humidity_pct` | Float | Kelembapan relatif ruang sortasi saat pengukuran (%). |
| `label` | String | Kondisi internal nyata hasil uji belah destruktif: `normal` atau `anomali`. |

---

## 🛡️ Prinsip Validasi Ilmiah

1. **Pemisahan Berbasis Buah Fisik (`GroupKFold`):**
   Semua 3 pindaian rotasi dari satu buah fisik yang sama wajib selalu berada dalam lipatan (*fold*) latih yang sama atau uji yang sama. Pemisahan baris acak (*random shuffle*) dilarang keras karena menyebabkan *optimistic bias* palsu.
2. **Holdout Test Set (`holdout_fruits.json`):**
   Terdapat 13 buah fisik (7 buah `AMAN` dan 6 buah `BOSOK`) yang dipisahkan secara permanen dengan *random seed* 42. Dataset ini dipakai sebagai evaluasi akhir *hardware simulator* dan kalibrasi ambang putusan produksi.
3. **Fokus Recall Anomali (Zero False Negatives):**
   Dalam bisnis buah segar premium, meloloskan buah berulat (*False Negative*) jauh lebih merusak reputasi merek daripada menolak buah normal (*False Positive*). Model produksi dikalibrasi untuk meminimalkan *False Negative* hingga 0 pada holdout set.
