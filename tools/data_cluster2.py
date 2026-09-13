# -*- coding: utf-8 -*-
"""
Kluster 2: Kalkulasi Ekonomi, Yield & Manajemen Stok (Artikel 06 - 09)
Standar Data Science: Cooking Thermodynamics, Yield Ratio, Inventory Operations Research (SS, ROP, MOQ)
"""

cluster2_articles = [
    {
        "id": 6,
        "slug": "cara-menghitung-cooking-yield-beras",
        "title": "Cara Menghitung Cooking Yield & Rendemen Nasi Dapur B2B",
        "h1": "Formula Matematis Menghitung Cooking Yield & Rasio Rendemen Nasi Dapur B2B",
        "category": "Sains Kuliner & Yield",
        "badge": "📊 Formula Sains Kuliner",
        "read_time": "8 Menit",
        "description": "Formula matematis menghitung cooking yield beras. Ketahui rendemen nasi matang per kg, konversi porsi katering 150g, dan pengaruh kadar amilosa bulir.",
        "keywords": "cara menghitung cooking yield beras, rendemen nasi per kg, porsi nasi 1 kg beras, yield multiplier beras, porsi katering",
        "direct_answer": "Cooking Yield Beras adalah rasio perbandingan berat nasi matang terhadap berat beras mentah sebelum dimasak: Yield Multiplier = Berat Nasi Matang (kg) / Berat Beras Mentah (kg). Beras premium beramilosa sedang (20%–24%) seperti Beras Ladori memiliki yield multiplier 2.2x hingga 2.4x. Artinya, 1 kg beras mentah menghasilkan 2.2–2.4 kg nasi matang, atau setara dengan 14.6 hingga 16 porsi nasi katering standar (150 gram per porsi).",
        "sections": [
            {
                "h2": "1. Sains di Balik Rendemen: Mengapa Beras Bisa Mengembang Berbeda",
                "content": """
                <p>Dalam ilmu teknologi pangan, kemampuan bulir beras menyerap air panas dan mengembang disebut proses <em>gelatinisasi pati</em>. Struktur pati beras terdiri dari dua polimer utama: <strong>amilosa</strong> (rantai lurus) dan <strong>amilopektin</strong> (rantai bercabang).</p>
                <p>Beras dengan amilosa rendah (&lt; 18%) seperti beras ketan cenderung menyerap sedikit air dan menghasilkan nasi sangat lengket. Sebaliknya, beras dengan amilosa tinggi (&gt; 25%) mengembang sangat besar namun nasinya mengeras saat dingin. Beras Ladori dikurasi pada kadar amilosa optimal <strong>20%&ndash;24%</strong> (karakter pulen mekar alami), memberikan volume penyerapan air optimal (yield multiplier 2.2x&ndash;2.4x) dengan tekstur lembut yang tetap empuk setelah 24 jam.</p>
                """
            },
            {
                "h2": "2. Tabel Konversi Rendemen Beras Mentah ke Porsi Saji",
                "content": """
                <p>Berikut tabel referensi perhitungan porsi nasi matang berbasis ukuran porsi standar katering dan instansi (150 gram nasi matang per piring/kotak):</p>
                <div class="overflow-x-auto my-4">
                  <table class="w-full text-left border-collapse border border-slate-200 text-xs sm:text-sm bg-white rounded-xl shadow-sm">
                    <thead>
                      <tr class="bg-brand-50 text-brand-900 border-b border-slate-200">
                        <th class="p-3 font-bold">Volume Beras Mentah</th>
                        <th class="p-3 font-bold">Nasi Matang Rendah (Yield 1.9x)</th>
                        <th class="p-3 font-bold text-brand-800">Nasi Matang Ladori (Yield 2.35x)</th>
                        <th class="p-3 font-bold text-brand-800">Porsi Saji Standar (150g)</th>
                      </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 text-slate-700">
                      <tr>
                        <td class="p-3 font-semibold">1 kg Beras</td>
                        <td class="p-3 text-slate-500">1.90 kg (12.6 porsi)</td>
                        <td class="p-3 font-bold text-brand-700">2.35 kg</td>
                        <td class="p-3 font-bold text-brand-700">15.6 &ndash; 16 Porsi</td>
                      </tr>
                      <tr>
                        <td class="p-3 font-semibold">1 Karung (25 kg)</td>
                        <td class="p-3 text-slate-500">47.50 kg (316 porsi)</td>
                        <td class="p-3 font-bold text-brand-700">58.75 kg</td>
                        <td class="p-3 font-bold text-brand-700">391 Porsi (+75 porsi)</td>
                      </tr>
                      <tr>
                        <td class="p-3 font-semibold">4 Karung (100 kg)</td>
                        <td class="p-3 text-slate-500">190.0 kg (1.266 porsi)</td>
                        <td class="p-3 font-bold text-brand-700">235.0 kg</td>
                        <td class="p-3 font-bold text-brand-700">1.566 Porsi (+300 porsi)</td>
                      </tr>
                      <tr class="bg-brand-50/50 font-bold">
                        <td class="p-3">1 Ton (1.000 kg)</td>
                        <td class="p-3 text-slate-500">1.900 kg (12.666 porsi)</td>
                        <td class="p-3 text-brand-800">2.350 kg</td>
                        <td class="p-3 text-brand-800">15.666 Porsi (+3.000 porsi)</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <div class="bg-emerald-50 border border-emerald-300 p-4 rounded-xl my-4 text-xs sm:text-sm text-emerald-900">
                  <strong>Insight Finansial:</strong> Setiap 1 karung Beras Ladori 25 kg menghasilkan surplus <strong>75 porsi nasi</strong> dibanding beras pasar murah. Jika 1 porsi nasi dinilai Rp 2.500 dalam paket menu, Anda memperoleh nilai tambah <strong>Rp 187.500 per karung</strong>!
                </div>
                """
            },
            {
                "h2": "3. Standarisasi SOP Dapur untuk Memaksimalkan Yield",
                "content": """
                <p>Untuk mencapai yield multiplier konsisten 2.3x&ndash;2.4x, instruksikan tim juru masak dapur Anda untuk menerapkan SOP berikut:</p>
                <ol class="list-decimal pl-5 space-y-2 text-xs sm:text-sm text-slate-600 my-3">
                  <li><strong>Gunakan Air Dingin Bersih:</strong> Hindari mencuci beras menggunakan air hangat karena memicu pelepasan pati permukaan prematur.</li>
                  <li><strong>Rasio Air Tepat (1:1.2 &ndash; 1:1.3):</strong> Untuk Beras Ladori, rasio air 1 bagian beras berbanding 1.25&ndash;1.3 bagian air matang menghasilkan tekstur pulen mekar maksimal.</li>
                  <li><strong>Waktu Resting Tertutup:</strong> Jangan langsung mengaduk nasi begitu matang. Diamkan rice cooker tertutup selama 15 menit agar kristalisasi uap merata sempurna ke tengah bulir.</li>
                </ol>
                """
            }
        ],
        "related_links": [
            {"title": "Total Cost of Ownership Beras Dapur Komersial", "href": "/artikel/total-cost-beras-dapur-komersial"},
            {"title": "Cara Uji Sampel Beras yang Benar Sebelum Kontrak Pasokan", "href": "/artikel/uji-sampel-beras-sebelum-kontrak"},
            {"title": "Spesifikasi Fisik Beras Ladori 25 kg", "href": "/produk/beras-ladori-25kg"},
            {"title": "Pengadaan Beras Dapur SPPG Makan Bergizi Gratis", "href": "/program/sppg-mbg"},
            {"title": "Hub Layanan Pengadaan Sleman", "href": "/wilayah/sleman"}
        ]
    },
    {
        "id": 7,
        "slug": "menentukan-moq-dan-frekuensi-pengiriman-beras",
        "title": "Cara Menentukan MOQ & Frekuensi Kirim Beras yang Efisien",
        "h1": "Cara Mengoptimasi Minimum Order Quantity (MOQ) dan Frekuensi Pengiriman Beras B2B",
        "category": "Manajemen Rantai Pasok",
        "badge": "📦 Optimasi Logistik",
        "read_time": "7 Menit",
        "description": "Optimasi Minimum Order Quantity (MOQ) dan frekuensi kirim beras. Seimbangkan biaya angkut armada vs biaya simpan gudang dan risiko penurunan mutu beras.",
        "keywords": "moq beras grosir, frekuensi pengiriman beras, ukuran order beras b2b, manajemen persediaan beras, biaya simpan gudang",
        "direct_answer": "Menentukan Minimum Order Quantity (MOQ) dan frekuensi kirim beras adalah mencari titik ekuilibrium antara biaya transportasi (ongkos kirim armada) dengan biaya penyimpanan (holding cost, risiko kutu, dan penyusutan susut ruang). Untuk dapur katering dan institusi di koridor Magelang–Jogja, pola pemesanan paling efisien adalah 2–3 kali seminggu dengan ukuran order 10–20 karung (250–500 kg), memaksimalkan perputaran modal kerja tanpa membebani kapasitas gudang.",
        "sections": [
            {
                "h2": "1. Trade-off Klasik: Order Besar Sekaligus vs Order Kecil Sering",
                "content": """
                <p>Banyak pengusaha dapur tergoda membeli beras dalam jumlah sangat besar (misal 5&ndash;10 ton) demi mendapatkan potongan harga beberapa ratus rupiah. Namun, dalam manajemen rantai pasok (<em>Operations Research</em>), menumpuk beras dalam jumlah masif di gudang membawa risiko tersembunyi yang mahal:</p>
                <ul class="list-disc pl-5 space-y-2 text-xs sm:text-sm text-slate-600 my-3">
                  <li><strong>Modal Kerja Mandek (Working Capital Tie-Up):</strong> Jutaan rupiah dana tunai membeku dalam bentuk tumpukan karung, mengurangi fleksibilitas arus kas operasional harian.</li>
                  <li><strong>Risiko Infestasi Hama Gudang:</strong> Beras alami tanpa pestisida kimiawi rentan dihinggapi kutu beras (*Sitophilus oryzae*) jika disimpan di ruangan lembab lebih dari 30 hari.</li>
                  <li><strong>Beban Ruang Gudang:</strong> Karung beras menyita luas lantai berharga yang seharusnya bisa digunakan untuk preparasi masak atau penyimpanan bahan segar lainnya.</li>
                </ul>
                """
            },
            {
                "h2": "2. Matriks Penentuan Frekuensi Pengiriman Berdasarkan Konsumsi",
                "content": """
                <p>Gunakan matriks operasional berikut untuk menyelaraskan frekuensi pemesanan dengan kapasitas konsumsi dapur Anda:</p>
                <div class="overflow-x-auto my-4">
                  <table class="w-full text-left border-collapse border border-slate-200 text-xs sm:text-sm bg-white rounded-xl shadow-sm">
                    <thead>
                      <tr class="bg-brand-50 text-brand-900 border-b border-slate-200">
                        <th class="p-3 font-bold">Skala Konsumsi Harian</th>
                        <th class="p-3 font-bold">Profil Dapur Tipikal</th>
                        <th class="p-3 font-bold">Frekuensi Kirim Ideal</th>
                        <th class="p-3 font-bold text-brand-800">Ukuran Order Optimal (Beras Ladori)</th>
                      </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 text-slate-700">
                      <tr>
                        <td class="p-3 font-semibold">50 &ndash; 100 kg / hari</td>
                        <td class="p-3">Restoran, Warung Makan, Katering Kecil</td>
                        <td class="p-3">1 &ndash; 2 kali / minggu</td>
                        <td class="p-3 font-bold text-brand-700">10 &ndash; 15 Karung (250 &ndash; 375 kg)</td>
                      </tr>
                      <tr>
                        <td class="p-3 font-semibold">150 &ndash; 300 kg / hari</td>
                        <td class="p-3">Unit Dapur SPPG MBG, Katering Pernikahan</td>
                        <td class="p-3">2 &ndash; 3 kali / minggu</td>
                        <td class="p-3 font-bold text-brand-700">20 &ndash; 36 Karung (500 &ndash; 900 kg)</td>
                      </tr>
                      <tr>
                        <td class="p-3 font-semibold">&gt; 500 kg / hari</td>
                        <td class="p-3">Pondok Pesantren Besar, RS Rujukan</td>
                        <td class="p-3">3 kali / minggu (Jadwal Tetap)</td>
                        <td class="p-3 font-bold text-brand-700">40 &ndash; 80 Karung (1 &ndash; 2 Ton)</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "h2": "3. Fasilitas Rute Reguler Beras Ladori Koridor Magelang–Jogja",
                "content": """
                <p>Karena Beras Ladori mengoperasikan armada rute terjadwal di sepanjang koridor Muntilan, Magelang, Sleman, Yogyakarta, dan Temanggung, mitra B2B kami tidak perlu menanggung risiko stok menumpuk. Anda dapat menikmati fasilitas <strong>pengiriman gratis ongkir</strong> dengan MOQ fleksibel mulai dari 10 karung (250 kg) sesuai jadwal rute reguler kami.</p>
                """
            }
        ],
        "related_links": [
            {"title": "Menghitung Safety Stock Beras Dapur Komersial & SPPG", "href": "/artikel/safety-stock-beras-dapur-komersial"},
            {"title": "Rumus Reorder Point Beras Dapur B2B Cegah Stok Kosong", "href": "/artikel/reorder-point-beras"},
            {"title": "Mengapa Jadwal Rute Kirim Beras Sama Pentingnya Harga", "href": "/artikel/mengapa-jadwal-rute-supplier-beras-penting"},
            {"title": "Koridor Pasokan Beras Muntilan-Magelang-Sleman-Jogja", "href": "/artikel/koridor-pasokan-beras-muntilan-magelang-sleman-jogja"},
            {"title": "Gudang Basis Muntilan", "href": "/wilayah/muntilan"}
        ]
    },
    {
        "id": 8,
        "slug": "safety-stock-beras-dapur-komersial",
        "title": "Menghitung Safety Stock Beras Dapur Komersial & SPPG",
        "h1": "Formula Ilmiah Menghitung Safety Stock (Persediaan Pengaman) Beras Dapur B2B",
        "category": "Manajemen Rantai Pasok",
        "badge": "🛡️ Manajemen Risiko Stok",
        "read_time": "8 Menit",
        "description": "Panduan menghitung safety stock beras dapur komersial. Rumus persediaan pengaman saat fluktuasi order hajatan dan keterlambatan armada logistik beras.",
        "keywords": "safety stock beras, persediaan pengaman beras, stok buffer beras, rumus safety stock dapur, manajemen risiko dapur",
        "direct_answer": "Safety Stock (persediaan pengaman) beras adalah jumlah cadangan beras minimum yang wajib ada di gudang dapur untuk mengantisipasi lonjakan permintaan mendadak atau keterlambatan pengiriman armada supplier. Rumus praktis operasional dapur komersial: Safety Stock = (Konsumsi Maksimum Harian x Lead Time Maksimum) - (Konsumsi Rata-rata Harian x Lead Time Rata-rata). Untuk dapur berkapasitas 200 kg/hari dengan lead time 2 hari, cadangan aman ideal adalah sekitar 200–250 kg (8–10 karung 25kg).",
        "sections": [
            {
                "h2": "1. Bahaya Dua Sisi: Krisis Stok Kosong vs Stok Berlebih",
                "content": """
                <p>Dalam operasional dapur komersial, kehabisan beras di tengah sesi memasak adalah bencana mutlak: pesanan nasi box terlambat, reputasi katering rusak seketika, dan manajemen panik mencari beras substitusi di warung terdekat yang belum tentu cocok rasanya.</p>
                <p>Di sisi lain, menyimpan terlalu banyak beras berisiko mengundang kutu dan menurunkan kesegaran nasi. Menghitung <em>Safety Stock</em> (SS) secara kuantitatif memberikan kepastian operasional: dapur memiliki benteng pertahanan tanpa harus menyulap dapur menjadi gudang logistik raksasa.</p>
                """
            },
            {
                "h2": "2. Langkah Menghitung Formula Safety Stock Dapur",
                "content": """
                <div class="bg-slate-100 p-4 rounded-xl border border-slate-200 my-4 text-xs sm:text-sm font-mono text-slate-800">
                  <strong>FORMULA PRAKTIS SAFETY STOCK DAPUR:</strong><br>
                  SS = (D<sub>max</sub> &times; L<sub>max</sub>) &minus; (D<sub>avg</sub> &times; L<sub>avg</sub>)<br><br>
                  <em>Keterangan Parameter:</em><br>
                  &bull; D<sub>max</sub> = Pemakaian beras harian tertinggi saat beban puncak (peak demand)<br>
                  &bull; L<sub>max</sub> = Waktu tunggu terlama jika pengiriman supplier terhambat macet/hujan<br>
                  &bull; D<sub>avg</sub> = Pemakaian beras harian pada kondisi normal rata-rata<br>
                  &bull; L<sub>avg</sub> = Waktu tunggu normal pengiriman supplier
                </div>
                <div class="bg-white p-5 rounded-xl border border-slate-200 my-4 space-y-2 text-xs sm:text-sm text-slate-700">
                  <h4 class="font-bold text-slate-900">Simulasi Kasus Dapur Katering Hajatan di Sleman:</h4>
                  <p>&bull; Pemakaian normal (D<sub>avg</sub>) = 150 kg/hari (6 karung @ 25kg)<br>
                  &bull; Pemakaian puncak saat akhir pekan (D<sub>max</sub>) = 250 kg/hari (10 karung @ 25kg)<br>
                  &bull; Lead time normal supplier (L<sub>avg</sub>) = 1 hari<br>
                  &bull; Lead time maksimal jika ada kendala armada (L<sub>max</sub>) = 2 hari</p>
                  <p class="font-mono font-bold text-brand-800 pt-1">
                    Kalkulasi: SS = (250 &times; 2) &minus; (150 &times; 1) = 500 &minus; 150 = <strong>350 kg (14 Karung 25kg)</strong>
                  </p>
                  <p class="text-xs text-slate-500">Dengan menyiagakan cadangan pengaman 14 karung di atas palet kayu, dapur dijamin tidak akan pernah mengalami krisis kehabisan bahan baku dalam skenario terburuk sekalipun.</p>
                </div>
                """
            },
            {
                "h2": "3. Integrasikan Safety Stock dengan Mitra Terpercaya",
                "content": """
                <p>Keberhasilan safety stock sangat bergantung pada kepastian lead time supplier. Distributor resmi Beras Ladori menjamin stok buffer ratusan ton selalu siap di hub Muntilan dan Magelang Tengah, memastikan pesanan pengaman Anda selalu dapat dipenuhi secara presisi.</p>
                """
            }
        ],
        "related_links": [
            {"title": "Rumus Reorder Point Beras Dapur B2B Cegah Stok Kosong", "href": "/artikel/reorder-point-beras"},
            {"title": "Cara Menentukan MOQ & Frekuensi Kirim Beras yang Efisien", "href": "/artikel/menentukan-moq-dan-frekuensi-pengiriman-beras"},
            {"title": "10 Checklist QC Beras Masuk Gudang: Standar Dapur B2B", "href": "/artikel/checklist-qc-beras-masuk-gudang"},
            {"title": "Layanan Pengadaan Beras Wilayah Magelang", "href": "/wilayah/magelang"},
            {"title": "Program Pasokan Beras Dapur SPPG MBG", "href": "/program/sppg-mbg"}
        ]
    },
    {
        "id": 9,
        "slug": "reorder-point-beras",
        "title": "Rumus Reorder Point Beras Dapur B2B Cegah Stok Kosong",
        "h1": "Formula Reorder Point (ROP) Beras untuk Mencegah Krisis Kehabisan Stok di Dapur B2B",
        "category": "Manajemen Rantai Pasok",
        "badge": "⏱️ Manajemen Inventory Presisi",
        "read_time": "7 Menit",
        "description": "Formula Reorder Point (ROP) beras dapur B2B. Ketahui kapan tepatnya PO beras harus diterbitkan agar dapur tidak pernah kehabisan stok beras mendadak.",
        "keywords": "reorder point beras, rumus rop beras, titik pemesanan ulang beras, manajemen persediaan beras dapur, rop katering",
        "direct_answer": "Reorder Point (ROP) adalah batas sisa stok fisik di gudang di mana tim purchasing harus segera menerbitkan Purchase Order (PO) beras baru ke supplier. Rumus ilmiahnya: ROP = (Konsumsi Harian Rata-rata x Lead Time Pengiriman) + Safety Stock. Jika sebuah dapur memakai 200 kg beras per hari, lead time pengiriman 2 hari, dan safety stock 250 kg, maka ROP = (200 x 2) + 250 = 650 kg (26 karung 25kg). Ketika sisa stok tersisa 26 karung, PO wajib segera dikirim.",
        "sections": [
            {
                "h2": "1. Kapan Harus Mengorder Lagi: Menghilangkan Tebak-tebakan",
                "content": """
                <p>Banyak dapur katering dan restoran memesan beras menggunakan perasaan: <em>"Tampaknya karung di gudang sudah tinggal sedikit, mari telepon supplier besok."</em> Kebiasaan ini adalah pemicu utama pembelian panik darurat dengan harga mahal saat supplier ternyata tidak bisa langsung mengirim pada hari yang sama.</p>
                <p>Dalam ilmu operasional pergudangan, titik pemesanan ulang (<strong>Reorder Point / ROP</strong>) adalah trigger otomatis yang menghilangkan ketergantungan pada intuisi. Sisa stok di angka tertentu memicu tindakan pemesanan tanpa menunggu gudang kosong.</p>
                """
            },
            {
                "h2": "2. Diagram Alur & Rumus Reorder Point",
                "content": """
                <div class="bg-slate-900 text-slate-100 p-5 rounded-2xl my-4 text-xs sm:text-sm font-mono space-y-2">
                  <p class="text-gold-400 font-bold">// FORMULA REORDER POINT (ROP) BERAS</p>
                  <p class="text-base font-bold text-white">ROP = (D &times; L) + SS</p>
                  <p class="text-slate-400 pt-2">Dimana:</p>
                  <ul class="list-disc pl-5 text-slate-300 space-y-1">
                    <li><strong>D (Demand):</strong> Rata-rata pemakaian beras harian (kg/hari)</li>
                    <li><strong>L (Lead Time):</strong> Waktu sejak PO diterbitkan hingga beras tiba di gudang (hari)</li>
                    <li><strong>SS (Safety Stock):</strong> Persediaan cadangan pengaman hasil kalkulasi (kg)</li>
                  </ul>
                </div>
                <div class="bg-white p-5 rounded-xl border border-slate-200 my-4 space-y-3 text-xs sm:text-sm text-slate-700">
                  <h4 class="font-bold text-slate-900">Simulasi Nyata Unit Dapur SPPG MBG (3.000 Penerima Manfaat):</h4>
                  <p>&bull; Kebutuhan harian (D) = 270 kg/hari (kurang lebih 11 karung @ 25kg)<br>
                  &bull; Lead time supplier Beras Ladori (L) = 1 hari kerja<br>
                  &bull; Safety Stock dapur (SS) = 270 kg (cadangan 1 hari penuh)</p>
                  <div class="p-3 bg-brand-50 rounded-lg text-brand-900 font-mono font-bold">
                    ROP = (270 &times; 1) + 270 = 540 kg (sekitar 21&ndash;22 karung 25kg)
                  </div>
                  <p class="text-xs text-slate-500">Artinya: Begitu petugas gudang melihat stok di atas palet tersisa 22 karung, saat itu juga PO pemesanan batch berikutnya wajib diterbitkan ke distributor Beras Ladori.</p>
                </div>
                """
            },
            {
                "h2": "3. Sinkronisasi ROP dengan Jadwal Rute Mingguan",
                "content": """
                <p>Mengintegrasikan ROP dengan hari kedatangan armada Beras Ladori (misal rute hari Selasa & Jumat) akan membuat dapur Anda beroperasi seperti jam mekanis yang presisi: modal kerja efisien, beras selalu segar gilingan baru, dan risiko dapur mogok sama dengan nol.</p>
                """
            }
        ],
        "related_links": [
            {"title": "Menghitung Safety Stock Beras Dapur Komersial & SPPG", "href": "/artikel/safety-stock-beras-dapur-komersial"},
            {"title": "Cara Menentukan MOQ & Frekuensi Kirim Beras yang Efisien", "href": "/artikel/menentukan-moq-dan-frekuensi-pengiriman-beras"},
            {"title": "SOP Penerimaan Beras di Loading Dock Dapur Komersial", "href": "/artikel/sop-penerimaan-beras-dapur-b2b"},
            {"title": "Spesifikasi Pasokan Dapur SPPG Makan Bergizi Gratis", "href": "/program/sppg-mbg"},
            {"title": "Layanan Pengadaan Beras Wilayah Temanggung", "href": "/wilayah/temanggung"}
        ]
    }
]
