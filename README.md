# Tugas Individu 2
Nama:   Luvenia Feodora Saragih  
NPM:    2306228402  
Kelas:  PBP F

Link Menuju Project: http://luvenia-feodora-luveinasstore.pbp.cs.ui.ac.id/

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Untuk membuat project Django baru, hal pertama yang saya lakukan adalah membuat repositori baru di github dan kemudian melakukan clone repositori ke direktori lokal yang akan digunakan untuk membuat project. Setelah itu, saya menambahkan file `.gitignore` yang diisi dengan berkas-berkas yang tidak perlu didetect oleh Git. Kemudian, saya membuat virtual environment dan mengaktifkannya untuk mengunduh module-module yang diperlukan dalam pengembangan web berbasis Django. Setelah melakukan seluruh hal tersebut, baru saya dapat membuat project Django yang bernama "luveinas_store" dengan cara menjalankan kode berikut:  
``` django-admin startproject luveinas_store . ```

2. Untuk membuat aplikasi bernama "main", saya perlu untuk menjalankan kode:  
``` python manage.py startapp main ```  
Setelah itu, saya harus memasukkan "main" ke dalam daftar aplikasi yang terdapat pada `settings.py`

3. Agar aplikasi main pada proyek dapat dijalankan, saya harus membuat file `urls.py` terlebih dahulu pada direktori "main" yang berisi rute menuju fungsi yang akan menampilkan aplikasi main. Kemudian, saya juga menambahkan "main.urls" pada variabel urlpatterns di `urls.py` yang berada di direktori project untuk memastikan bahwa aplikasi main juga dapat diakses dengan menggunakan url menuju project.

4. Untuk membuat model pada aplikasi main dengan nama Product dan memiliki atribut name, price, dan description, saya harus mengganti file `models.py` yang terdapat pada direktori main, yaitu dengan mengganti nama class dengan "Product" dan mengisi class dengan atribut-atribut yang disesuaikan dengan tipe data yang mewakili atribut tersebut.

5. Agar dapat dilihat oleh orang lain, saya melakukan deployment melalui PWS dengan cara menekan tombol add new project, mengisi field project name dengan nama project yang akan saya buat dan kemudian menekan tombol create new project. Setelah itu, saya memasukkan URL deployment PWS saya ke variabel ALLOWED_HOSTS yang terdapat pada ```settings.py``` di direktori project Django saya. Setelah semua perubahan saya lakukan, termasuk membuat README ini, saya melakukan git add, commit, dan push ke GitHub dan PWS sehingga project ini dapat dilihat oleh orang lain.

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas html.  
![bagan_request](images/bagan_request.png)

### Jelaskan fungsi git dalam pengembangan perangkat lunak!  
Git berfungsi dalam memberikan fasilitas kepada para pengembang perangkat lunak untuk dapat berkolaborasi dalam prosesnya. Git mampu melacak perubahan yang dibuat pada source code (version control), membuat jalur pengembangan terpisah dari cabang utama (branching) dan menggabungkan kembali ke cabang utama (merge). 

### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, framework Django dijadikan permulaan dalam pembelajaran pengembangan perangkat lunak karena terdapat banyak fitur bawaan yang siap untuk digunakan sehingga cocok untuk para pemula yang lebih diprioritaskan untuk mempelajari konsep terlebih dahulu. Selain itu juga, karena framework ini menggunakan bahasa pemrograman python, pemula juga akan dimudahkan dalam prosesnya karena python memiliki sintaks yang mudah dipahami.  

### Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM karena mengkonversi datanya dalam basis data berbentuk tabel relasional. Hal ini membuat pengembang dapat berinteraksi dengan basis data tanpa perlu menulis SQL secara langsung.

# Tugas Individu 3
### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Kita memerlukan data delivery dalam pengimplementasian sebuah platform untuk memastikan bahwa data yang diperlukan oleh pengguna dapat diperoleh dengan cepat dan efisien.

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, JSON lebih unggul karena strukturnya yang lebih sederhana dan mudah dimengerti oleh manusia dibandingkan dengan XML. Dalam XML, terdapat banyak tag yang harus dibuka dan ditutup, yang membuatnya lebih rumit dan panjang. Sebaliknya, struktur JSON menyerupai dictionary dalam Python, sehingga lebih mudah dibaca. Selain itu, JSON lebih populer karena lebih mudah diproses oleh bahasa pemrograman modern seperti JavaScript, di mana data dalam format JSON dapat langsung diolah tanpa memerlukan library tambahan atau alat bantu khusus. Ukuran file JSON yang umumnya lebih kecil dibandingkan dengan XML juga membuatnya lebih efisien dalam pengiriman data melalui jaringan, sehingga mempercepat proses transmisi.

### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method `is_valid()` pada form Django berfungsi untuk memastikan bahwa isi/data dari pengisian form merupakan informasi yang valid yang sesuai dengan retriksi yang diberikan. Kita membutuhkan method `is_valid()` agar dapat memperoleh data yang bersih dan sesuai dengan format yang kita inginkan.

### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Kita membutuhkan `crsf_token` saat membuat form di Django untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). Cross-Site Request Forgery (CSRF) adalah serangan yang bertujuan untuk membuat seorang pengguna melakukan hal-hal yang tidak diinginkan terhadap aplikasi berbasis web tanpa sepengetahuan pengguna tersebut. Keberadaan `csrf_token` adalah untuk memastikan semua token yang dikirimkan pada permintaan POST yang diterima oleh server sesuai dengan token yang dihasilkan oleh sesi dari pengguna tersebut untuk dapat melakukan POST. Ketidakadaan `csrf_token` dapat dimanfaatkan oleh penyerang untuk mengirimkan permintaan POST dengan menggunakan sesi pengguna yang aktif tanpa diketahui oleh server bahwa permintaan tersebut bukanlah permintaan yang sah dari pengguna.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Hal pertama yang saya lakukan adalah membuat `base.html` di dalam direktori templates pada direktori utama sebagai template umum untuk halaman web lainnya pada proyek. Kemudian, saya juga menambahkan base.html sebagai templates pada `settings.py` dan mengubah `main.html` saya ke dalam struktur yang telah didefinisikan pada `base.html`

2. Kemudian, saya menambahkan variabel id yang berisi UUID (string acak) pada class Product pada berkas `models.py` di direktori main agar setiap respons memiliki id yang unik.

3. Ketiga, saya membuat form input data produk dengan cara membuat berkas `forms.py` di direktori main yang bertujuan untuk menerima data produk baru yang akan dijual oleh Luveina's Store. pada file `forms.py` ini, saya membuat class ProductForm yang berisi fields nama produk, harga produk dan deskripsi produk.

4. Untuk memastikan bahwa form yang telah saya buat dapat ditampilkan ke pengguna, saya memodifikasi `views.py` milik direktori main dengan menambahkan fungsi baru yaitu `create_product(request)` yang menerima parameter request dengan tujuan untuk menampilkan form kepada pengguna dan menangkap respons pengguna melalui proses validasi hingga penyimpanan data. Selain itu, saya juga membuat file `create_product.html` sebagai file yang akan ditampilkan kepada pengguna.

5. Selain fungsi create_product, saya juga menambahkan 4 fungsi lainnya yaitu `show_xml(request)` dan `show_json(request)` untuk menampilkan data respons dalam bentuk xml dan JSON serta `show_xml_by_id(request, id)` dan `show_json_by_id(request, id)` untuk menampilkan data respons sesuai dengan id yang diberikan dalam bentuk xml dan JSON.

6. Untuk memastikan `urls.py` dapat mengarahkan pengguna ke laman yang tepat, saya mengimpor semua fungsi baru yang telah saya buat tadi dan menambahkan path URLnya ke dalam variabel urlpatterns milik `urls.py` pada direktori main

### Screenshot Postman
![xml](images/xml.png)
![json](images/json.png)
![xml_by_id](images/xml_id.png)
![json_by_id](images/json_id.png)