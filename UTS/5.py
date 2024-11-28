class Hewan:
    def suara(self):
        pass

class Kucing(Hewan):
    def suara(self):
        return "Meow"

class Anjing(Hewan):
    def suara(self):
        return "Guk Guk"

# Membuat objek
kucing = Kucing()
anjing = Anjing()

print(f"Kucing: {kucing.suara()}")
print(f"Anjing: {anjing.suara()}")

