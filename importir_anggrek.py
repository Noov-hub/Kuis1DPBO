from orang import Orang
from anggrek import Anggrek

class ImportirAnggrek(Orang):
    def __init__(self, no_ktp, nama, alamat, tahun_awal_impor, no_ijin_impor):
        super().__init__(no_ktp, nama, alamat)
        self.tahun_awal_impor = tahun_awal_impor
        self.no_ijin_impor = no_ijin_impor
        self.list_anggrek = []
    
    def get_tahun_awal_impor(self): return self.tahun_awal_impor
    def get_no_ijin_impor(self): return self.no_ijin_impor
    def get_list_anggrek(self): return self.list_anggrek
    
    def set_tahun_awal_impor(self, tahun): self.tahun_awal_impor = tahun
    def set_no_ijin_impor(self, no_ijin): self.no_ijin_impor = no_ijin
    def tambah_anggrek(self, anggrek): self.list_anggrek.append(anggrek)
    
    def tampilkan_data(self):
        data = super().tampilkan_data() + f", Tahun Awal Impor: {self.tahun_awal_impor}, No Ijin Impor: {self.no_ijin_impor}\nAnggrek yang diimpor:\n"
        for anggrek in self.list_anggrek:
            data += anggrek.tampilkan_data() + "\n"
        return data