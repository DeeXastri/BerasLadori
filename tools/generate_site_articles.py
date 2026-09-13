# -*- coding: utf-8 -*-
"""
Main Builder Script to generate all 30 B2B Articles and update website/artikel/index.html
"""

import os
import json
import re

from data_cluster1 import cluster1_articles
from data_cluster2 import cluster2_articles
from data_cluster3 import cluster3_articles
from data_cluster4 import cluster4_articles
from data_cluster5 import cluster5_articles

all_articles = (
    cluster1_articles +
    cluster2_articles +
    cluster3_articles +
    cluster4_articles +
    cluster5_articles
)

print(f"Total articles to build: {len(all_articles)}")

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

  <!-- Open Graph / WhatsApp Preview Meta Tags -->
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
          <a href="https://wa.me/6282227420003?text=Halo%20Distributor%20Beras%20Ladori%2C%20saya%20ingin%20konsultasi%20pengadaan%20beras%20B2B." target="_blank" class="hidden sm:inline-flex bg-brand-700 hover:bg-brand-800 text-white px-4 py-2 rounded-lg text-sm font-semibold transition">
            Minta Sampel Tester (WA)
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
      <span class="text-brand-700">{breadcrumb_title}</span>
    </nav>

    <div class="inline-flex items-center gap-2 bg-emerald-100 text-emerald-900 px-3 py-1 rounded-full text-xs font-bold mb-4">
      <span>{badge}</span>
      <span>&bull;</span>
      <span>{category}</span>
    </div>

    <h1 class="text-3xl sm:text-4xl lg:text-5xl font-black text-slate-900 tracking-tight leading-tight mb-4">
      {h1}
    </h1>

    <div class="flex items-center gap-4 text-xs text-slate-500 border-b border-slate-200 pb-6 mb-8">
      <span>Oleh: <strong>Tim Kontrol Kualitas & Logistik Beras Ladori</strong></span>
      <span>&bull;</span>
      <span>Diperbarui: 13 September 2026</span>
      <span>&bull;</span>
      <span>Waktu Baca: {read_time}</span>
    </div>

    <!-- Direct Answer Box -->
    <div class="bg-emerald-50 border-2 border-brand-600 rounded-2xl p-6 mb-10 text-slate-800 shadow-sm">
      <h3 class="text-xs font-bold text-brand-800 uppercase tracking-wider mb-2">Ringkasan Sains & Solusi Dapur:</h3>
      <p class="text-sm leading-relaxed text-slate-700">
        {direct_answer}
      </p>
    </div>

    <!-- Body Content -->
    <div class="space-y-8 text-sm sm:text-base text-slate-700 leading-relaxed">
{rendered_sections}
    </div>

    <!-- Related Articles Grid -->
    <div class="mt-12 pt-8 border-t border-slate-200">
      <h3 class="text-lg font-bold text-slate-900 mb-4">Artikel & Panduan Terkait:</h3>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
{rendered_related}
      </div>
    </div>

    <!-- CTA Box -->
    <div class="bg-brand-900 text-white p-8 rounded-3xl text-center space-y-4 my-12 shadow-xl">
      <span class="text-xs font-bold text-gold-400 uppercase tracking-widest block">Layanan Pasokan B2B Terpercaya</span>
      <h2 class="text-2xl sm:text-3xl font-black">Konsultasikan Pengadaan Beras Dapur Anda Bersama Beras Ladori</h2>
      <p class="text-xs sm:text-sm text-slate-300 max-w-lg mx-auto">
        Dapatkan penawaran harga grosir pabrik, jadwal rute armada gratis ongkir, dan paket sampel tester 1&ndash;2 kg gratis untuk uji tanak langsung di dapur Anda.
      </p>
      <div class="pt-2">
        <a href="https://wa.me/6282227420003?text=Halo%20Distributor%20Beras%20Ladori%2C%20saya%20tertarik%20dengan%20panduan%20{wa_title_encoded}%20dan%20ingin%20konsultasi%20sampel%20B2B." target="_blank" class="inline-flex items-center gap-2 bg-emerald-600 hover:bg-emerald-700 text-white font-bold px-8 py-4 rounded-xl text-sm shadow-lg transition">
          <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
          Minta Sampel Tester Uji Masak (WhatsApp)
        </a>
      </div>
    </div>
  </article>

  <!-- Footer -->
  <footer class="bg-slate-900 text-slate-400 text-xs py-8 border-t border-slate-800 text-center">
    <div class="max-w-4xl mx-auto px-4 space-y-2">
      <div class="flex flex-wrap justify-center gap-3 text-slate-400">
        <a href="/" class="hover:text-white">Beranda</a> &bull;
        <a href="/produk/beras-ladori-25kg" class="hover:text-white">Produk 25 kg</a> &bull;
        <a href="/tentang/beras-ladori" class="hover:text-white">Tentang Beras Ladori</a> &bull;
        <a href="/wilayah/magelang" class="hover:text-white">Magelang</a> &bull;
        <a href="/wilayah/muntilan" class="hover:text-white">Muntilan</a> &bull;
        <a href="/wilayah/sleman" class="hover:text-white">Sleman</a> &bull;
        <a href="/wilayah/jogja" class="hover:text-white">Jogja</a> &bull;
        <a href="/wilayah/temanggung" class="hover:text-white">Temanggung</a>
      </div>
      <p>&copy; 2026 Beras Ladori (BerasLadori.com) &bull; Edukasi Mutu Beras Koridor Jogja, Sleman & Magelang Raya</p>
    </div>
  </footer>

</body>
</html>
"""

output_dir = "website/artikel"
os.makedirs(output_dir, exist_ok=True)

for art in all_articles:
    slug = art["slug"]
    title = art["title"]
    h1 = art["h1"]
    desc = art["description"]
    keywords = art["keywords"]
    badge = art["badge"]
    cat = art["category"]
    read_time = art["read_time"]
    direct_ans = art["direct_answer"]
    breadcrumb_title = title.split(":")[0].strip() if ":" in title else title[:30].strip()

    # Section formatting
    rendered_sections = ""
    for sec in art["sections"]:
        rendered_sections += f"""      <section class="space-y-4">
        <h2 class="text-2xl font-bold text-slate-900">{sec['h2']}</h2>
{sec['content']}
      </section>\n\n"""

    # Related links formatting
    rendered_related = ""
    for rel in art["related_links"]:
        rendered_related += f"""        <a href="{rel['href']}" class="flex items-center gap-2 p-3 rounded-xl bg-white border border-slate-200 hover:border-brand-600 hover:text-brand-700 transition text-xs sm:text-sm font-semibold text-slate-700 shadow-sm">
          <span>&rarr;</span>
          <span>{rel['title']}</span>
        </a>\n"""

    html = TEMPLATE.format(
        title=title,
        description=desc,
        keywords=keywords,
        slug=slug,
        h1=h1,
        h1_escaped=h1.replace('"', '\\"'),
        description_escaped=desc.replace('"', '\\"'),
        breadcrumb_title=breadcrumb_title,
        breadcrumb_title_escaped=breadcrumb_title.replace('"', '\\"'),
        badge=badge,
        category=cat,
        read_time=read_time,
        direct_answer=direct_ans,
        rendered_sections=rendered_sections,
        rendered_related=rendered_related,
        wa_title_encoded=title.replace(" ", "%20")
    )

    filepath = os.path.join(output_dir, f"{slug}.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated: {filepath} ({len(title)} chars title, {len(desc)} chars desc)")

print(f"\nSuccessfully created all {len(all_articles)} article HTML files!")
