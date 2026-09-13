# -*- coding: utf-8 -*-
"""
Kluster 1: Evaluasi & Seleksi Supplier B2B (Artikel 01 - 05)
Standar Data Science: Scoring Matrix, Yield vs Price Tradeoff, Total Cost of Ownership
"""

cluster1_articles = [
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
                <p>Sering kali percakapan antara bagian pengadaan (purchasing) dengan sales beras hanya berputar pada pertanyaan dangkal seputar harga per kilogram dan rasa pulen. Pendekatan ini adalah penyebab utama kekacauan dapur sebulan kemudian ketika nasi berubah tekstur, pengiriman molor, atau timbangan karung berkurang.</p>
                <p>Gunakan daftar 15 pertanyaan terstruktur berikut sebagai lembar kualifikasi resmi di meja pengadaan Anda.</p>
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
    },
    {
        "id": 3,
        "slug": "uji-sampel-beras-sebelum-kontrak",
        "title": "Cara Uji Sampel Beras yang Benar Sebelum Kontrak Pasokan",
        "h1": "Metode Ilmiah Uji Sampel Beras di Dapur Komersial Sebelum Penandatanganan Kontrak",
        "category": "Pengujian Laboratorium & Dapur",
        "badge": "🔬 Metodologi Sains Dapur",
        "read_time": "7 Menit",
        "description": "Protokol ilmiah uji sampel beras di dapur komersial. Standar rasio air, pengukuran rendemen gramasi matang, dan uji ketahanan nasi 24 jam di warmer.",
        "keywords": "uji sampel beras, uji tanak beras, tes rendemen nasi, uji lab beras sebelum beli, uji beras katering",
        "direct_answer": "Uji sampel beras yang valid tidak dilakukan dengan mencicipi semangkuk nasi yang dibawa sales, melainkan dimasak mandiri di dapur pembeli menggunakan alat dapur riil. Prosedurnya: timbang persis 1.000g beras, gunakan rasio air terukur (1:1.2 &ndash; 1:1.4), masak dalam rice cooker komersial, catat berat nasi matang untuk mengukur rendemen multiplier, dan uji ketahanan organoleptik setelah 12 hingga 24 jam di rice warmer.",
        "sections": [
            {
                "h2": "1. Jebakan Bias Sampel Sales: Mengapa Harus Diuji Sendiri",
                "content": """
                <p>Banyak pengelola katering dan restoran kecewa setelah mengikat kontrak pasokan beras. Saat presentasi penjualan, nasi yang disajikan sales terasa sangat harum dan pulen. Namun ketika beras dikirim satu truk ke gudang dapur, nasinya keras atau cepat basi. Mengapa ini terjadi?</p>
                <p>Dalam sains data pangan, ini dikenal sebagai <em>sampling bias</em>. Sales sering membawa beras varietas khusus yang dimasak dengan air mineral tertentu dan takaran khusus. Satu-satunya cara melindungi dapur Anda adalah meminta sampel mentah karung tertutup (1&ndash;2 kg), lalu mengujinya menggunakan SOP dan peralatan dapur Anda sendiri.</p>
                """
            },
            {
                "h2": "2. Protokol 5 Langkah Uji Tanak Terstandarisasi",
                "content": """
                <div class="space-y-3 my-4">
                  <div class="bg-white p-4 rounded-xl border border-slate-200">
                    <strong class="text-brand-800 text-sm block mb-1">Langkah 1: Penimbangan Presisi Beras Mentah</strong>
                    <p class="text-xs sm:text-sm text-slate-600">Gunakan timbangan digital dapur. Timbang tepat 1.000 gram beras mentah. Jangan menggunakan takaran cangkir (cup) karena densitas bulir bervariasi.</p>
                  </div>
                  <div class="bg-white p-4 rounded-xl border border-slate-200">
                    <strong class="text-brand-800 text-sm block mb-1">Langkah 2: Standarisasi Pencucian & Rasio Air</strong>
                    <p class="text-xs sm:text-sm text-slate-600">Cuci beras maksimal 2&ndash;3 kali secara cepat untuk mencegah butir patah menyerap air berlebih sebelum matang. Tiriskan 3 menit. Tambahkan air dengan rasio berat terukur: 1.200 gram air untuk beras pulen (rasio 1:1.2) atau 1.400 gram untuk tipe pulen mekar (rasio 1:1.4).</p>
                  </div>
                  <div class="bg-white p-4 rounded-xl border border-slate-200">
                    <strong class="text-brand-800 text-sm block mb-1">Langkah 3: Pemasakan & Resting 15 Menit</strong>
                    <p class="text-xs sm:text-sm text-slate-600">Masak dalam rice cooker. Saat tombol beralih ke <em>Warm</em>, jangan langsung dibuka. Biarkan fase resting (penyerapan uap air) selama 15 menit agar gelatinisasi pati sempurna hingga inti bulir.</p>
                  </div>
                  <div class="bg-white p-4 rounded-xl border border-slate-200">
                    <strong class="text-brand-800 text-sm block mb-1">Langkah 4: Penimbangan Berat Nasi Matang (Yield)</strong>
                    <p class="text-xs sm:text-sm text-slate-600">Aduk rata nasi, lalu timbang seluruh nasi matang. Hitung angka <em>Cooking Yield Multiplier</em> = Berat Nasi (g) &divide; 1.000g. Beras premium berkualitas tinggi wajib menghasilkan minimal 2.200g &ndash; 2.400g nasi matang (yield 2.2x &ndash; 2.4x).</p>
                  </div>
                  <div class="bg-white p-4 rounded-xl border border-slate-200">
                    <strong class="text-brand-800 text-sm block mb-1">Langkah 5: Uji Ketahanan 24 Jam di Rice Warmer</strong>
                    <p class="text-xs sm:text-sm text-slate-600">Simpan nasi di rice warmer pada suhu standar 65&ndash;70&deg;C. Amati pada jam ke-6, ke-12, ke-18, dan ke-24. Beras alami bebas pemutih kimiawi seperti Beras Ladori akan tetap lembut, harum segar, dan tidak berlendir setelah 24 jam pemanasan.</p>
                  </div>
                </div>
                """
            },
            {
                "h2": "3. Fasilitas Sampel Uji Tanak Gratis Beras Ladori",
                "content": """
                <p>Kami sangat mendukung uji independen di dapur Anda. Beras Ladori menyediakan paket sampel tester 1&ndash;2 kg bagi katering, hotel, restoran, pondok pesantren, dan SPPG di wilayah Muntilan, Magelang, Sleman, Yogyakarta, dan Temanggung. Hubungi kami untuk menjadwalkan pengiriman sampel ke alamat dapur Anda.</p>
                """
            }
        ],
        "related_links": [
            {"title": "Cara Menghitung Cooking Yield & Rendemen Nasi Dapur B2B", "href": "/artikel/cara-menghitung-cooking-yield-beras"},
            {"title": "5 Cara Membedakan Beras Alami vs Beras Berpemutih Kimia", "href": "/artikel/cara-membedakan-beras-pulen-alami-bebas-pemutih"},
            {"title": "Cara Membandingkan 2 Supplier Beras Secara Adil & Akurat", "href": "/artikel/cara-membandingkan-supplier-beras"},
            {"title": "Spesifikasi Lengkap Beras Ladori 25 kg", "href": "/produk/beras-ladori-25kg"},
            {"title": "Hub Distribusi Wilayah Sleman", "href": "/wilayah/sleman"}
        ]
    },
    {
        "id": 4,
        "slug": "cara-membandingkan-supplier-beras",
        "title": "Cara Membandingkan 2 Supplier Beras Secara Adil & Akurat",
        "h1": "Cara Membandingkan Dua Supplier Beras B2B Secara Adil Menggunakan Matriks Kuantitatif",
        "category": "Audit & Kualifikasi Vendor",
        "badge": "⚖️ Analisis Komparasi B2B",
        "read_time": "7 Menit",
        "description": "Matriks perbandingan supplier beras B2B secara adil: hitung biaya riil per porsi nasi matang, persentase broken, ketepatan jadwal armada, dan MOQ.",
        "keywords": "membandingkan supplier beras, komparasi vendor beras, perbandingan harga beras b2b, audit supplier beras catering",
        "direct_answer": "Membandingkan dua calon supplier beras secara adil wajib menggunakan metrik terstandarisasi: normalisasi biaya porsi matang (bukan harga beli karung), persentase butir patah (broken ratio), ambang batas kadar air (&le; 13.8%), kebijakan MOQ & ongkos kirim, serta garansi retur (SLA). Supplier dengan harga Rp 500/kg lebih mahal sering kali menghemat biaya operasional hingga belasan juta rupiah per bulan berkat tingginya rendemen dan nol karung terbuang.",
        "sections": [
            {
                "h2": "1. Kesalahan Umum Saat Membandingkan Penawaran Supplier",
                "content": """
                <p>Ketika bagian purchasing menerima proposal dari dua distributor beras, tabel komparasi yang dibuat sering kali hanya mencantumkan kolom: <em>Nama Supplier, Jenis Beras, dan Harga per Kg</em>. Ini adalah perbandingan semu yang menyesatkan.</p>
                <p>Dalam ilmu <em>Supply Chain Economics</em>, komoditas bahan pangan curah memiliki variabel laten yang sangat memengaruhi laba bersih dapur: tingkat penyusutan kadar air, persentase menir/batu yang harus dibuang koki, serta kemampuan butir menyerap air saat ditanak.</p>
                """
            },
            {
                "h2": "2. Studi Kasus Riil: Supplier A vs Supplier B (Beras Ladori)",
                "content": """
                <p>Berikut adalah contoh audit nyata perbandingan dua supplier beras untuk katering berkapasitas produksi 1.000 porsi per hari (30.000 porsi/bulan):</p>
                <div class="overflow-x-auto my-4">
                  <table class="w-full text-left border-collapse border border-slate-200 text-xs sm:text-sm bg-white rounded-xl shadow-sm">
                    <thead>
                      <tr class="bg-slate-100 text-slate-900 border-b border-slate-200">
                        <th class="p-3 font-bold">Variabel Evaluasi</th>
                        <th class="p-3 font-bold text-red-700">Supplier A (Pasar Curah)</th>
                        <th class="p-3 font-bold text-brand-800">Supplier B (Beras Ladori)</th>
                      </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 text-slate-700">
                      <tr>
                        <td class="p-3 font-semibold">Harga Beli Mentah</td>
                        <td class="p-3 text-red-700 font-bold">Rp 13.700 / kg</td>
                        <td class="p-3 text-brand-800 font-bold">Rp 14.200 / kg</td>
                      </tr>
                      <tr>
                        <td class="p-3 font-semibold">Kadar Air (Moisture)</td>
                        <td class="p-3">14.8% (Lembab, susut tinggi)</td>
                        <td class="p-3">13.5% (Kering giling stabil)</td>
                      </tr>
                      <tr>
                        <td class="p-3 font-semibold">Butir Patah (Broken)</td>
                        <td class="p-3">22% (Banyak menir)</td>
                        <td class="p-3">&le; 10% (Dominan kepala)</td>
                      </tr>
                      <tr>
                        <td class="p-3 font-semibold">Cooking Yield Multiplier</td>
                        <td class="p-3">1.95x</td>
                        <td class="p-3">2.35x</td>
                      </tr>
                      <tr>
                        <td class="p-3 font-semibold">Porsi Nasi per kg (150g)</td>
                        <td class="p-3">13.0 porsi</td>
                        <td class="p-3">15.66 porsi</td>
                      </tr>
                      <tr class="bg-brand-50/50">
                        <td class="p-3 font-semibold">Biaya Riil per Porsi Nasi</td>
                        <td class="p-3 text-red-700 font-bold">Rp 1.053 / porsi</td>
                        <td class="p-3 text-brand-800 font-bold">Rp 906 / porsi</td>
                      </tr>
                      <tr class="bg-brand-100/60 font-bold text-slate-900">
                        <td class="p-3">Total Biaya Bulanan (30.000 porsi)</td>
                        <td class="p-3 text-red-700">Rp 31.590.000</td>
                        <td class="p-3 text-brand-800">Rp 27.180.000</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <div class="bg-emerald-50 border border-emerald-300 p-4 rounded-xl my-4 text-xs sm:text-sm text-emerald-900">
                  <strong>Kesimpulan Analisis Data:</strong> Meskipun harga mentah Supplier B tampak lebih mahal Rp 500/kg di awal, efisiensi rendemennya menghemat <strong>Rp 4.410.000 per bulan</strong> (penghematan 14% dari total biaya beras)!
                </div>
                """
            },
            {
                "h2": "3. Terapkan Lembar Uji Komparasi Sebelum Memutuskan",
                "content": """
                <p>Jangan biarkan emosi atau kedekatan personal menentukan keputusan procurement Anda. Lakukan uji tanak paralel berdampingan (*side-by-side cooking test*) menggunakan sampel dari kedua supplier. Bandingkan aroma, ketahanan nasi di pemanas hingga sore hari, dan tingkat kepuasan pelanggan Anda.</p>
                """
            }
        ],
        "related_links": [
            {"title": "Total Cost of Ownership Beras Dapur Komersial", "href": "/artikel/total-cost-beras-dapur-komersial"},
            {"title": "Cara Menghitung Cooking Yield & Rendemen Nasi Dapur B2B", "href": "/artikel/cara-menghitung-cooking-yield-beras"},
            {"title": "Cara Memilih Supplier Beras B2B untuk Dapur Komersial", "href": "/artikel/cara-memilih-supplier-beras-b2b"},
            {"title": "Daftar Harga Resmi Beras Ladori 25 kg", "href": "/artikel/daftar-harga-beras-ladori-25kg"},
            {"title": "Layanan Pengadaan Beras Wilayah Kota Jogja", "href": "/wilayah/jogja"}
        ]
    },
    {
        "id": 5,
        "slug": "total-cost-beras-dapur-komersial",
        "title": "Total Cost of Ownership Beras: Jangan Tertipu Murah",
        "h1": "Total Cost of Ownership (TCO) Beras Dapur Komersial: Mengapa Beras Murah Bisa Membuat Bangkrut",
        "category": "Kalkulasi Ekonomi Dapur",
        "badge": "💰 Kalkulasi Finansial",
        "read_time": "8 Menit",
        "description": "Analisis TCO pengadaan beras dapur komersial. Mengapa beras murah kadar air tinggi dan patah banyak justru membuat biaya per porsi nasi membengkak.",
        "keywords": "total cost beras komersial, tco pengadaan beras, biaya porsi nasi katering, food cost beras restoran, efisiensi beras dapur",
        "direct_answer": "Total Cost of Ownership (TCO) beras komersial adalah penjumlahan biaya pembelian, biaya penyusutan kadar air (moisture loss), biaya limbah benda asing/menir, biaya nasi terbuang akibat cepat basi, dan biaya logistik darurat. Beras murah berkadar air tinggi dan banyak patahan memiliki TCO hingga 20% lebih mahal dibandingkan beras premium berkadar air stabil 13.5% yang mekar sempurna.",
        "sections": [
            {
                "h2": "1. Anatomi Biaya Tersembunyi pada Beras Murahan",
                "content": """
                <p>Dalam akuntansi biaya dapur profesional, harga yang tercantum di faktur supplier hanyalah puncak gunung es (<em>the tip of the iceberg</em>). Biaya riil yang menggerus profitabilitas usaha kuliner Anda bersembunyi di bawah permukaan operasi dapur harian:</p>
                <ul class="list-disc pl-5 space-y-2 text-xs sm:text-sm text-slate-600 my-3">
                  <li><strong>Biaya Air Terbungkus (Susut Bobot):</strong> Jika beras dibeli dengan kadar air 15.5% (di atas batas SNI 14%), Anda membayar harga beras untuk ratusan liter air. Selama penyimpanan seminggu di gudang, bobot karung menyusut 1&ndash;2% akibat penguapan alami.</li>
                  <li><strong>Biaya Tenaga Kerja Sortir:</strong> Beras kotor yang mengandung kerikil atau gabah memaksa koki meluangkan waktu 30&ndash;45 menit setiap hari untuk menampi dan memilah beras.</li>
                  <li><strong>Biaya Nasi Terbuang (Basi Cepat):</strong> Beras dengan residu pemutih atau kadar amilopektin hancur cenderung berair di rice warmer setelah 10 jam. Nasi sisa siang terpaksa dibuang karena sudah berlendir saat jam makan malam.</li>
                  <li><strong>Biaya Pembelian Darurat (Emergency Purchase):</strong> Supplier tanpa jadwal rute tetap sering membuat dapur kehabisan stok, memaksa manajer membeli eceran di warung terdekat dengan harga 25% lebih tinggi.</li>
                </ul>
                """
            },
            {
                "h2": "2. Formula Matematis Total Cost of Ownership Beras",
                "content": """
                <div class="bg-slate-900 text-slate-100 p-5 rounded-2xl my-4 text-xs sm:text-sm font-mono space-y-2">
                  <p class="text-gold-400 font-bold">// FORMULA TCO PENGADAAN BERAS KOMERSIAL</p>
                  <p>TCO = C<sub>beli</sub> + C<sub>susut</sub> + C<sub>sortir</sub> + C<sub>basi</sub> + C<sub>logistik</sub></p>
                  <p class="text-slate-400">Dimana:</p>
                  <ul class="list-disc pl-5 text-slate-300 space-y-1">
                    <li>C<sub>beli</sub> = Volume Beras (kg) &times; Harga per kg</li>
                    <li>C<sub>susut</sub> = Kerugian susut kadar air & rendemen rendah vs benchmark</li>
                    <li>C<sub>sortir</sub> = Jam kerja staf &times; Upah per jam untuk pembersihan beras</li>
                    <li>C<sub>basi</sub> = Nilai nasi matang yang dibuang akibat basi sebelum saji</li>
                    <li>C<sub>logistik</sub> = Biaya pengiriman ad-hoc atau selisih harga eceran darurat</li>
                  </ul>
                </div>
                """
            },
            {
                "h2": "3. Studi Efisiensi: Beralih ke Standar Beras Ladori 25 kg",
                "content": """
                <p>Beras Ladori 25 kg diformulasikan khusus untuk menekan seluruh elemen biaya tersembunyi tersebut hingga mendekati nol:</p>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 my-4">
                  <div class="bg-white p-4 rounded-xl border border-slate-200 text-center">
                    <span class="text-2xl font-black text-brand-700 block">13.2% - 13.8%</span>
                    <span class="text-xs text-slate-600 mt-1 block">Kadar air stabil: Nol susut timbangan gudang</span>
                  </div>
                  <div class="bg-white p-4 rounded-xl border border-slate-200 text-center">
                    <span class="text-2xl font-black text-brand-700 block">100% De-Stoned</span>
                    <span class="text-xs text-slate-600 mt-1 block">Bebas batu & kerikil: Siap masak tanpa sortir</span>
                  </div>
                  <div class="bg-white p-4 rounded-xl border border-slate-200 text-center">
                    <span class="text-2xl font-black text-brand-700 block">&gt; 24 Jam</span>
                    <span class="text-xs text-slate-600 mt-1 block">Ketahanan di warmer: Nol nasi basi terbuang</span>
                  </div>
                </div>
                <p>Hasilnya: margin katering Anda terlindungi dan operasional berjalan tenang tanpa komplain pelanggan.</p>
                """
            }
        ],
        "related_links": [
            {"title": "Cara Membandingkan 2 Supplier Beras Secara Adil & Akurat", "href": "/artikel/cara-membandingkan-supplier-beras"},
            {"title": "Cara Menghitung Cooking Yield & Rendemen Nasi Dapur B2B", "href": "/artikel/cara-menghitung-cooking-yield-beras"},
            {"title": "Supplier Beras Catering: Kunci Food Cost & Nasi Pulen", "href": "/artikel/supplier-beras-catering-food-cost-konsistensi"},
            {"title": "Program Pasokan Beras Dapur Katering & Horeka", "href": "/program/katering-horeka"},
            {"title": "Distributor Resmi Beras Magelang", "href": "/wilayah/magelang"}
        ]
    }
]
