from anggrek import Anggrek

class AnggrekHasilImpor:
    def __init__(self, negara_asal, tanggal_pengiriman, kondisi):
        self.negara_asal = negara_asal
        self.tanggal_pengiriman = tanggal_pengiriman
        self.kondisi = kondisi
        self.list_anggrek_impor = []
    
    def get_negara_asal(self): return self.negara_asal
    def get_tanggal_pengiriman(self): return self.tanggal_pengiriman
    def get_kondisi(self): return self.kondisi
    def get_list_anggrek_impor(self): return self.list_anggrek_impor
    
    def set_negara_asal(self, negara): self.negara_asal = negara
    def set_tanggal_pengiriman(self, tanggal): self.tanggal_pengiriman = tanggal
    def set_kondisi(self, kondisi): self.kondisi = kondisi
    def tambah_anggrek_impor(self, anggrek): self.list_anggrek_impor.append(anggrek)
    
    def tampilkan_data(self):
        data = f"Negara Asal: {self.negara_asal}, Tanggal Pengiriman: {self.tanggal_pengiriman}, Kondisi: {self.kondisi}\nAnggrek Impor:\n"
        for anggrek in self.list_anggrek_impor:
            data += anggrek.tampilkan_data() + "\n"
        return data