# LAPORAN PRAKTIKUM 6
Nama : Fia Naefa Sahwa

Nim : 312510170

Kelas : TI.25.A2

Pertemuan : 11

# Program Daftar Nilai Mahasiswa

## 📝 1. Tujuan Praktikum

Praktikum ini bertujuan untuk:

Memahami penggunaan fungsi (def) dalam Python.

Mengimplementasikan fungsi dengan parameter, return, dan modularisasi kode.

Membuat program sederhana menggunakan beberapa fungsi untuk operasi:

tambah data

tampilkan data

hapus data

ubah data

Mengelola data menggunakan struktur dictionary.

## 🧩 2. Dasar Teori
Fungsi dalam Python

Fungsi adalah blok kode yang dapat dipanggil berkali-kali untuk melakukan tugas tertentu.

Keuntungan menggunakan fungsi:

Menghindari pengulangan kode (reusable)

Program lebih rapi dan modular

Memudahkan maintenance

## Struktur Fungsi
```
def nama_fungsi(parameter):
    statement
    return nilai   # optional
```
## Dictionary

Digunakan untuk menyimpan data mahasiswa dengan format:
```
mahasiswa = {
  "Ari": 90,
  "Dina": 85
}

```
Dictionary dipilih karena memudahkan proses CRUD berdasarkan nama sebagai key.

## ⚙️ 3. Flowchart Program
```
                ┌──────────────────┐
                │      MULAI        │
                └───────┬──────────┘
                        │
                ┌───────▼──────────┐
                │  TAMPILKAN MENU   │
                └───────┬──────────┘
                        │
            ┌───────────▼───────────┐
            │   INPUT PILIHAN MENU   │
            └───┬─────────┬─────────┘
                │         │
      ┌─────────▼     ┌───▼─────────┐
      │ Pilihan = 1    │ Pilihan = 2 │
      └──────┬────────└─────┬────────┘
             │              │
     ┌───────▼──────┐  ┌────▼──────────┐
     │  tambah()     │  │ tampilkan()   │
     └───────────────┘  └─────┬────────┘
                               │
                ┌─────────────▼────────────┐
                │       Pilihan = 3?        │
                └───────────┬──────────────┘
                            │
                     ┌──────▼───────┐
                     │  hapus()      │
                     └──────┬────────┘
                            │
                ┌───────────▼────────────┐
                │      Pilihan = 4?       │
                └───────────┬────────────┘
                            │
                     ┌──────▼───────┐
                     │   ubah()      │
                     └──────┬────────┘
                            │
                ┌───────────▼────────────┐
                │      Pilihan = 5?       │
                └───────────┬────────────┘
                            │
                     ┌──────▼───────┐
                     │    SELESAI    │
                     └───────────────┘
```

## 💻 4. Kode Program

## Program Daftar Nilai Mahasiswa (CRUD)
```
mahasiswa = {}  # tempat menyimpan data mahasiswa

# ---- FUNGSI TAMBAH DATA ----
def tambah():
    print("\n=== TAMBAH DATA ===")
    nama = input("Nama mahasiswa : ")
    nilai = float(input("Nilai         : "))
    mahasiswa[nama] = nilai
    print("Data berhasil ditambahkan.\n")

# ---- FUNGSI TAMPILKAN DATA ----
def tampilkan():
    print("\n=== DAFTAR NILAI MAHASISWA ===")
    if not mahasiswa:
        print("Belum ada data.\n")
    else:
        for nama, nilai in mahasiswa.items():
            print(f"- {nama} : {nilai}")
        print()

# ---- FUNGSI HAPUS DATA ----
def hapus(nama):
    print("\n=== HAPUS DATA ===")
    if nama in mahasiswa:
        del mahasiswa[nama]
        print(f"Data '{nama}' berhasil dihapus.\n")
    else:
        print("Nama tidak ditemukan.\n")

# ---- FUNGSI UBAH DATA ----
def ubah(nama):
    print("\n=== UBAH DATA ===")
    if nama in mahasiswa:
        nilai_baru = float(input("Nilai baru : "))
        mahasiswa[nama] = nilai_baru
        print(f"Data '{nama}' berhasil diubah.\n")
    else:
        print("Nama tidak ditemukan.\n")

# ---- MENU UTAMA ----
while True:
    print("=== MENU ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")

    pilihan = input("Pilih menu : ")

    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        nama_hapus = input("Nama yang ingin dihapus : ")
        hapus(nama_hapus)
    elif pilihan == "4":
        nama_ubah = input("Nama yang ingin diubah : ")
        ubah(nama_ubah)
    elif pilihan == "5":
        print("\nProgram selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.\n")
```
## 📌 5. Cara Kerja Program

Program menampilkan menu pilihan (tambah, tampilkan, hapus, ubah, keluar).

User memilih menu dengan memasukkan angka.

Program menjalankan fungsi sesuai pilihan.

Data menggunakan dictionary sehingga mudah diubah/hapus berdasarkan nama.

Program terus berjalan hingga user memilih menu Keluar.

## 📚 6. Kesimpulan

Dalam praktikum ini, mahasiswa berhasil mempelajari:

Konsep fungsi (def) dan penerapannya.

Penggunaan parameter, return, dan struktur fungsi yang baik.

Cara membuat program modular menggunakan beberapa fungsi.

Implementasi CRUD sederhana dengan memanfaatkan dictionary.

Membangun program interaktif yang dapat dijalankan berulang melalui menu.

Program ini membuktikan bahwa penggunaan fungsi membuat kode lebih rapi, modular, mudah dibaca, dan mudah dikembangkan.
