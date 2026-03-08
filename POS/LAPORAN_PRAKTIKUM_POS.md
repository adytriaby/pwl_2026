# Laporan Praktikum Laravel POS

## Catatan Eksekusi
Project Laravel **POS** sudah dibuat lengkap sesuai jobsheet (route, controller, dan view). Saat proses menjalankan via Composer/Artisan di mesin ini, environment Windows mengalami kendala pada autoload Composer, sehingga screenshot halaman di bawah disusun dari output view yang sama dengan yang digunakan project Laravel.

Lokasi project:
`C:\Users\aditr\.openclaw\workspace\POS`

## 1. Halaman Home
**Route:** `/`

**Screenshot kode:** `report_assets/02_home_controller.png` dan `report_assets/06_view_home.png`

**Screenshot website:** `report_assets/13_page_home.png`

**Penjelasan singkat:**
Halaman Home menggunakan `HomeController@index` yang memanggil view `home.blade.php`. Saat route `/` diakses, sistem menampilkan halaman awal website POS.

## 2. Halaman Products
### 2.1 Food & Beverage
**Route:** `/category/food-beverage`

**Screenshot kode:** `report_assets/03_product_controller.png` dan `report_assets/07_view_food_beverage.png`

**Screenshot website:** `report_assets/14_page_food_beverage.png`

**Penjelasan singkat:**
Route prefix `category` digunakan untuk mengelompokkan halaman produk. Method `foodBeverage()` pada `ProductController` memanggil view kategori makanan dan minuman.

### 2.2 Beauty & Health
**Route:** `/category/beauty-health`

**Screenshot kode:** `report_assets/03_product_controller.png` dan `report_assets/08_view_beauty_health.png`

**Screenshot website:** `report_assets/15_page_beauty_health.png`

**Penjelasan singkat:**
Method `beautyHealth()` memproses route kategori beauty & health dan menampilkan view yang sesuai.

### 2.3 Home Care
**Route:** `/category/home-care`

**Screenshot kode:** `report_assets/03_product_controller.png` dan `report_assets/09_view_home_care.png`

**Screenshot website:** `report_assets/16_page_home_care.png`

**Penjelasan singkat:**
Method `homeCare()` digunakan untuk menampilkan halaman kategori home care melalui view `products.home-care`.

### 2.4 Baby Kid
**Route:** `/category/baby-kid`

**Screenshot kode:** `report_assets/03_product_controller.png` dan `report_assets/10_view_baby_kid.png`

**Screenshot website:** `report_assets/17_page_baby_kid.png`

**Penjelasan singkat:**
Method `babyKid()` menampilkan halaman kategori baby kid pada project POS.

## 3. Halaman User
**Route:** `/user/{id}/name/{name}`

**Contoh akses:** `/user/1/name/Budi`

**Screenshot kode:** `report_assets/04_user_controller.png` dan `report_assets/11_view_user.png`

**Screenshot website:** `report_assets/18_page_user.png`

**Penjelasan singkat:**
Route ini menggunakan parameter dinamis `id` dan `name`. Nilai parameter dikirim ke view melalui `UserController@profile`, lalu ditampilkan pada halaman profil pengguna.

## 4. Halaman Penjualan
**Route:** `/sales`

**Screenshot kode:** `report_assets/05_sales_controller.png` dan `report_assets/12_view_sales.png`

**Screenshot website:** `report_assets/19_page_sales.png`

**Penjelasan singkat:**
Halaman penjualan menggunakan `SalesController@index` dan menampilkan view `sales.blade.php` yang berisi informasi halaman transaksi POS.

## 5. Routing Utama
**Screenshot kode routing:** `report_assets/01_routes_web_php.png`

**Penjelasan singkat:**
File `routes/web.php` berisi seluruh route utama project POS, yaitu route home, route prefix category, route parameter user, dan route sales.

## Kesimpulan
Berdasarkan praktikum ini, konsep MVC pada Laravel diterapkan dengan membagi aplikasi menjadi:
- **Route** sebagai penghubung URL
- **Controller** sebagai pengatur logika
- **View** sebagai tampilan halaman

Dengan struktur tersebut, aplikasi POS menjadi lebih rapi, mudah dipelihara, dan mudah dikembangkan.
