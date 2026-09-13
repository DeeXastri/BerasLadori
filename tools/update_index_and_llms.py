# -*- coding: utf-8 -*-
"""
Script to update:
1. website/artikel/index.html (add P0 section + tool banner)
2. website/llms.txt
3. website/llms-full.txt
"""

import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# 1. READ P0 ARTICLES
sys.path.insert(0, os.path.dirname(__file__))
from data_p0_part1 import p0_part1_articles
from data_p0_part2 import p0_part2_articles

all_p0 = p0_part1_articles + p0_part2_articles

# 2. GENERATE HTML CARDS FOR P0 SECTION
cards_html = []
for art in all_p0:
    card = f"""        <article class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-md hover:border-brand-500 transition flex flex-col justify-between p-6">
          <div>
            <div class="inline-flex items-center text-xs font-bold text-brand-700 bg-brand-50 px-2.5 py-1 rounded-full mb-3">
              {art['category_badge']}
            </div>
            <h3 class="text-base sm:text-lg font-bold text-slate-900 hover:text-brand-700 transition leading-snug">
              <a href="/artikel/{art['slug']}">{art['h1']}</a>
            </h3>
            <p class="text-xs text-slate-400 mt-1">Waktu Baca: {art['read_time']} Menit</p>
            <p class="text-xs sm:text-sm text-slate-600 mt-3 leading-relaxed">
              {art['description']}
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-100">
            <a href="/artikel/{art['slug']}" class="text-brand-700 font-bold text-xs sm:text-sm hover:underline inline-flex items-center gap-1">
              Baca Panduan Lengkap &rarr;
            </a>
          </div>
        </article>"""
    cards_html.append(card)

cards_joined = "\n".join(cards_html)

p0_section_html = f"""    <!-- Pilar Prioritas P0: Standar Mutu, Porsi Acara & Solusi Dapur -->
    <section>
      <div class="border-b border-slate-200 pb-4 mb-8 flex flex-col sm:flex-row sm:items-end justify-between gap-4">
        <div>
          <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-amber-50 text-amber-800 border border-amber-200 mb-2">
            ⭐ Fondasi Master Audit 2026 (Prioritas P0)
          </div>
          <h2 class="text-2xl font-black text-slate-900">Pilar Inti: Mutu, Porsi Acara, & Manajemen Dapur</h2>
          <p class="text-xs sm:text-sm text-slate-500 mt-1">Panduan otoritatif dari sains rendemen masak, toleransi kadar air, hingga mitigasi hama gudang.</p>
        </div>
        <a href="/tools/kalkulator-kebutuhan-beras" class="inline-flex items-center gap-2 px-4 py-2 bg-brand-700 text-white rounded-xl text-xs sm:text-sm font-bold hover:bg-brand-800 transition shadow-sm">
          <span>🧮</span> Buka Kalkulator Porsi Otomatis
        </a>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
{cards_joined}
      </div>
    </section>
"""

# Insert into website/artikel/index.html
with open('website/artikel/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

target_marker = "<!-- Pilar 1: Evaluasi & Kualifikasi Supplier B2B -->"
if target_marker in index_content:
    new_index_content = index_content.replace(target_marker, p0_section_html + "\n\n    " + target_marker)
    with open('website/artikel/index.html', 'w', encoding='utf-8') as f:
        f.write(new_index_content)
    print("Successfully updated website/artikel/index.html with 14 P0 article cards!")
else:
    print("Warning: Target marker not found in website/artikel/index.html")

# 3. UPDATE website/llms.txt
p0_llms_lines = [
    f"- [{art['h1']}](https://www.berasladori.com/artikel/{art['slug']}): {art['description']}"
    for art in all_p0
]
tool_llms_line = "- [Kalkulator Kebutuhan Beras Acara & Dapur](https://www.berasladori.com/tools/kalkulator-kebutuhan-beras): Kalkulator otomatis kebutuhan kg beras mentah, cooking yield nasi matang 2.4x, dan estimasi food cost per porsi untuk katering, prasmanan, dan SPPG MBG."

with open('website/llms.txt', 'r', encoding='utf-8') as f:
    llms_txt = f.read()

if "## Arsip Panduan Fondasi & Porsi Beras (14 Panduan P0 Master Audit)" not in llms_txt:
    insert_block = f"""## Arsip Panduan Fondasi & Porsi Beras (14 Panduan P0 Master Audit)
{tool_llms_line}
""" + "\n".join(p0_llms_lines) + "\n\n"

    # Insert before Arsip Panduan Sains Pengadaan Beras B2B
    split_point = "## Arsip Panduan Sains Pengadaan Beras B2B"
    if split_point in llms_txt:
        llms_txt = llms_txt.replace(split_point, insert_block + split_point)
        with open('website/llms.txt', 'w', encoding='utf-8') as f:
            f.write(llms_txt)
        print("Successfully updated website/llms.txt with 14 P0 guides and calculator tool!")

# 4. UPDATE website/llms-full.txt
with open('website/llms-full.txt', 'r', encoding='utf-8') as f:
    llms_full_txt = f.read()

if "## Arsip Panduan Fondasi & Porsi Beras (14 Panduan P0 Master Audit)" not in llms_full_txt:
    split_point = "## Arsip Panduan Sains Pengadaan Beras B2B"
    if split_point in llms_full_txt:
        llms_full_txt = llms_full_txt.replace(split_point, insert_block + split_point)
        with open('website/llms-full.txt', 'w', encoding='utf-8') as f:
            f.write(llms_full_txt)
        print("Successfully updated website/llms-full.txt with 14 P0 guides and calculator tool!")
