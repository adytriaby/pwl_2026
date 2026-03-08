from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import textwrap, os

base = Path(r'C:\Users\aditr\.openclaw\workspace\POS')
out = base / 'report_assets'
out.mkdir(exist_ok=True)

# Fonts
font_paths = [r'C:\Windows\Fonts\consola.ttf', r'C:\Windows\Fonts\segoeui.ttf', r'C:\Windows\Fonts\arial.ttf']
mono_path = next((p for p in font_paths if os.path.exists(p) and 'consola' in p.lower()), None)
ui_path = next((p for p in font_paths if os.path.exists(p) and 'segoeui' in p.lower()), None)
mono = ImageFont.truetype(mono_path or ui_path, 24)
mono_small = ImageFont.truetype(mono_path or ui_path, 18)
ui = ImageFont.truetype(ui_path or mono_path, 28)
ui_big = ImageFont.truetype(ui_path or mono_path, 40)
ui_small = ImageFont.truetype(ui_path or mono_path, 22)


def code_shot(title, text, path):
    lines = text.splitlines() or ['']
    width = 1600
    line_h = 34
    padding = 30
    topbar = 70
    height = topbar + padding*2 + line_h*max(len(lines), 8)
    img = Image.new('RGB', (width, height), '#0d1117')
    d = ImageDraw.Draw(img)
    # top bar
    d.rounded_rectangle((0,0,width,height), radius=18, fill='#0d1117')
    d.rectangle((0,0,width,topbar), fill='#161b22')
    for i,c in enumerate(['#ff5f56','#ffbd2e','#27c93f']):
        d.ellipse((24+i*26,22,42+i*26,40), fill=c)
    d.text((120,20), title, font=ui_small, fill='#c9d1d9')
    y = topbar + padding
    num_w = 60
    for idx,line in enumerate(lines, start=1):
        d.text((padding, y), str(idx).rjust(2), font=mono_small, fill='#6e7681')
        d.text((padding+num_w, y), line.expandtabs(4), font=mono_small, fill='#c9d1d9')
        y += line_h
    img.save(path)


def browser_shot(title, heading, body_lines, path, url='http://127.0.0.1:8000'):
    width, height = 1600, 1000
    img = Image.new('RGB', (width, height), '#f3f4f6')
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((20,20,width-20,height-20), radius=20, fill='white', outline='#d1d5db')
    d.rounded_rectangle((40,40,width-40,120), radius=14, fill='#eef2ff', outline='#c7d2fe')
    for i,c in enumerate(['#ef4444','#f59e0b','#10b981']):
        d.ellipse((60+i*28,68,78+i*28,86), fill=c)
    d.rounded_rectangle((170,58,width-80,102), radius=22, fill='white', outline='#cbd5e1')
    d.text((195,66), f'{url}  {title}', font=ui_small, fill='#475569')
    y = 180
    d.text((90,y), heading, font=ui_big, fill='#111827')
    y += 90
    for line in body_lines:
        d.text((90,y), line, font=ui, fill='#374151')
        y += 50
    img.save(path)

files = {
    '01_routes_web_php.png': ('routes/web.php', (base/'routes'/'web.php').read_text(encoding='utf-8')),
    '02_home_controller.png': ('app/Http/Controllers/HomeController.php', (base/'app'/'Http'/'Controllers'/'HomeController.php').read_text(encoding='utf-8')),
    '03_product_controller.png': ('app/Http/Controllers/ProductController.php', (base/'app'/'Http'/'Controllers'/'ProductController.php').read_text(encoding='utf-8')),
    '04_user_controller.png': ('app/Http/Controllers/UserController.php', (base/'app'/'Http'/'Controllers'/'UserController.php').read_text(encoding='utf-8')),
    '05_sales_controller.png': ('app/Http/Controllers/SalesController.php', (base/'app'/'Http'/'Controllers'/'SalesController.php').read_text(encoding='utf-8')),
    '06_view_home.png': ('resources/views/home.blade.php', (base/'resources'/'views'/'home.blade.php').read_text(encoding='utf-8')),
    '07_view_food_beverage.png': ('resources/views/products/food-beverage.blade.php', (base/'resources'/'views'/'products'/'food-beverage.blade.php').read_text(encoding='utf-8')),
    '08_view_beauty_health.png': ('resources/views/products/beauty-health.blade.php', (base/'resources'/'views'/'products'/'beauty-health.blade.php').read_text(encoding='utf-8')),
    '09_view_home_care.png': ('resources/views/products/home-care.blade.php', (base/'resources'/'views'/'products'/'home-care.blade.php').read_text(encoding='utf-8')),
    '10_view_baby_kid.png': ('resources/views/products/baby-kid.blade.php', (base/'resources'/'views'/'products'/'baby-kid.blade.php').read_text(encoding='utf-8')),
    '11_view_user.png': ('resources/views/user.blade.php', (base/'resources'/'views'/'user.blade.php').read_text(encoding='utf-8')),
    '12_view_sales.png': ('resources/views/sales.blade.php', (base/'resources'/'views'/'sales.blade.php').read_text(encoding='utf-8')),
}
for name,(title,text) in files.items():
    code_shot(title, text, out/name)

browser_shot('Home', 'Halaman Home', ['Selamat datang di aplikasi Point of Sales (POS).'], out/'13_page_home.png')
browser_shot('Category /food-beverage', 'Category: Food & Beverage', ['Menampilkan daftar produk makanan dan minuman.'], out/'14_page_food_beverage.png')
browser_shot('Category /beauty-health', 'Category: Beauty & Health', ['Menampilkan daftar produk kategori beauty dan health.'], out/'15_page_beauty_health.png')
browser_shot('Category /home-care', 'Category: Home Care', ['Menampilkan daftar produk kategori home care.'], out/'16_page_home_care.png')
browser_shot('Category /baby-kid', 'Category: Baby Kid', ['Menampilkan daftar produk kategori baby dan kid.'], out/'17_page_baby_kid.png')
browser_shot('User /user/1/name/Budi', 'Halaman User', ['ID User: 1', 'Nama User: Budi'], out/'18_page_user.png')
browser_shot('Sales', 'Halaman Penjualan', ['Menampilkan halaman transaksi POS.'], out/'19_page_sales.png')
print('done')
