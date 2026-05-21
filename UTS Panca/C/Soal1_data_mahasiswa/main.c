#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Mahasiswa {
    char nama[50];
    char nim[15];
    float tugas;
    float uts;
    float uas;
    float nilai_akhir;
    char mutu;
    struct Mahasiswa* next;
} Mahasiswa;

void hitungNilai(Mahasiswa* m) {
    // 40% UAS, 30% UTS, 30% tugas
    m->nilai_akhir = (0.30 * m->tugas) + (0.30 * m->uts) + (0.40 * m->uas);
    
    if (m->nilai_akhir >= 80.0) m->mutu = 'A';
    else if (m->nilai_akhir >= 70.0) m->mutu = 'B';
    else if (m->nilai_akhir >= 60.0) m->mutu = 'C';
    else if (m->nilai_akhir >= 50.0) m->mutu = 'D';
    else m->mutu = 'E';
}

void addMahasiswa(Mahasiswa** head) {
    Mahasiswa* nodeBaru = (Mahasiswa*)malloc(sizeof(Mahasiswa));
    if (!nodeBaru) {
        printf("Gagal alokasi memori!\n");
        return;
    }
    
    printf("\n--- Input Data Mahasiswa ---\n");
    printf("Nama      : "); scanf(" %[^\n]", nodeBaru->nama);
    printf("NIM       : "); scanf("%s", nodeBaru->nim);
    printf("Nilai Tugas: "); scanf("%f", &nodeBaru->tugas);
    printf("Nilai UTS  : "); scanf("%f", &nodeBaru->uts);
    printf("Nilai UAS  : "); scanf("%f", &nodeBaru->uas);
    
    hitungNilai(nodeBaru);
    nodeBaru->next = NULL;
    
    if (*head == NULL) {
        *head = nodeBaru;
    } else {
        Mahasiswa* temp = *head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = nodeBaru;
    }
    printf("Data berhasil ditambahkan!\n");
}

void printTabel(Mahasiswa* head) {
    if (head == NULL) {
        printf("\nLinked list kosong, tidak ada data.\n");
        return;
    }
    printf("\n=========================================================================\n");
    printf("| %-15s | %-10s | %-5s | %-5s | %-5s | %-10s | %-4s |\n", 
           "Nama", "NIM", "Tugas", "UTS", "UAS", "N. Akhir", "Mutu");
    printf("=========================================================================\n");
    Mahasiswa* temp = head;
    while (temp != NULL) {
        printf("| %-15s | %-10s | %-5.1f | %-5.1f | %-5.1f | %-10.2f | %-4c |\n",
               temp->nama, temp->nim, temp->tugas, temp->uts, temp->uas, temp->nilai_akhir, temp->mutu);
        temp = temp->next;
    }
    printf("=========================================================================\n");
}

void searchMahasiswa(Mahasiswa* head, char* nimCari) {
    Mahasiswa* temp = head;
    while (temp != NULL) {
        if (strcmp(temp->nim, nimCari) == 0) {
            printf("\nData Ditemukan:\n");
            printf("Nama: %s\nNIM: %s\nNilai Akhir: %.2f\nHuruf Mutu: %c\n", 
                   temp->nama, temp->nim, temp->nilai_akhir, temp->mutu);
            return;
        }
        temp = temp->next;
    }
    printf("\nMahasiswa dengan NIM %s tidak ditemukan.\n", nimCari);
}

void deleteMahasiswa(Mahasiswa** head, char* nimHapus) {
    Mahasiswa* temp = *head;
    Mahasiswa* prev = NULL;
    
    if (temp != NULL && strcmp(temp->nim, nimHapus) == 0) {
        *head = temp->next;
        free(temp);
        printf("\nData NIM %s berhasil dihapus dan memori di-free.\n", nimHapus);
        return;
    }
    
    while (temp != NULL && strcmp(temp->nim, nimHapus) != 0) {
        prev = temp;
        temp = temp->next;
    }
    
    if (temp == NULL) {
        printf("\nData NIM %s tidak ditemukan untuk dihapus.\n", nimHapus);
        return;
    }
    
    prev->next = temp->next;
    free(temp);
    printf("\nData NIM %s berhasil dihapus dan memori di-free.\n", nimHapus);
}

void saveToCSV(Mahasiswa* head) {
    FILE* file = fopen("data_mahasiswa.csv", "w");
    if (!file) {
        printf("Gagal membuka/membuat file CSV!\n");
        return;
    }
    
    fprintf(file, "Nama,NIM,Tugas,UTS,UAS,NilaiAkhir,Mutu\n");
    
    Mahasiswa* temp = head;
    while (temp != NULL) {
        fprintf(file, "%s,%s,%.1f,%.1f,%.1f,%.2f,%c\n",
                temp->nama, temp->nim, temp->tugas, temp->uts, temp->uas, temp->nilai_akhir, temp->mutu);
        temp = temp->next;
    }
    
    fclose(file);
    printf("\nSeluruh data sukses disimpan ke 'data_mahasiswa.csv'.\n");
}

int main() {
    Mahasiswa* head = NULL;
    int pilihan;
    char nimTarget[15];
    
    do {
        printf("\n=== MENU MANAJEMEN MAHASISWA ===\n");
        printf("1. Tambah Data Mahasiswa\n");
        printf("2. Tampilkan Tabel Data\n");
        printf("3. Cari Mahasiswa (NIM)\n");
        printf("4. Hapus Mahasiswa (NIM)\n");
        printf("5. Simpan ke File CSV\n");
        printf("6. Keluar\n");
        printf("Pilihan Anda: ");
        scanf("%d", &pilihan);
        
        switch(pilihan) {
            case 1: addMahasiswa(&head); break;
            case 2: printTabel(head); break;
            case 3: 
                printf("Masukkan NIM yang dicari: "); scanf("%s", nimTarget);
                searchMahasiswa(head, nimTarget);
                break;
            case 4:
                printf("Masukkan NIM yang akan dihapus: "); scanf("%s", nimTarget);
                deleteMahasiswa(&head, nimTarget);
                break;
            case 5: saveToCSV(head); break;
            case 6: printf("Keluar dari program.\n"); break;
            default: printf("Pilihan tidak valid!\n");
        }
    } while(pilihan != 6);
    
    Mahasiswa* temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
    return 0;
}