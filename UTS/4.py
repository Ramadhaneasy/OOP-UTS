class AkunBank:
    def __init__(self, norek, saldo):
        self.norek = norek
        self.__saldo = saldo

    def get_saldo(self): return self.__saldo
    def set_saldo(self, saldo): self.__saldo = saldo if saldo >= 0 else self.__saldo
    def tambah_saldo(self, jumlah): self.__saldo += jumlah
    def tarik_saldo(self, jumlah): 
        if jumlah <= self.__saldo: self.__saldo -= jumlah

akun = AkunBank("12345", 100000)
akun.tambah_saldo(50000)
akun.tarik_saldo(30000)
print(akun.get_saldo())
