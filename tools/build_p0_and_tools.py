# -*- coding: utf-8 -*-
"""
Builder Script for:
1. Standalone Utility Hub: website/tools/kalkulator-kebutuhan-beras.html
2. 14 Priority P0 Articles in website/artikel/ with full merge integrations
"""

import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

os.makedirs('website/tools', exist_ok=True)
os.makedirs('website/artikel', exist_ok=True)

# Load extracted text from master 120
with open('tools/extracted_master_120.txt', 'r', encoding='utf-8') as f:
    full_text = f.read()

splits = list(re.finditer(r'ARTIKEL\s+(\d{3})\s*[—\-]\s*([^\n]+)', full_text))
raw_articles = {}
for i, m in enumerate(splits):
    num = int(m.group(1))
    start = m.start()
    end = splits[i+1].start() if i+1 < len(splits) else len(full_text)
    raw_articles[num] = {
        'title': m.group(2).strip(),
        'text': full_text[start:end].strip()
    }

def get_body(raw_text):
    copy_idx = raw_text.find('Copy Artikel')
    linking_idx = raw_text.find('Internal Linking Saat Publish')
    if copy_idx != -1 and linking_idx != -1:
        return raw_text[copy_idx+len('Copy Artikel'):linking_idx].strip()
    elif copy_idx != -1:
        return raw_text[copy_idx+len('Copy Artikel'):].strip()
    return raw_text

print(f"Loaded {len(raw_articles)} raw articles from docx extraction.")

# ==============================================================================
# 1. BUILD STANDALONE UTILITY TOOL: website/tools/kalkulator-kebutuhan-beras.html
# ==============================================================================
TOOL_HTML = """<!DOCTYPE html>
<html lang="id" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Kalkulator Kebutuhan Beras: Porsi Acara & Usaha Kuliner</title>
  <meta name="description" content="Kalkulator kebutuhan beras otomatis untuk catering, SPPG MBG, dan hajatan. Hitung porsi nasi matang, kebutuhan beras mentah, dan estimasi food cost.">
  <meta name="keywords" content="kalkulator beras catering, hitung porsi beras, kebutuhan beras 100 orang, kebutuhan beras 50 orang, food cost beras per porsi">
  <link rel="canonical" href="https://www.berasladori.com/tools/kalkulator-kebutuhan-beras">
  <meta name="robots" content="noindex, follow">

  <!-- Local SEO Geotags -->
  <meta name="geo.region" content="ID-JT">
  <meta name="geo.placename" content="Muntilan, Magelang, Temanggung, Sleman, Jawa Tengah">
  <meta name="geo.position" content="-7.5818;110.2868">
  <meta name="ICBM" content="-7.5818, 110.2868">

  <!-- Favicon & Brand Icons -->
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/images/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/assets/images/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#15803d">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.berasladori.com/tools/kalkulator-kebutuhan-beras">
  <meta property="og:site_name" content="Distributor Resmi Beras Ladori">
  <meta property="og:locale" content="id_ID">
  <meta property="og:title" content="Kalkulator Kebutuhan Beras: Porsi Acara & Usaha Kuliner">
  <meta property="og:description" content="Kalkulator kebutuhan beras otomatis untuk catering, SPPG MBG, dan hajatan. Hitung porsi nasi matang, kebutuhan beras mentah, dan estimasi food cost.">
  <meta property="og:image" content="https://www.berasladori.com/assets/images/og-image.jpg">
  <meta property="og:image:secure_url" content="https://www.berasladori.com/assets/images/og-image.jpg">
  <meta property="og:image:type" content="image/jpeg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Kalkulator Kebutuhan Beras: Porsi Acara & Usaha Kuliner">
  <meta name="twitter:description" content="Kalkulator kebutuhan beras otomatis untuk catering, SPPG MBG, dan hajatan. Hitung porsi nasi matang, kebutuhan beras mentah, dan estimasi food cost.">
  <meta name="twitter:image" content="https://www.berasladori.com/assets/images/og-image.jpg">

  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            brand: {
              50: '#f0fdf4',
              100: '#dcfce7',
              700: '#15803d',
              800: '#166534',
              900: '#14532d',
            },
            gold: {
              400: '#fbbf24',
              500: '#f59e0b',
              600: '#d97706',
            }
          }
        }
      }
    }
  </script>
  <link rel="stylesheet" href="/assets/css/custom.css">

  <script type="application/ld+json">
  [
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Kalkulator Kebutuhan Beras Acara & Dapur Komersial",
      "operatingSystem": "All",
      "applicationCategory": "BusinessApplication",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "IDR"
      },
      "description": "Kalkulator praktis menghitung kebutuhan kg beras mentah, cooking yield nasi matang, dan estimasi food cost per porsi untuk katering, prasmanan, dan SPPG MBG."
    },
    {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Beranda",
          "item": "https://www.berasladori.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Tools & Utility",
          "item": "https://www.berasladori.com/tools/kalkulator-kebutuhan-beras"
        }
      ]
    }
  ]
  </script>
</head>
<body class="bg-slate-50 text-slate-800 antialiased font-sans">

  <!-- Header Nav -->
  <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-md shadow-sm border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-20">
        <a href="/" class="flex items-center gap-3">
          <img src="/favicon.svg" alt="Logo Beras Ladori" class="w-11 h-11 rounded-xl shadow-md" width="44" height="44">
          <div>
            <span class="text-xl font-bold tracking-tight text-slate-900 block leading-tight">Distributor Beras Ladori</span>
            <span class="text-xs text-brand-700 font-semibold tracking-wider uppercase block">Pusat Informasi & Pengadaan B2B</span>
          </div>
        </a>

        <div class="flex items-center gap-4">
          <a href="/artikel" class="text-sm font-semibold text-slate-600 hover:text-brand-700">&larr; Semua Artikel</a>
          <a href="/produk/beras-ladori-25kg" class="text-sm font-semibold text-slate-600 hover:text-brand-700">Produk 25 Kg</a>
          <a href="https://wa.me/6282227420003?text=Halo%20Distributor%20Beras%20Ladori%2C%20saya%20ingin%20konsultasi%20kebutuhan%20beras%20skala%20acara." target="_blank" class="hidden sm:inline-flex bg-brand-700 hover:bg-brand-800 text-white px-4 py-2 rounded-lg text-sm font-semibold transition">
            Konsultasi Pasokan (WA)
          </a>
        </div>
      </div>
    </div>
  </header>

  <main class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <!-- Breadcrumb -->
    <nav class="flex text-xs font-semibold text-slate-500 mb-4 space-x-2">
      <a href="/" class="hover:text-brand-700">Beranda</a>
      <span>/</span>
      <span class="text-slate-800">Kalkulator Kebutuhan Beras</span>
    </nav>

    <header class="mb-8">
      <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-brand-50 text-brand-800 border border-brand-200 mb-3">
        🧮 Utility Resmi Pengadaan Dapur & Acara
      </div>
      <h1 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight leading-tight">
        Kalkulator Kebutuhan Beras: Porsi Acara & Usaha Kuliner
      </h1>
      <p class="text-base text-slate-600 mt-3 leading-relaxed">
        Hitung secara presisi kebutuhan kilogram beras mentah dari target porsi tamu atau orang. Menggunakan formula ilmiah <em>Cooking Yield Multiplier</em> (2.2x – 2.5x) beras berkualitas, buffer susut penyajian, dan estimasi food cost per porsi.
      </p>
    </header>

    <!-- INTERACTIVE CALCULATOR CARD -->
    <div class="bg-white rounded-3xl shadow-xl border border-slate-200 p-6 sm:p-8 mb-12">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        
        <!-- INPUT CONTROLS -->
        <div class="space-y-6">
          <h2 class="text-lg font-bold text-slate-900 border-b pb-2 flex items-center gap-2">
            <span>⚙️</span> Parameter Input Acara / Dapur
          </h2>

          <!-- Presets -->
          <div>
            <label class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-2">Preset Cepat Jumlah Orang</label>
            <div class="grid grid-cols-5 gap-1.5">
              <button type="button" onclick="setPreset(10)" class="preset-btn px-2 py-1.5 text-xs font-bold rounded-lg border border-slate-200 hover:border-brand-600 hover:bg-brand-50 transition text-slate-700">10 Org</button>
              <button type="button" onclick="setPreset(50)" class="preset-btn px-2 py-1.5 text-xs font-bold rounded-lg border border-slate-200 hover:border-brand-600 hover:bg-brand-50 transition text-slate-700">50 Org</button>
              <button type="button" onclick="setPreset(100)" class="preset-btn px-2 py-1.5 text-xs font-bold rounded-lg border border-brand-600 bg-brand-50 text-brand-800 font-extrabold transition">100 Org</button>
              <button type="button" onclick="setPreset(200)" class="preset-btn px-2 py-1.5 text-xs font-bold rounded-lg border border-slate-200 hover:border-brand-600 hover:bg-brand-50 transition text-slate-700">200 Org</button>
              <button type="button" onclick="setPreset(500)" class="preset-btn px-2 py-1.5 text-xs font-bold rounded-lg border border-slate-200 hover:border-brand-600 hover:bg-brand-50 transition text-slate-700">500 Org</button>
            </div>
          </div>

          <!-- Target Tamu Input -->
          <div>
            <label for="inputGuests" class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
              Jumlah Porsi / Tamu (Orang)
            </label>
            <div class="flex items-center gap-3">
              <input type="range" id="sliderGuests" min="5" max="1000" step="5" value="100" class="w-full accent-brand-700" oninput="syncGuests(this.value)">
              <input type="number" id="inputGuests" min="1" max="5000" value="100" class="w-24 px-3 py-2 border border-slate-300 rounded-lg text-center font-bold text-slate-900 focus:ring-2 focus:ring-brand-500" oninput="syncGuests(this.value)">
            </div>
          </div>

          <!-- Tipe Porsi -->
          <div>
            <label for="selectPortion" class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
              Gramasi Nasi Matang per Porsi
            </label>
            <select id="selectPortion" class="w-full px-3 py-2 border border-slate-300 rounded-lg font-medium text-slate-800 focus:ring-2 focus:ring-brand-500 bg-slate-50" onchange="calculate()">
              <option value="100">Porsi Anak / Diet (100 gram)</option>
              <option value="130">Nasi Kotak Hemat (130 gram)</option>
              <option value="150" selected>Nasi Kotak Standar / Resto (150 gram)</option>
              <option value="180">Porsi Warung Makan Mantap (180 gram)</option>
              <option value="200">Prasmanan / Hajatan Bebas Ambil (200 gram)</option>
              <option value="250">Porsi Jumbo Pekerja Fisik (250 gram)</option>
            </select>
          </div>

          <!-- Cooking Yield -->
          <div>
            <label for="selectYield" class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
              Yield Nasi Beras (Faktor Pengali Masak)
            </label>
            <select id="selectYield" class="w-full px-3 py-2 border border-slate-300 rounded-lg font-medium text-slate-800 focus:ring-2 focus:ring-brand-500 bg-slate-50" onchange="calculate()">
              <option value="2.2">Yield Standar / Pera Sedang (2.2x)</option>
              <option value="2.4" selected>Beras Premium Ladori C4/IR64 (2.4x) - Rekomendasi</option>
              <option value="2.5">Beras Pulen Mekar Sempurna (2.5x)</option>
            </select>
            <p class="text-[11px] text-slate-500 mt-1">1 kg beras Ladori menghasilkan rata-rata 2,4 kg nasi pulen matang.</p>
          </div>

          <!-- Buffer Cadangan -->
          <div>
            <label for="selectBuffer" class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
              Safety Stock / Cadangan Susut Dapur
            </label>
            <select id="selectBuffer" class="w-full px-3 py-2 border border-slate-300 rounded-lg font-medium text-slate-800 focus:ring-2 focus:ring-brand-500 bg-slate-50" onchange="calculate()">
              <option value="0">Tanpa Cadangan (0% - Pas Persis)</option>
              <option value="0.05">Cadangan Ringan 5% (Disarankan Nasi Kotak)</option>
              <option value="0.10" selected>Cadangan Standar 10% (Sangat Aman Prasmanan)</option>
            </select>
          </div>

          <!-- Estimasi Harga Beras per Kg -->
          <div>
            <label for="inputPrice" class="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-1">
              Asumsi Harga Beras per Kg (Rp)
            </label>
            <input type="number" id="inputPrice" value="14500" step="100" class="w-full px-3 py-2 border border-slate-300 rounded-lg font-medium text-slate-800 focus:ring-2 focus:ring-brand-500 bg-slate-50" oninput="calculate()">
          </div>

        </div>

        <!-- OUTPUT DASHBOARD -->
        <div class="bg-gradient-to-br from-brand-900 to-slate-900 text-white rounded-2xl p-6 flex flex-col justify-between shadow-inner">
          <div>
            <span class="text-xs font-bold text-brand-400 uppercase tracking-wider block mb-1">📊 Rekomendasi Pengadaan Dapur</span>
            <h3 class="text-xl font-black tracking-tight text-white mb-6">Hasil Kalkulasi Pengadaan</h3>

            <div class="space-y-4">
              <!-- Result 1: Kebutuhan Beras Mentah -->
              <div class="bg-white/10 rounded-xl p-4 border border-white/10 backdrop-blur-sm">
                <span class="text-xs text-slate-300 block">Total Kebutuhan Beras Mentah</span>
                <div class="flex items-baseline gap-2 mt-1">
                  <span id="resRawKg" class="text-3xl sm:text-4xl font-black text-amber-400">6.88</span>
                  <span class="text-base font-bold text-slate-200">Kilogram (kg)</span>
                </div>
                <span id="resNoteBags" class="text-xs text-brand-300 font-medium block mt-1">Setara 1 karung Beras Ladori 25 kg (hemat untuk stok)</span>
              </div>

              <!-- Result 2: Nasi Matang -->
              <div class="grid grid-cols-2 gap-3">
                <div class="bg-white/10 rounded-xl p-3 border border-white/10">
                  <span class="text-[11px] text-slate-300 block">Total Nasi Matang</span>
                  <span id="resCookedKg" class="text-lg font-black text-white block mt-1">16.5 kg</span>
                </div>
                <div class="bg-white/10 rounded-xl p-3 border border-white/10">
                  <span class="text-[11px] text-slate-300 block">Estimasi Air Masak</span>
                  <span id="resWaterLiters" class="text-lg font-black text-white block mt-1">8.25 Liter</span>
                </div>
              </div>

              <!-- Result 3: Food Cost -->
              <div class="grid grid-cols-2 gap-3">
                <div class="bg-white/10 rounded-xl p-3 border border-white/10">
                  <span class="text-[11px] text-slate-300 block">Total Biaya Beras</span>
                  <span id="resTotalPrice" class="text-base font-bold text-amber-300 block mt-1">Rp 99.760</span>
                </div>
                <div class="bg-white/10 rounded-xl p-3 border border-white/10">
                  <span class="text-[11px] text-slate-300 block">Food Cost per Porsi</span>
                  <span id="resCostPerPortion" class="text-base font-bold text-emerald-400 block mt-1">Rp 998 / porsi</span>
                </div>
              </div>
            </div>
          </div>

          <div class="mt-6 pt-4 border-t border-white/20">
            <a id="waBtn" href="#" target="_blank" class="w-full bg-emerald-500 hover:bg-emerald-600 text-slate-950 font-black py-3 px-4 rounded-xl text-center flex items-center justify-center gap-2 transition shadow-lg text-sm">
              <span>💬</span> Hubungi Tim Pengadaan Ladori (WA)
            </a>
            <p class="text-[10px] text-center text-slate-400 mt-2">Dukungan pengiriman cepat armada Ladori: Muntilan, Magelang, Sleman, Jogja, Temanggung.</p>
          </div>
        </div>

      </div>
    </div>

    <!-- PANDUAN PENGHITUNGAN & DATA SCIENCE SECTION -->
    <section class="prose prose-slate max-w-none text-slate-700 space-y-6">
      <h2 class="text-2xl font-bold text-slate-900 border-b pb-2">Formula & Dasar Sains Penghitungan Porsi Beras</h2>
      
      <p>
        Dalam tata kelola dapur komersial, katering pesta, maupun Satuan Pelayanan Pemenuhan Gizi (SPPG) Program Makan Bergizi Gratis (MBG), penghitungan beras tidak boleh didasarkan pada asumsi acak. Perbedaan takaran sebesar 10 gram per porsi akan terakumulasi menjadi defisit 10 kg beras pada pengadaan skala 1.000 porsi.
      </p>

      <div class="p-4 bg-brand-50 border-l-4 border-brand-700 rounded-r-xl">
        <h3 class="text-base font-bold text-brand-900 m-0 mb-1">Rumus Matematis Dua Tahap:</h3>
        <ol class="list-decimal pl-5 space-y-1 text-sm text-brand-950 m-0">
          <li><strong>Kebutuhan Nasi Matang (kg)</strong> = [Jumlah Tamu &times; Gramasi Nasi per Porsi (gram)] &divide; 1.000 &times; (1 + Buffer Cadangan).</li>
          <li><strong>Kebutuhan Beras Mentah (kg)</strong> = Kebutuhan Nasi Matang &divide; Cooking Yield Multiplier (2.2x – 2.5x).</li>
        </ol>
      </div>

      <h3 class="text-xl font-bold text-slate-900">Tabel Patokan Cepat: Jumlah Tamu vs Kebutuhan Beras Ladori</h3>
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse border border-slate-200 text-sm">
          <thead>
            <tr class="bg-slate-100 text-slate-900 border-b border-slate-300">
              <th class="p-3 border">Jumlah Tamu</th>
              <th class="p-3 border">Nasi Kotak (130-150g)</th>
              <th class="p-3 border">Prasmanan (180-200g)</th>
              <th class="p-3 border">Rekomendasi Kemasan Ladori</th>
            </tr>
          </thead>
          <tbody>
            <tr class="border-b">
              <td class="p-3 border font-semibold">10 Orang</td>
              <td class="p-3 border">0.6 – 0.7 kg</td>
              <td class="p-3 border">0.8 – 0.9 kg</td>
              <td class="p-3 border">Kemasan eceran / 5 kg</td>
            </tr>
            <tr class="border-b bg-slate-50">
              <td class="p-3 border font-semibold">50 Orang</td>
              <td class="p-3 border">3.0 – 3.5 kg</td>
              <td class="p-3 border">4.2 – 4.6 kg</td>
              <td class="p-3 border">1 karung 5 kg atau bagian dari 25 kg</td>
            </tr>
            <tr class="border-b">
              <td class="p-3 border font-semibold">100 Orang</td>
              <td class="p-3 border">6.0 – 6.9 kg</td>
              <td class="p-3 border">8.3 – 9.2 kg</td>
              <td class="p-3 border">1 karung Beras Ladori 25 kg (hemat & ada sisa)</td>
            </tr>
            <tr class="border-b bg-slate-50">
              <td class="p-3 border font-semibold">200 Orang</td>
              <td class="p-3 border">12.0 – 13.8 kg</td>
              <td class="p-3 border">16.5 – 18.4 kg</td>
              <td class="p-3 border">1 karung Beras Ladori 25 kg (sangat pas)</td>
            </tr>
            <tr class="border-b">
              <td class="p-3 border font-semibold">500 Orang</td>
              <td class="p-3 border">30.0 – 34.5 kg</td>
              <td class="p-3 border">41.3 – 46.0 kg</td>
              <td class="p-3 border">2 karung Beras Ladori 25 kg</td>
            </tr>
            <tr class="border-b bg-slate-50">
              <td class="p-3 border font-semibold">1.000 Orang</td>
              <td class="p-3 border">60.0 – 69.0 kg</td>
              <td class="p-3 border">82.5 – 92.0 kg</td>
              <td class="p-3 border">3 s.d. 4 karung Beras Ladori 25 kg</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3 class="text-xl font-bold text-slate-900 mt-8">Artikel Edukasi Terkait Porsi & Pengadaan</h3>
      <p class="text-sm text-slate-600">Pelajari metodologi pengukuran mendalam dari tim riset beras Ladori:</p>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 not-prose mt-4">
        <a href="/artikel/1-kg-beras-berapa-porsi" class="block p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition">
          <span class="text-xs font-bold text-brand-700 block mb-1">Panduan Utama Porsi</span>
          <span class="text-sm font-bold text-slate-900 block leading-snug">1 Kg Beras Jadi Berapa Porsi Nasi? Ini Cara Menghitungnya</span>
          <span class="text-xs text-slate-500 mt-1 block">Pelajari faktor susut dan hasil uji timbang aktual dapur.</span>
        </a>
        <a href="/artikel/cara-menghitung-harga-beras-per-porsi" class="block p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition">
          <span class="text-xs font-bold text-brand-700 block mb-1">Manajemen Biaya Resto</span>
          <span class="text-sm font-bold text-slate-900 block leading-snug">Cara Menghitung Harga Beras per Porsi untuk Warung Makan</span>
          <span class="text-xs text-slate-500 mt-1 block">Simulasi margin dan food cost nasi matang per piring.</span>
        </a>
        <a href="/artikel/cara-menghitung-stok-beras-sebulan" class="block p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition">
          <span class="text-xs font-bold text-brand-700 block mb-1">Kontrol Inventori</span>
          <span class="text-sm font-bold text-slate-900 block leading-snug">Cara Menghitung Stok Beras Sebulan Tanpa Menimbun Lebih</span>
          <span class="text-xs text-slate-500 mt-1 block">Cegah apek dan kutu dengan formula Reorder Point (ROP).</span>
        </a>
        <a href="/program/katering-horeka" class="block p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition">
          <span class="text-xs font-bold text-brand-700 block mb-1">Layanan B2B</span>
          <span class="text-sm font-bold text-slate-900 block leading-snug">Program Pasokan Beras Katering & Horeka</span>
          <span class="text-xs text-slate-500 mt-1 block">Pasokan rutin konsisten untuk hotel, resto, dan catering.</span>
        </a>
      </div>
    </section>

  </main>

  <!-- Footer -->
  <footer class="bg-slate-900 text-slate-400 py-12 border-t border-slate-800 mt-16 text-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-4">
      <p class="font-semibold text-slate-200">Distributor Resmi Beras Ladori — Muntilan, Magelang, Sleman, Temanggung, Jogja</p>
      <p class="text-xs text-slate-500">
        &copy; 2026 PT Beras Ladori Indonesia. Seluruh hak cipta dilindungi undang-undang.
      </p>
      <div class="flex flex-wrap justify-center gap-4 text-xs pt-2">
        <a href="/" class="hover:text-white">Beranda</a>
        <a href="/artikel" class="hover:text-white">Artikel</a>
        <a href="/produk/beras-ladori-25kg" class="hover:text-white">Beras Ladori 25 Kg</a>
        <a href="/program/katering-horeka" class="hover:text-white">Program Katering</a>
        <a href="/program/sppg-mbg" class="hover:text-white">Program SPPG MBG</a>
      </div>
    </div>
  </footer>

  <script>
    function setPreset(n) {
      document.getElementById('inputGuests').value = n;
      document.getElementById('sliderGuests').value = n;
      document.querySelectorAll('.preset-btn').forEach(b => {
        b.classList.remove('border-brand-600', 'bg-brand-50', 'text-brand-800', 'font-extrabold');
      });
      event.target.classList.add('border-brand-600', 'bg-brand-50', 'text-brand-800', 'font-extrabold');
      calculate();
    }

    function syncGuests(val) {
      val = Math.max(1, parseInt(val) || 1);
      document.getElementById('inputGuests').value = val;
      document.getElementById('sliderGuests').value = Math.min(1000, val);
      calculate();
    }

    function calculate() {
      const guests = parseInt(document.getElementById('inputGuests').value) || 1;
      const gramPerPortion = parseInt(document.getElementById('selectPortion').value) || 150;
      const yieldFactor = parseFloat(document.getElementById('selectYield').value) || 2.4;
      const buffer = parseFloat(document.getElementById('selectBuffer').value) || 0.10;
      const pricePerKg = parseFloat(document.getElementById('inputPrice').value) || 14500;

      // 1. Total Cooked Rice (kg) with buffer
      const cookedRiceKg = (guests * gramPerPortion / 1000) * (1 + buffer);
      
      // 2. Total Raw Rice (kg)
      const rawRiceKg = cookedRiceKg / yieldFactor;

      // 3. Total Price & Cost Per Portion
      const totalPrice = rawRiceKg * pricePerKg;
      const costPerPortion = totalPrice / guests;

      // 4. Water Estimate (kg beras * 1.2 liter)
      const waterLiters = rawRiceKg * 1.2;

      // Update DOM
      document.getElementById('resRawKg').textContent = rawRiceKg.toFixed(2);
      document.getElementById('resCookedKg').textContent = cookedRiceKg.toFixed(1) + ' kg';
      document.getElementById('resWaterLiters').textContent = waterLiters.toFixed(1) + ' L';
      document.getElementById('resTotalPrice').textContent = 'Rp ' + Math.round(totalPrice).toLocaleString('id-ID');
      document.getElementById('resCostPerPortion').textContent = 'Rp ' + Math.round(costPerPortion).toLocaleString('id-ID') + ' / porsi';

      // Bag notes
      const bags25 = rawRiceKg / 25;
      let bagNote = '';
      if (rawRiceKg <= 5) {
        bagNote = 'Cukup menggunakan 1 pack kemasan 5 kg.';
      } else if (rawRiceKg <= 25) {
        bagNote = 'Sangat efisien memesan 1 karung Beras Ladori 25 kg (tersisa cadangan aman).';
      } else {
        const fullBags = Math.floor(bags25);
        const rem = rawRiceKg % 25;
        bagNote = `Disarankan memesan ${fullBags + (rem > 0 ? 1 : 0)} karung Beras Ladori 25 kg.`;
      }
      document.getElementById('resNoteBags').textContent = bagNote;

      // WhatsApp Button URL
      const textMsg = encodeURIComponent(
        `Halo Distributor Beras Ladori, saya telah menghitung di Kalkulator Kebutuhan Beras:\\n- Jumlah Tamu: ${guests} orang\\n- Tipe Porsi: ${gramPerPortion}g nasi matang\\n- Total Kebutuhan Beras: ${rawRiceKg.toFixed(1)} kg\\nSaya ingin konsultasi pasokan Beras Ladori untuk acara ini.`
      );
      document.getElementById('waBtn').href = `https://wa.me/6282227420003?text=${textMsg}`;
    }

    // Run initial calculation
    calculate();
  </script>
</body>
</html>
"""

with open('website/tools/kalkulator-kebutuhan-beras.html', 'w', encoding='utf-8') as f:
    f.write(TOOL_HTML)
print("Successfully generated website/tools/kalkulator-kebutuhan-beras.html")
