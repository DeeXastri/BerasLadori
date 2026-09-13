import urllib.request
import re
import time

urls = [
    'https://www.berasladori.com/',
    'https://www.berasladori.com/produk/beras-ladori-25kg',
    'https://www.berasladori.com/tentang/beras-ladori',
    'https://www.berasladori.com/wilayah/magelang',
    'https://www.berasladori.com/artikel',
    'https://www.berasladori.com/artikel/cara-memilih-supplier-beras-b2b',
    'https://www.berasladori.com/artikel/cara-menghitung-cooking-yield-beras',
    'https://www.berasladori.com/artikel/sop-penerimaan-beras-dapur-b2b',
    'https://www.berasladori.com/artikel/memilih-supplier-beras-untuk-sppg-mbg',
    'https://www.berasladori.com/artikel/koridor-pasokan-beras-muntilan-magelang-sleman-jogja',
    'https://www.berasladori.com/sitemap.xml'
]

print("=== VERIFIKASI LIVE PRODUCTION (VERCEL DEPLOYMENT) ===")
for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read().decode('utf-8')
            if 'sitemap.xml' in url:
                has_subpage = 'produk/beras-ladori-25kg' in data
                total_urls = len(re.findall(r'<loc>', data))
                print(f"[200 OK] {url} -> Total URLs: {total_urls} (Hanya homepage? {not has_subpage})")
            else:
                m = re.search(r'<meta\s+name=["\']robots["\']\s+content=["\'](.*?)["\']', data)
                robots_val = m.group(1) if m else 'NOT FOUND'
                print(f"[200 OK] {url} -> Robots: {robots_val}")
    except Exception as e:
        print(f"[FAIL] {url} -> Error: {e}")
