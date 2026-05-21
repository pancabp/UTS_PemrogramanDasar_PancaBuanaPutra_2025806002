DOKUMENTASI FOLDER /C (Soal 1: Sistem Data Mahasiswa Terin)
1. Penjelasan ProgramProgram ini ditulis dalam bahasa C untuk memecahkan studi kasus perekapan nilai mahasiswa akhir semester oleh asisten dosen. Implementasi menggunakan konsep dasar tingkat lanjut yang meliputi:

Struct & Dynamic Memory (Linked List): Data dialokasikan secara dinamis menggunakan malloc() ke dalam simpul-simpul Singly Linked List, sehingga penggunaan memori bersifat adaptif (tidak hardcoded seperti array statis).

Pointer to Struct: Manipulasi simpul seperti penambahan data di akhir (addMahasiswa), pencarian data (searchMahasiswa), dan penghapusan data (deleteMahasiswa) menggunakan mekanisme pointer-to-pointer (head) agar perubahan langsung merefleksikan memori utama.

Memory Management: Jika fungsi hapus dijalankan, memori simpul yang bersangkutan akan dibersihkan secara eksplisit menggunakan perintah free() untuk mencegah terjadinya kebocoran memori (memory leak).
File I/O (CSV Export): Seluruh record mahasiswa yang aktif di memori dapat diekspor menjadi berkas teks terstruktur berekstensi data_mahasiswa.csv. 

2. Aturan Perhitungan NilaiNilai Akhir (NA): 
$(30\% \times \text{Tugas}) + (30\% \times \text{UTS}) + (40\% \times \text{UAS})$Huruf Mutu:$\text{NA} \ge 80.0 \rightarrow \mathbf{A}$$\text{NA} \ge 70.0 \rightarrow \mathbf{B}$$\text{NA} \ge 60.0 \rightarrow \mathbf{C}$$\text{NA} \ge 50.0 \rightarrow \mathbf{D}$$\text{NA} < 50.0 \rightarrow \mathbf{E}$

3. Contoh Hasil Output Program CTampilan Menu & Tabel Data di Layar CLI:
Plaintext
=== MENU MANAJEMEN MAHASISWA ===
1. Tambah Data Mahasiswa
2. Tampilkan Tabel Data
3. Cari Mahasiswa (NIM)
4. Hapus Mahasiswa (NIM)
5. Simpan ke File CSV
6. Keluar
Pilihan Anda: 2

=========================================================================
| Nama            | NIM        | Tugas | UTS   | UAS   | N. Akhir   | Mutu |
=========================================================================
| Rina            | 2310001    | 80.0  | 85.0  | 90.0  | 85.50      | A    |
| Doni            | 2310002    | 60.0  | 55.0  | 70.0  | 61.50      | C    |
=========================================================================

Isi Berkas data_mahasiswa.csv setelah diekspor:Cuplikan kodeNama,NIM,Tugas,UTS,UAS,NilaiAkhir,Mutu
Rina,2310001,80.0,85.0,90.0,85.50,A
Doni,2310002,60.0,55.0,70.0,61.50,C

4. Instruksi Menjalankan Program CBuka terminal di dalam direktori proyek, kemudian jalankan baris perintah berikut:Bash# Kompilasi berkas utama
gcc C/main.c -o C/program_mhs

# Eksekusi program biner hasil kompilasi
./C/program_mhs