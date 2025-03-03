from anggrek_hasil_impor import AnggrekHasilImpor
from anggrek_hasil_lokal import AnggrekHasilLokal
from anggrek import Anggrek
from pedagang_anggrek import PedagangAnggrek
from importir_anggrek import ImportirAnggrek
# Membuat objek Anggrek
anggrek1 = Anggrek(1, "Dendrobium", "Dendrobium Biru", "Keriting", "Hybrid", "Biru", "Putih", "Lokal")
anggrek2 = Anggrek(2, "Cattleya", "Cattleya Pink", "-", "Spesies", "Pink", "Kuning", "Impor")

# Membuat objek AnggrekHasilLokal
hasil_lokal = AnggrekHasilLokal("Nursery Sejahtera", "Bandung", "01/10/2023", "Dewasa")
hasil_lokal.tambah_anggrek_lokal(anggrek1)

# Membuat objek AnggrekHasilImpor
hasil_impor = AnggrekHasilImpor("Thailand", "15/09/2023", "Seedling")
hasil_impor.tambah_anggrek_impor(anggrek2)


pedagang1 = PedagangAnggrek("12345", "Budi", "Jakarta", 2010, "Reseller")
pedagang1.tambah_anggrek(anggrek1)
pedagang1.tambah_anggrek(anggrek2)

importir1 = ImportirAnggrek("67890", "Siti", "Surabaya", 2015, "I12345")
importir1.tambah_anggrek(anggrek2)


print("=== pedagang ===")
print(pedagang1.tampilkan_data())
print("=== importir ===")
print(importir1.tampilkan_data())
# Menampilkan data
print("=== Hasil Anggrek Lokal ===")
print(hasil_lokal.tampilkan_data())

print("\n=== Hasil Anggrek Impor ===")
print(hasil_impor.tampilkan_data())