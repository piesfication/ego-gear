Muhammad Rafi Sugianto / PBP B / 2406357135

===============================================================================================

0. Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy

Tautan: https://muhammad-rafi42-egogear.pbp.cs.ui.ac.id/

-----------------------------------------------------------------------------------------------

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jawab: 
Langkah pertama yang saya lakukan untuk mengimplementasikan checklist diatas adalah memikirkan konsep tugas saya. Dalam tugas individu kali ini, saya memikirkan sebuah toko peralatan sepakbola yang terinspirasi dari fiksi "Blue Lock". Toko ini dikhususkan untuk pemain ambisius yang menjadikan ego mereka sebagai bahan bakar utama, bernama EGO Gear.

Kemudian, langkah selanjutnya saya memulai membuat django project untuk Ego Gear. Saya membuat direktori baru bernama ego-gear dan menambahkan requirements.txt di dalamnya. requirements.txt ini akan berisi dependencies, yaitu komponen, library, framework, atau modul eksternal yang dibutuhkan oleh suatu program bisa berjalan. Kemudian, saya mengaktifkan virtual environment dan menginstall dependencies yang dicantumkan di requirements.txt tadi.

Selanjutnya, saya membuat django project dengan perintah "django-admin startproject ego_gear ." , dengan ini saya telah mengimplementasikan checklist pertama, yaitu "Membuat sebuah proyek Django baru"

Langkah berikutnya adalah mengonfigurasi environment variables. Saya membuat .env dan menambahkan konfigurasi PRODUCTION=false agar django tahu kalau saya sedang di mode development lokal. Saya juga menambahkan .env.prod dan mengisi dengan konfigurasi produksi seperti nama database, host database, dst. Hal ini bertujuan agar pada saat projek django tsb dijalankan di server, dia akan tahu ini pakai database yg mana, skema apa yg digunakan (misal tutorial, tugas individu), dan tahu kalau ini production mode.

Kemudian, saya memodifikasi settings.py agar django bisa baca konfigurasi dari file .env / .env.prod (seperti DB_NAME, DB_USER, PRODUCTION). Saya menambahkan "localhost" dan "127.0.0.1" agar mengizinkan django menerima request dari alamat lokal. Saya juga menambahkan konfigurasi di settings.py agar django bisa membedakan apakah dia sedang running di development atau production, berdasarkan isi file .env. Selain itu juga dilakukan konfigurasi agar django bisa otomatis memilih database berdasarkan environment (PRODUCTION=True atau False), misal ketika PRODUCTION=True maka pakai PostgreSQL dengan kredensial dari .env.prod., sedangkan kalau PRODUCTION=False maka pakai pakai SQLite (file database lokal).

Pada langkah selanjutnya, saya menjalankan perintah python manage.py runserver untuk menerapkan migration django ke database. Migrasi bertujuan supaya struktur database selalu sesuai dengan model yang tertulis di kode. Misalnya ketika menambahkan model baru atau mengubah field di models.py, django tidak otomatis mengubah database. Saat menjalankan python manage.py migrate, django membaca file-file migrasi yang sudah dibuat sebelumnya dan kemudian menerapkan perubahan itu ke database.

Langkah berikutnya yang saya lakukan selanjutnya adalah melakukan push ke github. Sebelum itu tentunya saya telah membuat repo baru di github dan menginisiasi direktori saya sebagai repo git. Saya juga menambahkan file .gitignore agar berkas-berkas yang dicantumkan tidak ikut di-push ke git.

Selanjutnya, saya mengakses https://pbp.cs.ui.ac.id/ dan membuat proyek baru bernama egogear. Saya menyimpan environment variable dan menambahkan url deployment saya pada ALLOWED_HOSTS (settings.py). Saya menjalankan perintah yang terdapat pada informasi project command dan melakukan deployment ke PWS. Dengan melakukan langkah ini saya telah mengimplementasikan checklist ke-tujuh, yaitu "Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet."

Setelah menyelesaikan rangkaian pembuatan proyek django hingga deployment di atas, selanjutnya saya melangkah ke proses pembuatan aplikasi main. Saya menjalankan perintah "python manage.py startapp main" dan mendaftarkan aplikasi main di settings.py. Hal ini dilakukan dengan menambahkan 'main' ke dalam variabel INSTALLED_APPS. Dengan begitu saya telah mengimplementasikan checklist ke-dua, yaitu "Membuat aplikasi dengan nama main pada proyek tersebut".

Langkah selanjutnya adalah melakukan implementasi dengan html. Saya membuat direktori templates di dalam direktori main, dan menambahkan main.html di dalam direktori templates. Saya mengisi main.html dengan konten sederhana berupa heading yang menampilkan nama toko "EGO Gear" dan isian berupa nama dan kelas. 

Setelah selesai dengan html, saya menyiapkan model yang akan saya gunakan. Berdasarkan deskripsi tugas, model harus mengikuti beberapa ketentuan, yaitu memiliki nama Product, dan memiliki atribut wajib sebagai berikut:
- name sebagai nama item dengan tipe CharField.
- price sebagai harga item dengan tipe IntegerField.
- description sebagai deskripsi item dengan tipe TextField.
- thumbnail sebagai gambar item dengan tipe URLField.
- category sebagai kategori item dengan tipe CharField.
- is_featured sebagai status unggulan item dengan tipe BooleanField.

Untuk mengimplementasikannya, saya menambahkan model sebagai berikut di dalam model.py:

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)                 
    price = models.IntegerField()                           
    description = models.TextField()                        
    thumbnail = models.URLField(blank=True, null=True)      
    category = models.CharField(max_length=100)              
    is_featured = models.BooleanField(default=False)        
    stock = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=50, blank=True, null=True)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.name} - {self.category}"

Pada model tersebut saya menambahkan beberapa atribut pelengkap seperti stock, brand, dan rating. Pada step ini, saya telah mengimplementasikan checklist ke-empat, yaitu "Membuat model pada aplikasi main". Saya juga telah menjalankan migrasi pada model dengan perintah "python manage.py makemigrations" dan "python manage.py migrate"

Langkah selanjutnya yang saya lakukan adalah menghubungkan view dengan template. Tujuan dari tahap ini adalah agar data dari database bisa ditampilkan dengan template, hal ini memerlukan perantara dari views (views.py). Saya menambahkan fungsi show_main di views.py yang akan menerima http request dan mengembalikan respons berupa halaman html. Pada fungsi ini data-data yang ingin ditampilkan di template berupa nama toko, nama mahasiswa, dan kelas akan di-hardcode pada dictionary, jadi views tidak mengambil datanya langsung dari database. Dengan melakukan langkah ini, saya telah mengimplementasi checklist ke-lima, yaitu "Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu."

Selanjutnya adalah tahap routing url project. Tahap ini dibagi menjadi routing url pada tingkat proyek dan routing url pada tingkat aplikasi. Pada tingkat proyek, routing url dilakukan dengan menambahkan "path('', include('main.urls'))" pada urls.py tingkat proyek. Tahap ini berfungsi agar saat ada request ke root proyek (''), teruskan ke routing yang ada di aplikasi main. Secara sederhana, routing pada tingkat proyek berfungsi sebagai gerbang utama yang memutuskan aplikasi mana yang akan menangani request. Kemudian tahap berlanjut ke routing tingkat aplikasi.

Routing pada tingkat aplikasi dilakukan dengan membuat berkas urls.py pada direktori main. Kemudian saya mengimpor fungsi path dari django, path digunakan untuk mendefinisikan pola url dan menentukan view mana yang dijalankan saat url itu diakses. Pada urls.py tsb saya mendefinisikan path dengan path('', show_main, name='show_main'). Sehingga, jika ada request ke root aplikasi, django akan memanggil fungsi show_main untuk menyiapkan data dan merender template. 

Dengan dua langkah tersebut, saya telah mengimplementasi checkpoint ke-tiga dan ke-enam, yaitu "Melakukan routing pada proyek agar dapat menjalankan aplikasi main." dan "Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py."

-----------------------------------------------------------------------------------------------

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Jawab: 
![Bagan](<WhatsApp Image 2025-09-09 at 23.14.32_594a1523.jpg>)

Penjelasan: Request dari client pertama kali masuk ke urls.py tingkat proyek untuk dicek aturan routingnya. Jika ada yang sesuai, request lanjut ke urls.py tingkat aplikasi. Dari sana, request diarahkan ke views.py. View bertugas memproses logika, bisa berinteraksi dengan models.py seperti membaca atau menulis data ke database. Setelah data siap, view memanggil template untuk merender data tsb ke dalam bentuk HTML. Hasil render template ini kemudian dikirim kembali ke client sebagai HTTP response.

Kaitan antara urls.py, views.py, models.py, dan html adalah seagai berikut:
- urls.py akan menerima http request dan mengecek pola URL yang cocok, kemudian menunjuk ke fungsi yang ada di views.py.
- views.py bertugas mengerjakan logika dan memproses data dari database melalui models.py
- data yang telah diproses, views memanggil template berupa file .html untuk merender data tsb
- hasil render template dikirim kembali ke client sebagai http response

-----------------------------------------------------------------------------------------------

3. Jelaskan peran settings.py dalam proyek Django!

Jawab: Sesuai dengan namanya, settings.py berperan dalam mengatur bagaimana proyek berjalan, settings.py memastikan smeua komponen dalam proyek berjalan sesuai konfigurasi. Jika dalam kasus tugas individu kali ini, saya memanfaatkan peran settings.py sebagai pengatur perilaku proyek django agar sesuai dengan environment tempat dia dijalankan. settings.py bertugas membaca variabel dari .env atau .env.prod agar kredensial database dan mode aplikasi dipisahkan secara aman. settings.py juga berperan mengatur host mana saja yang boleh mengakses aplikasi, misalnya dengan menambahkan localhost dan 127.0.0.1 supaya request dari alamat lokal diterima. Selanjutnya , settings.py menentukan apakah aplikasi berjalan di development atau production dengan membaca variabel PRODUCTION, lalu memilih database yang sesuai, misal SQLite untuk development karena lebih sederhana, atau PostgreSQL dengan kredensial lengkap untuk production. Dengan begitu, settings.py berperan sebagai pengendali utama yang memastikan django bisa beradaptasi pada environmentnya.

-----------------------------------------------------------------------------------------------

4. Bagaimana cara kerja migrasi database di Django?

Jawab: Sebelum menjawab tentang cara kerja migrasi database, ada baiknya saya menjelaskan terlebih dahulu tentang database dan model. Database adalah tempat menyimpan data aplikasi yang tersusun dalam tabel dengan kolom dan baris, terstruktur, dan kuat untuk dipakai aplikasi.
Di django, kita tidak bisa langsung menulis tabel database, oleh karena itu digunakan model, yg merupakan representasi tabel database dalam bentuk class Python yang ditulis di models.py.

Migrasi adalah cara django untuk menerjemahkan perubahan di models.py menjadi instruksi yang mengubah struktur database. Django mencatat perubahan dalam file migrasi, lalu ketika dijalankan dengan perintah python manage.py migrate, Django akan mengeksekusi instruksi tersebut ke database sehingga tabel benar-benar dibuat atau diperbarui. Dengan begini kita bisa mengubah struktur data lewat kode Python (model), lalu melakukan migrasi agar perubahan itu sinkron dengan database.

-----------------------------------------------------------------------------------------------

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Jawab: Menurut saya django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena lebih mudah dipelajari dan menyediakan alur pengembangan yang lengkap. Selain itu framework django lebih umum digunakan oleh pemula dan video tutorialnya banyak ditemukan di internet, sehingga menjadikan django salah satu framework yang mudah dipelajari. 

-----------------------------------------------------------------------------------------------

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Jawab: Penjelasan tutorial sudah sangat baik dan lengkap karena tidak hanya menyediakan langkah yg harus dilakukan, melainkan juga menjelaskan kegunaan dari tiap kode serta konsep yang mendasarinya, makasih kak :D