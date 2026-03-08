<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PWL_POS - Home</title>
    <style>
        body{margin:0;font-family:Arial,sans-serif;background:#f5f7fb;color:#1f2937}
        .hero{max-width:1000px;margin:60px auto;padding:48px;background:white;border-radius:24px;box-shadow:0 10px 30px rgba(0,0,0,.08)}
        h1{font-size:44px;margin:0 0 12px}
        p{font-size:18px;color:#4b5563;margin:0 0 24px}
        .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;margin-top:28px}
        .card{padding:20px;border-radius:18px;background:#eef2ff;text-decoration:none;color:#111827;display:block}
        .card strong{display:block;font-size:18px;margin-bottom:6px}
    </style>
</head>
<body>
    <div class="hero">
        <h1>Point of Sales</h1>
        <p>Selamat datang di aplikasi PWL_POS. Pilih kategori produk, buka profil user, atau masuk ke halaman penjualan.</p>
        <div class="grid">
            <a class="card" href="/category/food-beverage"><strong>Food & Beverage</strong><span>Produk makanan dan minuman</span></a>
            <a class="card" href="/category/beauty-health"><strong>Beauty & Health</strong><span>Produk kecantikan dan kesehatan</span></a>
            <a class="card" href="/category/home-care"><strong>Home Care</strong><span>Produk kebutuhan rumah</span></a>
            <a class="card" href="/category/baby-kid"><strong>Baby Kid</strong><span>Produk bayi dan anak</span></a>
            <a class="card" href="/user/1/name/Yab"><strong>User Profile</strong><span>Lihat profil pengguna</span></a>
            <a class="card" href="/sales"><strong>Sales</strong><span>Buka halaman transaksi</span></a>
        </div>
    </div>
</body>
</html>
