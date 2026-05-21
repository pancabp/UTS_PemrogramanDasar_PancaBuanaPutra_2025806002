import csv
import json
import os

def konversi_csv_ke_json(csv_file="data_mahasiswa.csv", json_file="data_mahasiswa.json"):
    if not os.path.exists(csv_file):
        print(f"File '{csv_file}' tidak ditemukan. Jalankan program C terlebih dahulu untuk generate datanya.")
        return

    data_mahasiswa = []
    total_nilai_akhir = 0.0
    jumlah_mahasiswa = 0

    print("\n" + "="*20 + " MEMBACA DATA CSV MAHASISWA " + "="*20)
    print(f"{'Nama':<15} | {'NIM':<10} | {'Nilai Akhir':<12} | {'Mutu':<5}")
    print("-"*60)

    with open(csv_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            nama = row['Nama']
            nim = row['NIM']
            nilai_akhir = float(row['NilaiAkhir'])
            mutu = row['Mutu']

            print(f"{nama:<15} | {nim:<10} | {nilai_akhir:<12.2f} | {mutu:<5}")

            total_nilai_akhir += nilai_akhir
            jumlah_mahasiswa += 1

            data_mahasiswa.append({
                "nama": nama,
                "nim": nim,
                "nilai_akhir": nilai_akhir,
                "mutu": mutu
            })

    print("-"*60)
    
    if jumlah_mahasiswa > 0:
        rata_rata = total_nilai_akhir / jumlah_mahasiswa
        print(f"Total Mahasiswa        : {jumlah_mahasiswa}")
        print(f"Rata-rata Nilai Akhir  : {rata_rata:.2f}")
    else:
        print("Tidak ada data mahasiswa terproses.")
        return

    with open(json_file, 'w', encoding='utf-8') as jf:
        json.dump(data_mahasiswa, jf, indent=4)
        
    print(f"\nSukses! Data dikonversi dan disimpan ke dalam file format '{json_file}'.")

if __name__ == "__main__":
    konversi_csv_ke_json()