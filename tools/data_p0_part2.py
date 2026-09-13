# -*- coding: utf-8 -*-
"""
Part 2 of Priority P0 Articles: #028, #052, #053, #057, #060, #089, #120
"""

p0_part2_articles = [
    # --------------------------------------------------------------------------
    # 8. ARTIKEL #028: Beras Premium vs Medium: Apa Perbedaannya Menurut Standar Mutu?
    # Merges: #096 (Beras Premium vs Medium: Jangan Hanya Menilai dari Warna Putih)
    # --------------------------------------------------------------------------
    {
        "id": "OLD-028",
        "slug": "beras-premium-vs-medium",
        "title": "Beras Premium vs Medium: Perbedaan Menurut Standar Mutu",
        "h1": "Beras Premium vs Medium: Apa Perbedaannya Menurut Standar Mutu?",
        "description": "Beras premium vs medium: apa bedanya menurut SNI dan Permendag? Bandingkan kadar air, butir patah, derajat sosoh, serta implikasinya pada masakan.",
        "keywords": "beras premium vs medium, perbedaan beras premium dan medium, standar sni 6128, derajat sosoh beras, ciri beras premium asli",
        "category_badge": "🔬 Mutu, QC & Standar Beras",
        "breadcrumb_title": "Beras Premium vs Medium",
        "read_time": "8",
        "key_takeaways": "Perbedaan beras premium dan medium diatur secara ketat oleh SNI 6128:2020 dan Permendag. Beras Premium mensyaratkan derajat sosoh minimal 95%, butir patah (broken) maksimal 15% (bahkan <5% pada kelas super), dan kadar air maks 14%. Beras Medium mentoleransi butir patah hingga 20–25% dan derajat sosoh 80–90%. Jangan pernah menilai mutu hanya dari warna putih mengkilap, karena warna putih ekstrim bisa merupakan indikasi zat pemutih sintetis.",
        "body_html": """
<p class="lead text-lg font-medium text-slate-800">
  Di pasar tradisional maupun rak supermarket modern, kata <strong>'Premium'</strong> dan <strong>'Medium'</strong> tercetak jelas di karung beras. Sebagian konsumen mengira perbedaan keduanya hanyalah soal merek, gengsi kemasan, atau selisih harga beberapa ribu rupiah. Bahkan ada anggapan umum bahwa beras yang lebih putih mengkilap pastilah beras kelas premium.
</p>

<p>
  Faktanya, istilah premium dan medium adalah <strong>kelas mutu teknis</strong> yang diatur secara hukum oleh Kementerian Pertanian (Kementan) dan Badan Standardisasi Nasional (BSN) lewat regulasi SNI 6128:2020 serta Peraturan Menteri Perdagangan (Permendag). Menilai mutu beras hanya dari warna putih adalah mitos keliru yang sering dimanfaatkan oknum penjual nakal dengan menggunakan bahan pemutih kimia klorin.
</p>

<h2 class="text-2xl font-bold text-slate-900">Mitos Warna Putih: Mengapa Beras Terlalu Putih Patut Dicurigai?</h2>
<p>
  Beras alami memiliki warna putih susu transparan dengan sedikit semburat bening alami endosperma padi. Warna putih alami ini didapatkan dari proses penyosohan mekanis (pengikisan lapisan kulit ari atau bekatul).
</p>
<ul class="list-disc pl-6 space-y-2">
  <li><strong>Derajat Sosoh Alami (Milling Degree):</strong> Beras premium disosoh dengan derajat 95% hingga 100%. Kulit arinya bersih, namun struktur butir tetap utuh dan beraroma segar khas gabah baru.</li>
  <li><strong>Indikasi Pemutih Kimia:</strong> Jika butiran beras berwarna putih kapur sangat mencolok, mengilap licin tidak alami, tidak beraroma gabah sama sekali atau tercium bau kimia obat pemutih, dan saat dicuci airnya langsung keruh putih pekat seperti susu encer, beras tersebut patut dicurigai telah dipoles menggunakan zat klorin atau talk sintetis ilegal.</li>
</ul>

<h2 class="text-2xl font-bold text-slate-900">Tabel Perbandingan Mutu SNI 6128:2020: Premium vs Medium</h2>
<div class="overflow-x-auto my-6">
  <table class="w-full text-left border-collapse border border-slate-200 text-sm">
    <thead>
      <tr class="bg-slate-100 text-slate-900 border-b">
        <th class="p-3 border">Komponen Parameter Mutu</th>
        <th class="p-3 border bg-emerald-50">Beras Premium</th>
        <th class="p-3 border">Beras Medium I</th>
        <th class="p-3 border">Beras Medium II</th>
      </tr>
    </thead>
    <tbody>
      <tr class="border-b">
        <td class="p-3 border font-semibold">Derajat Sosoh (Minimal)</td>
        <td class="p-3 border font-bold text-brand-800 bg-emerald-50/50">95 %</td>
        <td class="p-3 border">90 %</td>
        <td class="p-3 border">80 %</td>
      </tr>
      <tr class="border-b">
        <td class="p-3 border font-semibold">Kadar Air (Maksimal)</td>
        <td class="p-3 border font-bold text-brand-800 bg-emerald-50/50">14.0 %</td>
        <td class="p-3 border">14.0 %</td>
        <td class="p-3 border">14.0 %</td>
      </tr>
      <tr class="border-b">
        <td class="p-3 border font-semibold">Butir Kepala (Minimal)</td>
        <td class="p-3 border font-bold text-brand-800 bg-emerald-50/50">85.0 % (Ladori: &ge;95%)</td>
        <td class="p-3 border">75.0 %</td>
        <td class="p-3 border">65.0 %</td>
      </tr>
      <tr class="border-b">
        <td class="p-3 border font-semibold">Butir Patah / Broken (Maksimal)</td>
        <td class="p-3 border font-bold text-brand-800 bg-emerald-50/50">15.0 % (Ladori: &le;5%)</td>
        <td class="p-3 border">25.0 %</td>
        <td class="p-3 border">35.0 %</td>
      </tr>
      <tr class="border-b">
        <td class="p-3 border font-semibold">Menir (Maksimal)</td>
        <td class="p-3 border font-bold text-brand-800 bg-emerald-50/50">0.0 % (Bebas Menir)</td>
        <td class="p-3 border">1.0 %</td>
        <td class="p-3 border">2.0 %</td>
      </tr>
      <tr class="border-b">
        <td class="p-3 border font-semibold">Batu / Benda Asing</td>
        <td class="p-3 border font-bold text-brand-800 bg-emerald-50/50">0.0 % (Nol Toleransi)</td>
        <td class="p-3 border">0.05 %</td>
        <td class="p-3 border">0.10 %</td>
      </tr>
    </tbody>
  </table>
</div>

<h2 class="text-2xl font-bold text-slate-900">Implikasi Perbedaan Mutu di Meja Makan & Dapur Katering</h2>
<p>
  Mengapa dapur profesional lebih memilih beras premium meskipun harga belinya sedikit lebih tinggi?
</p>
<ol class="list-decimal pl-6 space-y-2">
  <li><strong>Rendemen Nasi Mekar:</strong> Beras premium menghasilkan nasi matang hingga 2,4–2,5 kg per 1 kg beras mentah. Beras medium dengan broken tinggi menyerap air tidak merata dan hanya menghasilkan sekitar 2,0–2,1 kg nasi matang.</li>
  <li><strong>Ketahanan Basi di Warmer:</strong> Derajat sosoh 95% membuang seluruh minyak lemak dedak yang rawan teroksidasi. Nasi dari beras premium tetap putih cerah dan wangi hingga 12 jam di pemanas, sedangkan nasi beras medium sering menguning dan berbau apek dalam 6 jam.</li>
  <li><strong>Efisiensi Waktu Cuci:</strong> Beras premium bersih tanpa batu kerikil atau menir, sehingga proses pencucian dapur hanya butuh 1–2 menit tanpa perlu proses penampian (sortir manual) yang melelahkan.</li>
</ol>

<p>
  Seluruh produk <strong><a href="/produk/beras-ladori-25kg" class="text-brand-700 font-bold hover:underline">Beras Premium Ladori 25 kg</a></strong> diproduksi dengan standar kualitas tertinggi: derajat sosoh 95%, butir kepala minimal 95%, dan 100% bebas bahan kimia pemutih, pewangi sintetis, maupun pengawet.
</p>
""",
        "related_links_html": """
<a href="/artikel/cara-membedakan-beras-pulen-alami-bebas-pemutih" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Edukasi Konsumen</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Cara Membedakan Beras Bebas Pemutih</span>
    <p class="text-xs text-slate-500 mt-1">Uji sederhana mendeteksi pemutih klorin dan parfum kimia pada beras.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/artikel/cara-memilih-beras-yang-bagus" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Checklist Mutu</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">12 Pemeriksaan Memilih Beras Berkualitas</span>
    <p class="text-xs text-slate-500 mt-1">Panduan lengkap sebelum membeli beras untuk kebutuhan rumah atau usaha.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/produk/beras-ladori-25kg" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Katalog Produk</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Beras Premium Ladori Kemasan 25 Kg</span>
    <p class="text-xs text-slate-500 mt-1">Standar mutu SNI terverifikasi resmi untuk katering dan Horeka.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Lihat Produk &rarr;</span>
</a>
<a href="/program/sppg-mbg" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Standar Gizi</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Program Pasokan Beras SPPG MBG</span>
    <p class="text-xs text-slate-500 mt-1">Kualifikasi beras higienis dan aman untuk pemenuhan gizi anak bangsa.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Pelajari Program &rarr;</span>
</a>
"""
    },

    # --------------------------------------------------------------------------
    # 9. ARTIKEL #052: Kenapa Harga Beras Bisa Berbeda Jauh Padahal Sama-Sama 5 Kg?
    # --------------------------------------------------------------------------
    {
        "id": "OLD-052",
        "slug": "kenapa-harga-beras-berbeda",
        "title": "Kenapa Harga Beras Berbeda Jauh Padahal Sama Ukuran 5 Kg?",
        "h1": "Kenapa Harga Beras Bisa Berbeda Jauh Padahal Sama-Sama 5 Kg?",
        "description": "Kenapa harga beras berbeda jauh padahal sama-sama 5 kg? Bongkar faktor varietas, kadar air, persentase broken, optical sorting, dan biaya logistik.",
        "keywords": "kenapa harga beras berbeda, selisih harga beras 5 kg, faktor penentu harga beras, beras murah vs beras mahal, perbandingan kualitas beras",
        "category_badge": "💰 Harga & Komparasi",
        "breadcrumb_title": "Kenapa Harga Beras Berbeda",
        "read_time": "7",
        "key_takeaways": "Harga dua kantong beras berukuran sama (5 kg atau 25 kg) dapat berselisih hingga 30–50% bukan semata karena permainan pedagang. Selisih harga tersebut ditentukan oleh 5 faktor struktural: varietas bibit gabah, kadar air awal (13% vs 15%), persentase butir utuh vs patah, investasi mesin optical color sorter, dan legalitas kemasan pangan (izin Kementan, uji lab, dan food grade bag).",
        "body_html": """
<p class="lead text-lg font-medium text-slate-800">
  Ketika berbelanja beras, Anda mungkin sering terheran-heran: mengapa dua karung beras yang beratnya sama-sama 5 kg atau 25 kg bisa memiliki selisih harga hingga Rp 15.000 sampai Rp 30.000? Apakah beras yang lebih mahal murni karena merek terkenal, ataukah memang ada substansi mutu nyata yang membedakannya?
</p>

<p>
  Dalam industri pangan, beras tidak boleh dinilai hanya sebagai komoditas butir putih kiloan. Nilai sejati sebuah kemasan beras ditentukan oleh biaya proses di hulu, efisiensi teknologi penggilingan, dan kepastian keamanan saat masuk ke saluran pencernaan keluarga Anda.
</p>

<h2 class="text-2xl font-bold text-slate-900">5 Faktor Penentu Selisih Harga Beras di Pasaran</h2>

<div class="space-y-4 my-6 not-prose">
  <div class="p-5 bg-white border border-slate-200 rounded-2xl shadow-sm">
    <div class="text-xs font-bold text-brand-700 uppercase tracking-wider mb-1">Faktor 1</div>
    <h3 class="text-base font-bold text-slate-900 mb-1">Kualitas Gabah Awal & Varietas Benih</h3>
    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
      Gabah Kering Giling (GKG) varietas unggul seperti C4, Mentik Wangi, atau Inpari 32 dari sawah berpengairan teknis memiliki harga beli gabah lebih tinggi dibandingkan gabah campuran asalan. Varietas ini menghasilkan tekstur pulen alami yang konsisten tanpa memerlukan campuran kimiawi.
    </p>
  </div>

  <div class="p-5 bg-white border border-slate-200 rounded-2xl shadow-sm">
    <div class="text-xs font-bold text-brand-700 uppercase tracking-wider mb-1">Faktor 2</div>
    <h3 class="text-base font-bold text-slate-900 mb-1">Kadar Air dan Timbangan Riil</h3>
    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
      Beras murah sering kali memiliki kadar air tinggi (15% hingga 16%). Artinya, pembeli membayar lebih banyak untuk berat air. Beras berkualitas seperti Beras Ladori dikeringkan tuntas pada kadar air 13,2%–13,8%. Menurunkan kadar air gabah membutuhkan biaya bahan bakar dryer dan waktu penjemuran ekstra, namun menjamin beras tahan disimpan berbulan-bulan tanpa bau apek.
    </p>
  </div>

  <div class="p-5 bg-white border border-slate-200 rounded-2xl shadow-sm">
    <div class="text-xs font-bold text-brand-700 uppercase tracking-wider mb-1">Faktor 3</div>
    <h3 class="text-base font-bold text-slate-900 mb-1">Investasi Mesin Modern (Optical Color Sorter)</h3>
    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
      Beras tanpa sortir mengandung banyak batu kerikil, gabah hampa, dan butir patah. Untuk menghasilkan beras bersih dengan butir kepala minimal 95%, pabrik harus berinvestasi pada mesin pemisah batu (destoner), grader silinder, dan mesin kamera laser (color sorter). Proses penyortiran ini mengurangi volume hasil akhir siap jual, namun menghasilkan beras premium yang bebas batu dan bersih higienis.
    </p>
  </div>

  <div class="p-5 bg-white border border-slate-200 rounded-2xl shadow-sm">
    <div class="text-xs font-bold text-brand-700 uppercase tracking-wider mb-1">Faktor 4</div>
    <h3 class="text-base font-bold text-slate-900 mb-1">Keamanan Pangan & Uji Laboratorium Rutin</h3>
    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
      Beras berizin edar resmi Kementan RI PD wajib melakukan pengujian laboratorium berkala untuk memastikan residu pestisida, logam berat (timbal, kadmium, arsenik), dan pemutih klorin bernilai 0% (negatif). Biaya kepatuhan dan audit mutu ini menjamin keamanan kesehatan jangka panjang konsumen.
    </p>
  </div>

  <div class="p-5 bg-white border border-slate-200 rounded-2xl shadow-sm">
    <div class="text-xs font-bold text-brand-700 uppercase tracking-wider mb-1">Faktor 5</div>
    <h3 class="text-base font-bold text-slate-900 mb-1">Efisiensi Hasil Masak (Yield per Porsi)</h3>
    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
      Beras murah dengan broken tinggi sering kali menghasilkan nasi matang yang sedikit karena menyerap air tidak efisien (yield 2.0x). Sementara beras premium Ladori menghasilkan yield hingga 2.4x. Selisih porsi matang ini membuat biaya nasi per porsi dari beras premium justru sering kali <strong>jauh lebih murah</strong> dibandingkan beras murah asalan.
    </p>
  </div>
</div>

<p>
  Sebelum tergiur harga murah, selalu periksa label kemasan, persentase butir patah, dan reputasi distributor. Di <strong><a href="/produk/beras-ladori-25kg" class="text-brand-700 font-bold hover:underline">Beras Premium Ladori 25 kg</a></strong>, setiap rupiah yang Anda keluarkan terkonversi menjadi butiran nasi berkualitas terbaik yang menguntungkan dapur usaha dan menyehatkan keluarga.
</p>
""",
        "related_links_html": """
<a href="/artikel/cara-memilih-beras-yang-bagus" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Panduan Inspeksi</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">12 Cara Memilih Beras yang Bagus</span>
    <p class="text-xs text-slate-500 mt-1">Checklist detail memeriksa mutu beras sebelum memutuskan membeli.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/artikel/cara-membandingkan-supplier-beras" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Strategi Vendor</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Cara Membandingkan Supplier Beras B2B</span>
    <p class="text-xs text-slate-500 mt-1">Evaluasi total cost, konsistensi batch, dan keandalan armada pengiriman.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/produk/beras-ladori-25kg" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Produk Resmi</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Beras Ladori 25 Kg Berkualitas Tinggi</span>
    <p class="text-xs text-slate-500 mt-1">Kualitas premium dengan transparansi harga dan spesifikasi resmi.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Lihat Produk &rarr;</span>
</a>
<a href="/program/sppg-mbg" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Pengadaan SPPG</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Efisiensi Biaya Beras SPPG MBG</span>
    <p class="text-xs text-slate-500 mt-1">Solusi beras premium dengan efisiensi anggaran pengadaan publik.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Pelajari Program &rarr;</span>
</a>
"""
    },

    # --------------------------------------------------------------------------
    # 10. ARTIKEL #053: Cara Menghitung Harga Beras per Porsi untuk Warung Makan
    # --------------------------------------------------------------------------
    {
        "id": "OLD-053",
        "slug": "cara-menghitung-harga-beras-per-porsi",
        "title": "Cara Menghitung Harga Beras per Porsi untuk Warung Makan",
        "h1": "Cara Menghitung Harga Beras per Porsi untuk Warung Makan",
        "description": "Cara menghitung harga beras per porsi untuk warung makan dan resto. Simak rumus food cost nasi matang, faktor yield 2.4x, dan simulasi margin usaha.",
        "keywords": "harga beras per porsi, cara menghitung food cost nasi, biaya nasi per piring warung makan, yield beras katering, margin keuntungan kuliner",
        "category_badge": "💼 Manajemen Bisnis Kuliner",
        "breadcrumb_title": "Harga Beras per Porsi",
        "read_time": "8",
        "key_takeaways": "Harga beras per kilogram tidak mencerminkan biaya nasi di piring konsumen. Menghitung food cost beras wajib menggunakan rumus: [Harga Beras per Kg / (Cooking Yield x 1.000)] x Gramasi Porsi Nasi Matang. Menggunakan beras ber-yield tinggi 2.4x seperti Beras Ladori mampu memotong biaya beras hingga Rp 150–Rp 250 per piring dibandingkan beras murah ber-yield rendah.",
        "body_html": """
<p class="lead text-lg font-medium text-slate-800">
  Banyak pemilik warung makan, warteg, restoran padang, dan kafe mengeluhkan margin usaha yang kian menipis saat harga beras di pasar merangkak naik. Namun ketika ditanya <em>"berapa sebenarnya biaya modal nasi putih di satu piring yang disajikan ke pelanggan?"</em>, sebagian besar hanya bisa memperkirakan dengan tebakan kasar.
</p>

<p>
  Menghitung harga beras per porsi secara presisi adalah fondasi paling awal dari <em>food cost control</em>. Memahami matematika sederhana ini akan membuka mata Anda mengapa membeli beras yang lebih murah per karung justru kerap kali membuat bisnis kuliner Anda rugi tanpa disadari.
</p>

<h2 class="text-2xl font-bold text-slate-900">Rumus Matematis Menghitung Biaya Nasi per Porsi</h2>
<p>
  Untuk menghitung food cost nasi matang per piring, gunakan rumus dua langkah berikut:
</p>

<div class="p-5 bg-brand-50 border-2 border-brand-200 rounded-2xl my-6 not-prose font-mono text-sm text-brand-950">
  <div class="font-bold text-base text-brand-900 mb-2">1. Hitung Jumlah Porsi per 1 Kg Beras Mentah:</div>
  <p class="pl-4">Jumlah Porsi = [ 1.000 gram &times; Cooking Yield ] &divide; Gramasi Nasi per Porsi</p>
  
  <div class="font-bold text-base text-brand-900 mt-4 mb-2">2. Hitung Modal Beras per Porsi:</div>
  <p class="pl-4">Biaya Beras per Porsi = Harga Beli Beras per Kg &divide; Jumlah Porsi yang Dihasilkan</p>
</div>

<h2 class="text-2xl font-bold text-slate-900">Simulasi Komparasi Riil: Beras Murah vs Beras Premium Ladori</h2>
<p>
  Mari kita bandingkan dua skenario nyata di dapur warung makan dengan target porsi nasi standar 150 gram per piring:
</p>

<div class="grid grid-cols-1 sm:grid-cols-2 gap-4 my-6 not-prose">
  <div class="p-5 bg-slate-50 border border-slate-200 rounded-2xl">
    <div class="text-xs font-bold text-slate-500 uppercase tracking-wider mb-1">Skenario A</div>
    <h3 class="text-lg font-bold text-slate-900 mb-2">Beras Murah Asalan (Broken Tinggi)</h3>
    <ul class="text-xs space-y-1.5 text-slate-700">
      <li><strong>Harga Beli:</strong> Rp 13.500 / kg</li>
      <li><strong>Cooking Yield:</strong> Hanya 2,0x (karena butir patah rapuh)</li>
      <li><strong>Hasil Nasi Matang:</strong> 2.000 gram</li>
      <li><strong>Porsi Didapat:</strong> 2.000 &divide; 150g = <strong>13,3 porsi</strong></li>
      <li><strong>Biaya per Porsi:</strong> Rp 13.500 &divide; 13,3 = <strong class="text-rose-700 text-sm font-bold">Rp 1.015 / porsi</strong></li>
    </ul>
    <p class="text-[11px] text-slate-500 mt-3 pt-2 border-t">
      Catatan: Nasi mudah patah, cepat kuning dan apek di warmer setelah jam makan siang.
    </p>
  </div>

  <div class="p-5 bg-emerald-50 border border-emerald-200 rounded-2xl">
    <div class="text-xs font-bold text-brand-700 uppercase tracking-wider mb-1">Skenario B</div>
    <h3 class="text-lg font-bold text-brand-950 mb-2">Beras Premium Ladori 25 Kg</h3>
    <ul class="text-xs space-y-1.5 text-brand-950">
      <li><strong>Harga Beli:</strong> Rp 14.500 / kg</li>
      <li><strong>Cooking Yield:</strong> 2,45x (butir utuh mekar maksimal)</li>
      <li><strong>Hasil Nasi Matang:</strong> 2.450 gram</li>
      <li><strong>Porsi Didapat:</strong> 2.450 &divide; 150g = <strong>16,3 porsi</strong></li>
      <li><strong>Biaya per Porsi:</strong> Rp 14.500 &divide; 16,3 = <strong class="text-emerald-700 text-sm font-bold">Rp 889 / porsi</strong></li>
    </ul>
    <p class="text-[11px] text-brand-800 mt-3 pt-2 border-t">
      Catatan: Nasi pulen putih bersih, aroma alami sedap, tahan hingga sore hari.
    </p>
  </div>
</div>

<div class="p-4 bg-amber-50 border-l-4 border-amber-500 rounded-r-xl my-6">
  <h3 class="text-base font-bold text-amber-900 mb-1">Kesimpulan Penghematan:</h3>
  <p class="text-sm text-amber-950">
    Meskipun Beras Ladori berharga Rp 1.000 lebih mahal per kilogram di depan, biaya modal nasi per porsinya justru <strong>LEBIH HEMAT Rp 126 per piring</strong>! Pada warung makan dengan penjualan 300 porsi per hari, efisiensi ini menghasilkan penghematan modal beras sebesar <strong>Rp 1.134.000 setiap bulannya</strong>, sekaligus meningkatkan kepuasan pelanggan berkat rasa nasi yang jauh lebih pulen dan nikmat.
  </p>
</div>

<p>
  Gunakan <a href="/tools/kalkulator-kebutuhan-beras" class="text-brand-700 font-bold hover:underline">kalkulator kebutuhan beras interaktif kami</a> untuk menghitung proyeksi biaya dapur Anda, dan pelajari lebih lanjut mengenai <a href="/artikel/1-kg-beras-berapa-porsi" class="text-brand-700 font-bold hover:underline">simulasi 1 kg beras jadi berapa porsi</a>.
</p>
""",
        "related_links_html": """
<a href="/tools/kalkulator-kebutuhan-beras" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Tool Interaktif</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Kalkulator Kebutuhan Beras & Food Cost</span>
    <p class="text-xs text-slate-500 mt-1">Hitung otomatis porsi, yield, dan biaya per piring warung makan.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Buka Tool &rarr;</span>
</a>
<a href="/program/katering-horeka" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Program Bisnis</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Program Pasokan Beras Resto & Katering</span>
    <p class="text-xs text-slate-500 mt-1">Harga grosir distributor tangan pertama untuk efisiensi margin usaha.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Pelajari Program &rarr;</span>
</a>
<a href="/artikel/1-kg-beras-berapa-porsi" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Simulasi Porsi</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">1 Kg Beras Jadi Berapa Porsi Nasi?</span>
    <p class="text-xs text-slate-500 mt-1">Panduan lengkap gramasi porsi kecil, standar resto, hingga prasmanan.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/artikel/cara-menghitung-stok-beras-sebulan" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Manajemen Stok</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Cara Menghitung Stok Beras Sebulan</span>
    <p class="text-xs text-slate-500 mt-1">Metode Reorder Point mencegah kehabisan beras di jam sibuk resto.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
"""
    },

    # --------------------------------------------------------------------------
    # 11. ARTIKEL #057: Cara Menghitung Stok Beras untuk Sebulan Tanpa Menimbun Berlebihan
    # --------------------------------------------------------------------------
    {
        "id": "OLD-057",
        "slug": "cara-menghitung-stok-beras-sebulan",
        "title": "Cara Menghitung Stok Beras Sebulan Tanpa Menimbun Lebih",
        "h1": "Cara Menghitung Stok Beras untuk Sebulan Tanpa Menimbun Berlebihan",
        "description": "Cara menghitung stok beras untuk sebulan bagi keluarga atau usaha kuliner. Terapkan safety stock, reorder point (ROP), dan cegah beras turun mutu.",
        "keywords": "stok beras sebulan, kebutuhan beras bulanan, reorder point beras, safety stock dapur, cara menyimpan beras agar tidak apek",
        "category_badge": "📦 Manajemen Gudang & Stok",
        "breadcrumb_title": "Stok Beras Sebulan",
        "read_time": "7",
        "key_takeaways": "Membeli beras dalam jumlah terlalu besar tanpa perhitungan matang meningkatkan risiko penurunan mutu, bau apek, dan serangan kutu gudang. Gunakan formula konsumsi nyata: [Jumlah Anggota x Rata-rata Konsumsi Harian x 30 Hari] + Safety Stock 10–15%. Terapkan sistem Reorder Point (ROP) agar pesanan baru tiba tepat sebelum stok minimal habis, menjaga beras selalu dalam kondisi segar panen.",
        "body_html": """
<p class="lead text-lg font-medium text-slate-800">
  Membeli beras dalam karung besar sekaligus untuk persediaan sebulan adalah kebiasaan banyak rumah tangga dan pelaku usaha kuliner di Indonesia. Alasan utamanya adalah kepraktisan: sekali beli, urusan pangan pokok beres. Namun jika pembelian tidak dihitung berdasarkan laju konsumsi nyata, stok beras yang mengendap terlalu lama di sudut dapur berisiko mengalami penurunan mutu, menyerap bau lembap, dan menjadi sarang kutu.
</p>

<p>
  Kunci manajemen persediaan yang bijak bukanlah menimbun sebanyak-banyaknya, melainkan menjaga <strong>aliran perputaran stok (inventory turnover)</strong> yang segar. Dengan menghitung kebutuhan riil dan menerapkan metode pengadaan berkala, Anda menikmati nasi segar berkualitas tinggi setiap hari tanpa ada beras yang terbuang sia-sia.
</p>

<h2 class="text-2xl font-bold text-slate-900">Rumus Menghitung Kebutuhan Beras Bulanan Rumah Tangga</h2>
<p>
  Rata-rata konsumsi beras orang dewasa di Indonesia adalah sekitar 250 hingga 300 gram beras mentah per hari (menghasilkan sekitar 600–700 gram nasi matang untuk 3 kali makan).
</p>

<div class="overflow-x-auto my-6">
  <table class="w-full text-left border-collapse border border-slate-200 text-sm">
    <thead>
      <tr class="bg-slate-100 text-slate-900 border-b">
        <th class="p-3 border">Jumlah Anggota Keluarga</th>
        <th class="p-3 border">Konsumsi Riil 30 Hari</th>
        <th class="p-3 border">Safety Buffer (+15%)</th>
        <th class="p-3 border">Rekomendasi Pembelian</th>
      </tr>
    </thead>
    <tbody>
      <tr class="border-b">
        <td class="p-3 border font-semibold">1 Orang (Mahasiswa / Pekerja)</td>
        <td class="p-3 border">7.5 – 9.0 kg</td>
        <td class="p-3 border">1.5 kg</td>
        <td class="p-3 border">Kemasan 5 kg &times; 2 pack</td>
      </tr>
      <tr class="border-b bg-slate-50">
        <td class="p-3 border font-semibold">2 Orang (Pasangan Muda)</td>
        <td class="p-3 border">15.0 – 18.0 kg</td>
        <td class="p-3 border">2.5 kg</td>
        <td class="p-3 border">Kemasan 5 kg &times; 4 pack atau 1 karung 20–25 kg</td>
      </tr>
      <tr class="border-b">
        <td class="p-3 border font-semibold">4 Orang (Keluarga Standar)</td>
        <td class="p-3 border">30.0 – 36.0 kg</td>
        <td class="p-3 border">4.0 kg</td>
        <td class="p-3 border font-bold text-brand-800">1 karung Beras Ladori 25 kg + 2 pack 5 kg</td>
      </tr>
      <tr class="border-b bg-slate-50">
        <td class="p-3 border font-semibold">6 Orang (Keluarga Besar / Kost)</td>
        <td class="p-3 border">45.0 – 54.0 kg</td>
        <td class="p-3 border">6.0 kg</td>
        <td class="p-3 border font-bold text-brand-800">2 karung Beras Ladori 25 kg (Sangat Pas)</td>
      </tr>
    </tbody>
  </table>
</div>

<h2 class="text-2xl font-bold text-slate-900">Menerapkan Reorder Point (Kapan Waktunya Membeli Lagi?)</h2>
<p>
  Di dapur usaha warung makan atau katering, jangan menunggu sampai beras di dasar tong benar-benar tandas baru memesan ke distributor. Terapkan prinsip <strong>Reorder Point (ROP)</strong>:
</p>

<div class="p-4 bg-slate-100 border border-slate-300 rounded-xl my-4 text-center font-mono text-sm font-bold text-slate-900">
  Reorder Point (Kg) = ( Rata-rata Konsumsi Harian &times; Waktu Pengiriman / Lead Time ) + Safety Stock
</div>

<p>
  <strong>Contoh Kasus Katering:</strong> Dapur katering Anda menghabiskan 25 kg beras per hari. Armada distributor Beras Ladori membutuhkan waktu pengiriman 1 hari kerja (lead time = 1 hari). Anda menetapkan safety stock cadangan darurat sebesar 25 kg (1 karung).
</p>
<p class="font-mono text-sm pl-4 text-slate-700">
  ROP = (25 kg &times; 1 hari) + 25 kg = <strong>50 kg (2 karung)</strong>.
</p>
<p>
  Begitu persediaan di gudang tersisa 2 karung, staf purchasing wajib segera melakukan <em>repeat order</em>. Ketika pesanan baru datang keesokan harinya, stok aman Anda tidak pernah kosong dan operasional dapur berjalan tanpa hambatan.
</p>

<h2 class="text-2xl font-bold text-slate-900">Keuntungan Berlangganan Pasokan Rutin Beras Ladori</h2>
<p>
  Daripada menimbun ratusan kilogram beras di tempat yang rawan lembap, bermitralah dengan distributor resmi yang memiliki jadwal pengiriman teratur. Melalui jaringan armada kami di <a href="/wilayah/muntilan" class="text-brand-700 font-bold hover:underline">Muntilan</a>, <a href="/wilayah/magelang" class="text-brand-700 font-bold hover:underline">Magelang</a>, Sleman, dan <a href="/wilayah/jogja" class="text-brand-700 font-bold hover:underline">Jogja</a>, <strong><a href="/produk/beras-ladori-25kg" class="text-brand-700 font-bold hover:underline">Beras Premium Ladori 25 kg</a></strong> siap diantar terjadwal sesuai ritme kebutuhan dapur Anda.
</p>
""",
        "related_links_html": """
<a href="/tools/kalkulator-kebutuhan-beras" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Utility Praktis</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Kalkulator Kebutuhan Beras Interaktif</span>
    <p class="text-xs text-slate-500 mt-1">Hitung kebutuhan stok bulanan keluarga atau usaha kuliner secara otomatis.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Buka Tool &rarr;</span>
</a>
<a href="/artikel/cara-menghitung-harga-beras-per-porsi" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Efisiensi Usaha</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Cara Menghitung Harga Beras per Porsi</span>
    <p class="text-xs text-slate-500 mt-1">Analisis margin food cost dan efisiensi yield nasi matang.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/artikel/cara-menyimpan-beras-25-kg" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Penyimpanan Aman</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Cara Menyimpan Beras 25 Kg agar Awet</span>
    <p class="text-xs text-slate-500 mt-1">Standar sanitasi wadah, pallet, dan ventilasi mencegah kutu dan apek.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/program/katering-horeka" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Layanan Pengiriman</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Jadwal Pengiriman Beras Katering Rutin</span>
    <p class="text-xs text-slate-500 mt-1">Kontrak pasokan mingguan dan bulanan dengan garansi ketepatan waktu.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Pelajari Layanan &rarr;</span>
</a>
"""
    },

    # --------------------------------------------------------------------------
    # 12. ARTIKEL #060: Cara Membaca Label Kemasan Beras Sebelum Membeli
    # --------------------------------------------------------------------------
    {
        "id": "OLD-060",
        "slug": "cara-membaca-label-kemasan-beras",
        "title": "Cara Membaca Label Kemasan Beras Sebelum Membeli",
        "h1": "Cara Membaca Label Kemasan Beras Sebelum Membeli",
        "description": "Cara membaca label kemasan beras sebelum membeli: nomor izin Kementan, kelas mutu premium/medium, tanggal kemas, dan klaim tanpa pemutih sintetis.",
        "keywords": "label kemasan beras, cara membaca label beras, izin kementan ri pd beras, tanggal kemas beras, izin edar psat beras",
        "category_badge": "🏷️ Regulasi & Konsumen",
        "breadcrumb_title": "Label Kemasan Beras",
        "read_time": "7",
        "key_takeaways": "Label kemasan beras adalah identitas resmi transparansi mutu dan keterlacakan keamanan pangan. Berdasarkan Permentan No. 31/2017 dan regulasi Bapanas, label wajib memuat 6 komponen kunci: merek dagang, kelas mutu (Premium/Medium), berat bersih, nama & alamat produsen/distributor, nomor registrasi izin edar (Kementan RI PD / PSAT), dan tanggal kemas. Beras tanpa label resmi memiliki risiko tinggi dicampur beras oplosan atau bahan kimia pemutih.",
        "body_html": """
<p class="lead text-lg font-medium text-slate-800">
  Bagi sebagian besar konsumen, memilih beras di toko sering kali hanya berfokus pada dua hal: gambar logo kemasan yang menarik dan harga per karung. Padahal, label yang tercetak di karung atau kantong beras menyimpan informasi krusial mengenai legalitas, kebersihan proses pabrikasi, jaminan keamanan bebas bahan berbahaya, serta kepastian kualitas butir.
</p>

<p>
  Kementerian Pertanian Republik Indonesia dan Badan Pangan Nasional (Bapanas) telah menetapkan regulasi ketat mengenai pelabelan beras kemasan. Memahami cara membaca label kemasan beras sebelum membeli adalah perisai terbaik Anda untuk menghindari produk beras oplosan, beras berpemutih klorin, atau beras afkir yang dikemas ulang dengan karung palsu.
</p>

<h2 class="text-2xl font-bold text-slate-900">6 Informasi Wajib pada Label Kemasan Beras Resmi</h2>
<div class="space-y-4 my-6 not-prose">
  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <h3 class="text-base font-bold text-slate-900 mb-1">1. Nama Merek & Identitas Produsen / Pengemas</h3>
    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
      Kemasan wajib mencantumkan nama produsen atau distributor resmi secara jelas beserta alamat kota produksi. Jangan membeli beras yang hanya bertuliskan 'Beras Pulen Cianjur' atau 'Beras Rojolele' tanpa ada nama badan usaha pengemas yang bertanggung jawab secara hukum.
    </p>
  </div>

  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <h3 class="text-base font-bold text-slate-900 mb-1">2. Kelas Mutu (Premium atau Medium)</h3>
    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
      Pernyataan kelas mutu wajib dicantumkan sesuai standar SNI. Jika berlabel <strong>Premium</strong>, butir kepala wajib minimal 85% (Ladori: &ge;95%) dan derajat sosoh minimal 95%. Pencantuman kelas mutu palsu melanggar Undang-Undang Perlindungan Konsumen No. 8/1999.
    </p>
  </div>

  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <h3 class="text-base font-bold text-slate-900 mb-1">3. Nomor Izin Edar Resmi (Kementan RI PD / PSAT)</h3>
    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
      Beras dalam kemasan bermerek wajib memiliki nomor Pendaftaran Produk Domestik (Kementan RI PD) atau Izin Edar Pangan Segar Asal Tumbuhan (PSAT) dari Otoritas Kompeten Keamanan Pangan Daerah (OKKPD). Nomor ini membuktikan bahwa pabrik dan produk telah diaudit bebas dari residu pestisida, timbal, dan pemutih.
    </p>
  </div>

  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <h3 class="text-base font-bold text-slate-900 mb-1">4. Berat Bersih (Netto)</h3>
    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
      Pencantuman berat bersih standar metrik (misalnya 5 kg, 10 kg, 25 kg). Produsen berintegritas menggunakan timbangan digital tersertifikasi tera metrologi legal sehingga berat karung tidak berkurang saat sampai di tangan pembeli.
    </p>
  </div>

  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <h3 class="text-base font-bold text-slate-900 mb-1">5. Tanggal Kemas & Kode Batch Produksi</h3>
    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
      Berbeda dengan makanan kaleng yang memiliki tanggal kedaluwarsa tetap, beras yang disimpan kering dapat bertahan lama. Namun tanggal kemas memberi tahu seberapa segar beras tersebut keluar dari mesin penggilingan. Pilihlah beras dengan tanggal kemas terbaru (di bawah 1–2 bulan).
    </p>
  </div>

  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <h3 class="text-base font-bold text-slate-900 mb-1">6. Keterangan Tanpa Bahan Pengawet & Pemutih</h3>
    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
      Pernyataan tertulis bahwa produk diproses secara higienis tanpa tambahan pemutih klorin, pewangi kimia sintetik, maupun pestisida pascapanen.
    </p>
  </div>
</div>

<h2 class="text-2xl font-bold text-slate-900">Transparansi Mutu Kemasan Beras Premium Ladori 25 Kg</h2>
<p>
  Sebagai produsen dan distributor beras resmi, <strong><a href="/produk/beras-ladori-25kg" class="text-brand-700 font-bold hover:underline">Beras Premium Ladori 25 kg</a></strong> menerapkan transparansi 100%. Kemasan kami terbuat dari karung anyaman bermutu tinggi yang dilengkapi label spesifikasi lengkap, nomor registrasi izin edar resmi, kode batch ketertelusuran (traceability), dan panduan penyimpanan higienis. Ini memberikan ketenangan mutlak bagi manajer katering, pengelola pesantren, serta <a href="/program/sppg-mbg" class="text-brand-700 font-bold hover:underline">tim procurement dapur gizi SPPG MBG</a>.
</p>
""",
        "related_links_html": """
<a href="/artikel/cara-membaca-coa-beras" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Audit Dokumen</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Cara Membaca Certificate of Analysis (COA) Beras</span>
    <p class="text-xs text-slate-500 mt-1">Memeriksa hasil uji lab klorin 0%, logam berat, dan pestisida.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/artikel/cara-memilih-beras-yang-bagus" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Checklist Fisik</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">12 Cara Memilih Beras yang Bagus</span>
    <p class="text-xs text-slate-500 mt-1">Uji visual, aroma, kadar air, dan keutuhan butir beras.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/produk/beras-ladori-25kg" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Produk Resmi</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Beras Ladori Kemasan 25 Kg</span>
    <p class="text-xs text-slate-500 mt-1">Karung berlabel resmi Kementan RI dengan sertifikasi mutu terpercaya.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Lihat Produk &rarr;</span>
</a>
<a href="/program/sppg-mbg" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Standar Keamanan</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Standar Beras Dapur MBG Terverifikasi</span>
    <p class="text-xs text-slate-500 mt-1">Pengadaan beras berizin edar resmi untuk program gizi nasional.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Pelajari Program &rarr;</span>
</a>
"""
    },

    # --------------------------------------------------------------------------
    # 13. ARTIKEL #089: Cara Menyimpan Beras 25 Kg di Rumah agar Tidak Cepat Turun Mutu
    # --------------------------------------------------------------------------
    {
        "id": "OLD-089",
        "slug": "cara-menyimpan-beras-25-kg",
        "title": "Cara Menyimpan Beras 25 Kg agar Tidak Cepat Turun Mutu",
        "h1": "Cara Menyimpan Beras 25 Kg di Rumah agar Tidak Cepat Turun Mutu",
        "description": "Cara menyimpan beras 25 kg di rumah atau gudang dapur usaha. Panduan memakai pallet, wadah kedap udara, kontrol kelembapan, dan sanitasi berkala.",
        "keywords": "cara menyimpan beras 25 kg, tips simpan beras karung, pallet beras gudang, beras tidak cepat kutuan, wadah beras kedap udara",
        "category_badge": "🛡️ Penyimpanan & Problem Solving",
        "breadcrumb_title": "Menyimpan Beras 25 Kg",
        "read_time": "7",
        "key_takeaways": "Menyimpan beras karung besar 25 kg membutuhkan tata kelola ruang yang baik: jangan meletakkan karung menempel langsung di lantai semen atau dinding (selalu gunakan alas pallet kayu/plastik minimal setinggi 10–15 cm untuk menghindari kondensasi uap dingin), simpan di ruangan sejuk kering dengan sirkulasi udara baik, dan pindahkan sebagian beras ke wadah dispenser harian kedap udara.",
        "body_html": """
<p class="lead text-lg font-medium text-slate-800">
  Membeli beras kemasan karung 25 kg adalah pilihan paling ekonomis bagi keluarga besar, asrama, katering, maupun warung makan. Harga per kilogramnya jauh lebih hemat dibandingkan membeli eceran kemasan 1 kg atau 5 kg. Namun kemasan 25 kg memiliki waktu habis yang lebih panjang (sering kali antara 3 hingga 6 minggu), sehingga jika disimpan sembarangan, butiran beras sangat rentan mengalami penurunan mutu.
</p>

<p>
  Musuh utama beras karung bukanlah kutu yang datang tiba-tiba dari luar, melainkan <strong>kelembapan udara (relative humidity)</strong> dan <strong>kondensasi suhu lantai</strong>. Berikut adalah panduan langkah demi langkah menyimpan beras karung 25 kg agar tetap harum, kering, dan higienis hingga butir terakhir.
</p>

<h2 class="text-2xl font-bold text-slate-900">5 Aturan Emas Menyimpan Beras Karung 25 Kg</h2>
<div class="space-y-4 my-6 not-prose">
  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <h3 class="text-base font-bold text-slate-900 mb-1">1. Wajib Menggunakan Pallet (Jangan Menempel Lantai Semen)</h3>
    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
      Lantai semen atau keramik memancarkan suhu dingin dari tanah bawah fondasi rumah. Ketika karung beras bersentuhan langsung dengan lantai dingin, terjadi peristiwa kondensasi uap air di lapisan karung bagian bawah. Dalam waktu 10 hari, beras di dasar karung akan menjadi lembap, mengeras membentuk bongkahan, dan berjamur apek. Selalu gunakan pallet kayu atau rak plastik berjarak minimal 10–15 cm dari lantai.
    </p>
  </div>

  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <h3 class="text-base font-bold text-slate-900 mb-1">2. Beri Jarak dari Dinding Tembok Minimal 15–20 Cm</h3>
    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
      Dinding tembok rumah menyerap kelembapan air hujan saat cuaca lembap. Meletakkan karung beras menempel rapat ke tembok akan menghalangi sirkulasi angin dan memicu pertumbuhan kutu di bagian belakang karung. Berikan ruang udara bebas di sekeliling tumpukan karung.
    </p>
  </div>

  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <h3 class="text-base font-bold text-slate-900 mb-1">3. Pindahkan Sebagian ke Wadah Kedap Udara Harian</h3>
    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
      Membuka-tutup ikatan karung besar 25 kg setiap kali hendak menanak nasi akan memasukkan udara lembap dapur dan partikel uap kompor ke dalam seluruh isi karung. Cara terbaik: ambil 5 kg beras dari karung, masukkan ke dalam wadah dispenser plastik food-grade kedap udara untuk pemakaian harian. Karung 25 kg diikat rapat kembali menggunakan klem atau tali pengikat.
    </p>
  </div>

  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <h3 class="text-base font-bold text-slate-900 mb-1">4. Ruangan Sejuk, Kering, dan Bebas Bau Tajam</h3>
    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
      Beras memiliki sifat higroskopis dan mudah menyerap bau lingkungan sekitar. Jangan pernah menyimpan karung beras di dekat deterjen pakaian, minyak tanah, tabung gas LPG, bawang merah/putih, atau bahan kimia pembersih lantai, karena aroma menyengat tersebut akan terserap ke dalam beras dan merusak rasa nasi.
    </p>
  </div>

  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <h3 class="text-base font-bold text-slate-900 mb-1">5. Terapkan Sistem FIFO (First-In, First-Out)</h3>
    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
      Jika Anda membeli lebih dari satu karung beras, habiskan karung yang dibeli lebih dulu sebelum membuka karung yang baru datang. Tuliskan tanggal penerimaan karung menggunakan spidol pada jahitan karung bagian atas.
    </p>
  </div>
</div>

<p>
  Di gudang pusat distribusi kami di <a href="/wilayah/muntilan" class="text-brand-700 font-bold hover:underline">Muntilan Magelang</a>, <strong><a href="/produk/beras-ladori-25kg" class="text-brand-700 font-bold hover:underline">Beras Premium Ladori 25 kg</a></strong> disimpan dengan protokol pergudangan modern ber-pallet plastik, pengontrol suhu ruang, dan sistem perputaran stok ketat. Beras yang kami kirim selalu berada dalam kondisi kesegaran maksimal.
</p>
""",
        "related_links_html": """
<a href="/artikel/beras-berkutu-masih-bisa-dimakan" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Problem Solving</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Beras Berkutu Masih Bisa Dimakan?</span>
    <p class="text-xs text-slate-500 mt-1">Panduan penyelamatan beras berkutu ringan dan kapan wajib dibuang.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/artikel/kadar-air-beras" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Sains Penyimpanan</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Kadar Air Beras & Ketahanan Simpan</span>
    <p class="text-xs text-slate-500 mt-1">Kadar air 13.5% sebagai kunci daya simpan beras tanpa pengawet.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/produk/beras-ladori-25kg" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Pilihan Kemasan</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Beras Premium Ladori Karung 25 Kg</span>
    <p class="text-xs text-slate-500 mt-1">Kemasan anyaman kuat food-grade menjaga mutu beras tetap stabil.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Lihat Produk &rarr;</span>
</a>
<a href="/wilayah/muntilan" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Pusat Gudang</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Gudang Logistik Muntilan Magelang</span>
    <p class="text-xs text-slate-500 mt-1">Armada pengiriman langsung siap kirim beras segar ke pintu dapur Anda.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Lihat Lokasi &rarr;</span>
</a>
"""
    },

    # --------------------------------------------------------------------------
    # 14. ARTIKEL #120: Panduan Memilih Beras: 12 Pemeriksaan Sebelum Membeli untuk Rumah atau Usaha
    # --------------------------------------------------------------------------
    {
        "id": "OLD-120",
        "slug": "cara-memilih-beras-yang-bagus",
        "title": "Cara Memilih Beras yang Bagus: 12 Panduan Inspeksi Mutu",
        "h1": "Panduan Memilih Beras: 12 Pemeriksaan Sebelum Membeli untuk Rumah atau Usaha",
        "description": "12 cara memilih beras yang bagus untuk rumah tangga dan usaha kuliner. Periksa visual, aroma, kelembapan, patahan menir, dan bebas zat kimia berbahaya.",
        "keywords": "cara memilih beras yang bagus, tips membeli beras berkualitas, checklist mutu beras, ciri beras bebas pemutih, beras pulen wangi alami",
        "category_badge": "🔍 Panduan Lengkap Mutu",
        "breadcrumb_title": "Memilih Beras yang Bagus",
        "read_time": "9",
        "key_takeaways": "Beras yang 'bagus' bukanlah beras yang paling putih mengilap di pasar. Memilih beras bermutu prima membutuhkan 12 titik inspeksi komprehensif yang mencakup aspek visual butir, aroma segar non-parfum kimiawi, tekstur kesat tidak bertepung, persentase butir utuh minimal 85–95%, ketiadaan butir kapur berlebih, kadar air terstandar 13–14%, legalitas izin edar Kementan RI, dan stabilitas hasil uji tanak di dapur.",
        "body_html": """
<p class="lead text-lg font-medium text-slate-800">
  Bagi masyarakat Indonesia, beras adalah sumber energi pokok harian. Namun di tengah banyaknya pilihan merek, kelas mutu, dan variasi harga di pasar, menemukan beras yang benar-benar berkualitas sering kali membingungkan. Terlebih lagi, maraknya pemberitaan tentang beras oplosan, beras berpemutih klorin, dan beras lama yang dipoles pewangi sintetis membuat konsumen harus semakin cermat.
</p>

<p>
  Beras yang bagus bukanlah satu produk seragam untuk semua orang. Rumah tangga mungkin mencari kepulenan lembut dan aroma sedap, sedangkan warung nasi goreng atau katering membutuhkan rendemen mekar tinggi dan ketahanan tidak mudah basi. Untuk membantu Anda memilih dengan percaya diri, berikut adalah <strong>12 pemeriksaan menyeluruh</strong> standar quality control (QC) yang dapat Anda terapkan langsung di pasar atau toko beras.
</p>

<h2 class="text-2xl font-bold text-slate-900">Checklist 12 Titik Pemeriksaan Mutu Beras</h2>

<div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-6 not-prose">
  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <div class="w-7 h-7 bg-brand-100 text-brand-800 rounded-lg flex items-center justify-center font-bold text-xs mb-2">1</div>
    <h3 class="text-sm font-bold text-slate-900 mb-1">Warna Bening Alami (Bukan Putih Mengilap)</h3>
    <p class="text-xs text-slate-600">
      Beras sehat berkualitas memiliki warna putih susu bening transparan alami. Hindari beras yang berwarna putih sangat mencolok seperti cat tembok atau mengilat licin seperti dilapisi minyak/lilin.
    </p>
  </div>

  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <div class="w-7 h-7 bg-brand-100 text-brand-800 rounded-lg flex items-center justify-center font-bold text-xs mb-2">2</div>
    <h3 class="text-sm font-bold text-slate-900 mb-1">Aroma Segar Gabah Baru (Bebas Parfum Sintetis)</h3>
    <p class="text-xs text-slate-600">
      Dekatkan segenggam beras ke hidung. Beras alami beraroma segar khas butir padi. Waspadai beras yang berbau wangi pandan terlalu tajam menusuk (indikasi esens kimia semprotan) atau tercium bau apek/tengik.
    </p>
  </div>

  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <div class="w-7 h-7 bg-brand-100 text-brand-800 rounded-lg flex items-center justify-center font-bold text-xs mb-2">3</div>
    <h3 class="text-sm font-bold text-slate-900 mb-1">Tekstur Kesat Kering Saat Digenggam</h3>
    <p class="text-xs text-slate-600">
      Genggam beras erat-erat lalu lepaskan. Beras dengan kadar air baik (13–14%) akan terasa kesat, padat, dan butirannya langsung jatuh terurai. Jika beras terasa dingin lembap atau menempel basah di telapak tangan, kadar airnya terlalu tinggi.
    </p>
  </div>

  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <div class="w-7 h-7 bg-brand-100 text-brand-800 rounded-lg flex items-center justify-center font-bold text-xs mb-2">4</div>
    <h3 class="text-sm font-bold text-slate-900 mb-1">Persentase Butir Kepala Tinggi (&ge;85–95%)</h3>
    <p class="text-xs text-slate-600">
      Perhatikan proporsi butir utuh. Beras kelas Premium memiliki beras kepala minimal 85% (Ladori: &ge;95%). Semakin banyak butir utuh, nasi matang akan semakin rapi dan tidak lembek berlendir.
    </p>
  </div>

  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <div class="w-7 h-7 bg-brand-100 text-brand-800 rounded-lg flex items-center justify-center font-bold text-xs mb-2">5</div>
    <h3 class="text-sm font-bold text-slate-900 mb-1">Minim Butir Patah dan Bebas Menir</h3>
    <p class="text-xs text-slate-600">
      Butir patah harus di bawah 15% pada kelas premium, dan serbuk menir mikro wajib 0%. Menir yang banyak akan membuat nasi matang menjadi benyek di dasar panci.
    </p>
  </div>

  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <div class="w-7 h-7 bg-brand-100 text-brand-800 rounded-lg flex items-center justify-center font-bold text-xs mb-2">6</div>
    <h3 class="text-sm font-bold text-slate-900 mb-1">Bebas Butir Kapur (Chalky Grains) Berlebih</h3>
    <p class="text-xs text-slate-600">
      Butir kapur adalah bagian beras yang berwarna putih keruh pekat seperti kapur tulis akibat gabah belum matang sempurna saat dipanen. Butir kapur sangat rapuh dan menurunkan tekstur pulen.
    </p>
  </div>

  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <div class="w-7 h-7 bg-brand-100 text-brand-800 rounded-lg flex items-center justify-center font-bold text-xs mb-2">7</div>
    <h3 class="text-sm font-bold text-slate-900 mb-1">Tidak Ada Butir Kuning, Rusak, & Mengapur</h3>
    <p class="text-xs text-slate-600">
      Butir kuning menandakan gabah pernah basah terfermentasi saat penumpukan sebelum digiling. Toleransi butir kuning pada beras premium maksimal hanya 0,5%.
    </p>
  </div>

  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <div class="w-7 h-7 bg-brand-100 text-brand-800 rounded-lg flex items-center justify-center font-bold text-xs mb-2">8</div>
    <h3 class="text-sm font-bold text-slate-900 mb-1">Bebas Benda Asing (Batu, Gabah, Kerikil)</h3>
    <p class="text-xs text-slate-600">
      Pabrik penggilingan modern wajib menggunakan mesin <em>destoner</em> pemisah batu. Beras premium berstandar 0% benda asing sehingga aman untuk gigi dan peralatan masak.
    </p>
  </div>

  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <div class="w-7 h-7 bg-brand-100 text-brand-800 rounded-lg flex items-center justify-center font-bold text-xs mb-2">9</div>
    <h3 class="text-sm font-bold text-slate-900 mb-1">Bebas Hama Gudang & Telur Kutu Hidup</h3>
    <p class="text-xs text-slate-600">
      Periksa celah-celah karung. Tidak boleh ada serangga <em>Sitophilus oryzae</em> yang merayap aktif, jaring kepompong, maupun butir berlubang kopong.
    </p>
  </div>

  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <div class="w-7 h-7 bg-brand-100 text-brand-800 rounded-lg flex items-center justify-center font-bold text-xs mb-2">10</div>
    <h3 class="text-sm font-bold text-slate-900 mb-1">Kadar Air Terstandar Maksimal 14%</h3>
    <p class="text-xs text-slate-600">
      Kadar air ideal adalah 13,2%–13,8%. Rentang ini memberikan ketahanan simpan 3–6 bulan tanpa risiko apek dan menjamin pemuaian nasi mekar saat ditanak.
    </p>
  </div>

  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <div class="w-7 h-7 bg-brand-100 text-brand-800 rounded-lg flex items-center justify-center font-bold text-xs mb-2">11</div>
    <h3 class="text-sm font-bold text-slate-900 mb-1">Legalitas Kemasan & Nomor Izin Kementan RI</h3>
    <p class="text-xs text-slate-600">
      Kemasan bermerek wajib mencantumkan nomor registrasi izin edar (Kementan RI PD / PSAT), identitas produsen jelas, dan informasi kelas mutu resmi.
    </p>
  </div>

  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <div class="w-7 h-7 bg-brand-100 text-brand-800 rounded-lg flex items-center justify-center font-bold text-xs mb-2">12</div>
    <h3 class="text-sm font-bold text-slate-900 mb-1">Konsistensi Hasil Uji Tanak Dapur (Yield Tinggi)</h3>
    <p class="text-xs text-slate-600">
      Uji masak 1 kg sampel. Nasi matang harus pulen mekar (yield min 2.3x–2.4x), rasa manis alami tidak hambar, dan tahan di warmer minimal 10 jam tanpa berair.
    </p>
  </div>
</div>

<h2 class="text-2xl font-bold text-slate-900">Jaminan Mutu Beras Premium Ladori</h2>
<p>
  Sebagai komitmen kami kepada masyarakat dan pelaku usaha kuliner di wilayah Jawa Tengah dan Yogyakarta, setiap butir <strong><a href="/produk/beras-ladori-25kg" class="text-brand-700 font-bold hover:underline">Beras Premium Ladori 25 kg</a></strong> telah melewati 12 titik inspeksi ketat ini di fasilitas pemrosesan modern kami. Dapatkan sampel uji tanak gratis untuk katering, restoran, dan lembaga Anda dengan menghubungi tim kami di <a href="/wilayah/magelang" class="text-brand-700 font-bold hover:underline">Magelang</a>.
</p>
""",
        "related_links_html": """
<a href="/artikel/kadar-air-beras" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Pemeriksaan Kunci</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Kadar Air Beras & Angka 14 Persen</span>
    <p class="text-xs text-slate-500 mt-1">Mengapa kelembapan butir sangat menentukan masa simpan beras.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/artikel/beras-premium-vs-medium" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Standar Mutu</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Beras Premium vs Medium: Bedanya Menurut SNI</span>
    <p class="text-xs text-slate-500 mt-1">Memahami parameter derajat sosoh, broken rice, dan kemurnian.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/produk/beras-ladori-25kg" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Produk Teruji</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Beras Premium Ladori 25 Kg</span>
    <p class="text-xs text-slate-500 mt-1">Lolos 12 titik inspeksi mutu ketat bebas bahan kimia sintetis.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Lihat Produk &rarr;</span>
</a>
<a href="/program/katering-horeka" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Kemitraan B2B</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Pasokan Beras Katering Horeka</span>
    <p class="text-xs text-slate-500 mt-1">Solusi pasokan beras stabil untuk usaha boga dan dapur institusi.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Pelajari Program &rarr;</span>
</a>
"""
    }
]

print(f"Loaded {len(p0_part2_articles)} articles in data_p0_part2.py")
