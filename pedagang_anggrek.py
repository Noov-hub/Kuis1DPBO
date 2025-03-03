from orang import Orang
from anggrek import Anggrek

class PedagangAnggrek(Orang):
    def __init__(self, no_ktp, nama, alamat, tahun_awal_dagang, jenis):
        super().__init__(no_ktp, nama, alamat)
        self.tahun_awal_dagang = tahun_awal_dagang
        self.jenis = jenis
        self.list_anggrek = []
    
    def get_tahun_awal_dagang(self): return self.tahun_awal_dagang
    def get_jenis(self): return self.jenis
    def get_list_anggrek(self): return self.list_anggrek
    
    def set_tahun_awal_dagang(self, tahun): self.tahun_awal_dagang = tahun
    def set_jenis(self, jenis): self.jenis = jenis
    def tambah_anggrek(self, anggrek): self.list_anggrek.append(anggrek)
    
    def tampilkan_data(self):
        data = super().tampilkan_data() + f", Tahun Awal Dagang: {self.tahun_awal_dagang}, Jenis: {self.jenis}\nAnggrek yang dijual:\n"
        for anggrek in self.list_anggrek:
            data += anggrek.tampilkan_data() + "\n"
        return data