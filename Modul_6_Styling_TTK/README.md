# Nama    : Hesti Febriyani
# NIM     : 24106050010

# Modul 6: Styling TTK, Responsive Design, dan Animasi

Folder ini berisi implementasi seluruh latihan praktikum dan analisis tugas menggunakan `tkinter` dan `ttk`.

## Struktur File
* `praktikum_1_1.py` — Perbandingan widget Tkinter standar vs `ttk`
* `praktikum_1_2.py` — Implementasi *Theme Switcher* dinamis
* `praktikum_2_1.py` — *Custom Styling* menggunakan `ttk.Style` dan `style.map()`
* `praktikum_2_2.py` — *Responsive Design* (Breakpoint Desktop, Tablet, Mobile)
* `praktikum_3_1.py` — Animasi & transisi halus (*Progress*, *Slide*, *Fade*) dengan `threading`
* `praktikum_3_2.py` — *Interactive System Dashboard* dengan pembaruan *real-time*

---

## Catatan Lingkungan Eksekusi & Penyesuaian Tampilan (Windows)
* **Rendering Tombol `ttk` di Windows:** Pada sistem operasi **Windows**, *theme* bawaan `ttk` (`vista` / `xpnative`) secara default mempertahankan gaya tombol native OS sehingga mengabaikan konfigurasi warna `background` kustom pada `ttk.Button` (misalnya tombol pada `praktikum_2_1.py` tetap tampil terang bawaan Windows). Untuk menampilkan warna latar belakang tombol kustom secara penuh, *theme* dapat dialihkan ke `clam` melalui `self.style.theme_use('clam')`.
* **Penyesuaian Dimensi Window:** Pada `praktikum_2_2.py`, batas lebar minimum (`minsize`) disesuaikan ke `380px` agar fitur simulasi *Mobile* (`400x600`, breakpoint `< 500px`) dapat berjalan optimal. Pada `praktikum_3_1.py`, tinggi jendela dan kontainer *sliding panel* disesuaikan (`800x650`) agar seluruh kontrol animasi termasuk tombol *Fade Out* dan *Fade In* tampil utuh pada layar beresolusi 768p.

---

## Ringkasan Hasil & Analisis Tugas

### 1. Dasar `ttk` & Theme Switching (`1.1` & `1.2`)
* **Perbandingan Tkinter vs `ttk`:** Kedua sisi berbagi variabel kontrol (`StringVar` dan `BooleanVar`) sehingga input tersinkronisasi secara langsung. Widget `ttk` tampil lebih modern dan mengikuti gaya native OS dibandingkan widget `tk` klasik.
* **Theme Switching:** Pemanggilan `self.style.theme_use(selected_theme)` melalui event `<<ComboboxSelected>>` mengubah tampilan seluruh widget secara serentak dan konsisten (mulai dari gaya datar pada `clam`, tampilan native Windows pada `vista`, hingga efek bevel 3D retro pada `classic`).

### 2. Styling Advanced & Responsive Design (`2.1` & `2.2`)
* **Custom Styling:** Penamaan style berhierarki (`Custom.TButton`, `Custom.TEntry`, `Title.TLabel`) memungkinkan kustomisasi elemen spesifik serta perubahan state interaktif (`active` dan `pressed`) melalui `style.map()`.
* **Responsive Design:** Event `<Configure>` mendeteksi perubahan lebar jendela secara langsung dan menyesuaikan tata letak dari **3 kolom** (Desktop $\ge 700\text{px}$), **2 kolom** (Tablet $500\text{–}699\text{px}$), hingga **1 kolom vertikal** (Mobile $< 500\text{px}$) beserta penyesuaian ukuran font dan padding.

### 3. Animasi & Real-time Dashboard (`3.1` & `3.2`)
* **Animasi dengan Threading:** Penggunaan `threading.Thread(..., daemon=True)` memisahkan proses perulangan animasi (`time.sleep()`) dari *main event loop* Tkinter sehingga antarmuka tetap responsif dan tidak mengalami *freeze*.
* **Interactive Dashboard:** Pembaruan waktu berjalan non-blocking menggunakan `root.after(1000, ...)`, sedangkan simulasi metrik (CPU, Memory, Network) berjalan di *background thread* dengan pembatasan buffer maksimal 50 data terakhir (*sliding window*) agar penggunaan memori tetap efisien.