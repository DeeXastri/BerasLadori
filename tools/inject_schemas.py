import os

base_dir = r"C:\Users\user\Desktop\Project_Antigravity\BERAS LADORI\website"

territories = {
    "muntilan.html": {
        "name": "Distributor Beras Ladori Gudang Pusat Muntilan",
        "area": "Kecamatan Muntilan & Koridor Magelang-Jogja",
        "city": "Muntilan"
    },
    "sleman.html": {
        "name": "Distributor Beras Ladori Wilayah Sleman",
        "area": "Kabupaten Sleman, D.I. Yogyakarta",
        "city": "Sleman"
    },
    "jogja.html": {
        "name": "Distributor Beras Ladori Wilayah Kota Yogyakarta",
        "area": "Kota Yogyakarta, D.I. Yogyakarta",
        "city": "Yogyakarta"
    },
    "temanggung.html": {
        "name": "Distributor Beras Ladori Wilayah Temanggung",
        "area": "Kabupaten Temanggung, Jawa Tengah",
        "city": "Temanggung"
    }
}

for fname, info in territories.items():
    fpath = os.path.join(base_dir, "wilayah", fname)
    with open(fpath, "r", encoding="utf-8") as fp:
        html = fp.read()
    
    schema_code = f"""  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "{info['name']}",
    "description": "Layanan pasokan beras grosir dan tonase partai besar untuk {info['area']}.",
    "telephone": "+6281234567890",
    "areaServed": {{
      "@type": "AdministrativeArea",
      "name": "{info['area']}"
    }},
    "address": {{
      "@type": "PostalAddress",
      "addressLocality": "{info['city']}",
      "addressRegion": "Jawa Tengah / DIY",
      "addressCountry": "ID"
    }}
  }}
  </script>
</head>"""

    if '</head>' in html and 'application/ld+json' not in html:
        html = html.replace('</head>', schema_code)
        with open(fpath, "w", encoding="utf-8") as fp:
            fp.write(html)
        print(f"Injected schema into wilayah/{fname}")

# Inject into artikel/index.html
art_index = os.path.join(base_dir, "artikel", "index.html")
with open(art_index, "r", encoding="utf-8") as fp:
    art_html = fp.read()

art_schema = """  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    "name": "Pusat Informasi & Panduan Beras B2B",
    "url": "https://distributorberasladori.com/artikel",
    "description": "Kumpulan artikel edukasi pengadaan beras grosir, standar mutu dapur MBG, dan analisis rendemen beras katering."
  }
  </script>
</head>"""

if '</head>' in art_html and 'application/ld+json' not in art_html:
    art_html = art_html.replace('</head>', art_schema)
    with open(art_index, "w", encoding="utf-8") as fp:
        fp.write(art_html)
    print("Injected schema into artikel/index.html")

print("All schemas injected!")
