# -*- coding: utf-8 -*-
"""
Builder Script to generate all 14 Priority P0 Articles with MERGE integrations,
high-density UI styling, interactive portion calculator widget in Article #001,
and full link graph alignment.
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Ensure tools directory is in sys.path
sys.path.insert(0, os.path.dirname(__file__))

from data_p0_part1 import p0_part1_articles
from data_p0_part2 import p0_part2_articles

all_p0 = p0_part1_articles + p0_part2_articles
print(f"Total P0 articles to build: {len(all_p0)}")

TEMPLATE = """<!DOCTYPE html>
<html lang="id" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="keywords" content="{keywords}">
  <link rel="canonical" href="https://www.berasladori.com/artikel/{slug}">
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
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://www.berasladori.com/artikel/{slug}">
  <meta property="og:site_name" content="Distributor Resmi Beras Ladori">
  <meta property="og:locale" content="id_ID">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="https://www.berasladori.com/assets/images/og-image.jpg">
  <meta property="og:image:secure_url" content="https://www.berasladori.com/assets/images/og-image.jpg">
  <meta property="og:image:type" content="image/jpeg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{title}">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="https://www.berasladori.com/assets/images/og-image.jpg">

  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            brand: {{
              50: '#f0fdf4',
              100: '#dcfce7',
              700: '#15803d',
              800: '#166534',
              900: '#14532d',
            }},
            gold: {{
              400: '#fbbf24',
              500: '#f59e0b',
              600: '#d97706',
            }}
          }}
        }}
      }}
    }}
  </script>
  <link rel="stylesheet" href="/assets/css/custom.css">

  <script type="application/ld+json">
  [
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{h1_escaped}",
      "description": "{description_escaped}",
      "image": "https://www.berasladori.com/assets/images/og-image.jpg",
      "mainEntityOfPage": {{
        "@type": "WebPage",
        "@id": "https://www.berasladori.com/artikel/{slug}"
      }},
      "author": {{
        "@type": "Organization",
        "name": "Distributor Beras Ladori",
        "url": "https://www.berasladori.com/"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "Distributor Beras Ladori",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://www.berasladori.com/assets/images/android-chrome-512x512.png"
        }}
      }},
      "datePublished": "2026-09-13",
      "dateModified": "2026-09-13"
    }},
    {{
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{
          "@type": "ListItem",
          "position": 1,
          "name": "Beranda",
          "item": "https://www.berasladori.com/"
        }},
        {{
          "@type": "ListItem",
          "position": 2,
          "name": "Artikel",
          "item": "https://www.berasladori.com/artikel"
        }},
        {{
          "@type": "ListItem",
          "position": 3,
          "name": "{breadcrumb_title_escaped}",
          "item": "https://www.berasladori.com/artikel/{slug}"
        }}
      ]
    }}
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
          <a href="/tools/kalkulator-kebutuhan-beras" class="text-sm font-semibold text-slate-600 hover:text-brand-700">Kalkulator Porsi</a>
          <a href="https://wa.me/6282227420003?text=Halo%20Distributor%20Beras%20Ladori%2C%20saya%20ingin%20konsultasi%20pengadaan%20beras." target="_blank" class="hidden sm:inline-flex bg-brand-700 hover:bg-brand-800 text-white px-4 py-2 rounded-lg text-sm font-semibold transition">
            Minta Sampel (WA)
          </a>
        </div>
      </div>
    </div>
  </header>

  <!-- Article Container -->
  <article class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <nav class="flex text-xs font-semibold text-slate-500 mb-4 space-x-2">
      <a href="/" class="hover:text-brand-700">Beranda</a>
      <span>/</span>
      <a href="/artikel" class="hover:text-brand-700">Artikel</a>
      <span>/</span>
      <span class="text-slate-800">{breadcrumb_title_escaped}</span>
    </nav>

    <header class="mb-10">
      <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-brand-50 text-brand-800 border border-brand-200 mb-3">
        {category_badge}
      </div>
      <h1 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight leading-tight">
        {h1}
      </h1>
      <div class="flex flex-wrap items-center gap-4 mt-4 text-xs text-slate-500 border-b border-slate-200 pb-4">
        <span>Ditulis oleh: <strong>Tim Riset & QC Beras Ladori</strong></span>
        <span>&bull;</span>
        <span>Diperbarui: 13 September 2026</span>
        <span>&bull;</span>
        <span>Waktu Baca: {read_time} menit</span>
      </div>
    </header>

    <!-- Key Takeaway Box -->
    <div class="p-5 bg-gradient-to-r from-brand-50 to-emerald-50 border-l-4 border-brand-700 rounded-r-2xl mb-10 shadow-sm">
      <h2 class="text-base font-black text-brand-900 mb-1 flex items-center gap-2">
        <span>💡</span> Intisari & Ringkasan Cepat:
      </h2>
      <p class="text-sm text-brand-950 leading-relaxed">
        {key_takeaways}
      </p>
    </div>

    <!-- Main Content Body -->
    <div class="prose prose-slate max-w-none text-slate-700 space-y-8 leading-relaxed">
      {body_html}
    </div>

    <!-- Related Links / Internal Linking Section -->
    <div class="mt-12 pt-8 border-t border-slate-200">
      <h3 class="text-lg font-bold text-slate-900 mb-4">Artikel & Layanan Terkait:</h3>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
        {related_links_html}
      </div>
    </div>

    <!-- CTA Box -->
    <div class="mt-12 bg-gradient-to-br from-slate-900 to-brand-950 text-white rounded-3xl p-8 shadow-xl">
      <div class="max-w-2xl">
        <h3 class="text-2xl font-black tracking-tight mb-2">Konsultasi Pasokan Beras Premium Ladori 25 Kg</h3>
        <p class="text-sm text-slate-300 leading-relaxed mb-6">
          Dapatkan beras kualitas konsisten dengan kadar air terukur 13.5%, derajat sosoh 95%, dan rendemen mekar 2.4x untuk katering, restoran, dan program gizi SPPG MBG. Pengiriman armada langsung se-Magelang, Muntilan, Sleman, Jogja, dan Temanggung.
        </p>
        <div class="flex flex-wrap items-center gap-4">
          <a href="https://wa.me/6282227420003?text=Halo%20Distributor%20Beras%20Ladori%2C%20saya%20ingin%20konsultasi%20sampel%20dan%20harga%20beras." target="_blank" class="bg-emerald-500 hover:bg-emerald-600 text-slate-950 font-black px-6 py-3 rounded-xl text-sm transition shadow-lg inline-flex items-center gap-2">
            <span>💬</span> Hubungi Tim Penjualan via WhatsApp
          </a>
          <a href="/produk/beras-ladori-25kg" class="text-slate-300 hover:text-white text-sm font-semibold underline underline-offset-4">
            Lihat Spesifikasi Beras Ladori 25 Kg &rarr;
          </a>
        </div>
      </div>
    </div>
  </article>

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

</body>
</html>
"""

for art in all_p0:
    slug = art['slug']
    filepath = f"website/artikel/{slug}.html"
    
    html = TEMPLATE.format(
        title=art['title'],
        description=art['description'],
        keywords=art['keywords'],
        slug=slug,
        h1=art['h1'],
        h1_escaped=art['h1'].replace('"', '\\"'),
        description_escaped=art['description'].replace('"', '\\"'),
        breadcrumb_title_escaped=art['breadcrumb_title'].replace('"', '\\"'),
        category_badge=art['category_badge'],
        read_time=art['read_time'],
        key_takeaways=art['key_takeaways'],
        body_html=art['body_html'],
        related_links_html=art['related_links_html']
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated: {filepath} ({len(art['title'])} chars title, {len(art['description'])} chars desc)")

print(f"\nSuccessfully built all {len(all_p0)} Priority P0 Articles!")
