# -*- coding: utf-8 -*-
"""
Kluster 3: Quality Control, Laboratorium & Traceability (Artikel 10 - 18)
Standar Data Science: ISO 24333 Sampling, SNI 6128:2020, Metrologi Kadar Air, Spektrofotometri COA, Traceability Coding
"""

cluster3_articles = [
    {
        "id": 10,
        "slug": "sop-penerimaan-beras-dapur-b2b",
        "title": "SOP Penerimaan Beras di Loading Dock Dapur Komersial",
        "h1": "Standar Operasional Prosedur (SOP) 5 Langkah Penerimaan Beras di Loading Dock Dapur Komersial",
        "category": "Quality Assurance & SOP",
        "badge": "📋 SOP Operasional Loading Dock",
        "read_time": "8 Menit",
        "description": "Standar Operasional Prosedur (SOP) 5 langkah penerimaan beras di loading dock: periksa surat jalan, hitung karung, uji fisik, suhu, dan pencatatan batch.",
        "keywords": "sop penerimaan beras, prosedur loading dock beras, inspeksi beras masuk, receiving beras dapur, audit gudang beras",
        "direct_answer": "SOP penerimaan beras di loading dock dapur komersial terdiri dari 5 gerbang verifikasi wajib: (1) Verifikasi dokumen surat jalan & kesesuaian nomor PO, (2) Penghitungan fisik karung & penimbangan acak bobot bruto, (3) Inspeksi visual integritas kemasan, segel jahitan, dan bebas kutu, (4) Uji cepat kadar air menggunakan grain moisture meter (&le; 13.8%), serta (5) Pencatatan nomor batch di kartu stok dan penataan di atas palet kayu dengan prinsip FIFO.",
        "sections": [
            {
                "h2": "1. Mengapa Loading Dock Adalah Garis Pertahanan Pertama Dapur Anda",
                "content": """
                <p>Dalam sistem manajemen mutu pangan HACCP (<em>Hazard Analysis Critical Control Point</em>), area penerimaan barang (loading dock) adalah <em>Critical Control Point (CCP)</em> utama untuk bahan baku kering. Begitu karung beras yang basah, apek, atau berkutu lolos masuk ke dalam ruang penyimpanan utama, seluruh persediaan beras di gudang tersebut berisiko terkontaminasi.</p>
                <p>Penerapan SOP 5 langkah yang disiplin memastikan tidak ada kompromi mutu sebelum staf gudang menandatangani surat jalan pengiriman supplier.</p>
                """
            },
            {
                "h2": "2. Alur 5 Gerbang Verifikasi Penerimaan Beras",
                "content": """
                <div class="space-y-4 my-4">
                  <div class="bg-white p-4 rounded-xl border border-slate-200">
                    <strong class="text-brand-800 font-bold block mb-1">Gerbang 1: Verifikasi Dokumen & Surat Jalan Resmi</strong>
                    <p class="text-xs sm:text-sm text-slate-600">Cocokkan nomor Purchase Order (PO) dapur dengan Surat Jalan yang dibawa sopir armada: nama varietas (Beras Ladori 25 kg), jumlah karung, tanggal pengiriman, dan stempel resmi distributor.</p>
                  </div>
                  <div class="bg-white p-4 rounded-xl border border-slate-200">
                    <strong class="text-brand-800 font-bold block mb-1">Gerbang 2: Hitung Fisik & Uji Timbang Bruto Acak</strong>
                    <p class="text-xs sm:text-sm text-slate-600">Hitung total karung yang diturunkan. Ambil minimal 10% karung secara acak dan timbang di atas timbangan lantai digital terkalibrasi. Berat bruto karung 25 kg wajib berada pada rentang 25.05 &ndash; 25.15 kg (berat bersih beras 25.00 kg + bobot karung karung 80&ndash;100g).</p>
                  </div>
                  <div class="bg-white p-4 rounded-xl border border-slate-200">
                    <strong class="text-brand-800 font-bold block mb-1">Gerbang 3: Inspeksi Fisik Kemasan & Jahitan Segel Pabrik</strong>
                    <p class="text-xs sm:text-sm text-slate-600">Pastikan karung tidak bernoda air, tidak berlubang gigitan hewan, dan jahitan mulut karung adalah segel ganda benang orisinal pabrik (bukan jahitan tangan ulang pedagang perantara).</p>
                  </div>
                  <div class="bg-white p-4 rounded-xl border border-slate-200">
                    <strong class="text-brand-800 font-bold block mb-1">Gerbang 4: Uji Cepat Kadar Air (Moisture Meter &le; 13.8%)</strong>
                    <p class="text-xs sm:text-sm text-slate-600">Tusukkan probe moisture meter terkalibrasi. Jika kadar air melebihi batas 14.0%, lot pengiriman berhak ditolak langsung di tempat karena berisiko tinggi membusuk selama penyimpanan.</p>
                  </div>
                  <div class="bg-white p-4 rounded-xl border border-slate-200">
                    <strong class="text-brand-800 font-bold block mb-1">Gerbang 5: Registrasi Batch & Penyusunan Palet FIFO</strong>
                    <p class="text-xs sm:text-sm text-slate-600">Catat kode batch pengiriman pada kartu stok digital/fisik. Susun karung di atas palet kayu (jarak minimal 15 cm dari lantai dan 20 cm dari dinding tembok) menggunakan sistem rotasi <em>First-In, First-Out (FIFO)</em>.</p>
                  </div>
                </div>
                """
            },
            {
                "h2": "3. Transparansi Pengiriman Resmi Beras Ladori",
                "content": """
                <p>Armada Beras Ladori selalu dibekali surat jalan berstempel resmi, sertifikat jaminan mutu lot, dan timbangan digital armada yang siap dikalibrasi bersama staf penerima dapur Anda di lokasi. Kami mendukung penegakan SOP receiving yang ketat demi menjaga standar mutu pangan bersama.</p>
                """
            }
        ],
        "related_links": [
            {"title": "10 Checklist QC Beras Masuk Gudang: Standar Dapur B2B", "href": "/artikel/checklist-qc-beras-masuk-gudang"},
            {"title": "Teknik Sampling Beras Karung Standar ISO 24333 & SNI", "href": "/artikel/cara-sampling-beras-karung"},
            {"title": "Kebijakan Komplain & Retur Supplier Beras: Prosedur B2B", "href": "/artikel/kebijakan-komplain-supplier-beras"},
            {"title": "Standar Dapur SPPG Makan Bergizi Gratis", "href": "/artikel/standar-beras-dapur-sppg-mbg"},
            {"title": "Hub Wilayah Muntilan", "href": "/wilayah/muntilan"}
        ]
    },
    {
        "id": 11,
        "slug": "checklist-qc-beras-masuk-gudang",
        "title": "10 Checklist QC Beras Masuk Gudang: Standar Dapur B2B",
        "h1": "10 Parameter Lembar Checklist Quality Control (QC) Beras Masuk Gudang Komersial",
        "category": "Quality Assurance & SOP",
        "badge": "✅ Lembar Checklist QC",
        "read_time": "8 Menit",
        "description": "10 parameter checklist quality control beras masuk gudang. Deteksi aroma, butir kapur, kerikil, kutu, kadar air, hingga uji kejernihan rendaman beras.",
        "keywords": "checklist qc beras, audit mutu beras, parameter kualitas beras, penerimaan beras gudang, standar fisik beras",
        "direct_answer": "Checklist Quality Control (QC) beras masuk gudang mencakup 10 parameter terukur: kadar air (&le; 13.8%), persentase butir kepala (&ge; 85%), batas butir patah (&le; 12%), butir kapur (< 2%), benda asing/batu (< 0.02%), infestasi hama (0 ekor kutu), aroma gabah segar alami, kejernihan air cucian pertama, kebersihan jahitan karung ganda, serta kelengkapan label nomor batch tanggal produksi.",
        "sections": [
            {
                "h2": "1. Mengapa Lembar Audit QC Tertulis Wajib Ada di Gudang",
                "content": """
                <p>Tanpa lembar audit QC tertulis dengan parameter kuantitatif yang jelas, keputusan menerima atau menolak beras sering kali bergantung pada persepsi subjektif staf loading dock yang berganti-ganti shift. Akibatnya, beras berkualitas rendah kerap lolos ke dapur utama dan baru disadari saat tamu katering melayangkan keluhan rasa nasi.</p>
                <p>Format lembar audit 10 parameter berikut dirancang berbasis <strong>SNI 6128:2020</strong> untuk beras mutu premium siap pakai.</p>
                """
            },
            {
                "h2": "2. Tabel 10 Parameter QC Masuk Gudang Beras Ladori",
                "content": """
                <div class="overflow-x-auto my-4">
                  <table class="w-full text-left border-collapse border border-slate-200 text-xs sm:text-sm bg-white rounded-xl shadow-sm">
                    <thead>
                      <tr class="bg-brand-50 text-brand-900 border-b border-slate-200">
                        <th class="p-3 font-bold">No</th>
                        <th class="p-3 font-bold">Parameter Audit QC</th>
                        <th class="p-3 font-bold">Standar Toleransi Mutu</th>
                        <th class="p-3 font-bold">Metode Uji Cepat</th>
                      </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 text-slate-700">
                      <tr>
                        <td class="p-3">1</td>
                        <td class="p-3 font-semibold">Kadar Air (Moisture Content)</td>
                        <td class="p-3 font-bold text-brand-700">&le; 13.8%</td>
                        <td class="p-3">Grain Moisture Meter terkalibrasi</td>
                      </tr>
                      <tr>
                        <td class="p-3">2</td>
                        <td class="p-3 font-semibold">Butir Kepala (Head Rice)</td>
                        <td class="p-3 font-bold text-brand-700">&ge; 85% &ndash; 88%</td>
                        <td class="p-3">Pemisah grid sampling 100 butir</td>
                      </tr>
                      <tr>
                        <td class="p-3">3</td>
                        <td class="p-3 font-semibold">Butir Patah (Broken Rice)</td>
                        <td class="p-3 font-bold text-brand-700">&le; 10% &ndash; 12%</td>
                        <td class="p-3">Ayakan slot grader 2.0 mm</td>
                      </tr>
                      <tr>
                        <td class="p-3">4</td>
                        <td class="p-3 font-semibold">Butir Menir (Small Broken)</td>
                        <td class="p-3 font-bold text-brand-700">&le; 0.5%</td>
                        <td class="p-3">Ayakan kawat lab</td>
                      </tr>
                      <tr>
                        <td class="p-3">5</td>
                        <td class="p-3 font-semibold">Benda Asing & Kerikil (Stones)</td>
                        <td class="p-3 font-bold text-brand-700">0.00% (Maks &le; 0.02%)</td>
                        <td class="p-3">Uji sebar nampan visual 1 kg</td>
                      </tr>
                      <tr>
                        <td class="p-3">6</td>
                        <td class="p-3 font-semibold">Infestasi Kutu Hidup / Ulat</td>
                        <td class="p-3 font-bold text-brand-700">Nihil (0 Ekor)</td>
                        <td class="p-3">Inspeksi visual lipatan karung</td>
                      </tr>
                      <tr>
                        <td class="p-3">7</td>
                        <td class="p-3 font-semibold">Aroma Bulir Mentah</td>
                        <td class="p-3 font-bold text-brand-700">Segar Khas Gabah Alami</td>
                        <td class="p-3">Uji organoleptik hirup hidung (Bebas Apek/Wangi Kimia)</td>
                      </tr>
                      <tr>
                        <td class="p-3">8</td>
                        <td class="p-3 font-semibold">Kejernihan Cucian Rendaman</td>
                        <td class="p-3 font-bold text-brand-700">Putih Tajin Alami</td>
                        <td class="p-3">Bebas busa klorin & air keruh pekat</td>
                      </tr>
                      <tr>
                        <td class="p-3">9</td>
                        <td class="p-3 font-semibold">Integritas Kemasan Karung</td>
                        <td class="p-3 font-bold text-brand-700">Segel Jahit Pabrik Utuh</td>
                        <td class="p-3">Kerapatan rajutan karung karung PP</td>
                      </tr>
                      <tr>
                        <td class="p-3">10</td>
                        <td class="p-3 font-semibold">Kelengkapan Batch & Tanggal Giling</td>
                        <td class="p-3 font-bold text-brand-700">Tertera Jelas</td>
                        <td class="p-3">Pencatatan kartu stok penerimaan</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "h2": "3. Tindakan Korektif Jika Terjadi Ketidaksesuaian Mutu",
                "content": """
                <p>Jika satu saja dari parameter kritis (kadar air &gt; 14%, terdapat kutu hidup, atau aroma berbau apek/klorin) terdeteksi, tim loading dock wajib membubuhkan stempel <strong>REJECT / DITOLAK</strong> pada surat jalan dan meminta penggantian armada pada hari yang sama sesuai Service Level Agreement (SLA).</p>
                """
            }
        ],
        "related_links": [
            {"title": "SOP Penerimaan Beras di Loading Dock Dapur Komersial", "href": "/artikel/sop-penerimaan-beras-dapur-b2b"},
            {"title": "Cara Memakai Moisture Meter Beras & Koreksi Suhu Akurat", "href": "/artikel/cara-menggunakan-moisture-meter-beras"},
            {"title": "Beras Kepala, Broken, dan Menir: Panduan Purchasing B2B", "href": "/artikel/beras-kepala-broken-menir-untuk-purchasing"},
            {"title": "Tentang Komitmen Mutu Beras Ladori", "href": "/tentang/beras-ladori"},
            {"title": "Spesifikasi Kemasan Beras Ladori 25 kg", "href": "/produk/beras-ladori-25kg"}
        ]
    },
    {
        "id": 12,
        "slug": "cara-sampling-beras-karung",
        "title": "Teknik Sampling Beras Karung Standar ISO 24333 & SNI",
        "h1": "Metodologi Pengambilan Sampel (Sampling) Beras Karung Berbasis Standar ISO 24333 dan SNI",
        "category": "Metrologi & Laboratorium",
        "badge": "🔬 Metodologi Sampling Probabilitas",
        "read_time": "7 Menit",
        "description": "Cara sampling beras karung yang akurat agar hasil uji tidak bias. Gunakan probe tusuk diagonal dan rumus akar karung untuk mewakili seluruh lot kiriman.",
        "keywords": "cara sampling beras karung, teknik sampling beras iso 24333, alat tusuk beras grain trier, sampling acak beras, audit mutu pangan",
        "direct_answer": "Sampling beras karung yang benar harus mewakili seluruh populasi kiriman dan menghindari fenomena stratifikasi butir (butir broken mengendap ke dasar karung). Gunakan rumus ISO 24333: Jumlah Karung Sampel = Akar Kuadrat dari Total Karung + 1. Untuk pengiriman 100 karung, uji 11 karung acak menggunakan alat tusuk beras (grain trier) yang dimasukkan secara diagonal dengan sudut 45 derajat menembus lapisan atas, tengah, dan bawah karung.",
        "sections": [
            {
                "h2": "1. Fenomena Granular Segregation: Mengapa Mengambil Sampel dari Mulut Karung Sangat Menyesatkan",
                "content": """
                <p>Dalam ilmu fisika material butiran (<em>Granular Physics</em>), butir beras yang diangkut menggunakan truk mengalami getaran terus-menerus di jalan raya. Hal ini memicu fenomena <strong>stratifikasi granulasi (percolation effect)</strong>: butir beras kepala yang utuh dan besar cenderung terdorong ke atas, sementara butir broken yang kecil dan menir menyelinap turun ke dasar karung.</p>
                <p>Jika staf Anda hanya mengambil segenggam beras dari mulut karung bagian atas, hasil pengujian akan tampak sangat mulus dan menipu. Begitu karung dituang ke wadah masak, barulah butir patah dan menir terlihat di bagian dasar.</p>
                """
            },
            {
                "h2": "2. Rumus Menentukan Jumlah Karung Sampel (Sample Size)",
                "content": """
                <p>Berdasarkan standar internasional <strong>ISO 24333:2009</strong> (<em>Cereals and cereal products &ndash; Sampling</em>), ukuran sampel acak ditentukan dengan formula:</p>
                <div class="bg-slate-100 p-4 rounded-xl border border-slate-200 my-4 text-xs sm:text-sm font-mono text-slate-800">
                  <strong>FORMULA SAMPLE SIZE ISO 24333:</strong><br>
                  n = &radic;N + 1<br><br>
                  <em>Dimana:</em><br>
                  &bull; n = Jumlah karung yang wajib diambil sampelnya secara acak<br>
                  &bull; N = Total seluruh karung dalam satu surat jalan pengiriman<br><br>
                  <em>Contoh Perhitungan Dapur:</em><br>
                  &bull; Kiriman 16 karung (400 kg) &rarr; &radic;16 + 1 = <strong>5 karung sampel</strong><br>
                  &bull; Kiriman 40 karung (1 ton) &rarr; &radic;40 + 1 &approx; 6.3 + 1 = <strong>7 karung sampel</strong><br>
                  &bull; Kiriman 100 karung (2.5 ton) &rarr; &radic;100 + 1 = <strong>11 karung sampel</strong>
                </div>
                """
            },
            {
                "h2": "3. Teknik Penusukan Probe Grain Trier Sudut 45 Derajat",
                "content": """
                <p>Gunakan probe sampling bertabung ganda (<em>grain sampling trier</em> berbahan stainless steel food-grade):</p>
                <ol class="list-decimal pl-5 space-y-2 text-xs sm:text-sm text-slate-600 my-3">
                  <li>Posisikan probe dalam kondisi celah lubang tertutup.</li>
                  <li>Tusukkan probe dari sudut atas karung secara diagonal 45&deg; mengarah ke sudut bawah yang berlawanan, sehingga probe menembus zona atas, zona sentral, dan zona dasar karung.</li>
                  <li>Putar pegangan probe untuk membuka celah, biarkan beras mengisi rongga tabung, lalu putar kembali untuk menutup celah.</li>
                  <li>Tarik keluar probe dan tuang seluruh beras ke nampan komposit untuk diaduk rata sebelum diuji kadar air dan kadar patahannya.</li>
                </ol>
                """
            }
        ],
        "related_links": [
            {"title": "Cara Memakai Moisture Meter Beras & Koreksi Suhu Akurat", "href": "/artikel/cara-menggunakan-moisture-meter-beras"},
            {"title": "Beras Kepala, Broken, dan Menir: Panduan Purchasing B2B", "href": "/artikel/beras-kepala-broken-menir-untuk-purchasing"},
            {"title": "10 Checklist QC Beras Masuk Gudang: Standar Dapur B2B", "href": "/artikel/checklist-qc-beras-masuk-gudang"},
            {"title": "Program Pasokan Beras Dapur SPPG MBG", "href": "/program/sppg-mbg"},
            {"title": "Hub Layanan Pengadaan Magelang", "href": "/wilayah/magelang"}
        ]
    },
    {
        "id": 13,
        "slug": "cara-menggunakan-moisture-meter-beras",
        "title": "Cara Memakai Moisture Meter Beras & Koreksi Suhu Akurat",
        "h1": "Panduan Praktis Penggunaan Grain Moisture Meter Beras dan Formula Koreksi Suhu Kalibrasi",
        "category": "Metrologi & Laboratorium",
        "badge": "⚡ Metrologi Kadar Air Presisi",
        "read_time": "7 Menit",
        "description": "Panduan lengkap menggunakan grain moisture meter beras. Standar kadar air 13.2% - 13.8%, rumus koreksi temperatur, dan pencegahan error pengukuran.",
        "keywords": "cara menggunakan moisture meter beras, alat cek kadar air beras, kett riceter beras, kalibrasi moisture meter, batas kadar air beras sni",
        "direct_answer": "Menggunakan grain moisture meter beras membutuhkan ketelitian metrologi: bersihkan mangkuk sensor dari bekatul halus, ratakan butir tanpa dipadatkan paksa, dan selalu terapkan rumus koreksi temperatur jika suhu sampel berbeda dari suhu kalibrasi pabrik (25°C). Rumus koreksinya: Kadar Air Terkoreksi = Nilai Alat + [(Suhu Sampel - 25°C) x 0.1%]. Kadar air beras premium Beras Ladori dikurasi stabil pada rentang 13.2% hingga 13.8%, aman dari serangan kapang dan penyusutan bobot.",
        "sections": [
            {
                "h2": "1. Fisika Kadar Air: Resistansi Elektrik vs Kapasitansi Dielektrik",
                "content": """
                <p>Alat ukur kadar air beras portabel (seperti tipe <em>Kett Riceter</em> atau digital grain probe) bekerja dengan prinsip fisika kelistrikan: mengukur resistansi listrik atau konstanta dielektrik dari molekul air bebas (<em>free water</em>) yang berada di antara struktur sel pati beras.</p>
                <p>Air adalah konduktor listrik yang jauh lebih baik dibanding bahan kering pati. Semakin lembab butir beras, semakin rendah resistansi listriknya. Namun, suhu lingkungan sangat memengaruhi konduktivitas: sampel beras yang panas setelah terpapar terik matahari di bak truk akan terbaca lebih basah daripada kondisi aslinya jika tidak dikoreksi secara termal.</p>
                """
            },
            {
                "h2": "2. Formula Koreksi Suhu (Temperature Compensation Formula)",
                "content": """
                <p>Jika alat moisture meter Anda belum memiliki sensor termokopel otomatis, gunakan formula koreksi suhu standar metrologi pangan berikut:</p>
                <div class="bg-slate-900 text-slate-100 p-5 rounded-2xl my-4 text-xs sm:text-sm font-mono space-y-2">
                  <p class="text-gold-400 font-bold">// FORMULA KOREKSI SUHU KADAR AIR BERAS</p>
                  <p class="text-white text-base">MC<sub>koreksi</sub> = MC<sub>baca</sub> + [(T<sub>sampel</sub> &minus; 25&deg;C) &times; 0.1%]</p>
                  <p class="text-slate-400 pt-1">Dimana:</p>
                  <ul class="list-disc pl-5 text-slate-300 space-y-1">
                    <li>MC<sub>koreksi</sub> = Kadar air sebenarnya (%)</li>
                    <li>MC<sub>baca</sub> = Angka yang tampil di layar display digital alat</li>
                    <li>T<sub>sampel</sub> = Suhu aktual butir beras saat pengukuran (&deg;C)</li>
                    <li>25&deg;C = Temperatur acuan kalibrasi laboratorium</li>
                  </ul>
                </div>
                <div class="bg-white p-4 rounded-xl border border-slate-200 text-xs sm:text-sm text-slate-700 my-3">
                  <strong>Contoh Simulasi:</strong> Saat kiriman truk tiba siang hari terik di Sleman, butir beras bersuhu 33&deg;C dan alat menunjukkan angka 13.2%.<br>
                  Koreksi: 13.2% + [(33 &minus; 25) &times; 0.1%] = 13.2% + 0.8% = <strong>14.0%</strong>.<br>
                  Nilai riilnya berada persis di batas atas toleransi SNI.
                </div>
                """
            },
            {
                "h2": "3. Standar Kadar Air Beras Ladori (13.2% &ndash; 13.8%)",
                "content": """
                <p>Beras Ladori diproses melalui mesin pengeringan (<em>continuous dryer</em>) terkontrol dengan suhu pemanasan bertahap (&le; 42&deg;C) untuk mencegah retak mikro (<em>fissuring</em>). Kadar air dikunci konsisten pada 13.2%&ndash;13.8%:</p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 my-4">
                  <div class="bg-brand-50 p-4 rounded-xl border border-brand-200">
                    <strong class="text-brand-900 text-sm block mb-1">Mencegah Jamur & Aflatoksin</strong>
                    <p class="text-xs text-slate-600">Kadar air di bawah 14.0% membuat aktivitas air (a<sub>w</sub>) berada di bawah 0.65, mematikan potensi spora kapang <em>Aspergillus flavus</em>.</p>
                  </div>
                  <div class="bg-brand-50 p-4 rounded-xl border border-brand-200">
                    <strong class="text-brand-900 text-sm block mb-1">Daya Mekar Sempurna Tanpa Hancur</strong>
                    <p class="text-xs text-slate-600">Kadar air di atas 13.0% menjaga elastisitas matriks pati bulir beras sehingga tidak hancur menjadi bubur saat proses pencucian dan perebusan.</p>
                  </div>
                </div>
                """
            }
        ],
        "related_links": [
            {"title": "Teknik Sampling Beras Karung Standar ISO 24333 & SNI", "href": "/artikel/cara-sampling-beras-karung"},
            {"title": "10 Checklist QC Beras Masuk Gudang: Standar Dapur B2B", "href": "/artikel/checklist-qc-beras-masuk-gudang"},
            {"title": "Beras Kepala, Broken, dan Menir: Panduan Purchasing B2B", "href": "/artikel/beras-kepala-broken-menir-untuk-purchasing"},
            {"title": "Produk Resmi Beras Ladori 25 kg", "href": "/produk/beras-ladori-25kg"},
            {"title": "Hub Layanan Pengadaan Temanggung", "href": "/wilayah/temanggung"}
        ]
    },
    {
        "id": 14,
        "slug": "beras-kepala-broken-menir-untuk-purchasing",
        "title": "Beras Kepala, Broken, dan Menir: Panduan Purchasing B2B",
        "h1": "Morfologi Butir Beras untuk Purchasing: Cara Membaca Rasio Beras Kepala, Butir Patah (Broken), dan Menir",
        "category": "Metrologi & Laboratorium",
        "badge": "🌾 Anatomi Butir Beras",
        "read_time": "7 Menit",
        "description": "Panduan purchasing membaca spesifikasi butir beras: definisi beras kepala, butir patah (broken), dan menir sesuai SNI 6128:2020 serta efeknya ke nasi.",
        "keywords": "beras kepala adalah, broken rice beras patah, menir beras, sni 6128 2020 beras premium, spesifikasi fisik beras",
        "direct_answer": "Berdasarkan standar SNI 6128:2020, butir beras digolongkan ke dalam 3 fraksi dimensi: (1) Beras Kepala (Head Rice) dengan panjang butir >= 0.8 bagian utuh (standar premium >= 85%), (2) Butir Patah (Broken Rice) dengan panjang 0.2 hingga < 0.8 bagian utuh (standar premium <= 15%), dan (3) Butir Menir dengan ukuran < 0.2 bagian utuh yang lolos ayakan 2.0 mm (standar premium <= 0.5%). Keberadaan menir berlebih menyebabkan nasi menjadi benyek, mudah berlendir di warmer, dan merusak tekstur porsi saji.",
        "sections": [
            {
                "h2": "1. Dimensi Fisik Butir Beras Berdasarkan SNI 6128:2020",
                "content": """
                <p>Dalam komunikasi pengadaan beras, istilah <em>"beras super"</em> atau <em>"beras mulus"</em> tidak memiliki bobot hukum maupun ilmiah. Bagian purchasing wajib mencantumkan spesifikasi fraksi butir secara kuantitatif sesuai Standar Nasional Indonesia (SNI 6128:2020):</p>
                <div class="overflow-x-auto my-4">
                  <table class="w-full text-left border-collapse border border-slate-200 text-xs sm:text-sm bg-white rounded-xl shadow-sm">
                    <thead>
                      <tr class="bg-brand-50 text-brand-900 border-b border-slate-200">
                        <th class="p-3 font-bold">Fraksi Butir</th>
                        <th class="p-3 font-bold">Definisi Morfologi Dimensi</th>
                        <th class="p-3 font-bold">SNI Beras Premium</th>
                        <th class="p-3 font-bold text-brand-800">Standar Beras Ladori</th>
                      </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 text-slate-700">
                      <tr>
                        <td class="p-3 font-semibold">Beras Kepala (Head Rice)</td>
                        <td class="p-3">Panjang butir &ge; 80% (0.8 bagian) dari butir utuh sempurna</td>
                        <td class="p-3">&ge; 85.0%</td>
                        <td class="p-3 font-bold text-brand-700">&ge; 88.0% &ndash; 90.0%</td>
                      </tr>
                      <tr>
                        <td class="p-3 font-semibold">Butir Patah (Broken Rice)</td>
                        <td class="p-3">Pecahan butir lebih besar dari 20% tetapi lebih kecil dari 80%</td>
                        <td class="p-3">&le; 15.0%</td>
                        <td class="p-3 font-bold text-brand-700">&le; 10.0% &ndash; 12.0%</td>
                      </tr>
                      <tr>
                        <td class="p-3 font-semibold">Butir Menir (Small Broken)</td>
                        <td class="p-3">Pecahan kecil &lt; 20% yang lolos ayakan lubang 2.0 mm</td>
                        <td class="p-3">&le; 0.5%</td>
                        <td class="p-3 font-bold text-brand-700">&le; 0.2% (Nyaris 0%)</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "h2": "2. Dampak Biokimia Menir Terhadap Kerusakan Nasi di Rice Warmer",
                "content": """
                <p>Mengapa koki katering sangat anti terhadap beras yang banyak mengandung menir? Jawabannya ada pada sains pelepasan amilosa bebas:</p>
                <p>Butir menir yang hancur memiliki luas permukaan kontak yang jauh lebih besar terhadap air mendidih dibanding butir beras kepala. Akibatnya, dinding sel pati menir pecah secara masif saat proses perebusan, melepaskan lelehan amilopektin lengket ke dalam air rebusan (efek pasta kanji). Lapisan pasta kanji ini membungkus butir beras lainnya, menghasilkan fenomena berikut:</p>
                <ul class="list-disc pl-5 space-y-2 text-xs sm:text-sm text-slate-600 my-3">
                  <li><strong>Nasi Benyek di Permukaan:</strong> Nasi tampak basah berair di bagian luar namun intinya belum matang sempurna (<em>uneven gelatinization</em>).</li>
                  <li><strong>Sarang Mikroba Pembusuk:</strong> Lapisan pati cair yang terperangkap di dasar rice warmer adalah media biakan sempurna bagi bakteri mesofilik, membuat nasi berbau asam dan berlendir hanya dalam 10&ndash;12 jam.</li>
                </ul>
                """
            },
            {
                "h2": "3. Mesin Color Sorter & Grader Beras Ladori",
                "content": """
                <p>Beras Ladori 25 kg diproses melewati silinder grader mekanik bertingkat dan <em>optical color sorter</em> berkecepatan tinggi. Butir patah kasar dan menir dipisahkan secara presisi, menjamin setiap porsi nasi katering Anda tampil anggun, pulen utuh, dan tidak saling menggumpal.</p>
                """
            }
        ],
        "related_links": [
            {"title": "Cara Menghitung Cooking Yield & Rendemen Nasi Dapur B2B", "href": "/artikel/cara-menghitung-cooking-yield-beras"},
            {"title": "Cara Membaca COA Beras: Panduan Procurement Dapur B2B", "href": "/artikel/cara-membaca-coa-beras"},
            {"title": "Teknik Sampling Beras Karung Standar ISO 24333 & SNI", "href": "/artikel/cara-sampling-beras-karung"},
            {"title": "Spesifikasi Fisik Beras Ladori 25 kg", "href": "/produk/beras-ladori-25kg"},
            {"title": "Pengadaan Beras Katering Hajatan & Restoran", "href": "/program/katering-horeka"}
        ]
    },
    {
        "id": 15,
        "slug": "cara-menguji-konsistensi-beras-antar-batch",
        "title": "Cara Menguji Konsistensi Beras Antar-Batch di Dapur B2B",
        "h1": "Metode Pengujian Konsistensi Mutu Beras Antar-Batch untuk Dapur Komersial Skala Besar",
        "category": "Quality Assurance & SOP",
        "badge": "🔄 Verifikasi Stabilitas Batch",
        "read_time": "7 Menit",
        "description": "Cara menjaga konsistensi rasa dan tekstur nasi antar-batch gilingan beras. Protokol uji takaran air, daya serap panas, dan waktu resting sebelum saji.",
        "keywords": "konsistensi beras antar batch, uji stabilitas beras, variasi mutu beras, audit batch gilingan beras, standarisasi dapur katering",
        "direct_answer": "Menguji konsistensi beras antar-batch dilakukan dengan melacak koefisien variasi (Coefficient of Variation / CV) pada tiga indikator fisik: kadar air (toleransi delta <= 0.3%), rasio penyerapan air matang (water absorption ratio delta <= 0.05), dan volume cooking yield (delta <= 3%). Dapur wajib mencatat batch log sheet setiap pergantian karung untuk menyesuaikan kalibrasi takaran air koki secara presisi.",
        "sections": [
            {
                "h2": "1. Masalah Klasik Dapur: Resep Tetap, Nasi Berubah Tekstur",
                "content": """
                <p>Salah satu keluhan paling sering dari kepala koki (Executive Chef) adalah inkonsistensi bahan baku: <em>"Bulan lalu pakai takaran air 10 liter hasilnya sangat pas. Bulan ini pakai takaran yang sama nasinya malah lembek seperti bubur!"</em></p>
                <p>Perubahan ini disebabkan oleh variasi antar-batch gilingan padi (musim panen hujan vs panen kemarau, lama masa simpan gabah di silo, atau perbedaan varietas yang dicampur pedagang pasar). Bagi restoran waralaba dan katering skala ribuan porsi, fluktuasi rasa ini sangat membahayakan loyalitas konsumen.</p>
                """
            },
            {
                "h2": "2. Protokol Batch Acceptance Testing 3 Titik",
                "content": """
                <p>Sebelum memasukkan lot beras baru ke alur produksi massal, terapkan uji penerimaan batch 3 titik berikut:</p>
                <div class="space-y-3 my-4">
                  <div class="bg-white p-4 rounded-xl border border-slate-200">
                    <strong class="text-brand-800 text-sm block mb-1">Titik 1: Verifikasi Delta Kadar Air (&Delta; &le; 0.3%)</strong>
                    <p class="text-xs sm:text-sm text-slate-600">Ukur kadar air lot baru dan bandingkan dengan lot lama. Jika lot baru memiliki kadar air lebih rendah 0.5% (misal gabah musim kemarau), koki harus menaikkan takaran air masak sebanyak 50 ml per kg beras.</p>
                  </div>
                  <div class="bg-white p-4 rounded-xl border border-slate-200">
                    <strong class="text-brand-800 text-sm block mb-1">Titik 2: Uji Water Absorption Ratio 100g</strong>
                    <p class="text-xs sm:text-sm text-slate-600">Rebus 100g beras dalam 300ml air selama 20 menit. Timbang nasi matang. Rasio serap air = (Berat Matang &minus; 100g) &divide; 100g. Nilai toleransi variasi antar-batch tidak boleh melebihi 5%.</p>
                  </div>
                  <div class="bg-white p-4 rounded-xl border border-slate-200">
                    <strong class="text-brand-800 text-sm block mb-1">Titik 3: Audit Profil Organoleptik Organik</strong>
                    <p class="text-xs sm:text-sm text-slate-600">Nilai tingkat kepulenan, kekenyalan (chewiness), dan warna putih alami setelah didiamkan 4 jam pada suhu ruang. Catat pada formulir <em>Batch Quality Log</em> dapur.</p>
                  </div>
                </div>
                """
            },
            {
                "h2": "3. Jaminan Konsistensi Pasokan Tunggal Beras Ladori",
                "content": """
                <p>Beras Ladori menjaga konsistensi antar-batch dengan menggunakan gabah varietas murni pilihan yang diproses di fasilitas penggilingan modern berkapasitas besar. Kami tidak pernah mengoplos beras baru dengan beras stok lama, sehingga resep dan SOP air di dapur Anda selalu presisi sepanjang tahun.</p>
                """
            }
        ],
        "related_links": [
            {"title": "Nomor Batch & Traceability Beras: Proteksi Dapur B2B", "href": "/artikel/traceability-dan-nomor-batch-beras"},
            {"title": "Cara Membaca COA Beras: Panduan Procurement Dapur B2B", "href": "/artikel/cara-membaca-coa-beras"},
            {"title": "Cara Menghitung Cooking Yield & Rendemen Nasi Dapur B2B", "href": "/artikel/cara-menghitung-cooking-yield-beras"},
            {"title": "Layanan Pengadaan Dapur Restoran & Hotel", "href": "/program/katering-horeka"},
            {"title": "Hub Distribusi Kota Jogja", "href": "/wilayah/jogja"}
        ]
    },
    {
        "id": 16,
        "slug": "cara-membaca-coa-beras",
        "title": "Cara Membaca COA Beras: Panduan Procurement Dapur B2B",
        "h1": "Cara Membaca Certificate of Analysis (COA) Beras: Panduan Procurement Dapur Komersial & Institusi",
        "category": "Pengujian Laboratorium & Dapur",
        "badge": "📑 Audit Laboratorium COA",
        "read_time": "8 Menit",
        "description": "Cara membaca Certificate of Analysis (COA) beras laboratorium. Pahami parameter kimia residu klorin 0%, pestisida, logam berat, dan derajat sosoh 100%.",
        "keywords": "coa beras laboratorium, certificate of analysis beras, hasil uji lab beras, residu klorin beras 0, sertifikasi beras pangan",
        "direct_answer": "Membaca Certificate of Analysis (COA) beras laboratorium berfokus pada 4 blok pengujian: (1) Parameter Fisik Mutu (derajat sosoh >= 95%, kadar air <= 13.8%, butir kepala >= 85%), (2) Uji Kimiawi Residu Pemutih (klorin bebas = Tidak Terdeteksi / Limit of Detection < 0.1 mg/kg), (3) Cemaran Logam Berat (Timbal Pb <= 0.2 mg/kg, Kadmium Cd <= 0.1 mg/kg sesuai standar BPOM), dan (4) Keabsahan Akreditasi Laboratorium (memiliki akreditasi KAN ISO/IEC 17025).",
        "sections": [
            {
                "h2": "1. Mengapa Lembar COA Laboratorium Sangat Krusial untuk Pembeli B2B",
                "content": """
                <p>Bagi institusi formal—seperti unit Dapur SPPG Makan Bergizi Gratis (MBG), Instalasi Gizi Rumah Sakit, dan jaringan hotel berbintang—membeli beras hanya bermodalkan kuitansi toko tanpa bukti uji laboratorium adalah pelanggaran tata kelola pengadaan pangan. Jika terjadi insiden keracunan pangan, lembar Certificate of Analysis (COA) adalah dokumen perlindungan hukum utama yang membuktikan integritas rantai pasok Anda.</p>
                """
            },
            {
                "h2": "2. Anatomi 4 Blok Parameter dalam Lembar COA Beras Resmi",
                "content": """
                <div class="overflow-x-auto my-4">
                  <table class="w-full text-left border-collapse border border-slate-200 text-xs sm:text-sm bg-white rounded-xl shadow-sm">
                    <thead>
                      <tr class="bg-brand-50 text-brand-900 border-b border-slate-200">
                        <th class="p-3 font-bold">Blok Analisis</th>
                        <th class="p-3 font-bold">Parameter Spesifik</th>
                        <th class="p-3 font-bold">Ambang Batas Maksimum (BPOM/SNI)</th>
                        <th class="p-3 font-bold text-brand-800">Standar Mutu Beras Ladori</th>
                      </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 text-slate-700">
                      <tr>
                        <td class="p-3 font-semibold">1. Fisika Mutu</td>
                        <td class="p-3">Derajat Sosoh, Kadar Air, Benda Asing</td>
                        <td class="p-3">Sosoh &ge; 95%, Air &le; 14.0%, Benda Asing &le; 0.02%</td>
                        <td class="p-3 font-bold text-brand-700">Sosoh 100%, Air 13.5%, Benda Asing 0%</td>
                      </tr>
                      <tr>
                        <td class="p-3 font-semibold">2. Residu Pemutih</td>
                        <td class="p-3">Klorin Bebas (Free Available Chlorine)</td>
                        <td class="p-3">Tidak Boleh Ada (Zero Chlorine)</td>
                        <td class="p-3 font-bold text-brand-700">Negative / Not Detected (&lt; 0.05 mg/kg)</td>
                      </tr>
                      <tr>
                        <td class="p-3 font-semibold">3. Logam Berat</td>
                        <td class="p-3">Timbal (Pb), Kadmium (Cd), Arsenik (As)</td>
                        <td class="p-3">Pb &le; 0.2 mg/kg, Cd &le; 0.1 mg/kg</td>
                        <td class="p-3 font-bold text-brand-700">Jauh di Bawah Limit Deteksi Lab (Aman)</td>
                      </tr>
                      <tr>
                        <td class="p-3 font-semibold">4. Mikrobiologi</td>
                        <td class="p-3">Aflatoksin Total (B1+B2+G1+G2)</td>
                        <td class="p-3">&le; 20 &mu;g/kg</td>
                        <td class="p-3 font-bold text-brand-700">Not Detected (Kadar Air Kering Terkendali)</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "h2": "3. Cara Memverifikasi Keaslian Dokumen COA",
                "content": """
                <p>Pastikan lembar COA yang diserahkan supplier memenuhi kaidah formal:</p>
                <ul class="list-disc pl-5 space-y-1 text-xs sm:text-sm text-slate-600 my-3">
                  <li>Diterbitkan oleh laboratorium terakreditasi <strong>KAN (Komite Akreditasi Nasional)</strong> atau Balai Pengujian Mutu Pangan Pemerintah.</li>
                  <li>Nomor batch lot pada COA cocok dengan kode batch yang tercetak pada karung pengiriman yang Anda terima.</li>
                  <li>Terdapat tanda tangan basah/digital tersertifikasi dari manajer teknis laboratorium penguji.</li>
                </ul>
                """
            }
        ],
        "related_links": [
            {"title": "Nomor Batch & Traceability Beras: Proteksi Dapur B2B", "href": "/artikel/traceability-dan-nomor-batch-beras"},
            {"title": "5 Cara Membedakan Beras Alami vs Beras Berpemutih Kimia", "href": "/artikel/cara-membedakan-beras-pulen-alami-bebas-pemutih"},
            {"title": "10 Checklist QC Beras Masuk Gudang: Standar Dapur B2B", "href": "/artikel/checklist-qc-beras-masuk-gudang"},
            {"title": "Standar Dapur SPPG Makan Bergizi Gratis", "href": "/artikel/standar-beras-dapur-sppg-mbg"},
            {"title": "Profil Brand & Legalitas Beras Ladori", "href": "/tentang/beras-ladori"}
        ]
    },
    {
        "id": 17,
        "slug": "traceability-dan-nomor-batch-beras",
        "title": "Nomor Batch & Traceability Beras: Proteksi Dapur B2B",
        "h1": "Sistem Ketertelusuran (Traceability) dan Kode Batch Beras: Proteksi Mutu Dapur Komersial & Institusi",
        "category": "Quality Assurance & SOP",
        "badge": "🔍 Ketertelusuran Rantai Pasok",
        "read_time": "7 Menit",
        "description": "Mengapa sistem nomor batch dan traceability beras penting bagi buyer B2B. Pelacakan tanggal sosoh, asal gabah, silo simpan, dan kemudahan audit pangan.",
        "keywords": "traceability beras pangan, nomor batch beras, ketertelusuran rantai pasok beras, audit haccp beras, barcode karung beras",
        "direct_answer": "Sistem Traceability (Ketertelusuran) Beras memungkinkan pelacakan riwayat setiap karung beras mulai dari asal gabah petani, tanggal proses giling/sosoh, silo penyimpanan, hingga nomor armada pengiriman. Menggunakan format kode batch terstandar (contoh: YYYYMMDD-SILO-LOT), buyer B2B dapat melakukan audit pangan, menerapkan rotasi gudang FIFO secara otomatis, dan mengisolasi karung spesifik tanpa harus meretur seluruh gudang jika terjadi anomali mutu.",
        "sections": [
            {
                "h2": "1. Mengapa Ketertelusuran Pangan Menjadi Standar Baru Pengadaan B2B",
                "content": """
                <p>Di era pengawasan mutu pangan yang ketat saat ini, beras tanpa identitas lot (<em>untraceable commodity</em>) membawa risiko hukum dan operasional yang sangat besar bagi pengelola dapur komersial. Jika terjadi keluhan rasa atau kecurigaan mutu pada salah satu batch, manajemen tidak dapat mengetahui karung mana yang harus ditarik.</p>
                <p>Sistem ketertelusuran modern mengubah komoditas beras menjadi produk industri terstandarisasi yang memiliki rekam jejak digital lengkap dari hulu ke hilir.</p>
                """
            },
            {
                "h2": "2. Struktur Pengkodean Lot Batch Beras Ladori",
                "content": """
                <div class="bg-slate-900 text-slate-100 p-5 rounded-2xl my-4 text-xs sm:text-sm font-mono space-y-2">
                  <p class="text-gold-400 font-bold">// STRUKTUR KODE BATCH LOT BERAS LADORI</p>
                  <p class="text-white text-base">Format: [YYYYMMDD] - [PLANT] - [SILO] - [LOT]</p>
                  <p class="text-slate-400">Contoh: <strong>20260913-MTL-S02-B08</strong></p>
                  <ul class="list-disc pl-5 text-slate-300 space-y-1 pt-2">
                    <li><strong>20260913:</strong> Tanggal pemrosesan sosoh & pengemasan (13 September 2026)</li>
                    <li><strong>MTL:</strong> Fasilitas Milling Hub Muntilan</li>
                    <li><strong>S02:</strong> Silo penyimpanan gabah asal nomor 02</li>
                    <li><strong>B08:</strong> Nomor antrean lot produksi hari berjalan</li>
                  </ul>
                </div>
                """
            },
            {
                "h2": "3. Manfaat Operasional Traceability untuk Dapur Anda",
                "content": """
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 my-4">
                  <div class="bg-white p-4 rounded-xl border border-slate-200">
                    <strong class="text-slate-900 text-sm block mb-1">Rotasi Stok FIFO Presisi</strong>
                    <p class="text-xs text-slate-600">Staf gudang dapat dengan mudah melihat tanggal produksi tercetak di karung, mencegah karung lama tertimbun di belakang palet.</p>
                  </div>
                  <div class="bg-white p-4 rounded-xl border border-slate-200">
                    <strong class="text-slate-900 text-sm block mb-1">Kemudahan Audit Institusi</strong>
                    <p class="text-xs text-slate-600">Laporan pertanggungjawaban untuk program SPPG MBG dan audit akreditasi rumah sakit menjadi sangat rapi dan dapat dipertanggungjawabkan.</p>
                  </div>
                  <div class="bg-white p-4 rounded-xl border border-slate-200">
                    <strong class="text-slate-900 text-sm block mb-1">Isolasi Cepat & Retur Zero-Dispute</strong>
                    <p class="text-xs text-slate-600">Jika ditemukan karung rusak, penggantian dari distributor cukup merujuk nomor batch tanpa perdebatan panjang.</p>
                  </div>
                </div>
                """
            }
        ],
        "related_links": [
            {"title": "Cara Membaca COA Beras: Panduan Procurement Dapur B2B", "href": "/artikel/cara-membaca-coa-beras"},
            {"title": "Kebijakan Komplain & Retur Supplier Beras: Prosedur B2B", "href": "/artikel/kebijakan-komplain-supplier-beras"},
            {"title": "SOP Penerimaan Beras di Loading Dock Dapur Komersial", "href": "/artikel/sop-penerimaan-beras-dapur-b2b"},
            {"title": "Profil Legalitas & Pabrik Beras Ladori", "href": "/tentang/beras-ladori"},
            {"title": "Hub Wilayah Muntilan", "href": "/wilayah/muntilan"}
        ]
    },
    {
        "id": 18,
        "slug": "kebijakan-komplain-supplier-beras",
        "title": "Kebijakan Komplain & Retur Supplier Beras: Prosedur B2B",
        "h1": "Service Level Agreement (SLA) Komplain dan Kebijakan Retur Penggantian Beras Supplier B2B",
        "category": "Tata Kelola Kontrak & SLA",
        "badge": "🤝 Service Level Agreement (SLA)",
        "read_time": "7 Menit",
        "description": "Prosedur komplain dan garansi retur supplier beras B2B. Aturan Service Level Agreement (SLA), batas waktu pelaporan, dan penggantian karung bermasalah.",
        "keywords": "kebijakan komplain supplier beras, garansi retur beras b2b, sla pengadaan beras, retur beras rusak, komplain beras kutu apek",
        "direct_answer": "Kebijakan komplain supplier beras B2B profesional diatur melalui Service Level Agreement (SLA) resmi: respons keluhan maksimal 2 jam setelah laporan, batas waktu investigasi klaim 1x24 jam, dan penggantian barang cacat 1-banding-1 (1:1 replacement) tanpa biaya kirim tambahan. Beras Ladori memberlakukan kebijakan Zero-Dispute Guarantee untuk karung cacat pabrik, kemasan sobek saat transit, atau anomali butir yang tidak sesuai sampel kontrak.",
        "sections": [
            {
                "h2": "1. Mengapa Klausul Komplain Wajib Disepakati Sebelum Transaksi Pertama",
                "content": """
                <p>Banyak pengelola katering dan restoran terjebak dalam hubungan bisnis yang menyiksa: saat promosi penjualan, supplier bersikap sangat ramah. Namun ketika ada karung beras yang apek, kutu, atau sobek, supplier berdalih kesalahan penyimpanan dapur pembeli dan menolak mengganti produk.</p>
                <p>Supplier B2B profesional memandang komplain bukan sebagai beban permusuhan, melainkan parameter kualitas layanan yang dijamin secara kontraktual melalui <strong>Service Level Agreement (SLA)</strong>.</p>
                """
            },
            {
                "h2": "2. Matriks SLA Penanganan Komplain Beras Ladori",
                "content": """
                <div class="overflow-x-auto my-4">
                  <table class="w-full text-left border-collapse border border-slate-200 text-xs sm:text-sm bg-white rounded-xl shadow-sm">
                    <thead>
                      <tr class="bg-brand-50 text-brand-900 border-b border-slate-200">
                        <th class="p-3 font-bold">Kategori Masalah</th>
                        <th class="p-3 font-bold">Batas Waktu Pelaporan</th>
                        <th class="p-3 font-bold text-brand-800">Tindakan Solusi Garansi Ladori</th>
                      </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 text-slate-700">
                      <tr>
                        <td class="p-3 font-semibold">Karung Sobek / Basah Transit</td>
                        <td class="p-3">Saat unloading di loading dock</td>
                        <td class="p-3 font-bold text-brand-700">Tolak langsung, diganti armada saat itu juga</td>
                      </tr>
                      <tr>
                        <td class="p-3 font-semibold">Kadar Air &gt; 14% / Benda Asing</td>
                        <td class="p-3">Maksimal 2x24 jam pasca terima</td>
                        <td class="p-3 font-bold text-brand-700">Tukar karung baru 100% gratis bebas ongkir</td>
                      </tr>
                      <tr>
                        <td class="p-3 font-semibold">Nasi Tidak Sesuai Karakter Sampel</td>
                        <td class="p-3">Maksimal 3x24 jam pasca uji tanak</td>
                        <td class="p-3 font-bold text-brand-700">Kunjungan tim QC ke dapur + penyesuaian lot / retur penuh</td>
                      </tr>
                      <tr>
                        <td class="p-3 font-semibold">Ditemukan Kutu Beras Gudang</td>
                        <td class="p-3">Maksimal 7 hari kalender</td>
                        <td class="p-3 font-bold text-brand-700">Inspeksi batch dan penggantian karung segar gilingan baru</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                "h2": "3. 3 Langkah Mudah Mengajukan Klaim Garansi",
                "content": """
                <p>Sebagai mitra B2B Beras Ladori di wilayah Sleman, Jogja, Muntilan, Magelang, dan Temanggung, pengajuan komplain sangat praktis tanpa birokrasi berbelit:</p>
                <ol class="list-decimal pl-5 space-y-1 text-xs sm:text-sm text-slate-600 my-3">
                  <li>Foto label nomor batch pada karung yang bermasalah.</li>
                  <li>Kirim foto/video kendala melalui kontak WhatsApp resmi customer care Beras Ladori.</li>
                  <li>Tim logistik kami akan menjadwalkan penggantian karung baru pada rute armada hari berikutnya ke alamat dapur Anda.</li>
                </ol>
                """
            }
        ],
        "related_links": [
            {"title": "Nomor Batch & Traceability Beras: Proteksi Dapur B2B", "href": "/artikel/traceability-dan-nomor-batch-beras"},
            {"title": "SOP Penerimaan Beras di Loading Dock Dapur Komersial", "href": "/artikel/sop-penerimaan-beras-dapur-b2b"},
            {"title": "15 Pertanyaan Wajib Sebelum Memilih Supplier Beras B2B", "href": "/artikel/pertanyaan-sebelum-memilih-supplier-beras"},
            {"title": "Spesifikasi Resmi Beras Ladori 25 kg", "href": "/produk/beras-ladori-25kg"},
            {"title": "Hub Wilayah Sleman", "href": "/wilayah/sleman"}
        ]
    }
]
