class Laptop:
    def __init__(self, merk, ram, processor):
        self.merk = merk
        self.ram = ram
        self.processor = processor
        print(f"Laptop {merk} telah dibuat.")

    def __del__(self):
        print(f"Laptop {self.merk} telah dihapus.")

# Membuat objek Laptop
laptop = Laptop("ASUS", 16, "Intel Core i7")

# Menghapus objek Laptop
del laptop
