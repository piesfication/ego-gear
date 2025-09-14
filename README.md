Muhammad Rafi Sugianto / PBP B / 2406357135

===============================================================================================

[TUGAS 2]

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

===============================================================================================

[TUGAS 3]

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
 
Jawab: Sebelum menjawab pertanyaan ii, saya akan menjelaskan terlebih dahulu apa itu data delivery. Data delivery adalah proses mengirim atau menyampaikan data dari satu tempat ke tempat lain agar bisa digunakan. Dalam konteks ini, tempat bisa berupa database tempat data disimpan, server atau backend tempat data diproses, template HTML di frontend tempat data ditampilkan ke pengguna, atau sistem lain yg menerima data melalui API seperti JSON atau XML.

Data delivery diperlukan dalam pengimplementasian sebuah platform karena data harus sampai ke pihak atau sistem yang membutuhkannya. Data delivery memastikan informasi yang tersimpan di database atau di backend dapat berpindah ke frontend untuk ditampilkan, atau ke sistem lain melalui API agar bisa diproses lebih lanjut. Jika tidak ada data delivery, maka input dari pengguna, misal melalui form, tidak bisa tersimpan di server, dan data yg sudah ada di server tidak bisa diakses oleh pengguna maupun aplikasi lain karena tidak adanya pergerakan data. Data delivery adalah mekanisme yang membuat data bergerak ke tempat yang membutuhkannya, sehingga platform bisa berjalan dengan interaktif.

-----------------------------------------------------------------------------------------------

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Jawab: Menurut saya, JSON terasa lebih sederhana dan mudah dipahami dibanding XML. Misal ketika ingin melihat informasi tentang seseorang. Dengan JSON, data ditulis dalam format key value, misal:

 {"name": "Burhan", "age": 25"}
 
Menurut saya teks tersebut bisa langsung dimengerti bahwa nama orang itu Burhan dan usianya 25 tahun.

Sementara itu, dengan XML, informasi yang sama ditulis dengan tag pembuka dan penutup, misal:

 <person>
    <name>Burhan</name>
    <age>25</age>
</person>
 
Bagi orang yang tidak terbiasa dengan kode, tanda < > dan struktur yang terdiri dari banyak lapisan bisa membuat data terlihat lebih rumit untuk dibaca. JSON terlihat lebih ringkas, rapi, dan langsung ke inti informasi, sehingga lebih mudah dibaca dan dimengerti.

Selain karena kemudahan pembacaan yang saya sebutkan sebelumnya, ada beberapa alasan lain yang menjadikan JSON lebih populer dibandingkan XML. Diantaranya adalah karena JSON lebih efisien untuk dikirim lewat jaringan karena ukurannya lebih kecil dan lebih mudah diproses oleh bahasa pemrograman modern.

-----------------------------------------------------------------------------------------------

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Jawab: Method is_valid() berfungsi untuk mengecek apakah data yang dikirim melalui telah memenuhi semua ketentuan yang ditetapkan. Dalam kasus tugas kali ini, karena form dibuat dari model menggunakan ModelForm, maka aturan yang sudah ditentukan di model otomatis diterapkan di form (misalnya menentukan tipe data dan jumlah karakter maksimal yang bisa dimasukkan di form).

Method ini diperlukan karena kita tidak ingin kasus seperti data kosong atau salah tipe tersimpan di database. Dengan is_valid(), kita memastikan hanya data yang benar dan sesuai aturan yang diterima dan diproses, sehingga aplikasi lebih aman dan data tetap konsisten.

-----------------------------------------------------------------------------------------------

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Jawab: Sebelum menjawab pertanyaan ini, saya akan menjelaskan terlebih dahulu apa yg dimaksud dengan CSRF token. CSRF token adalah kode unik yang dibuat oleh server dan disisipkan ke dalam form HTML untuk melindungi aplikasi dari serangan CSRF. Kode ini akan berfungsi sebagai tanda pengenal rahasia untuk memastikan request yang dikirim ke server berasal dari pengguna asli dan dari aplikasi itu sendiri, bukan dari pihak ketiga. 

Serangan CSRF itu sendiri adalah jenis serangan di mana penyerang mencoba membuat request palsu ke server menggunakan sesi login pengguna tanpa sepengetahuan pengguna. Oleh karena itu kita membutuhkan csrf_token saat membuat form di Django. Dengan menambahkan {% csrf_token %} di form, Django akan menyisipkan token unik yang terkait dengan sesi pengguna. Token ini dikirim bersama data form ketika pengguna submit. Server kemudian akan memeriksa token tersebut. Jika token valid, request diproses, namun jika token tidak ada atau salah, request ditolak.

Jika kita tidak menambahkan csrf_toke pada form Django, maka server tidak bisa membedakan request asli dari request palsu. Sehingga setiap request yang datang dari browser pengguna dianggap sah.

Hal ini dapat dimanfaatkan oleh penyerang dengan membuat halaman web jahat yang terlihat normal. Misalkan pengguna membuka halaman itu saat sedang login di situs lain yang tidak menerapkan csrf_token, maka halaman jahat bisa mengirim perintah palsu ke situs yang dimana ia sedang login (misalnya memindahkan uang atau mengubah data tanpa disadari pengguna). Karena server mengira request berasal dari pengguna tsb, maka perintah palsu tadi bisa dijalankan.

-----------------------------------------------------------------------------------------------

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jawab: 
Langkah pertama yang saya lakukan adalah membuat form sederhana untuk menginput produk baru pada aplikasi. Tapi sebelum itu, saya memberi beberapa perubahan pada model dengan menghapus beberapa atribut yang menurut saya tidak perlu, dan melakukan migrasi pada model. Selanjutnya untuk membuat form sederhana, saya menyiapkan sebuah class bernama ProductForm yang akan mewarisi ModelForm. Karena memakai ModelForm, form akan digenerate secara otomatis berdasarkan fields yg telah ditentukan. Selain itu, data yang diisi lewat form bisa langsung divalidasi dan disimpan sebagai objek product di database cukup dengan form.save(). 

Langkah selanjutnya yang saya lakukan adalah menghubungkan form dan data product dengan tampilan web. Saya mengimport beberapa fungsi bantu dari Django seperti render, redirect, dan get_object_or_404, masing2 berguna untuk merender template HTML, meredirect halaman setelah data tersimpan, dan mengambil objek dari database. 

Setelahnya, saya menambahkan .objects.all(), untuk mengambil semua product dari database, di fungsi show_main. Saya juga menambahkan fungsi create_product dan show_product. Fungsi create_product digunakan untuk menghasilkan form dimana pengguna dapat memasukkan data untuk product baru. Sementara show_product berguna untuk menampilkan product berdasarkan id, fungsi ini menggunakan get_object_or_404 sehingga akan mengembalikan halaman 404 ketika product tidak ditemukan. Saya mengimport kedua fungsi create_product dan show_product tersebut ke urls.py,dan menambahkan path urlnya di urlpatterns.

Berikutnya, saya melakukan implementasi skeleton pada kerangka views. Hal ini dilakukan supaya semua halaman pada tampilan web memiliki dasar yang sama. Saya menambahkan tag {% block %} dan {% endblock %} sebagai template dimana fitur unik tiap halaman diletakkan. Saya juga mengonfigurasi settings.py agar mendeteksi base.html sebagai file template.

Setelahnya, saya memperbarui main.html agar bisa menampilkan data product dan menambahkan tombol Add Product yang akan meredirect pengguna ke form. Kemudian saya membuat file create_product.html, yaitu form input data ketika menambahkan produk baru. Dengan ini, saya telah mengimplementasikan checklist ke-4, yaitu "Membuat halaman form untuk menambahkan objek model pada app sebelumnya." Saya juga membuat product_detail.html untuk halaman yang menampilkan detail produk. Dengan ini saya telah mengimplementasikan checklist ke-5, yaitu "Membuat halaman yang menampilkan detail dari setiap data objek model".

Pada rangkaian langkah tersebut juga saya telah mengimplementasikan checkpoint ke-3,yaitu "Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek."

Selanjutnya, saya menambahkan url deployment saya pada CSRF_TRUSTED_ORIGINS di settings.pyHal ini dilakukan untuk memberitahu Django bahwa alamat website yang sudah kamu deploy adalah alamat yang aman dan dipercaya untuk menerima permintaan yang membawa CSRF token.

Setelah menyelesaikan fitur form dan menampilkan detail produk, saya lanjut ke menampilkan data dalam bentuk XML dan JSON. Untuk melakukan implementasi tersebut, saya mengimport HttpResponse, serializers, dan menambahkan 2 fungsi baru di views.py. Fungsi pertama, show_xml akan mengambil semua objek produk dalam database, dan menerjemahkannya menjadi format xml, kemudian mengembalikan seluruh data produk dalam format xml sebagai http response. Fungsi kedua, show_json, juga akan mengambil semua objek produk dalam database, namun menerjemahkannya menjadi format json, kemudian mengembalikan seluruh data produk dalam format json sebagai http response. 

Selanjutnya saya juga menambahkan 2 fungsi lagi, show_xml_by_id dan show_json_by_id, yg berfungsi untuk mengembalikan data dalam bentuk xml dan json, tapi berdasarkan id. Cara kerjanya sama dengan 2 fungsi sebelumnya, tapi kita tidak mengambil semua objek dalma database, melainkan melakukan filter berdasarkan id dengan news_item = News.objects.filter(pk=news_id). Setelah itu saya juga mengimport keempat fungsi tadi ke urls.py dan menambahkan pathnya di urlpatterns. Dengan ini, saya telah mengimplementasikan checklist pertama dan kedua, yaitu "Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID." dan "Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1."

-----------------------------------------------------------------------------------------------

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

Jawab: Sejujurnya saya masih bingung tentang kegunaan postman selain membaca data dalam xml dan json, tapi selain itu penjelasan tutorial sudah sangat baik dan lengkap karena tidak hanya menyediakan langkah yg harus dilakukan, melainkan juga menjelaskan kegunaan dari tiap kode serta konsep yang mendasarinya, makasih kak :D

-----------------------------------------------------------------------------------------------

7. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.




