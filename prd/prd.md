# PRD Final

# Sistem Informasi Administrasi dan Website Profil HMI Cabang Pekanbaru Berbasis Web

---

## 1. Ringkasan Produk

Sistem ini adalah aplikasi web untuk **HMI Cabang Pekanbaru** yang menggabungkan dua kebutuhan utama:

1. Website profil organisasi yang dapat dikelola secara dinamis.
2. Sistem administrasi internal untuk pengelolaan kader, LK, arsip, surat, alumni, sertifikat, dan request upload berita.

Website publik akan menampilkan profil HMI, pengurus, program, berita, agenda, galeri, galeri Ketua Umum dari masa ke masa, serta tombol pendaftaran yang diarahkan ke  **Google Form** .

Admin panel digunakan untuk mengelola konten website, data komisariat, database kader, alumni, LK 1/2/3, penilaian LK, upload sertifikat LK, surat masuk, surat keluar, undangan, arsip administrasi, request upload berita, pembayaran berita, dan integrasi Gmail pada tahap lanjutan.

Sertifikat LK  **tidak dibuat otomatis oleh sistem** . Sertifikat dibuat secara manual oleh admin di luar sistem, kemudian file sertifikat di-upload dan diarsipkan ke sistem berdasarkan peserta LK.

---

## 2. Tujuan Produk

Tujuan utama sistem ini adalah:

1. Membuat website HMI Cabang Pekanbaru menjadi dinamis.
2. Mempermudah admin mengelola konten tanpa mengubah kode HTML.
3. Menyediakan database kader dan alumni yang rapi.
4. Mengelola data komisariat dan riwayat LK kader.
5. Mengelola administrasi LK 1, LK 2, dan LK 3.
6. Membantu proses penilaian LK dan pengarsipan sertifikat LK yang di-upload oleh admin.
7. Menyediakan arsip surat masuk, surat keluar, undangan, dan dokumen administrasi.
8. Menyediakan fitur request upload berita berbayar.
9. Menyediakan galeri Ketua Umum HMI Cabang Pekanbaru dari masa ke masa.
10. Menyediakan struktur backend yang rapi menggunakan Django MVT 4 layer.

---

## 3. Nama Sistem

Nama sistem:

```text
Sistem Informasi Administrasi dan Website Profil HMI Cabang Pekanbaru
```

Singkatan opsional:

```text
SI-HMI Pekanbaru
```

---

## 4. Stack Teknologi

### Backend

```text
Django 6.0.4
```

### Arsitektur

```text
Django MVT dengan 4 layer:
1. Presentation Layer
2. Business Logic Layer
3. Data Access Layer
4. Data Layer
```

### Database

```text
PostgreSQL
```

### Frontend

```text
Django Templates
Tailwind CSS CDN
Google Fonts CDN
Material Symbols CDN
```

### File Upload

```text
Django Media Storage
```

### Rich Text Editor

```text
CKEditor 5
```

### Import / Export

```text
OpenPyXL
```

### Form Styling

```text
django-widget-tweaks
```

### Debugging

```text
django-debug-toolbar
```

### Testing dan Code Quality

```text
pytest
pytest-django
ruff
```

### Deployment

```text
WhiteNoise
Gunicorn
```

### Pendaftaran

```text
Google Form redirect
```

### Sertifikat

```text
Sertifikat dibuat manual oleh admin, lalu di-upload ke sistem.
```

### Gmail

```text
Integrasi Gmail menjadi fitur tahap lanjutan.
```

---

## 5. Aktor Pengguna

Sistem memiliki empat aktor utama:

1. Pengunjung Website
2. Super Admin
3. Admin Website
4. Admin Administrasi

---

## 5.1 Pengunjung Website

Pengunjung adalah user umum yang membuka halaman publik website.

Pengunjung dapat:

```text
Melihat profil organisasi.
Melihat pengurus HMI.
Melihat program strategis.
Melihat berita.
Melihat agenda.
Melihat galeri.
Melihat galeri Ketua Umum dari masa ke masa.
Klik tombol pendaftaran Google Form.
Mengirim pesan kontak.
Mengajukan request upload berita.
Mengunggah bukti pembayaran request berita.
```

---

## 5.2 Super Admin

Super Admin adalah admin tertinggi.

Super Admin dapat:

```text
Mengelola semua fitur.
Mengelola akun admin.
Mengatur role admin.
Mengelola website.
Mengelola konten.
Mengelola administrasi.
Mengelola LK.
Mengelola data kader.
Mengelola alumni.
Mengelola request berita.
Mengelola integrasi Gmail.
```

---

## 5.3 Admin Website

Admin Website bertugas mengelola konten publik.

Admin Website dapat:

```text
Mengelola profil organisasi.
Mengelola pengurus.
Mengelola program.
Mengelola berita.
Mengelola agenda.
Mengelola galeri.
Mengelola galeri Ketua Umum.
Mengelola link Google Form.
Mengelola pesan kontak.
Mengelola request upload berita.
```

---

## 5.4 Admin Administrasi

Admin Administrasi bertugas mengelola data internal organisasi.

Admin Administrasi dapat:

```text
Mengelola komisariat.
Mengelola database kader.
Mengelola database alumni.
Mengelola LK 1, LK 2, LK 3.
Mengelola peserta LK.
Mengelola materi LK.
Mengelola penilaian LK.
Meng-upload sertifikat LK.
Mengarsipkan sertifikat LK.
Mengelola arsip administrasi.
Mengelola surat masuk.
Mengelola surat keluar.
Mengelola undangan.
```

---

# 6. Ruang Lingkup Sistem

---

## 6.1 Fitur Publik Website

Fitur yang tampil untuk pengunjung:

```text
Homepage
Profil organisasi
Pengurus aktif
Program strategis
Berita / Warta organisasi
Agenda kegiatan
Galeri
Galeri Ketua Umum dari masa ke masa
Link pendaftaran ke Google Form
Form kontak
Request upload berita
Upload bukti pembayaran request berita
```

---

## 6.2 Fitur Admin Panel

Fitur yang hanya bisa diakses admin:

```text
Login admin
Dashboard admin
Manajemen akun admin
Manajemen role
Manajemen profil organisasi
Manajemen pengurus
Manajemen program
Manajemen berita
Manajemen agenda
Manajemen galeri
Manajemen galeri Ketua Umum
Manajemen link pendaftaran Google Form
Manajemen pesan kontak
Manajemen komisariat
Manajemen kader
Manajemen alumni
Manajemen LK
Manajemen peserta LK
Manajemen materi LK
Manajemen penilaian LK
Upload sertifikat LK
Arsip sertifikat LK
Manajemen tanda tangan opsional
Manajemen arsip administrasi
Manajemen surat masuk
Manajemen surat keluar
Manajemen undangan
Integrasi Gmail tahap lanjutan
Log email
Request upload berita
Verifikasi pembayaran request berita
Publish berita dari request
```

---

# 7. Scope Database Final

Database final terdiri dari 35 tabel:

```text
1. roles
2. users
3. site_settings
4. organization_profile
5. navigation_menus
6. management_members
7. chairman_histories
8. programs
9. events
10. news_categories
11. news_posts
12. gallery_categories
13. gallery_images
14. registration_forms
15. contact_messages
16. commissariats
17. cadres
18. cadre_lk_histories
19. alumni
20. lk_levels
21. lk_batches
22. lk_participants
23. lk_materials
24. lk_assessments
25. lk_assessment_details
26. signatures
27. lk_certificates
28. document_archives
29. incoming_letters
30. outgoing_letters
31. invitations
32. gmail_integrations
33. email_logs
34. news_upload_requests
35. news_request_payments
```

Catatan:

```text
Tabel lk_certificates digunakan untuk menyimpan data sertifikat LK yang dibuat secara manual oleh admin dan di-upload ke sistem.
Sistem tidak melakukan generate PDF sertifikat otomatis.
```

---

# 8. Modul Sistem

---

## 8.1 Modul Auth dan Role

### Tabel terkait

```text
roles
users
```

### Tujuan

Mengatur login admin dan pembagian hak akses.

### Role utama

```text
super_admin
admin_website
admin_administrasi
```

### Fitur

```text
Login admin
Logout admin
Tambah admin
Edit admin
Nonaktifkan admin
Kelola role admin
Cek status admin aktif / tidak aktif
```

### Acceptance Criteria

```text
Admin hanya bisa login jika email dan password valid.
Admin inactive tidak bisa login.
Super Admin bisa mengelola semua admin.
Setiap admin memiliki role.
Role menentukan fitur yang dapat diakses.
Sistem menggunakan custom user model accounts.User.
Semua relasi admin menggunakan settings.AUTH_USER_MODEL.
```

---

## 8.2 Modul Website Setting

### Tabel terkait

```text
site_settings
navigation_menus
```

### Tujuan

Mengatur data umum website.

### Data yang dikelola

```text
Nama website
Hero title
Hero description
Hero image
CTA title
CTA description
Footer text
Link sosial media
Menu navbar
Menu footer
Nomor WhatsApp
Email organisasi
```

### Fitur

```text
Kelola setting website
Kelola menu navbar
Kelola menu footer
Aktifkan / nonaktifkan menu
Atur urutan menu
```

### Acceptance Criteria

```text
Admin dapat mengubah teks hero tanpa mengubah HTML.
Admin dapat mengatur menu navbar.
Menu inactive tidak tampil di halaman publik.
Perubahan setting langsung tampil di website.
```

---

## 8.3 Modul Profil Organisasi

### Tabel terkait

```text
organization_profile
```

### Tujuan

Mengelola identitas organisasi HMI Cabang Pekanbaru.

### Data yang dikelola

```text
Nama organisasi
Nama singkat
Deskripsi
Sejarah
Visi
Misi
Logo
Gambar profil
Tahun berdiri
Alamat
Email
Nomor telepon
```

### Fitur

```text
Edit profil organisasi
Upload logo
Upload gambar profil
Edit visi dan misi
Edit kontak organisasi
```

### Acceptance Criteria

```text
Profil organisasi dapat diperbarui dari admin panel.
Logo yang diunggah tampil di website.
Visi dan misi tampil di halaman publik.
Kontak organisasi tampil di footer atau halaman kontak.
```

---

## 8.4 Modul Pengurus

### Tabel terkait

```text
management_members
```

### Tujuan

Mengelola data pengurus aktif HMI Cabang Pekanbaru.

### Data yang dikelola

```text
Nama pengurus
Jabatan
Foto
Periode
Deskripsi
Urutan tampil
Status active / inactive
```

### Fitur

```text
Tambah pengurus
Edit pengurus
Hapus pengurus
Upload foto pengurus
Atur urutan tampil
Aktifkan / nonaktifkan pengurus
```

### Acceptance Criteria

```text
Hanya pengurus active yang tampil di website.
Pengurus bisa diurutkan berdasarkan sort_order.
Admin bisa upload foto pengurus.
```

---

## 8.5 Modul Galeri Ketua Umum dari Masa ke Masa

### Tabel terkait

```text
chairman_histories
```

### Tujuan

Menyimpan sejarah Ketua Umum HMI Cabang Pekanbaru.

### Data yang dikelola

```text
Nama Ketua Umum
Tahun mulai periode
Tahun selesai periode
Foto
Deskripsi
Urutan tampil
Status show / hide
```

### Fitur

```text
Tambah data Ketua Umum
Edit data Ketua Umum
Upload foto
Atur urutan periode
Tampilkan / sembunyikan data
```

### Acceptance Criteria

```text
Data Ketua Umum yang status show tampil di website.
Urutan dapat disusun berdasarkan periode atau sort_order.
Foto Ketua Umum dapat ditampilkan di halaman publik.
```

---

# 9. Modul Konten Website

---

## 9.1 Modul Program

### Tabel terkait

```text
programs
```

### Tujuan

Mengelola program strategis HMI.

### Data yang dikelola

```text
Judul program
Slug
Kategori
Deskripsi
Konten lengkap
Gambar
Ikon
Status featured
Teks tombol
Link tombol
Link Google Form opsional
Urutan tampil
Status draft / published
Admin pembuat
```

### Fitur

```text
Tambah program
Edit program
Hapus program
Publish / draft program
Tandai program sebagai featured
Masukkan link Google Form jika ada
```

### Acceptance Criteria

```text
Program published tampil di website.
Program draft tidak tampil di website.
Program featured tampil sebagai program utama.
Slug bersifat unik.
```

---

## 9.2 Modul Agenda

### Tabel terkait

```text
events
```

### Tujuan

Mengelola agenda kegiatan HMI.

### Data yang dikelola

```text
Judul agenda
Slug
Deskripsi
Konten
Gambar
Lokasi
Tanggal mulai
Tanggal selesai
Jam mulai
Jam selesai
Status featured
Link Google Form opsional
Status draft / published / finished
Admin pembuat
```

### Fitur

```text
Tambah agenda
Edit agenda
Hapus agenda
Publish / draft agenda
Tandai agenda selesai
Tandai agenda featured
Tambahkan link pendaftaran Google Form
```

### Acceptance Criteria

```text
Agenda published tampil di website.
Agenda finished dapat tetap disimpan sebagai arsip.
Agenda featured tampil sebagai agenda utama.
```

---

## 9.3 Modul Berita

### Tabel terkait

```text
news_categories
news_posts
```

### Tujuan

Mengelola berita, opini, kegiatan, dan informasi organisasi.

### Data kategori berita

```text
Nama kategori
Slug kategori
Deskripsi
```

### Data berita

```text
Kategori
Request ID jika berasal dari request upload
Judul
Slug
Ringkasan
Isi berita
Gambar
Nama penulis
Tanggal publish
Status draft / published
Admin pembuat
```

### Fitur

```text
Tambah kategori berita
Edit kategori berita
Tambah berita
Edit berita
Hapus berita
Publish berita
Draft berita
Upload gambar berita
Tampilkan berita terbaru di homepage
Tampilkan detail berita berdasarkan slug
```

### Acceptance Criteria

```text
Berita published tampil di website.
Berita draft tidak tampil di website.
Slug berita unik.
Berita dapat dikaitkan dengan kategori.
Berita dari request upload dapat dikaitkan dengan request_id.
```

---

## 9.4 Modul Galeri

### Tabel terkait

```text
gallery_categories
gallery_images
```

### Tujuan

Mengelola dokumentasi foto kegiatan HMI.

### Data kategori galeri

```text
Nama kategori
Slug
Deskripsi
```

### Data foto galeri

```text
Kategori
Judul foto
File gambar
Alt text
Deskripsi
Urutan tampil
Status show / hide
Admin uploader
```

### Fitur

```text
Tambah kategori galeri
Edit kategori galeri
Upload foto
Edit foto
Hapus foto
Tampilkan / sembunyikan foto
Atur urutan foto
```

### Acceptance Criteria

```text
Foto dengan status show tampil di website.
Foto dengan status hide tidak tampil.
Foto dapat difilter berdasarkan kategori.
```

---

# 10. Modul Pendaftaran Google Form

---

## 10.1 Registration Forms

### Tabel terkait

```text
registration_forms
```

### Tujuan

Menyimpan link Google Form untuk berbagai pendaftaran.

Karena pendaftaran diarahkan ke Google Form, sistem tidak menyimpan data pendaftar langsung di database utama.

### Jenis form

```text
kader
lk1
lk2
lk3
program
agenda
other
```

### Data yang dikelola

```text
Judul form
Jenis form
URL Google Form
Deskripsi
Status active / inactive
Admin pembuat
```

### Fitur

```text
Tambah link Google Form
Edit link Google Form
Aktifkan / nonaktifkan link
Tampilkan tombol daftar di website
```

### Acceptance Criteria

```text
Tombol pendaftaran di website membuka Google Form.
Link inactive tidak digunakan.
Admin dapat mengganti link Google Form dari admin panel.
```

---

# 11. Modul Pesan Kontak

---

## 11.1 Contact Messages

### Tabel terkait

```text
contact_messages
```

### Tujuan

Menyimpan pesan dari pengunjung website.

### Data yang disimpan

```text
Nama pengirim
Email
Nomor HP
Subjek
Isi pesan
Status unread / read / replied
Admin yang menangani
Tanggal kirim
```

### Fitur

```text
Pengunjung mengirim pesan kontak
Admin melihat daftar pesan
Admin membaca pesan
Admin mengubah status pesan
Admin menandai pesan sebagai replied
```

### Acceptance Criteria

```text
Pesan baru otomatis berstatus unread.
Admin bisa mengubah status menjadi read atau replied.
Pesan kontak tersimpan di database.
```

---

# 12. Modul Komisariat, Kader, dan Alumni

---

## 12.1 Modul Komisariat

### Tabel terkait

```text
commissariats
```

### Tujuan

Mengelola data komisariat HMI.

### Data yang dikelola

```text
Nama komisariat
Universitas
Alamat
Contact person
Nomor HP
Status active / inactive
```

### Fitur

```text
Tambah komisariat
Edit komisariat
Nonaktifkan komisariat
Lihat daftar kader per komisariat
Lihat alumni per komisariat
```

### Acceptance Criteria

```text
Satu komisariat dapat memiliki banyak kader.
Satu komisariat dapat memiliki banyak alumni.
Komisariat inactive tetap tersimpan sebagai arsip.
```

---

## 12.2 Modul Kader

### Tabel terkait

```text
cadres
cadre_lk_histories
```

### Tujuan

Mengelola database kader HMI Cabang Pekanbaru.

### Data kader

```text
Komisariat
Nama lengkap
Jenis kelamin
Tempat lahir
Tanggal lahir
Email
Nomor HP
Alamat
Universitas
Fakultas
Jurusan
Tahun masuk kuliah
Tahun LK 1
Status kader
Foto
Catatan
```

### Status kader

```text
active
alumni
inactive
```

### Data riwayat LK

```text
Kader
Level LK
Batch LK
Tahun mengikuti
Status registered / passed / failed
Nomor sertifikat
```

### Fitur

```text
Tambah kader
Edit kader
Hapus / nonaktifkan kader
Filter kader berdasarkan komisariat
Filter kader berdasarkan tahun LK 1
Filter kader berdasarkan status
Tambah riwayat LK
Lihat histori LK kader
```

### Acceptance Criteria

```text
Kader wajib memiliki nama.
Kader dapat dikaitkan dengan komisariat.
Kader dapat memiliki banyak riwayat LK.
Data kader 12 tahun dapat difilter berdasarkan lk1_year.
```

---

## 12.3 Modul Alumni

### Tabel terkait

```text
alumni
```

### Tujuan

Mengelola database alumni HMI.

### Data yang dikelola

```text
Relasi ke kader jika ada
Komisariat asal
Nama lengkap
Email
Nomor HP
Profesi
Tempat kerja
Jabatan sekarang
Tahun lulus
Tahun LK 1
Alamat
Foto
Catatan
```

### Fitur

```text
Tambah alumni
Edit alumni
Hapus alumni
Filter alumni berdasarkan komisariat
Filter alumni berdasarkan tahun LK 1
Filter alumni berdasarkan profesi
Hubungkan alumni dengan data kader
```

### Acceptance Criteria

```text
Alumni dapat berdiri sendiri walaupun tidak memiliki data kader.
Alumni dapat dihubungkan dengan tabel cadres jika datanya tersedia.
Komisariat dapat memiliki banyak alumni.
```

---

# 13. Modul LK 1, LK 2, LK 3

---

## 13.1 Modul Level LK

### Tabel terkait

```text
lk_levels
```

### Tujuan

Menyimpan jenis LK.

### Data awal

```text
LK 1
LK 2
LK 3
```

### Acceptance Criteria

```text
Level LK menjadi referensi untuk batch, materi, dan riwayat LK.
Level LK tidak boleh sembarang dihapus jika sudah dipakai.
```

---

## 13.2 Modul Batch LK

### Tabel terkait

```text
lk_batches
```

### Tujuan

Mengelola kegiatan LK tertentu.

### Data yang dikelola

```text
Level LK
Judul kegiatan
Tema
Lokasi
Tanggal mulai
Tanggal selesai
Tanggal buka pendaftaran
Tanggal tutup pendaftaran
Link Google Form pendaftaran
Status draft / open / closed / finished
Admin pembuat
```

### Fitur

```text
Tambah batch LK
Edit batch LK
Buka pendaftaran LK
Tutup pendaftaran LK
Tandai LK selesai
Masukkan link Google Form
```

### Acceptance Criteria

```text
Batch LK wajib memiliki level LK.
Batch LK dapat memiliki banyak peserta.
Batch LK dapat memiliki banyak materi.
Batch LK dapat memiliki banyak penilaian.
```

---

## 13.3 Modul Peserta LK

### Tabel terkait

```text
lk_participants
```

### Tujuan

Mengelola peserta LK setelah data dari Google Form direkap.

### Data yang dikelola

```text
Batch LK
Relasi ke kader jika ada
Komisariat
Nama lengkap
Email
Nomor HP
Universitas
Fakultas
Jurusan
Semester
Alamat
Motivasi
Foto
Status pendaftaran
Status kelulusan
```

### Status pendaftaran

```text
registered
verified
rejected
```

### Status kelulusan

```text
not_assessed
passed
failed
```

### Fitur

```text
Tambah peserta LK manual
Import peserta dari rekap Google Form secara manual
Edit peserta LK
Verifikasi peserta LK
Tolak peserta LK
Hubungkan peserta dengan data kader
Update status kelulusan setelah penilaian
```

### Acceptance Criteria

```text
Peserta wajib terkait dengan batch LK.
Peserta baru boleh belum memiliki cadre_id.
Setelah lulus LK 1, peserta dapat dimasukkan ke database kader.
```

---

## 13.4 Modul Materi LK

### Tabel terkait

```text
lk_materials
```

### Tujuan

Mengelola materi LK.

### Data yang dikelola

```text
Level LK
Batch LK opsional
Judul materi
Deskripsi
Urutan materi
Status active / inactive
```

### Fitur

```text
Tambah materi LK
Edit materi LK
Nonaktifkan materi
Atur urutan materi
Materi umum per level LK
Materi khusus per batch LK
```

### Acceptance Criteria

```text
Materi wajib terkait dengan level LK.
Materi dapat bersifat umum atau khusus batch tertentu.
Materi active digunakan pada form penilaian.
```

---

# 14. Modul Penilaian LK

---

## 14.1 Penilaian Utama LK

### Tabel terkait

```text
lk_assessments
```

### Tujuan

Menyimpan hasil penilaian utama peserta LK.

### Data yang dikelola

```text
Peserta LK
Batch LK
Penilai
Total nilai
Grade akhir
Catatan umum
Status hasil passed / failed / pending
Tanggal penilaian
```

### Fitur

```text
Buat penilaian peserta
Hitung total nilai
Tentukan grade akhir
Tentukan status lulus / tidak lulus
Update status kelulusan peserta
```

### Acceptance Criteria

```text
Penilaian wajib memiliki peserta.
Total nilai dihitung dari detail nilai.
Status kelulusan peserta berubah setelah penilaian selesai.
Penilaian dilakukan oleh admin/penilai.
```

---

## 14.2 Detail Penilaian LK

### Tabel terkait

```text
lk_assessment_details
```

### Tujuan

Menyimpan nilai per materi LK.

### Data yang dikelola

```text
Assessment
Materi LK
Nilai
Grade
Catatan penilai
```

### Fitur

```text
Input nilai per materi
Edit nilai per materi
Hitung grade per materi
Simpan catatan penilai
```

### Acceptance Criteria

```text
Satu assessment memiliki banyak detail nilai.
Setiap detail nilai terkait dengan satu materi.
Nilai detail digunakan untuk menghitung total score.
```

---

# 15. Modul Sertifikat dan Tanda Tangan

---

## 15.1 Modul Tanda Tangan

### Tabel terkait

```text
signatures
```

### Tujuan

Menyimpan data tanda tangan dan stempel organisasi jika dibutuhkan untuk dokumen administrasi.

Pada versi MVP, modul tanda tangan bersifat  **opsional** , karena sertifikat LK dibuat manual di luar sistem.

### Data yang dikelola

```text
Nama penanda tangan
Jabatan
File tanda tangan
File stempel
Status active / inactive
```

### Fitur

```text
Tambah tanda tangan
Edit tanda tangan
Upload file tanda tangan
Upload file stempel
Aktifkan / nonaktifkan tanda tangan
```

### Acceptance Criteria

```text
Admin dapat menyimpan data tanda tangan.
Tanda tangan active dapat digunakan jika nanti sistem membutuhkan dokumen digital.
Pada MVP, tanda tangan tidak wajib digunakan untuk sertifikat karena sertifikat dibuat manual.
```

---

## 15.2 Modul Sertifikat LK

### Tabel terkait

```text
lk_certificates
```

### Tujuan

Menyimpan dan mengarsipkan file sertifikat LK yang dibuat secara manual oleh admin.

Sistem tidak membuat sertifikat otomatis. Admin membuat sertifikat di luar sistem, misalnya melalui Canva, Word, Corel, atau aplikasi desain lain, lalu meng-upload file sertifikat ke sistem.

### Data yang dikelola

```text
Peserta LK
Assessment terkait
Nomor sertifikat
Judul sertifikat
Tanggal terbit
File sertifikat
Tanda tangan opsional
Jumlah cetak opsional
Tanggal upload
```

### Fitur

```text
Upload file sertifikat LK
Edit data sertifikat
Hapus sertifikat
Lihat sertifikat
Download sertifikat
Hubungkan sertifikat dengan peserta LK
Hubungkan sertifikat dengan hasil penilaian peserta
```

### Acceptance Criteria

```text
Sertifikat wajib terhubung dengan peserta LK.
Nomor sertifikat harus unik.
Admin dapat meng-upload file sertifikat.
Admin dapat melihat atau mengunduh sertifikat.
Sistem tidak perlu generate sertifikat otomatis.
Sistem tidak perlu generate PDF otomatis.
```

---

# 16. Modul Administrasi Surat dan Arsip

---

## 16.1 Arsip Administrasi

### Tabel terkait

```text
document_archives
```

### Tujuan

Menyimpan dokumen administrasi umum.

### Data yang dikelola

```text
Judul arsip
Nomor arsip
Kategori
Deskripsi
File dokumen
Tanggal arsip
Admin uploader
```

### Fitur

```text
Upload dokumen arsip
Edit data arsip
Hapus arsip
Cari arsip berdasarkan judul
Cari arsip berdasarkan nomor arsip
Filter berdasarkan kategori
```

### Acceptance Criteria

```text
Dokumen arsip dapat diupload.
Admin dapat mencari arsip.
Arsip tetap tersimpan walaupun tidak ditampilkan di website publik.
```

---

## 16.2 Surat Masuk

### Tabel terkait

```text
incoming_letters
```

### Tujuan

Mengelola surat masuk organisasi.

### Data yang dikelola

```text
Nomor surat
Pengirim
Perihal
Tanggal diterima
Tanggal surat
Deskripsi
File surat
Status new / processed / archived
Admin input
```

### Fitur

```text
Input surat masuk
Upload file surat masuk
Edit surat masuk
Ubah status surat
Arsipkan surat masuk
Cari surat masuk
```

### Acceptance Criteria

```text
Surat masuk dapat disimpan dengan file.
Status surat dapat berubah dari new ke processed atau archived.
```

---

## 16.3 Surat Keluar

### Tabel terkait

```text
outgoing_letters
```

### Tujuan

Mengelola surat keluar organisasi.

### Data yang dikelola

```text
Nomor surat
Penerima
Email penerima
Perihal
Tanggal surat
Isi surat
File surat
Status draft / sent / archived
Waktu pengiriman
Admin pembuat
```

### Fitur

```text
Buat surat keluar
Edit surat keluar
Upload file surat
Simpan sebagai draft
Tandai terkirim
Arsipkan surat
Kirim melalui Gmail pada tahap lanjutan
```

### Acceptance Criteria

```text
Surat keluar dapat dibuat sebagai draft.
Surat keluar dapat ditandai sent.
Surat keluar dapat diarsipkan.
```

---

## 16.4 Undangan

### Tabel terkait

```text
invitations
```

### Tujuan

Mengelola undangan HMI.

### Data yang dikelola

```text
Nomor undangan
Agenda terkait opsional
Penerima
Email penerima
Perihal
Isi undangan
Tanggal undangan
Tanggal acara
Lokasi acara
File PDF
Status draft / sent / archived
Waktu kirim
Admin pembuat
```

### Fitur

```text
Buat undangan
Hubungkan dengan agenda
Upload file undangan
Simpan sebagai draft
Tandai terkirim
Arsipkan undangan
Kirim melalui Gmail pada tahap lanjutan
```

### Acceptance Criteria

```text
Undangan bisa berdiri sendiri atau terkait dengan agenda.
Undangan dapat diarsipkan.
```

---

## 16.5 Integrasi Gmail

### Tabel terkait

```text
gmail_integrations
email_logs
```

### Tujuan

Menyediakan integrasi email HMI untuk pengiriman surat keluar dan undangan.

### Data Gmail Integration

```text
Email Gmail HMI
Access token
Refresh token
Tanggal token expired
Status connected / disconnected
Admin yang menghubungkan
```

### Data Email Logs

```text
Gmail integration
Related type
Related ID
Email penerima
Subject
Status pending / sent / failed
Tanggal kirim
Pesan error
```

### Fitur

```text
Hubungkan akun Gmail HMI
Kirim surat keluar via Gmail
Kirim undangan via Gmail
Simpan log email
Tandai email gagal / berhasil
```

### Acceptance Criteria

```text
Setiap pengiriman email tercatat di email_logs.
Jika pengiriman gagal, error_message tersimpan.
Token Gmail tidak boleh ditampilkan ke admin biasa.
```

### Catatan Prioritas

```text
Integrasi Gmail dikerjakan tahap akhir.
Untuk MVP cukup simpan surat dan undangan sebagai arsip.
```

---

# 17. Modul Request Upload Berita Berbayar

---

## 17.1 Request Upload Berita

### Tabel terkait

```text
news_upload_requests
```

### Tujuan

Mengelola pengajuan upload berita dengan biaya Rp50.000 per berita.

### Data yang dikelola

```text
Nama pengaju
Email pengaju
Nomor HP pengaju
Judul berita
Kategori berita
Isi berita
Gambar
Lampiran
Harga
Status request
Admin reviewer
Tanggal review
Catatan admin
```

### Status request

```text
pending
waiting_payment
paid
approved
rejected
published
```

### Fitur

```text
Pengunjung mengajukan berita
Sistem mencatat biaya Rp50.000
Admin melihat request berita
Admin review berita
Admin approve request
Admin reject request
Admin publish request menjadi news_posts
```

### Acceptance Criteria

```text
Request baru otomatis berstatus pending.
Harga default Rp50.000.
Request approved dapat dipublish menjadi berita.
Jika dipublish, data masuk ke news_posts.
```

---

## 17.2 Pembayaran Request Berita

### Tabel terkait

```text
news_request_payments
```

### Tujuan

Mencatat pembayaran request upload berita.

### Data yang dikelola

```text
Request berita
Nominal pembayaran
Metode pembayaran
Bukti pembayaran
Status unpaid / paid / verified / rejected
Admin verifikator
Tanggal verifikasi
```

### Fitur

```text
Upload bukti pembayaran
Admin verifikasi pembayaran
Admin tolak pembayaran
Ubah status pembayaran
```

### Acceptance Criteria

```text
Satu request berita memiliki satu data pembayaran.
Pembayaran verified membuat request siap direview.
Bukti pembayaran dapat dilihat admin.
```

---

# 18. Flow Utama Sistem

---

## 18.1 Flow Website Publik

```text
Pengunjung membuka website
        ↓
Sistem mengambil data dari database
        ↓
Website menampilkan profil, pengurus, program, berita, agenda, galeri
        ↓
Pengunjung dapat klik pendaftaran Google Form
        ↓
Pengunjung dapat mengirim pesan kontak
        ↓
Pengunjung dapat request upload berita
```

---

## 18.2 Flow Admin Website

```text
Admin login
        ↓
Masuk dashboard
        ↓
Kelola profil / konten / berita / agenda / galeri
        ↓
Data tersimpan ke database
        ↓
Website publik otomatis menampilkan data terbaru
```

---

## 18.3 Flow LK

```text
Admin membuat batch LK
        ↓
Admin memasukkan link Google Form pendaftaran
        ↓
Peserta mengisi Google Form
        ↓
Admin merekap data peserta ke sistem
        ↓
Admin mengisi materi LK
        ↓
Admin mengisi penilaian peserta
        ↓
Sistem menghitung nilai akhir
        ↓
Sistem menentukan status lulus / gagal
        ↓
Admin membuat sertifikat secara manual di luar sistem
        ↓
Admin upload file sertifikat ke sistem
        ↓
Sertifikat tersimpan sebagai arsip peserta LK
```

---

## 18.4 Flow Kader

```text
Admin input komisariat
        ↓
Admin input kader
        ↓
Admin menambahkan riwayat LK kader
        ↓
Data kader dapat difilter berdasarkan komisariat dan tahun LK 1
        ↓
Jika sudah alumni, data dapat dimasukkan ke alumni
```

---

## 18.5 Flow Request Upload Berita

```text
Pengunjung mengajukan berita
        ↓
Sistem membuat request dengan harga Rp50.000
        ↓
Pengunjung upload bukti pembayaran
        ↓
Admin verifikasi pembayaran
        ↓
Admin review isi berita
        ↓
Jika diterima, admin publish menjadi berita
        ↓
Berita tampil di website
```

---

## 18.6 Flow Administrasi Surat

```text
Admin login
        ↓
Masuk menu administrasi
        ↓
Input surat masuk / surat keluar / undangan / arsip
        ↓
Upload file dokumen
        ↓
Data tersimpan sebagai arsip internal
        ↓
Opsional dikirim melalui Gmail
```

---

# 19. Arsitektur Django MVT

Sistem menggunakan arsitektur Django MVT dengan 4 layer utama:

```text
1. Presentation Layer
2. Business Logic Layer
3. Data Access Layer
4. Data Layer
```

---

## 19.1 Layer Presentation

### File

```text
views.py
urls.py
templates/
forms.py
```

### Fungsi

```text
Menerima request dari user.
Memanggil selector untuk mengambil data.
Memanggil service untuk memproses aksi.
Mengembalikan response HTML atau JSON.
```

### Aturan

```text
Views tidak boleh query database langsung.
Views tidak boleh berisi logika perhitungan nilai.
Views tidak boleh mengirim email langsung.
Views tidak boleh memproses upload sertifikat secara langsung tanpa service.
```

---

## 19.2 Layer Business Logic

### File

```text
services.py
```

### Fungsi

```text
Create data.
Update data.
Delete data.
Validasi bisnis.
Generate nomor surat.
Hitung nilai LK.
Validasi upload sertifikat LK.
Menyimpan arsip sertifikat peserta LK.
Publish berita.
Verifikasi pembayaran.
Kirim email.
Integrasi API luar.
```

### Contoh service

```text
create_news_post()
publish_news_post()
create_lk_assessment()
upload_lk_certificate()
create_outgoing_letter()
send_invitation_email()
verify_news_request_payment()
publish_news_request_as_post()
```

---

## 19.3 Layer Data Access

### File

```text
selectors.py
```

### Fungsi

```text
Mengambil data dari database.
Query list.
Query detail.
Filter.
Search.
select_related.
prefetch_related.
annotate.
Pagination query.
```

### Contoh selector

```text
get_latest_news()
get_news_detail_by_slug()
get_active_management_members()
get_lk_batch_detail()
get_batch_participants()
get_cadre_by_commissariat()
get_document_archives()
```

---

## 19.4 Layer Data

### File

```text
models.py
```

### Fungsi

```text
Mendefinisikan tabel.
Mendefinisikan kolom.
Mendefinisikan relasi.
Mendefinisikan constraints.
Mendefinisikan choices.
Mendefinisikan index.
```

### Aturan

```text
Model tidak boleh berisi proses bisnis panjang.
Model tidak boleh berisi query kompleks.
Model hanya sebagai representasi database.
```

---

# 20. Struktur App Django

Struktur aplikasi:

```text
apps/
├── core/
├── accounts/
├── website/
├── organization/
├── content/
├── registration/
├── cadre/
├── training/
├── administration/
└── news_request/
```

---

## 20.1 App core

### Fungsi

```text
Helper umum
Base model
Choices
Pagination
Permission helper
Utility umum
```

### Isi

```text
models.py
choices.py
pagination.py
permissions.py
utils.py
```

---

## 20.2 App accounts

### Tabel

```text
roles
users
```

### Fungsi

```text
Login admin
Logout admin
Manajemen akun admin
Manajemen role
Custom user model Django
```

### Catatan

```text
Sistem menggunakan custom user model accounts.User.
Semua relasi admin menggunakan settings.AUTH_USER_MODEL.
```

---

## 20.3 App website

### Tabel

```text
site_settings
navigation_menus
contact_messages
```

### Fungsi

```text
Homepage
Setting website
Navbar
Footer
CTA
Hero section
Pesan kontak
```

---

## 20.4 App organization

### Tabel

```text
organization_profile
management_members
chairman_histories
```

### Fungsi

```text
Profil organisasi
Pengurus
Galeri Ketua Umum
```

---

## 20.5 App content

### Tabel

```text
programs
events
news_categories
news_posts
gallery_categories
gallery_images
```

### Fungsi

```text
Program
Agenda
Berita
Galeri
```

---

## 20.6 App registration

### Tabel

```text
registration_forms
```

### Fungsi

```text
Link Google Form pendaftaran
```

---

## 20.7 App cadre

### Tabel

```text
commissariats
cadres
cadre_lk_histories
alumni
```

### Fungsi

```text
Komisariat
Kader
Riwayat LK
Alumni
```

---

## 20.8 App training

### Tabel

```text
lk_levels
lk_batches
lk_participants
lk_materials
lk_assessments
lk_assessment_details
signatures
lk_certificates
```

### Fungsi

```text
LK 1, LK 2, LK 3
Materi
Peserta
Penilaian
Upload sertifikat
Arsip sertifikat
Tanda tangan opsional
```

---

## 20.9 App administration

### Tabel

```text
document_archives
incoming_letters
outgoing_letters
invitations
gmail_integrations
email_logs
```

### Fungsi

```text
Arsip
Surat masuk
Surat keluar
Undangan
Gmail
Log email
```

---

## 20.10 App news_request

### Tabel

```text
news_upload_requests
news_request_payments
```

### Fungsi

```text
Request upload berita
Pembayaran request berita
Publish request menjadi berita
```

---

# 21. Prinsip Engineering

---

## 21.1 SRP — Single Responsibility Principle

Aturan:

```text
1 class = 1 tanggung jawab.
1 fungsi = 1 tugas.
1 app = 1 domain utama.
```

Contoh benar:

```text
create_lk_assessment()
upload_lk_certificate()
verify_news_request_payment()
publish_news_request_as_post()
get_latest_news()
get_active_management_members()
```

Contoh yang dihindari:

```text
process_all_lk()
manage_everything()
save_send_print_letter()
```

---

## 21.2 KISS — Keep It Simple

Sistem dibuat sederhana untuk solo developer.

Prioritas awal:

```text
Gunakan Django MVT biasa.
Gunakan templates HTML.
Gunakan services.py dan selectors.py.
Gunakan Django ORM.
Gunakan upload file sertifikat manual.
Gunakan Google Form untuk pendaftaran.
Gunakan Tailwind CSS CDN.
```

Tidak perlu di awal:

```text
Microservices
Event bus
Celery
CQRS
Repository pattern kompleks
Permission engine terlalu detail
PDF generator
Generate sertifikat otomatis
```

---

## 21.3 YAGNI — You Ain’t Gonna Need It

Fitur yang ditunda:

```text
Import otomatis dari Google Form.
Integrasi Gmail OAuth penuh.
Generate sertifikat otomatis.
Generate PDF sertifikat.
Dashboard grafik realtime.
Notifikasi realtime.
Multi organisasi.
Payment gateway otomatis.
```

Dikerjakan jika sudah benar-benar dibutuhkan.

---

## 21.4 DRY — Don’t Repeat Yourself

Kode yang dipusatkan di `core`:

```text
Base timestamp model
Status choices
Pagination helper
Permission helper
Upload path helper
Slug generator
```

---

## 21.5 Dependency Inversion

Dipakai untuk integrasi luar:

```text
Gmail API
File storage eksternal jika nanti dibutuhkan
Google Form import
Payment gateway
```

Contoh:

```text
services.py tidak langsung bergantung pada Gmail API.
services.py memanggil EmailClient interface.
GmailEmailClient menjadi implementasi teknisnya.
```

---

# 22. Kebutuhan Non-Fungsional

---

## 22.1 Keamanan

```text
Password admin wajib di-hash.
Halaman admin wajib login.
Role admin membatasi akses fitur.
Sistem menggunakan custom user model berbasis email.
Relasi ke user/admin menggunakan settings.AUTH_USER_MODEL.
Token Gmail tidak boleh ditampilkan ke admin biasa.
Upload file harus dibatasi tipe dan ukuran.
Input form harus divalidasi.
Slug harus unik.
File .env tidak boleh di-push ke GitHub.
File upload seperti media, bukti pembayaran, sertifikat, dan arsip tidak boleh masuk repository.
```

---

## 22.2 Performa

```text
Gunakan select_related untuk relasi ForeignKey.
Gunakan prefetch_related untuk relasi one-to-many.
Gunakan pagination pada daftar data besar.
Gunakan index pada field pencarian seperti slug, status, tahun, kategori.
```

---

## 22.3 Maintainability

```text
Pisahkan models, selectors, services, views.
Gunakan nama fungsi yang jelas.
Gunakan app berdasarkan domain.
Hindari query langsung di views.
Hindari logic bisnis di templates.
```

---

## 22.4 Backup Data

Data penting yang perlu dibackup:

```text
Database kader
Database alumni
Riwayat LK
Penilaian LK
Sertifikat
Arsip surat
Request berita
File upload
```

---

## 22.5 Audit Minimal

Setiap data penting sebaiknya punya:

```text
created_at
updated_at
created_by / uploaded_by / handled_by
status
```

---

# 23. Prioritas Pengembangan

---

## Phase 1 — MVP Website Publik Dinamis

### Fitur

```text
Login admin
Dashboard sederhana
Profil organisasi
Pengurus
Program
Berita
Agenda
Galeri
Galeri Ketua Umum
Link Google Form pendaftaran
Pesan kontak
Setting website
```

### App yang dikerjakan

```text
accounts
website
organization
content
registration
```

---

## Phase 2 — Database Kader dan Alumni

### Fitur

```text
Komisariat
Kader
Riwayat LK kader
Alumni
Filter data kader 12 tahun
```

### App yang dikerjakan

```text
cadre
```

---

## Phase 3 — LK dan Penilaian

### Fitur

```text
Level LK
Batch LK
Peserta LK
Materi LK
Penilaian LK
Detail penilaian
Tanda tangan opsional
Upload sertifikat manual
Arsip sertifikat peserta LK
```

### App yang dikerjakan

```text
training
```

---

## Phase 4 — Administrasi Surat

### Fitur

```text
Arsip administrasi
Surat masuk
Surat keluar
Undangan
Upload file dokumen
```

### App yang dikerjakan

```text
administration
```

---

## Phase 5 — Request Upload Berita

### Fitur

```text
Request upload berita
Harga Rp50.000
Upload bukti pembayaran
Verifikasi pembayaran
Approve / reject request
Publish request menjadi berita
```

### App yang dikerjakan

```text
news_request
```

---

## Phase 6 — Integrasi Gmail

### Fitur

```text
Hubungkan Gmail HMI
Kirim surat keluar
Kirim undangan
Simpan email logs
```

### App yang dikembangkan

```text
administration
```

---

# 24. MVP Scope

Untuk versi pertama, fitur yang wajib ada:

```text
Login admin
3 role admin
Kelola profil organisasi
Kelola pengurus
Kelola program
Kelola berita
Kelola agenda
Kelola galeri
Kelola galeri Ketua Umum
Kelola link Google Form
Kelola pesan kontak
Kelola komisariat
Kelola kader
Kelola alumni
Kelola batch LK
Kelola peserta LK
Kelola penilaian LK
Upload sertifikat LK
Arsip sertifikat LK
```

Fitur yang bisa ditunda:

```text
Integrasi Gmail penuh
Generate sertifikat otomatis
Generate PDF otomatis
Import Google Form otomatis
Payment gateway otomatis
Dashboard statistik kompleks
```

---

# 25. Risiko dan Solusi

---

## Risiko 1: Scope terlalu besar

### Solusi

```text
Kerjakan bertahap per phase.
Jangan langsung membuat semua fitur.
Fokus MVP dulu.
```

---

## Risiko 2: Integrasi Gmail rumit

### Solusi

```text
Tunda Gmail ke phase akhir.
Awalnya cukup simpan surat dan upload file.
```

---

## Risiko 3: Data Google Form tidak otomatis masuk database

### Solusi

```text
Untuk awal, admin rekap manual ke sistem.
Import CSV bisa ditambahkan nanti.
```

---

## Risiko 4: Pengelolaan sertifikat terlalu kompleks jika dibuat otomatis

### Solusi

```text
Sertifikat tidak dibuat otomatis oleh sistem.
Admin membuat sertifikat secara manual di luar sistem.
Sistem hanya menyediakan fitur upload, arsip, lihat, dan download sertifikat.
```

---

## Risiko 5: Database kader besar

### Solusi

```text
Gunakan filter, search, dan pagination.
Tambahkan index pada field komisariat, lk1_year, status.
```

---

# 26. Kriteria Sukses Produk

Sistem dianggap berhasil jika:

```text
Admin dapat mengelola website tanpa mengubah kode.
Konten website tampil dinamis dari database.
Pendaftaran dapat diarahkan ke Google Form.
Admin dapat mengelola data komisariat.
Admin dapat mengelola data kader 12 tahun.
Admin dapat mengelola alumni.
Admin dapat membuat batch LK.
Admin dapat menginput peserta LK.
Admin dapat mengisi penilaian LK.
Admin dapat meng-upload dan mengarsipkan sertifikat LK berdasarkan peserta.
Admin dapat mengelola arsip surat.
Pengunjung dapat request upload berita.
Admin dapat memverifikasi request berita.
Admin dapat publish request menjadi berita.
Role admin membatasi akses sesuai tugas.
```

---

# 27. Kesimpulan PRD

Sistem ini dirancang sebagai aplikasi web terintegrasi untuk kebutuhan publik dan internal HMI Cabang Pekanbaru.

Secara publik, sistem berfungsi sebagai:

```text
Website profil organisasi
Media publikasi berita
Media informasi agenda
Media dokumentasi galeri
Media pendaftaran melalui Google Form
Media request upload berita
```

Secara internal, sistem berfungsi sebagai:

```text
Admin panel organisasi
Database komisariat
Database kader
Database alumni
Sistem administrasi LK
Sistem penilaian LK
Sistem upload dan arsip sertifikat LK
Sistem arsip surat
Sistem request berita berbayar
```

Arsitektur Django yang digunakan adalah:

```text
Presentation Layer
Business Logic Layer
Data Access Layer
Data Layer
```

Dengan pembagian:

```text
views.py + urls.py + templates/
    Untuk UI dan interaksi.

services.py
    Untuk aksi dan proses bisnis.

selectors.py
    Untuk query data.

models.py
    Untuk skema database.
```

PRD ini dapat dijadikan dasar untuk:

```text
Dokumentasi proyek
Presentasi tugas
Perancangan backend Django
Pembuatan ERD
Pembuatan roadmap development
Pembuatan backlog fitur
Acuan implementasi coding
```

---
