# -*- coding: utf-8 -*-
"""
Builder script to update website/artikel/index.html with all 34 B2B articles categorized by pillar.
"""

from data_cluster1 import cluster1_articles
from data_cluster2 import cluster2_articles
from data_cluster3 import cluster3_articles
from data_cluster4 import cluster4_articles
from data_cluster5 import cluster5_articles

# Additional core existing articles
core_articles = [
    {
        "slug": "daftar-harga-beras-ladori-25kg",
        "title": "Daftar Harga Beras Ladori 25 kg & DiHorein Grosir 2026",
        "badge": "💰 Daftar Harga Pabrik",
        "desc": "Update daftar harga beras Ladori 25 kg & DiHorein grosir pabrik untuk katering, SPPG, dan toko sembako di Jogja, Sleman, Magelang."
    },
    {
        "slug": "standar-beras-dapur-sppg-mbg",
        "title": "Standar Beras Dapur SPPG Makan Bergizi Gratis (MBG) BGN",
        "badge": "🏛️ Regulasi BGN",
        "desc": "Panduan standar mutu beras Dapur SPPG Makan Bergizi Gratis (MBG) Badan Gizi Nasional. Kadar air 13.8%, bebas klorin, dan sertifikasi halal."
    },
    {
        "slug": "cara-membedakan-beras-pulen-alami-bebas-pemutih",
        "title": "5 Cara Membedakan Beras Alami vs Beras Berpemutih Kimia",
        "badge": "🔬 Forensik Mutu Pangan",
        "desc": "Panduan koki & keluarga membedakan beras berpemutih klorin vs beras alami. Nasi tahan basi >24 jam tanpa lendir, uji visual, sentuhan, dan rendaman."
    },
    {
        "slug": "peluang-usaha-grosir-beras-kelontong",
        "title": "Peluang Usaha Kulakan Grosir Beras Toko Kelontong 2026",
        "badge": "🏪 Grosir & Retail",
        "desc": "Panduan kulakan Beras Ladori tangan pertama untuk toko sembako dan kelontong di Magelang, Muntilan, Sleman, Jogja. Margin tinggi dan perputaran cepat."
    }
]

pillars = [
    {
        "title": "Pilar 1: Evaluasi & Kualifikasi Supplier B2B",
        "desc": "Panduan menyeluruh memilih, menguji, dan membandingkan rekanan supplier beras komersial.",
        "articles": cluster1_articles
    },
    {
        "title": "Pilar 2: Kalkulasi Ekonomi, Yield & Manajemen Persediaan",
        "desc": "Formula ilmiah menghitung cooking yield, total cost of ownership, safety stock, dan reorder point.",
        "articles": cluster2_articles
    },
    {
        "title": "Pilar 3: Quality Control, Laboratorium & Traceability",
        "desc": "SOP penerimaan beras, metrologi moisture meter, pemisahan butir kepala vs broken, dan audit COA.",
        "articles": cluster3_articles
    },
    {
        "title": "Pilar 4: Panduan Khusus Segmen Dapur & Industri",
        "desc": "Kriteria pengadaan spesifik untuk unit Dapur SPPG MBG, pondok pesantren, katering, hotel, dan toko sembako.",
        "articles": cluster4_articles
    },
    {
        "title": "Pilar 5: Koridor Logistik & Pengadaan Regional",
        "desc": "Efisiensi rute arteri Muntilan–Magelang–Sleman–Jogja–Temanggung dan keandalan armada pengiriman.",
        "articles": cluster5_articles
    }
]

def render_article_card(art):
    slug = art["slug"]
    title = art["title"]
    badge = art.get("badge", "📄 Artikel B2B")
    desc = art.get("description", art.get("desc", ""))
    read_time = art.get("read_time", "7 Menit")

    return f"""        <article class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-md hover:border-brand-500 transition flex flex-col justify-between p-6">
          <div>
            <div class="inline-flex items-center text-xs font-bold text-brand-700 bg-brand-50 px-2.5 py-1 rounded-full mb-3">
              {badge}
            </div>
            <h3 class="text-base sm:text-lg font-bold text-slate-900 hover:text-brand-700 transition leading-snug">
              <a href="/artikel/{slug}">{title}</a>
            </h3>
            <p class="text-xs text-slate-400 mt-1">Waktu Baca: {read_time}</p>
            <p class="text-xs sm:text-sm text-slate-600 mt-3 leading-relaxed">
              {desc}
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-100">
            <a href="/artikel/{slug}" class="text-brand-700 font-bold text-xs sm:text-sm hover:underline inline-flex items-center gap-1">
              Baca Panduan Lengkap &rarr;
            </a>
          </div>
        </article>"""

hub_html = f"""<!DOCTYPE html>
<html lang="id" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Panduan Pengadaan Beras Katering | Distributor Beras Ladori</title>
  <meta name="description" content="Kumpulan artikel edukasi pengadaan beras, daftar harga grosir beras Ladori 25kg, tips memilih beras katering tahan basi, dan standar mutu dapur MBG.">
  <meta name="keywords" content="artikel beras b2b, panduan pengadaan beras, daftar harga beras ladori 25kg, standar beras dapur mbg, supplier beras catering">
  <link rel="canonical" href="https://www.berasladori.com/artikel">
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

  <!-- Open Graph Meta Tags -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.berasladori.com/artikel">
  <meta property="og:site_name" content="Distributor Resmi Beras Ladori">
  <meta property="og:locale" content="id_ID">
  <meta property="og:title" content="Panduan Pengadaan Beras Katering | Distributor Beras Ladori">
  <meta property="og:description" content="Kumpulan artikel edukasi pengadaan beras, panduan grosir beras Ladori 25kg, tips memilih beras katering tahan basi, dan standar mutu dapur MBG.">
  <meta property="og:image" content="https://www.berasladori.com/assets/images/og-image.jpg">
  <meta property="og:image:secure_url" content="https://www.berasladori.com/assets/images/og-image.jpg">
  <meta property="og:image:type" content="image/jpeg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Pusat Edukasi Beras Ladori">

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
      "@type": "CollectionPage",
      "name": "Pusat Informasi & Panduan Beras B2B Beras Ladori",
      "url": "https://www.berasladori.com/artikel",
      "description": "Kumpulan artikel edukasi pengadaan beras grosir, standar mutu dapur MBG, dan analisis rendemen beras katering."
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
          "name": "Artikel Edukasi Beras",
          "item": "https://www.berasladori.com/artikel"
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
          <a href="/" class="text-sm font-semibold text-slate-600 hover:text-brand-700">&larr; Beranda Utama</a>
          <a href="https://wa.me/6282227420003?text=Halo%20Distributor%20Beras%20Ladori%2C%20saya%20ingin%20konsultasi%20pengadaan%20beras%20B2B." target="_blank" class="hidden sm:inline-flex bg-brand-700 hover:bg-brand-800 text-white px-4 py-2 rounded-lg text-sm font-semibold transition">
            Minta Sampel Tester (WA)
          </a>
        </div>
      </div>
    </div>
  </header>

  <!-- Hero Banner -->
  <div class="bg-brand-900 text-white py-16">
    <div class="max-w-5xl mx-auto px-4 text-center">
      <span class="text-xs font-bold text-gold-400 uppercase tracking-widest block mb-2">Pusat Wawasan & Sains Pengadaan Pangan</span>
      <h1 class="text-3xl sm:text-5xl font-black tracking-tight">Pusat Informasi & Panduan Beras B2B</h1>
      <p class="text-brand-100 text-sm sm:text-base mt-4 max-w-2xl mx-auto leading-relaxed">
        34 panduan komprehensif berbasis data science untuk pemilik katering, pengelola dapur SPPG Makan Bergizi Gratis, hotel, restoran, pondok pesantren, dan toko sembako di koridor Magelang–Jogja.
      </p>
    </div>
  </div>

  <!-- Main Content Grid per Pillar -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 space-y-16">

    <!-- Featured Essential Guides -->
    <section>
      <div class="border-b border-slate-200 pb-4 mb-8">
        <h2 class="text-2xl font-black text-slate-900">⭐ Panduan Utama & Daftar Harga Resmi</h2>
        <p class="text-xs sm:text-sm text-slate-500 mt-1">Daftar harga pabrik terbaru, regulasi dapur MBG, dan uji kemurnian beras bebas pemutih.</p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
""" + "\n".join([render_article_card(a) for a in core_articles]) + """
      </div>
    </section>
"""

for p in pillars:
    hub_html += f"""
    <!-- {p['title']} -->
    <section>
      <div class="border-b border-slate-200 pb-4 mb-8">
        <h2 class="text-2xl font-black text-slate-900">{p['title']}</h2>
        <p class="text-xs sm:text-sm text-slate-500 mt-1">{p['desc']}</p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
""" + "\n".join([render_article_card(a) for a in p["articles"]]) + """
      </div>
    </section>
"""

hub_html += """
    <!-- Bottom CTA Banner -->
    <section class="bg-brand-900 text-white p-8 sm:p-12 rounded-3xl text-center space-y-4 shadow-xl">
      <span class="text-xs font-bold text-gold-400 uppercase tracking-widest block">Mitra Strategis Pengadaan Beras B2B</span>
      <h2 class="text-2xl sm:text-4xl font-black">Siap Meningkatkan Kualitas Nasi Dapur Anda?</h2>
      <p class="text-xs sm:text-sm text-slate-300 max-w-xl mx-auto">
        Diskusikan kebutuhan tonase rutin Anda bersama tim ahli Beras Ladori. Nikmati fasilitas uji sampel gratis, jadwal pengiriman reguler, dan harga tangan pertama pabrik.
      </p>
      <div class="pt-4 flex flex-wrap justify-center gap-4">
        <a href="https://wa.me/6282227420003?text=Halo%20Distributor%20Beras%20Ladori%2C%20saya%20ingin%20konsultasi%20pengadaan%20beras%20B2B." target="_blank" class="inline-flex items-center gap-2 bg-emerald-600 hover:bg-emerald-700 text-white font-bold px-8 py-4 rounded-xl text-sm shadow-lg transition">
          <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/></svg>
          Konsultasi Pengadaan (WhatsApp)
        </a>
        <a href="/produk/beras-ladori-25kg" class="inline-flex items-center gap-2 bg-white/10 hover:bg-white/20 text-white font-bold px-8 py-4 rounded-xl text-sm border border-white/20 transition">
          Lihat Spesifikasi Beras Ladori 25 kg &rarr;
        </a>
      </div>
    </section>

  </main>

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

with open("website/artikel/index.html", "w", encoding="utf-8") as f:
    f.write(hub_html)

print("Updated website/artikel/index.html successfully with all 34 articles!")
