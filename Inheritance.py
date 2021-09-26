class truk:
    def _init_(self, warna, tahun, merk):
        self.warna = warna
        self.tahun = tahun
        self.merk = merk

    def printname(self):
        print(self.warna)
        print(self.tahun)
        print(self.merk)

class diesel(truk):
     def _init_(self, warna, tahun, merk):
         truk._init_(self, warna, tahun, merk)
         self.bahanbakar = "Solar"

     def Diesel(Self):
        print("Warna       : ", Self.warna)
        print("Tahun       : ", Self.tahun)
        print("Merk        : ", Self.merk)
        print("Bahan Bakar : ", Self.bahanbakar)


class fuso(truk):
    def _init_(self, warna, tahun, merk):
          truk._init_(self, warna, tahun, merk)
          self.bahanbakar = "Pertamina Dex"

    def Fuso(Self):
        print("Warna       : ", Self.warna)
        print("Tahun       : ", Self.tahun)
        print("Merk        : ", Self.merk)
        print("Bahan Bakar : ", Self.bahanbakar)

x = diesel("hitam", 2020, "mitsubishi")
y = fuso("putih", 2021, "toyota")

x.Diesel()
y.Fuso()