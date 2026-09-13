# -*- coding: utf-8 -*-
"""
Generator 30 Artikel SEO B2B Beras Ladori 2026
Berbasis Kaidah Google 2026 (Information Gain, Anti-Slop, E-E-A-T)
dan Standarisasi Data Science / Food Science.
"""

import os
import re

articles_data = [
    {
        "id": 1,
        "slug": "cara-memilih-supplier-beras-b2b",
        "title": "Cara Memilih Supplier Beras B2B untuk Dapur Komersial",
        "h1": "Cara Memilih Supplier Beras B2B untuk Catering, Hotel, Restoran, dan SPPG",
        "category": "Strategi Pengadaan B2B",
        "badge": "🎯 Panduan Seleksi Vendor",
        "read_time": "7 Menit",
        "description": "Panduan memilih supplier beras B2B untuk katering, hotel, resto, dan SPPG. Evaluasi spesifikasi butir, uji tanak, konsistensi batch, dan total cost.",
        "keywords": "cara memilih supplier beras, supplier beras b2b, vendor beras catering, distributor beras horeka, evaluasi supplier beras",
        "direct_answer": "Memilih supplier beras B2B memerlukan pendekatan operasional berbasis sistem: tentukan profil kebutuhan nasi (kadar amilosa & tekstur), lakukan uji tanak dengan penimbangan rendemen (yield ratio), verifikasi kapasitas buffer stock gudang distributor, serta pastikan legalitas usaha (KBLI 46312) dan SLA komplain resmi. Supplier terbaik bukan yang menawarkan harga per kg termurah, melainkan yang menghasilkan biaya per porsi terendah secara konsisten.",
        "sections": [
            {
                "h2": "1. Pergeseran Paradigma: Mengapa Belanja Beras B2B Bukan Sekadar Harga per Kg",
                "content": """
                <p>Dalam operasional dapur komersial—baik katering hajatan, restoran, hotel, pondok pesantren, maupun unit Dapur SPPG Makan Bergizi Gratis (MBG)—beras adalah komponen biaya bahan baku utama (<em>Cost of Goods Sold / COGS</em>) dengan volume perputaran tertinggi. Kesalahan dalam memilih rekanan supplier tidak sekadar memicu keluhan rasa nasi, melainkan berakibat fatal pada pembengkakan <em>food cost</em>, terganggunya alur produksi, hingga risiko kehabisan stok saat jam operasional sibuk.</p>
                <p>Banyak pengelola dapur terjebak pada ilusi harga beli mentah: beras seharga Rp 13.800/kg sering kali disangka lebih hemat dibanding beras Rp 14.200/kg. Padahal, jika beras murah tersebut memiliki kadar air tinggi (>14.5%) dan butir patah (broken) di atas 20%, rendemen nasi matangnya anjlok drastis. Biaya riil per porsi nasi siap santap justru jauh lebih mahal.</p>
                """
            },
            {
                "h2": "2. Matriks Evaluasi 4 Pilar Kualifikasi Supplier Beras",
                "content": """
                <p>Purchasing institusional profesional menggunakan matriks kuadran untuk menyeleksi calon rekanan beras:</p>
                <div class="overflow-x-auto my-4">
                  <table class="w-full text-left border-collapse border border-slate-200 text-xs sm:text-sm bg-white rounded-xl shadow-sm">
                    <thead>
                      <tr class="bg-brand-50 text-brand-900 border-b border-slate-200">
                        <th class="p-3 font-bold">Pilar Evaluasi</th>
                        <th class="p-3 font-bold">Parameter Objektif (Data Science)</th>
                        <th class="p-3 font-bold">Standar Minimum Diterima</th>
                      </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 text-slate-700">
                      <tr>
                        <td class="p-3 font-semibold">1. Mutu Fisik & Lab</td>
                        <td class="p-3">Kadar air (Moisture), Beras Kepala (Head Rice), Butir Broken, Benda Asing</td>
                        <td class="p-3">Kadar air &le; 13.8%, Kepala &ge; 85%, Broken &le; 12%, Batu/Kutu = 0%</td>
                      </tr>
                      <tr>
                        <td class="p-3 font-semibold">2. Cooking Yield</td>
                        <td class="p-3">Multiplier rendemen berat matang vs mentah (<em>W<sub>cooked</sub> / W<sub>raw</sub></em>)</td>
                        <td class="p-3">Minimal 2.2x &ndash; 2.4x (1 kg beras mentah menghasilkan &ge; 2.2 kg nasi)</td>
                      </tr>
                      <tr>
                        <td class="p-3 font-semibold">3. Keandalan Logistik</td>
                        <td class="p-3">Jadwal rute armada tetap, lead time order, buffer stock cadangan</td>
                        <td class="p-3">Rute mingguan pasti, SLA keterlambatan 0 hari, buffer stock &ge; 3 hari</td>
                      </tr>
                      <tr>
                        <td class="p-3 font-semibold">4. Akuntabilitas Bisnis</td>
                        <td class="p-3">Legalitas izin edar KBLI 46312, faktur resmi, garansi retur cacat</td>
                        <td class="p-3">Faktur resmi tersedia, SLA retur barang cacat &lt; 24 jam gratis</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "h2": "3. Uji Tanak Berbasis Gramasi: Menghitung Biaya per Porsi Nasi",
                "content": """
                <p>Jangan pernah menandatangani kontrak pasokan hanya berdasarkan melihat segenggam beras mentah di telapak tangan. Selalu minta sampel uji tanak (1&ndash;2 kg) dan lakukan pengujian dengan resep dapur Anda sendiri:</p>
                <div class="bg-slate-100 p-4 rounded-xl border border-slate-200 my-4 text-xs sm:text-sm font-mono text-slate-800">
                  <strong>Rumus Biaya per Porsi:</strong><br>
                  Biaya per Porsi = Harga Beras per kg &divide; (Cooking Yield Multiplier &times; 1000g &divide; Gramasi Porsi Dapur)<br><br>
                  <em>Contoh:</em> Beras Ladori (Rp 14.200/kg) dengan Yield 2.35x dan porsi 150g nasi:<br>
                  Porsi per kg = (2.35 &times; 1000) &divide; 150 = 15.66 porsi<br>
                  Biaya per Porsi = Rp 14.200 &divide; 15.66 = <strong>Rp 906 per porsi</strong>
                </div>
                <p>Bandingkan dengan beras pasar murah (Rp 13.500/kg) berkadar air tinggi yang hanya menghasilkan yield 1.9x (12.6 porsi). Biaya per porsinya mencapai <strong>Rp 1.071</strong>. Beras murah ternyata 18% lebih boros!</p>
                """
            },
            {
                "h2": "4. Sinergi Rute Logistik: Mengapa Kedekatan Hub Sangat Menentukan",
                "content": """
                <p>Bagi pelaku usaha kuliner dan institusi di kawasan Magelang, Sleman, Kota Yogyakarta, dan Temanggung, pasokan yang berbasis di koridor Jalan Magelang–Muntilan menawarkan keunggulan logistik nyata. Waktu tempuh armada yang singkat (kurang dari 45 menit ke sentra Sleman/Jogja) memastikan jadwal pengiriman rutin mingguan dapat diandalkan tanpa risiko terjebak kendala antarkota jarak jauh.</p>
                <p>Pelajari spesifikasi produk resmi kami di halaman <a href="/produk/beras-ladori-25kg" class="text-brand-700 font-bold underline">Beras Ladori 25 kg</a> atau diskusikan kebutuhan pengadaan instansi Anda bersama tim kami.</p>
                """
            }
        ],
        "related_links": [
            {"title": "15 Pertanyaan Wajib Sebelum Memilih Supplier Beras B2B", "href": "/artikel/pertanyaan-sebelum-memilih-supplier-beras"},
            {"title": "Cara Uji Sampel Beras yang Benar Sebelum Kontrak Pasokan", "href": "/artikel/uji-sampel-beras-sebelum-kontrak"},
            {"title": "Total Cost of Ownership Beras Dapur Komersial", "href": "/artikel/total-cost-beras-dapur-komersial"},
            {"title": "Layanan Pengadaan Beras Katering & Restoran", "href": "/program/katering-horeka"},
            {"title": "Basis Gudang & Distribusi Beras Muntilan", "href": "/wilayah/muntilan"}
        ]
    },
    {
        "id": 2,
        "slug": "pertanyaan-sebelum-memilih-supplier-beras",
        "title": "15 Pertanyaan Wajib Sebelum Memilih Supplier Beras B2B",
        "h1": "15 Pertanyaan Esensial yang Wajib Diajukan Sebelum Menyetujui Kontrak Supplier Beras",
        "category": "Audit & Kualifikasi Vendor",
        "badge": "📋 Checklist Purchasing",
        "read_time": "8 Menit",
        "description": "15 pertanyaan esensial sebelum menyetujui kontrak supplier beras: kadar air, yield rendemen, MOQ, jadwal rute reguler, buffer stock, hingga SLA komplain.",
        "keywords": "pertanyaan memilih supplier beras, wawancara vendor beras, checklist purchasing beras, kontrak pasokan beras b2b",
        "direct_answer": "Sebelum menandatangani kontrak pengadaan beras rutin, tim purchasing wajib menanyakan 15 parameter kunci yang terbagi dalam 4 kategori: spesifikasi butir fisik (kadar air & broken), kepastian yield & stabilitas antar-batch, manajemen logistik (MOQ, jadwal rute, buffer stock), serta tata kelola administrasi (faktur resmi, izin KBLI 46312, dan SLA retur gratis tanpa debat).",
        "sections": [
            {
                "h2": "1. Mengapa Lembar Kualifikasi Supplier Beras Sangat Dibutuhkan",
                "content": """
                <p>Sering kali percakapan antara bagian pengadaan (purchasing) dengan sales beras hanya berputar pada pertanyaan: <em>"Berapa harga per kilogram?"</em> dan <em>"Berasnya pulen atau pera?"</em> Pendekatan dangkal seperti ini adalah penyebab utama kekacauan dapur sebulan kemudian ketika nasi berubah tekstur, pengiriman molor, atau timbangan karung berkurang.</p>
                <p>Gunakan daftar 15 pertanyaan terstruktur berikut sebagai lembar kualifikasi (<em>vendor qualification sheet</em>) resmi di meja pengadaan Anda.</p>
                """
            },
            {
                "h2": "2. Rincian 15 Pertanyaan Audit Supplier Beras",
                "content": """
                <div class="space-y-4">
                  <div class="bg-white p-4 rounded-xl border border-slate-200">
                    <h3 class="font-bold text-slate-900 text-sm mb-2">Kategori A: Mutu Fisik & Standar Laboratorium</h3>
                    <ul class="list-disc pl-5 space-y-1 text-xs sm:text-sm text-slate-600">
                      <li><strong>1. Berapa batas toleransi kadar air (moisture content) pada setiap karung yang dikirim?</strong> (Standar aman: &le; 13.8%).</li>
                      <li><strong>2. Berapa rasio butir kepala (head rice) dan butir patah (broken)?</strong> (Beras premium berkualitas &ge; 85% kepala).</li>
                      <li><strong>3. Apakah beras dijamin 100% bebas dari bahan pemutih klorin, pelicin parafin, dan pengharum buatan?</strong> (Wajib ada jaminan COA).</li>
                      <li><strong>4. Bagaimana supplier menjamin kebersihan dari kerikil dan benda asing?</strong> (Wajib melalui mesin <em>de-stoner</em> dan <em>color sorter</em> optik).</li>
                    </ul>
                  </div>

                  <div class="bg-white p-4 rounded-xl border border-slate-200">
                    <h3 class="font-bold text-slate-900 text-sm mb-2">Kategori B: Cooking Yield & Konsistensi Dapur</h3>
                    <ul class="list-disc pl-5 space-y-1 text-xs sm:text-sm text-slate-600">
                      <li><strong>5. Berapa rasio cooking yield matang yang digaransi saat dimasak dengan rice cooker komersial?</strong> (Ideal: 2.2x &ndash; 2.4x).</li>
                      <li><strong>6. Bagaimana sistem supplier menjaga stabilitas varietas antar-batch gilingan baru vs gilingan lama?</strong></li>
                      <li><strong>7. Berapa lama nasi hasil tanak mampu bertahan di rice warmer tanpa berair, kuning, atau berbau basi?</strong> (Standar Beras Ladori: &gt; 24 jam).</li>
                    </ul>
                  </div>

                  <div class="bg-white p-4 rounded-xl border border-slate-200">
                    <h3 class="font-bold text-slate-900 text-sm mb-2">Kategori C: Manajemen Rantai Pasok & Logistik</h3>
                    <ul class="list-disc pl-5 space-y-1 text-xs sm:text-sm text-slate-600">
                      <li><strong>8. Berapa Minimum Order Quantity (MOQ) untuk mendapatkan fasilitas gratis ongkos kirim ke lokasi dapur kami?</strong></li>
                      <li><strong>9. Hari apa saja jadwal rute armada reguler supplier melintasi area kami?</strong></li>
                      <li><strong>10. Berapa lead time pemesanan (cut-off time order) sebelum pengiriman dilakukan?</strong></li>
                      <li><strong>11. Berapa ton persediaan pengaman (buffer stock) yang disiagakan di gudang distributor supplier?</strong></li>
                    </ul>
                  </div>

                  <div class="bg-white p-4 rounded-xl border border-slate-200">
                    <h3 class="font-bold text-slate-900 text-sm mb-2">Kategori D: Legalitas, Pembayaran & Garansi Retur</h3>
                    <ul class="list-disc pl-5 space-y-1 text-xs sm:text-sm text-slate-600">
                      <li><strong>12. Apakah entitas usaha memiliki izin usaha legal perdagangan beras (KBLI 46312) dan NPWP resmi?</strong></li>
                      <li><strong>13. Apakah transaksi disertai nota bertanda tangan, surat jalan, dan faktur resmi untuk laporan pertanggungjawaban?</strong></li>
                      <li><strong>14. Bagaimana SOP dan Service Level Agreement (SLA) jika ditemukan karung robek, beras apek, atau kutu?</strong></li>
                      <li><strong>15. Apakah diperbolehkan melakukan kunjungan verifikasi (onsite audit) ke fasilitas gudang distributor?</strong></li>
                    </ul>
                  </div>
                </div>
                """
            },
            {
                "h2": "3. Penerapan Sistem Skoring Objektif",
                "content": """
                <p>Beri nilai 1&ndash;5 untuk setiap pertanyaan. Supplier yang layak dijadikan mitra kontrak rutin wajib mengantongi skor total minimal <strong>65 dari 75 poin</strong>. Distributor resmi Beras Ladori menyambut terbuka 15 pertanyaan ini dengan data konkret, transparansi gudang di Muntilan & Magelang, serta fasilitas uji sampel tanpa biaya.</p>
                """
            }
        ],
        "related_links": [
            {"title": "Cara Memilih Supplier Beras B2B untuk Dapur Komersial", "href": "/artikel/cara-memilih-supplier-beras-b2b"},
            {"title": "Cara Membandingkan 2 Supplier Beras Secara Adil & Akurat", "href": "/artikel/cara-membandingkan-supplier-beras"},
            {"title": "SOP Penerimaan Beras di Loading Dock Dapur Komersial", "href": "/artikel/sop-penerimaan-beras-dapur-b2b"},
            {"title": "Profil Legalitas & Entitas Resmi Beras Ladori", "href": "/tentang/beras-ladori"},
            {"title": "Program Pasokan Beras Dapur SPPG MBG", "href": "/program/sppg-mbg"}
        ]
    }
]

print(f"Loaded initial batch of {len(articles_data)} articles template.")
