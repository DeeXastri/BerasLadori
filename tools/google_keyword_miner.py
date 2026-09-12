#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==============================================================================
GOOGLE INDONESIA DEEP SEARCH KEYWORD MINER
Khusus Riset Kata Kunci Distribusi Beras Premium Ladori (Magelang & Temanggung)
==============================================================================
Metode: Alphabet Soup Expansion (A-Z) via Google Chrome Autosuggest API
Tanpa Biaya Langganan / 100% Menggunakan Data Pencarian Nyata Google.co.id
"""

import sys
import os
import json
import time
import urllib.request
import urllib.parse
from datetime import datetime

# Pastikan output console mendukung karakter UTF-8 di Windows
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
DATA_DIR = os.path.join(PROJECT_DIR, 'data')
os.makedirs(DATA_DIR, exist_ok=True)

SEEDS_CORE = [
    'beras premium',
    'beras ladori',
    'distributor beras',
    'grosir beras',
    'harga beras',
    'pabrik beras',
    'agen beras',
    'supplier beras',
    'beras mbg',
    'beras sppg',
    'beras makan bergizi gratis',
    'supplier beras katering',
    'beras katering hajatan',
    'beras dihorein',
    'beras pesantren',
    'beras pondok pesantren',
    'beras untuk santri',
    'supplier beras pesantren'
]

SEEDS_LOCAL = [
    'beras magelang',
    'grosir beras magelang',
    'distributor beras magelang',
    'beras katering magelang',
    'beras temanggung',
    'grosir beras temanggung',
    'distributor beras temanggung',
    'beras katering temanggung',
    'beras mertoyudan',
    'beras muntilan',
    'beras parakan'
]

QUESTION_PREFIXES = [
    'apa itu',
    'kenapa',
    'cara memilih',
    'berapa harga',
    'dimana beli'
]

ALPHABET = [chr(i) for i in range(ord('a'), ord('z') + 1)]

def fetch_suggestions(query):
    """Mengambil daftar saran pencarian langsung dari Google Suggest API."""
    encoded_q = urllib.parse.quote(query)
    url = f"http://suggestqueries.google.com/complete/search?client=chrome&hl=id&gl=id&q={encoded_q}"
    req = urllib.request.Request(
        url,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            if len(data) > 1 and isinstance(data[1], list):
                return data[1]
    except Exception:
        pass
    return []

def classify_intent(kw):
    """Mengklasifikasikan kata kunci ke dalam kelompok intent bisnis."""
    kw_lower = kw.lower()
    
    # 1. Pondok Pesantren & Beras DiHorein
    pesantren_tags = ['pesantren', 'ponpes', 'santri', 'pondok', 'dihorein']
    if any(p in kw_lower for p in pesantren_tags):
        return "Pondok Pesantren & DiHorein"

    # 2. SPPG MBG & Katering / HOREKA
    mbg_tags = ['mbg', 'sppg', 'bergizi', 'makan bergizi', 'katering', 'catering', 'hajatan', 'prasmanan', 'restoran', 'hotel']
    if any(m in kw_lower for m in mbg_tags):
        return "SPPG MBG & Katering (Institusi)"

    # 3. Wilayah Magelang & Temanggung
    local_tags = ['magelang', 'temanggung', 'mertoyudan', 'muntilan', 'parakan', 'secang', 'borobudur', 'kedu', 'ngadirejo']
    if any(loc in kw_lower for loc in local_tags):
        return "Hyperlocal (Magelang & Temanggung)"
    
    b2b_tags = ['distributor', 'grosir', 'pabrik', 'agen', 'supplier', 'kulakan', 'karung', 'partai', 'ton', 'kwintal']
    if any(b in kw_lower for b in b2b_tags):
        return "B2B Wholesale / Grosir"
    
    price_tags = ['harga', 'biaya', 'pricelist', 'het', 'murah', 'sekilo', 'per karung']
    if any(p in kw_lower for p in price_tags):
        return "Sensitif Harga / Komparasi"
        
    edu_tags = ['adalah', 'apa', 'ciri', 'cara', 'kenapa', 'bagus', 'terbaik', 'patahan', 'kutu', 'pemutih', 'review', 'ulasan']
    if any(ed in kw_lower for ed in edu_tags):
        return "Informasional / Edukasi / Review"
        
    spec_tags = ['5 kg', '5kg', '10 kg', '10kg', '25 kg', '25kg', '50 kg', '50kg', 'pulen', 'wangi', 'super']
    if any(sp in kw_lower for sp in spec_tags):
        return "Varian Kemasan & Spesifikasi"

    return "Umum / Konsumen Eceran"

def run_mining(quick_mode=False):
    print("=" * 70)
    print("🌾 GOOGLE INDONESIA DEEP SEARCH KEYWORD MINER")
    print("   Target: Beras Premium Ladori, Pasar Grosir & Wilayah Jateng")
    print(f"   Mode: {'QUICK SCAN (Seed Pokok Saja)' if quick_mode else 'FULL ALPHABET SOUP EXPANSION (A-Z)'}")
    print("=" * 70)

    all_queries = []
    for s in SEEDS_CORE + SEEDS_LOCAL:
        all_queries.append(s)
        
    if not quick_mode:
        print("⚡ Menyiapkan matriks Alphabet Soup (A-Z)...")
        for s in ['beras premium', 'beras ladori', 'distributor beras', 'grosir beras']:
            for char in ALPHABET:
                all_queries.append(f"{s} {char}")
        for qp in QUESTION_PREFIXES:
            all_queries.append(f"{qp} beras premium")
            all_queries.append(f"{qp} beras ladori")

    print(f"📡 Mengirim {len(all_queries)} kueri ke Google Indonesia...")
    
    harvested = set()
    counter = 0
    total = len(all_queries)
    
    for q in all_queries:
        counter += 1
        results = fetch_suggestions(q)
        for item in results:
            cleaned = item.strip().lower()
            if cleaned:
                harvested.add(cleaned)
        
        if counter % 10 == 0 or counter == total:
            sys.stdout.write(f"\rProgess: [{counter}/{total}] | Terjaring: {len(harvested)} kata kunci unik...")
            sys.stdout.flush()
        
        time.sleep(0.08)

    print("\n\n✅ Ekstraksi selesai! Mengklasifikasikan kata kunci...")

    categorized = {}
    for kw in sorted(harvested):
        cat = classify_intent(kw)
        if cat not in categorized:
            categorized[cat] = []
        categorized[cat].append(kw)

    output_json = os.path.join(DATA_DIR, 'hasil_keyword_mining.json')
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "total_keywords": len(harvested),
            "data_by_intent": categorized
        }, f, indent=2, ensure_ascii=False)

    output_md = os.path.join(DATA_DIR, 'hasil_keyword_mining.md')
    with open(output_md, 'w', encoding='utf-8') as f:
        f.write("# 🌾 Laporan Hasil Mining Kata Kunci Google Indonesia\n")
        f.write(f"**Tanggal Pemindaian:** {datetime.now().strftime('%d %B %Y, %H:%M WIB')}\n")
        f.write(f"**Total Kata Kunci Unik Terjaring:** `{len(harvested)} kata kunci`\n\n")
        f.write("---\n\n")
        
        for cat, kw_list in categorized.items():
            f.write(f"## 📌 Kelompok Intent: {cat} ({len(kw_list)} Kata Kunci)\n\n")
            f.write("| No | Kata Kunci Nyata di Google.co.id | Rekomendasi Penempatan |\n")
            f.write("|:---|:---|:---|\n")
            for idx, kw in enumerate(kw_list, 1):
                f.write(f"| {idx} | `{kw}` | {cat} |\n")
            f.write("\n---\n\n")

    print(f"📁 Data JSON berhasil disimpan ke: {output_json}")
    print(f"📄 Laporan Markdown berhasil disimpan ke: {output_md}")
    print("\nRingkasan Kategori:")
    for cat, items in categorized.items():
        print(f"  • {cat}: {len(items)} kata kunci")
    print("=" * 70)

if __name__ == '__main__':
    quick = '--quick' in sys.argv
    run_mining(quick_mode=quick)
