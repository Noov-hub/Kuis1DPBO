class Orang:
    def __init__(self, no_ktp, nama, alamat):
        self.no_ktp = no_ktp
        self.nama = nama
        self.alamat = alamat
    
    def get_no_ktp(self): return self.no_ktp
    def get_nama(self): return self.nama
    def get_alamat(self): return self.alamat
    
    def set_no_ktp(self, no_ktp): self.no_ktp = no_ktp
    def set_nama(self, nama): self.nama = nama
    def set_alamat(self, alamat): self.alamat = alamat
    
    def tampilkan_data(self):
        return f"KTP: {self.no_ktp}, Nama: {self.nama}, Alamat: {self.alamat}"