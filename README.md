# Kuis1DPBO
Soal Kuis 1 DPBO 2025 C2

Gunakan bahasa pemrograman Python untuk menyelesaikan soal ini. Kompilasi dilakukan pada semua kelas. Jadi di main harus melakukan link/import ke semua kelas. Topik kasus dalam soal ini adalah terkait UMKM Anggrek.


PedagangAnggrek
- NoKTP
- Nama
- Alamat
- TahunAwalDagang
- Jenis (reseller/petani/importir)
- ListAnggrek (daftar anggrek yang dijual)


ImportirAnggrek
- NoKTP
- Nama
- Alamat
- TahunAwalImpor
- NoIjinImpor
- ListAnggrek (daftar anggrek yang diimpor)


AnggrekDendrobium
- IdAnggrek
- Nama
- Jenis (bulat/keriting/semi-keriting)
- Status (spesies/hybrid)
- WarnaUtama
- WarnaSekunder
- Asal (impor/lokal)


AnggrekCattleya
- IdAnggrek
- Nama
- Status (spesies/hybrid)
- WarnaUtama
- WarnaSekunder
- Asal (impor/lokal)


AnggrekVanda
- IdAnggrek
- Nama
- Status (spesies/hybrid)
- WarnaUtama
- WarnaSekunder
- Asal (impor/lokal)


AnggrekHasilImpor
- NegaraAsal
- TanggalPengiriman (dd/mm/yyy dalam string)
- Kondisi (seedling, pra-remaja, remaja, pra-dewasa, dewasa)
- listAnggrekImpor


AnggrekHasilLokal
- NamaNursery
- KotaNursery
- TanggalPanen (dd/mm/yyy dalam string)
- Kondisi (seedling, pra-remaja, remaja, pra-dewasa, dewasa)
- listAnggrekLokal


Buatlah desain relasi antar kelas di atas menggunakan konsep composite (wajib) dan pewarisan (wajib) atau saling lepas (optional), sertakan alasannya. Diijinkan melakukan penggabungan atau pemisahan kelas dengan alasan yang mendukung. Implementasikan kelas-kelas di atas. Buatlah main yang dapat menampilkan:


Semua data dari desain kelas yang dibuat sesuai dengan relasi desain yang dibuat. 


semua data ditampilkan minimal 2 data (memeriksa apakah mahasiswa dapat mengimplementasikan array of object).


Semua data adalah hardcode (berupa simulasi saja). Semua kelas memiliki metode get set.


![image](https://github.com/user-attachments/assets/04ea1d1b-64f8-4a92-874e-0442cfe079f3)

### Pewarisan (Inheritance)
- Orang diwarisi oleh PedagangAnggrek dan ImportirAnggrek.
### Composite (List of Objects)
- PedagangAnggrek menyimpan list Anggrek
- ImportirAnggrek menyimpan list Anggrek
- AnggrekHasilImpor & AnggrekHasilLokal menyimpan list Anggrek

Pedagang dan importir mewarisi kelas orang karena sama sama manusia yang memiliki KTP nama dan alamat

Pedagang dan importir composite dengan anggrek karena pedagang dan importir memiliki list anggrek mereka masing masing
Hasil lokal dan hasil import juga composite dgn anggrek karena memiliki list object anggrek

Adanya penyatuan dari 3 kelas anggrek deondrium vanda dan cattluya,yang dimana setelah saya searching tipe2 angrek itu juga memiliki jenis2 nya masing masing sehingga kelas vanda dan cattluya mendapat atribut baru berupa jenis, nah sehingga bisa disatukan, selain itu jika 3 anggrek itu dijadikan subclass akan repot jika ada penambahan tipe anggrek diluar 3 anggrek itu(diperlukan penambahan kelas lagi)
