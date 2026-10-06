import json
from prettytable import PrettyTable


with open("nilai.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def tampilkan_data():
    print("\n=== DAFTAR NILAI MAHASISWA ===")
    tabel = PrettyTable()
    tabel.field_names = ["NIM", "Nama", "Mata Kuliah", "Nilai"]
    for mhs in data:
        tabel.add_row([mhs["nama"], mhs["nim"], mhs["matkul"], mhs["nilai"]])
    print(tabel)


def tambah_data(nama,nim, matkul, nilai):
    data.append({
        "nama": nama,
        "nim": nim,
        "matkul": matkul,
        "nilai": nilai
    })
    return "Data ditambah"


def simpan_file():
    with open("nilai.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    return "Tersimpan ke nilai.json"


def input_nilai():
    while True:
        nilai = input("Nilai (0-100): ")
        if nilai.isdigit():
            nilai = int(nilai)
            if nilai >= 0 and nilai <= 100:
                return nilai
            print("Nilai harus antara 0 sampai 100!")
        else:
            print("Nilai harus berupa angka bulat!")


while True:
    print("\n=== SISTEM PENCATATAN NILAI MAHASISWA ===")
    print("1. Lihat semua nilai")
    print("2. Tambah nilai baru")
    print("3. Keluar")
    pilihan = input("Pilih menu (1-3): ")

    if pilihan == "1":
        tampilkan_data()
    elif pilihan == "2":
        nama = input("Nama: ")
        nim = input("NIM: ")
        matkul = input("Mata Kuliah: ")
        nilai = input_nilai()
        print(tambah_data(nama, nim, matkul, nilai))
        print(simpan_file())
    elif pilihan == "3":
        print("exit")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
