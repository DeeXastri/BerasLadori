import urllib.request
import re
import time

urls = [
    'https://www.berasladori.com/',
    'https://www.berasladori.com/tools/kalkulator-kebutuhan-beras',
    'https://www.berasladori.com/artikel',
    'https://www.berasladori.com/artikel/1-kg-beras-berapa-porsi',
    'https://www.berasladori.com/artikel/kadar-air-beras',
    'https://www.berasladori.com/artikel/beras-kepala-beras-patah-menir',
    'https://www.berasladori.com/artikel/rendemen-beras',
    'https://www.berasladori.com/artikel/beras-untuk-catering',
    'https://www.berasladori.com/artikel/beras-berkutu-masih-bisa-dimakan',
    'https://www.berasladori.com/artikel/takaran-air-untuk-1-kg-beras',
    'https://www.berasladori.com/artikel/beras-premium-vs-medium',
    'https://www.berasladori.com/artikel/kenapa-harga-beras-berbeda',
    'https://www.berasladori.com/artikel/cara-menghitung-harga-beras-per-porsi',
    'https://www.berasladori.com/artikel/cara-menghitung-stok-beras-sebulan',
    'https://www.berasladori.com/artikel/cara-membaca-label-kemasan-beras',
    'https://www.berasladori.com/artikel/cara-menyimpan-beras-25-kg',
    'https://www.berasladori.com/program/pesantren',
    'https://www.berasladori.com/assets/images/beras-dihorein.webp',
    'https://www.berasladori.com/assets/images/beras-dihorein-600.webp',
    'https://www.berasladori.com/sitemap.xml'
]

print("=== VERIFIKASI LIVE PRODUCTION (VERCEL DEPLOYMENT) ===")
for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            if url.endswith('.webp') or url.endswith('.png') or url.endswith('.jpg'):
                content = resp.read()
                print(f"[200 OK] {url} -> Binary Image OK ({len(content)} bytes)")
            elif 'sitemap.xml' in url:
                data = resp.read().decode('utf-8')
                active_locs = re.findall(r'<loc>(.*?)</loc>', data)
                total_urls = len(active_locs)
                only_home = (total_urls == 1 and active_locs[0] == 'https://www.berasladori.com/')
                print(f"[200 OK] {url} -> Total URLs: {total_urls} (Hanya homepage? {only_home})")
            else:
                data = resp.read().decode('utf-8')
                m = re.search(r'<meta\s+name=["\']robots["\']\s+content=["\'](.*?)["\']', data)
                robots_val = m.group(1) if m else 'NOT FOUND'
                print(f"[200 OK] {url} -> Robots: {robots_val}")
    except Exception as e:
        print(f"[FAIL] {url} -> Error: {e}")
