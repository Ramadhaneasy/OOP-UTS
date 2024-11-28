class Mahasiswa:
    def __init__(self, nama, nim, program_studi):
        self.nama = nama
        self.nim = nim
        self.program_studi = program_studi

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Program Studi: {self.program_studi}")


# Input pengguna
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
program_studi = input("Masukkan Program Studi: ")

# Membuat objek Mahasiswa
mahasiswa = Mahasiswa(nama, nim, program_studi)

# Menampilkan informasi Mahasiswa
mahasiswa.tampilkan_info()
