from anggrek import Anggrek

class AnggrekHasilLokal:
    def __init__(self, nama_nursery, kota_nursery, tanggal_panen, kondisi):
        self.nama_nursery = nama_nursery
        self.kota_nursery = kota_nursery
        self.tanggal_panen = tanggal_panen
        self.kondisi = kondisi
        self.list_anggrek_lokal = []
    
    def get_nama_nursery(self): return self.nama_nursery
    def get_kota_nursery(self): return self.kota_nursery
    def get_tanggal_panen(self): return self.tanggal_panen
    def get_kondisi(self): return self.kondisi
    def get_list_anggrek_lokal(self): return self.list_anggrek_lokal
    
    def set_nama_nursery(self, nama): self.nama_nursery = nama
    def set_kota_nursery(self, kota): self.kota_nursery = kota
    def set_tanggal_panen(self, tanggal): self.tanggal_panen = tanggal
    def set_kondisi(self, kondisi): self.kondisi = kondisi
    def tambah_anggrek_lokal(self, anggrek): self.list_anggrek_lokal.append(anggrek)
    
    def tampilkan_data(self):
        data = f"Nama Nursery: {self.nama_nursery}, Kota Nursery: {self.kota_nursery}, Tanggal Panen: {self.tanggal_panen}, Kondisi: {self.kondisi}\nAnggrek Lokal:\n"
        for anggrek in self.list_anggrek_lokal:
            data += anggrek.tampilkan_data() + "\n"
        return data