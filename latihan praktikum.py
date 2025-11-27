data_mahasiswa = {}

def tambah():
    print("\n=== Tambah Data Mahasiswa ===")
    nama = input("Masukkan nama: ").strip()
    nilai = input("Masukkan nilai: ")

    if nama in data_mahasiswa:
        print("❌ Nama sudah ada! Gunakan fungsi ubah() untuk mengedit.")
    else:
        data_mahasiswa[nama] = nilai
        print("✔ Data berhasil ditambahkan!")


def tampilkan():
    print("\n=== Daftar Nilai Mahasiswa ===")
    if not data_mahasiswa:
        print("Tidak ada data.")
    else:
        for nama, nilai in data_mahasiswa.items():
            print(f"- {nama}: {nilai}")


def hapus(nama):
    print("\n=== Hapus Data ===")
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(f"✔ Data '{nama}' berhasil dihapus!")
    else:
        print(f"❌ Data dengan nama '{nama}' tidak ditemukan.")


def ubah(nama):
    print("\n=== Ubah Data ===")
    if nama in data_mahasiswa:
        nilai_baru = input(f"Masukkan nilai baru untuk {nama}: ")
        data_mahasiswa[nama] = nilai_baru
        print(f"✔ Data '{nama}' berhasil diubah!")
    else:
        print(f"❌ Data dengan nama '{nama}' tidak ditemukan.")


def menu():
    while True:
        print("\n==============================")
        print("PROGRAM DATA NILAI MAHASISWA")
        print("==============================")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah()
        elif pilihan == "2":
            tampilkan()
        elif pilihan == "3":
            nama = input("Masukkan nama yang ingin dihapus: ")
            hapus(nama)
        elif pilihan == "4":
            nama = input("Masukkan nama yang ingin diubah: ")
            ubah(nama)
        elif pilihan == "5":
            print("Program selesai.")
            break
        else:
            print("❌ Pilihan tidak valid. Coba lagi.")


menu()
