DOKOKUMENTASI FOLDER /Python (Soal 2, 3, & 4)
Soal 2: Game "Guess Battle"
1. Penjelasan Program
Sebuah game simulasi turnamen tebak angka interaktif berbasis CLI (Command Line Interface). Program ini dipecah secara modular guna memenuhi standar arsitektur kode yang bersih (clean code):

main.py: Mengatur alur login pemain dan inisialisasi urutan permainan.

game.py: Menampung logika inti tebakan, batasan batas atas/bawah angka acak (random), dan validasi input numerik menggunakan blok kontrol try-except untuk menangkap galat ValueError.

scoreboard.py: Berfungsi membaca dan merekam pencapaian skor ke dokumen scores.json secara dinamis, serta melakukan operasi sorting untuk menampilkan peringkat Top 5.

2. Aturan Permainan & Level
Pemain harus menyelesaikan level secara berurutan. Jika gagal menebak pada salah satu tingkat, permainan langsung berakhir (Game Over).
Level 1: Jangkauan angka 1-10 | Batas 3 Percobaan | Pengali Poin: 50
Level 2: Jangkauan angka 1-50 | Batas 5 Percobaan | Pengali Poin: 100
Level 3: Jangkauan angka 1-100 | Batas 7 Percobaan | Pengali Poin: 200
Rumus Skor Per Level: $\text{Sisa Percobaan} \times \text{Pengali Poin Level}$

3. Contoh Tampilan Layar Game (Colorama Effects)
(Output visual di terminal menggunakan warna teks bawaan library colorama)
=== WELCOME TO GUESS BATTLE GAME ===
Masukkan nama login Anda: Rina

--- MEMASUKI LEVEL 1 (Tebak angka 1-10) ---
Anda memiliki 3 percobaan.
Masukkan tebakan Anda (3x sisa): 5
Terlalu RENDAH!
Masukkan tebakan Anda (2x sisa): 8
HEBAT! Tebakan benar. Anda mendapatkan 100 poin.

... [Permainan Berlanjut Hingga Level 3] ...

Permainan selesai! Total skor Rina: 230 pts

======= TOP 5 SCORE =======
1. Rina       230 pts
2. Budi       200 pts
3. Dinda      170 pts
===========================

4. Instruksi Menjalankan Game
Bash
# Pastikan dependensi eksternal terinstal
pip install colorama

# Jalankan skrip utama game
python Python/main.py

Soal 3: Analisis Teks Otomatis
1. Penjelasan Program
Program utilitas tingkat lanjut untuk melakukan text-mining/analisis statistik dari dokumen mentah teks tidak terstruktur (teks.txt). Modul dipisah menjadi analyzer.py (pemrosesan data) dan main_analyzer.py (antarmuka CLI menggunakan library standar argparse).

Fitur analisis mencakup:

Pencacahan baris, total kata, serta klasifikasi total huruf vokal dan konsonan.

Penyaringan token kata dari simbol baca seperti koma atau titik.

Ekstraksi top 5 frekuensi kata menggunakan objek collections.Counter.

Pembuatan grafik horizontal berbasis representasi karakter ASCII (#).

2. Contoh Berkas Output (report.txt)
Apabila file teks.txt dianalisis, program akan menerbitkan ringkasan laporan otomatis seperti berikut:
=== LAPORAN STATISTIK TEKS ===
Jumlah baris           : 12
Jumlah kata            : 48
Jumlah huruf vokal     : 114
Jumlah huruf konsonan  : 185

=== 5 KATA TERBANYAK & GRAFIK FREKUENSI ===
python       : ######### (9x)
program      : ###### (6x)
belajar      : ### (3x)
dasar        : ## (2x)
kuliah       : # (1x)

Soal 4: Konversi Data Lintas Bahasa (CSV ke JSON)
1. Penjelasan Program
Program ini menjadi solusi jembatan (interoperabilitas data) yang mensimulasikan integrasi backend akademik. File CSV (data_mahasiswa.csv) yang sebelumnya dicetak oleh mesin program berbasis bahasa C (Soal 1), dibaca dan diparsing menggunakan modul internal csv.DictReader di Python.

Program kemudian mengolah agregasi statistik berupa nilai rata-rata (mean average) dari seluruh nilai akhir mahasiswa, mencetaknya secara bersih ke layar, lalu mengonversi struktur objek tabel tersebut menjadi berkas terstruktur data_mahasiswa.json.