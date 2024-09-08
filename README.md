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




