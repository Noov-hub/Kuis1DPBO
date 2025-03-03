class Anggrek:
    def __init__(self, id_anggrek, tipe_anggrek, nama, jenis, status, warna_utama, warna_sekunder, asal):
        self.id_anggrek = id_anggrek
        self.tipe_anggrek = tipe_anggrek
        self.nama = nama
        self.jenis = jenis
        self.status = status
        self.warna_utama = warna_utama
        self.warna_sekunder = warna_sekunder
        self.asal = asal
    
    def get_id_anggrek(self): return self.id_anggrek
    def get_tipe_anggrek(self): return self.tipe_anggrek
    def get_nama(self): return self.nama
    def get_jenis(self): return self.jenis
    def get_status(self): return self.status
    def get_warna_utama(self): return self.warna_utama
    def get_warna_sekunder(self): return self.warna_sekunder
    def get_asal(self): return self.asal
    
    def set_id_anggrek(self, id_anggrek): self.id_anggrek = id_anggrek
    def set_tipe_anggrek(self, tipe_anggrek): self.tipe_anggrek = tipe_anggrek
    def set_nama(self, nama): self.nama = nama
    def set_jenis(self, jenis): self.jenis = jenis
    def set_status(self, status): self.status = status
    def set_warna_utama(self, warna): self.warna_utama = warna
    def set_warna_sekunder(self, warna): self.warna_sekunder = warna
    def set_asal(self, asal): self.asal = asal
    
    def tampilkan_data(self):
        return f"ID: {self.id_anggrek}, Tipe: {self.tipe_anggrek}, Nama: {self.nama}, Jenis: {self.jenis}, Status: {self.status}, Warna Utama: {self.warna_utama}, Warna Sekunder: {self.warna_sekunder}, Asal: {self.asal}"