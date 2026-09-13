# -*- coding: utf-8 -*-
"""
Part 1 of Priority P0 Articles: #001, #009, #010, #014, #018, #022, #026
"""

p0_part1_articles = [
    # --------------------------------------------------------------------------
    # 1. ARTIKEL #001: 1 Kg Beras Jadi Berapa Porsi Nasi?
    # Merges: #003 (100 org), #004 (5 kg), #054 (50 org), #055 (200 org), #056 (10 kg)
    # --------------------------------------------------------------------------
    {
        "id": "OLD-001",
        "slug": "1-kg-beras-berapa-porsi",
        "title": "1 Kg Beras Berapa Porsi Nasi? Rumus & Simulasi Acara",
        "h1": "1 Kg Beras Jadi Berapa Porsi Nasi? Ini Cara Menghitungnya",
        "description": "1 kg beras jadi berapa porsi nasi? Simak hitungan akurat nasi kotak, prasmanan 50-200 orang, kalkulator porsi, dan tips hemat food cost usaha katering.",
        "keywords": "1 kg beras berapa porsi, 5 kg beras untuk berapa orang, beras 100 orang berapa kg, porsi nasi katering, takaran beras untuk hajatan",
        "category_badge": "🧮 Kalkulator & Kebutuhan Porsi",
        "breadcrumb_title": "1 Kg Beras Berapa Porsi",
        "read_time": "8",
        "key_takeaways": "1 kg beras mentah berkualitas baik menghasilkan sekitar 2,2 hingga 2,5 kg nasi matang. Untuk nasi kotak standar (150 gram nasi matang), 1 kg beras menghasilkan 15–16 porsi. Jangan pernah membagi berat beras mentah langsung dengan berat porsi; selalu gunakan rasio bobot nasi matang (cooking yield) dan sediakan safety margin 5–10% untuk acara.",
        "body_html": """
<p class="lead text-lg font-medium text-slate-800">
  Jawaban singkatnya, 1 kg beras tidak memiliki satu angka porsi mutlak yang berlaku untuk semua keadaan. Hasilnya bergantung pada dua faktor utama: <strong>berat nasi setelah matang (cooking yield)</strong> dan <strong>gramasi nasi yang diberikan per orang</strong>. Untuk perencanaan rumah tangga maupun usaha katering komersial, cara yang paling masuk akal adalah menghitung dari hasil nasi matang, bukan membagi 1.000 gram beras mentah langsung dengan porsi nasi.
</p>

<p>
  Saat ditanak, butir beras menyerap molekul air dalam jumlah besar melalui proses gelatinisasi pati sehingga bobot nasi matang meningkat pesat. Besarnya kenaikan bobot ini dipengaruhi oleh varietas beras, kadar air awal (ideal 13–14%), rasio amilosa, tingkat kepulenan, dan takaran air. Karena itu, bagi pelaku usaha katering dan pengadaan pangan, memahami konversi ini adalah kunci utama mengendalikan food cost tanpa risiko kekurangan porsi di hari acara.
</p>

<!-- INLINE QUICK CALCULATOR WIDGET -->
<div class="my-8 p-6 bg-gradient-to-br from-brand-50 to-slate-100 rounded-2xl border-2 border-brand-200 shadow-sm not-prose">
  <div class="flex items-center gap-2 mb-3">
    <span class="text-xl">🧮</span>
    <h3 class="text-base font-bold text-slate-900 m-0">Kalkulator Cepat Porsi Nasi Dapur</h3>
  </div>
  <p class="text-xs text-slate-600 mb-4">
    Masukkan jumlah porsi yang Anda butuhkan untuk melihat estimasi kebutuhan beras mentah secara instan:
  </p>
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 mb-4">
    <div>
      <label class="block text-xs font-semibold text-slate-700 mb-1">Target Porsi / Tamu</label>
      <input type="number" id="quickGuests" value="100" min="1" max="2000" class="w-full px-3 py-2 border rounded-lg text-sm font-bold" oninput="calcQuick()">
    </div>
    <div>
      <label class="block text-xs font-semibold text-slate-700 mb-1">Tipe Porsi Nasi Matang</label>
      <select id="quickPortion" class="w-full px-3 py-2 border rounded-lg text-sm font-medium" onchange="calcQuick()">
        <option value="130">Nasi Kotak Hemat (130g)</option>
        <option value="150" selected>Nasi Kotak Standar (150g)</option>
        <option value="200">Prasmanan Hajatan (200g)</option>
      </select>
    </div>
    <div>
      <label class="block text-xs font-semibold text-slate-700 mb-1">Hasil Kebutuhan Beras</label>
      <div id="quickResult" class="px-3 py-2 bg-brand-700 text-white rounded-lg text-sm font-black text-center">
        6.9 Kg Beras
      </div>
    </div>
  </div>
  <div class="flex items-center justify-between text-xs text-slate-500 pt-2 border-t border-slate-200">
    <span>Asumsi: Cooking Yield 2.4x + Cadangan Aman 10%</span>
    <a href="/tools/kalkulator-kebutuhan-beras" class="text-brand-700 font-bold hover:underline">Buka Kalkulator Lengkap Pengadaan &rarr;</a>
  </div>
</div>

<h2 class="text-2xl font-bold text-slate-900">Patokan Praktis: 1 Kg Beras Jadi Berapa Porsi Nasi?</h2>
<p>
  Beras berkualitas premium seperti <strong><a href="/produk/beras-ladori-25kg" class="text-brand-700 font-bold hover:underline">Beras Premium Ladori 25 kg</a></strong> dengan kadar amilosa sedang (20–22%) memiliki faktor pemuaian 2,3 hingga 2,5 kali lipat. Artinya, 1 kg beras mentah setelah dimasak menghasilkan sekitar <strong>2.300 hingga 2.500 gram (2,3–2,5 kg) nasi matang</strong>.
</p>
<p>
  Jika kita mengambil angka median praktis sebesar 2,4 kg (2.400 gram) nasi matang per 1 kg beras mentah, maka simulasinya adalah sebagai berikut:
</p>

<div class="overflow-x-auto my-6">
  <table class="w-full text-left border-collapse border border-slate-200 text-sm">
    <thead>
      <tr class="bg-slate-100 text-slate-900 border-b">
        <th class="p-3 border">Gramasi Nasi Matang</th>
        <th class="p-3 border">Peruntukan Menu</th>
        <th class="p-3 border">Hasil Porsi per 1 Kg Beras</th>
      </tr>
    </thead>
    <tbody>
      <tr class="border-b">
        <td class="p-3 border font-semibold">100 gram</td>
        <td class="p-3 border">Porsi anak-anak, diet rendah kalori, atau snack box</td>
        <td class="p-3 border font-bold text-brand-800">23 – 25 porsi</td>
      </tr>
      <tr class="border-b bg-slate-50">
        <td class="p-3 border font-semibold">130 gram</td>
        <td class="p-3 border">Nasi kotak ekonomis dengan lauk pauk padat</td>
        <td class="p-3 border font-bold text-brand-800">17 – 18 porsi</td>
      </tr>
      <tr class="border-b">
        <td class="p-3 border font-semibold">150 gram</td>
        <td class="p-3 border">Nasi kotak standar katering acara, kantor, dan syukuran</td>
        <td class="p-3 border font-bold text-brand-800">15 – 16 porsi</td>
      </tr>
      <tr class="border-b bg-slate-50">
        <td class="p-3 border font-semibold">180 – 200 gram</td>
        <td class="p-3 border">Porsi prasmanan pesta, hajatan, warung makan, dan pekerja lapangan</td>
        <td class="p-3 border font-bold text-brand-800">12 – 13 porsi</td>
      </tr>
      <tr class="border-b">
        <td class="p-3 border font-semibold">250 gram</td>
        <td class="p-3 border">Porsi jumbo nasi rames atau nasi liwet wareg</td>
        <td class="p-3 border font-bold text-brand-800">9 – 10 porsi</td>
      </tr>
    </tbody>
  </table>
</div>

<h2 class="text-2xl font-bold text-slate-900">Simulasi 5 Kg dan 10 Kg Beras untuk Berapa Orang?</h2>
<p>
  Bagi keluarga besar yang membeli beras kemasan 5 kg atau 10 kg, berikut adalah simulasi daya jangkau konsumsinya:
</p>
<ul class="list-disc pl-6 space-y-2">
  <li>
    <strong>5 Kg Beras untuk Berapa Orang?</strong> 5 kg beras menghasilkan sekitar 11,5 hingga 12,5 kg nasi matang. Jika rata-rata konsumsi harian keluarga adalah 3 kali makan per orang (sekitar 450 gram nasi matang/hari/orang), kemasan 5 kg mencukupi kebutuhan 1 orang selama 25–27 hari, atau untuk keluarga beranggotakan 4 orang selama 6–7 hari. Untuk sekali jamuan makan (misal rapat RT atau syukuran porsi 150g), 5 kg beras sanggup melayani <strong>75 hingga 80 orang</strong>.
  </li>
  <li>
    <strong>10 Kg Beras untuk Berapa Orang?</strong> Menghasilkan 23 hingga 25 kg nasi matang. Untuk konsumsi harian keluarga 4 orang, 10 kg beras habis dalam waktu 13–15 hari. Jika digunakan untuk acara katering atau selamatan dengan porsi 150 gram per tamu, 10 kg beras dapat mencukupi <strong>150 hingga 165 porsi nasi kotak</strong>, atau sekitar <strong>115 hingga 125 porsi prasmanan</strong> (asumsi porsi 180–200 gram per piring).
  </li>
</ul>

<h2 class="text-2xl font-bold text-slate-900">Simulasi Hajatan: Berapa Kg Beras untuk 50, 100, dan 200 Orang?</h2>
<p>
  Menyiapkan beras untuk acara besar memiliki risiko tersendiri: kekurangan nasi akan merusak reputasi acara, namun kelebihan berlebihan akan menimbulkan limbah (food waste). Berikut adalah panduan matematis dua tahap yang terbukti aman:
</p>

<div class="space-y-4 my-6">
  <div class="p-4 bg-slate-50 border rounded-xl">
    <h3 class="text-lg font-bold text-slate-900 mb-1">1. Kebutuhan Beras untuk 50 Orang</h3>
    <p class="text-sm text-slate-600">
      Untuk nasi kotak (150g/orang): 50 &times; 150g = 7,5 kg nasi matang. Dengan yield 2,4x, kebutuhan beras mentah murni adalah 3,12 kg. Tambahkan buffer cadangan 10%, maka disarankan memasak <strong>3,5 kg beras mentah</strong>. Jika prasmanan bebas ambil (200g/orang), sediakan <strong>4,5 kg beras mentah</strong>.
    </p>
  </div>

  <div class="p-4 bg-slate-50 border rounded-xl">
    <h3 class="text-lg font-bold text-slate-900 mb-1">2. Kebutuhan Beras untuk 100 Orang</h3>
    <p class="text-sm text-slate-600">
      Target 150g nasi matang: 100 &times; 150g = 15 kg nasi matang. Dibagi yield 2,4x = 6,25 kg beras mentah. Ditambah cadangan 10% untuk nasi menempel di centong/dandang, siapkan <strong>6,8 hingga 7 kg beras mentah</strong>. Untuk prasmanan pesta pernikahan, tamu cenderung mengambil porsi lebih leluasa (180–200g), sehingga kebutuhan aman adalah <strong>8,5 hingga 9 kg beras mentah</strong>.
    </p>
  </div>

  <div class="p-4 bg-slate-50 border rounded-xl">
    <h3 class="text-lg font-bold text-slate-900 mb-1">3. Kebutuhan Beras untuk 200 Orang Skala Besar</h3>
    <p class="text-sm text-slate-600">
      Pada skala 200 orang, selisih 20 gram per tamu setara dengan 4 kg nasi matang. Untuk 200 porsi nasi kotak, dibutuhkan 30 kg nasi matang = 12,5 kg beras mentah murni, atau <strong>14 kg beras mentah</strong> dengan buffer aman. Untuk prasmanan 200 orang, siapkan <strong>17 hingga 18 kg beras mentah</strong>. Memesan 1 karung <a href="/produk/beras-ladori-25kg" class="text-brand-700 font-bold hover:underline">Beras Ladori 25 kg</a> adalah solusi paling hemat dan memberikan rasa tenang karena sisa beras tetap awet tersimpan di karung kedap.
    </p>
  </div>
</div>

<h2 class="text-2xl font-bold text-slate-900">Mengapa Beras Ladori Lebih Mekar dan Menguntungkan Katering?</h2>
<p>
  Tidak semua beras di pasar menghasilkan rendemen porsi yang sama. Beras dengan butir patah (broken) tinggi di atas 25% atau kadar air basah (>14,5%) menyerap air secara tidak teratur, membuat tekstur nasi mudah lembek di bawah dan pera di atas. Sebaliknya, <strong>Beras Ladori</strong> diproses melalui penyortiran modern dengan kadar butir kepala utuh minimal 95% dan kadar air terukur 13,2–13,8%. Hasil tanaknya mengembang maksimal, berbutir rapi, tidak menggumpal, serta tetap pulen gurih hingga sore hari tanpa cepat basi di dalam warmer rice cooker.
</p>

<script>
  function calcQuick() {
    const guests = parseInt(document.getElementById('quickGuests').value) || 1;
    const portion = parseInt(document.getElementById('quickPortion').value) || 150;
    const cookedKg = (guests * portion / 1000) * 1.10; // buffer 10%
    const rawKg = cookedKg / 2.4;
    document.getElementById('quickResult').textContent = rawKg.toFixed(1) + ' Kg Beras';
  }
</script>
""",
        "related_links_html": """
<a href="/tools/kalkulator-kebutuhan-beras" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Utility Interaktif</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Kalkulator Kebutuhan Beras Otomatis</span>
    <p class="text-xs text-slate-500 mt-1">Hitung kebutuhan kg beras, buffer susut, dan estimasi food cost per porsi.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Buka Tool &rarr;</span>
</a>
<a href="/program/katering-horeka" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Layanan B2B</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Program Pasokan Beras Katering & Horeka</span>
    <p class="text-xs text-slate-500 mt-1">Solusi kontinuitas pasokan beras pulen mekar untuk usaha boga.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Pelajari Program &rarr;</span>
</a>
<a href="/artikel/cara-menghitung-harga-beras-per-porsi" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Manajemen Dapur</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Cara Menghitung Harga Beras per Porsi</span>
    <p class="text-xs text-slate-500 mt-1">Kalkulasi biaya riil nasi matang per piring untuk warung makan dan resto.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/artikel/cara-menghitung-stok-beras-sebulan" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Kontrol Stok</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Cara Menghitung Stok Beras Sebulan</span>
    <p class="text-xs text-slate-500 mt-1">Metode manajemen stok berkala tanpa risiko apek dan kutu.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
"""
    },

    # --------------------------------------------------------------------------
    # 2. ARTIKEL #009: Kadar Air Beras: Mengapa Angka 14 Persen Sangat Krusial?
    # --------------------------------------------------------------------------
    {
        "id": "OLD-009",
        "slug": "kadar-air-beras",
        "title": "Kadar Air Beras: Mengapa Angka 14 Persen Sangat Krusial?",
        "h1": "Kadar Air Beras: Mengapa Angka 14 Persen Sering Dibahas?",
        "description": "Mengapa kadar air beras maksimal 14% menurut SNI? Pahami pengaruhnya terhadap jamur, susut timbangan, daya simpan, dan tekstur tanak dapur komersial.",
        "keywords": "kadar air beras, batas kadar air sni, moisture meter beras, beras apek jamur, daya simpan beras",
        "category_badge": "🔬 Mutu, QC & Standar Beras",
        "breadcrumb_title": "Kadar Air Beras",
        "read_time": "7",
        "key_takeaways": "Angka 14% adalah batas maksimal kadar air beras berdasarkan SNI 6128:2020. Di atas 14%, aktivitas air memicu spora kapang Aspergillus dan kutu berkembang biak dengan cepat. Di bawah 12%, butir beras menjadi getas dan mudah hancur menjadi menir. Standar mutu Beras Ladori dijaga ketat pada kisaran 13,2%–13,8% untuk ketahanan simpan prima dan tekstur nasi pulen optimal.",
        "body_html": """
<p class="lead text-lg font-medium text-slate-800">
  Dalam perdagangan beras dan dokumen standar mutu pangan (SNI 6128:2020), angka <strong>14 persen</strong> hampir selalu disebut sebagai batas paling penting. Namun bagi konsumen rumah tangga atau bahkan pengelola dapur katering, angka ini sering kali terdengar seperti istilah teknis laboratorium yang abstrak. Apa sebenarnya makna kadar air, dan mengapa perbedaan 1–2 persen saja dapat menentukan nasib beras Anda?
</p>

<p>
  Secara sederhana, kadar air adalah persentase kandungan molekul air (H₂O) di dalam butir beras dibandingkan total bobot keseluruhannya. Air ini terikat secara fisiko-kimia di dalam jaringan pati endosperma. Mengontrol kadar air bukan sekadar mencegah pembeli membayar air dalam timbangan, melainkan pilar utama keamanan pangan, masa simpan, dan konsistensi rasa saat ditanak.
</p>

<h2 class="text-2xl font-bold text-slate-900">Bahaya Nyata Jika Kadar Air Beras di Atas 14 Persen</h2>
<p>
  Ketika kadar air beras melebihi ambang 14% (misalnya 14,5% hingga 16% akibat penjemuran gabah yang kurang tuntas atau penyimpanan di gudang lembap), serangkaian reaksi biologis yang merusak akan segera berlangsung:
</p>
<ul class="list-disc pl-6 space-y-2">
  <li>
    <strong>Aktivitas Air (aw) Memicu Jamur:</strong> Tingkat kelembapan tinggi menciptakan habitat ideal bagi spora jamur gudang seperti <em>Aspergillus flavus</em> dan <em>Penicillium</em>. Jamur ini memecah lemak beras menjadi asam lemak bebas yang menyebabkan bau apek (tengik) menyengat dan berisiko menghasilkan mikotoksin berbahaya.
  </li>
  <li>
    <strong>Ledakan Populasi Kutu Gudang:</strong> Kutu beras (<em>Sitophilus oryzae</em>) membutuhkan kelembapan butir minimal di atas 13,5% untuk mempercepat siklus penetasan telurnya. Beras basah adalah surga perkembangbiakan serangga.
  </li>
  <li>
    <strong>Kerugian Susut Bobot Timbangan:</strong> Beras dengan kadar air tinggi akan terus menguapkan air selama proses pengangkutan dan penyimpanan. Karung 25 kg yang dikemas pada kadar air 15% dapat menyusut menjadi 24,5 kg hanya dalam waktu dua minggu.
  </li>
</ul>

<h2 class="text-2xl font-bold text-slate-900">Risiko Jika Kadar Air Terlalu Rendah (Di Bawah 12 Persen)</h2>
<p>
  Sebagian orang mengira semakin kering beras, semakin baik mutunya. Pandangan ini keliru. Beras yang dikeringkan secara paksa di bawah 12% menghadapi masalah fisik yang serius:
</p>
<p>
  Butir pati endosperma kehilangan elastisitas alaminya sehingga butir beras menjadi sangat getas (brittle). Saat melewati mesin pemoles (polisher) atau saat dicuci di dapur, butir beras akan mudah patah (broken) dan retak-retak. Ketika dimasak, retakan tersebut melepaskan amilosa dan amilopektin secara liar, menghasilkan nasi yang berair di luar namun keras di dalam.
</p>

<h2 class="text-2xl font-bold text-slate-900">Tabel Komparasi Pengaruh Kadar Air pada Beras</h2>
<div class="overflow-x-auto my-6">
  <table class="w-full text-left border-collapse border border-slate-200 text-sm">
    <thead>
      <tr class="bg-slate-100 text-slate-900 border-b">
        <th class="p-3 border">Rentang Kadar Air</th>
        <th class="p-3 border">Kondisi Fisik & Daya Simpan</th>
        <th class="p-3 border">Kesesuaian Standar</th>
      </tr>
    </thead>
    <tbody>
      <tr class="border-b">
        <td class="p-3 border font-semibold">&lt; 12.0%</td>
        <td class="p-3 border">Butir getas, broken tinggi saat ditanak, tekstur cenderung pera keras</td>
        <td class="p-3 border text-amber-600 font-bold">Terlalu Kering</td>
      </tr>
      <tr class="border-b bg-emerald-50">
        <td class="p-3 border font-semibold">13.0% – 13.8%</td>
        <td class="p-3 border">Optimal. Nasi mekar pulen, tahan simpan 3–6 bulan tanpa apek, struktur butir kokoh</td>
        <td class="p-3 border text-brand-800 font-bold">Standar Beras Ladori (Golden Range)</td>
      </tr>
      <tr class="border-b">
        <td class="p-3 border font-semibold">14.0%</td>
        <td class="p-3 border">Batas toleransi maksimal menurut regulasi SNI dan Kementan RI</td>
        <td class="p-3 border text-slate-700 font-bold">Ambang Batas Maksimal SNI</td>
      </tr>
      <tr class="border-b bg-rose-50">
        <td class="p-3 border font-semibold">&gt; 14.5%</td>
        <td class="p-3 border">Rawan kapang, timbul bau apek dalam 7–14 hari, susut bobot tinggi, rawan kutu</td>
        <td class="p-3 border text-rose-700 font-bold">Substandar / Rawan Rusak</td>
      </tr>
    </tbody>
  </table>
</div>

<h2 class="text-2xl font-bold text-slate-900">Bagaimana Cara Mengukur Kadar Air dengan Akurat?</h2>
<p>
  Cara tradisional seperti menggigit butir beras hanya memberikan perkiraan kasar apakah beras sudah keras atau masih lunak. Di level pengadaan profesional, tim QC menggunakan <em>grain moisture tester</em> digital (seperti Kett Riceter atau model tusuk probe). Alat ini mengukur konduktivitas listrik atau dielektrik butir beras dan memberikan pembacaan presisi hingga dua angka di belakang koma dalam waktu 5 detik.
</p>

<p>
  Di gudang distribusi <a href="/produk/beras-ladori-25kg" class="text-brand-700 font-bold hover:underline">Beras Ladori 25 kg</a>, setiap batch gabah dan beras giling wajib lolos uji moisture meter di rentang 13,2%–13,8% sebelum diizinkan masuk ke lini pengemasan. Disiplin inilah yang menjamin katering dan mitra <a href="/program/sppg-mbg" class="text-brand-700 font-bold hover:underline">dapur SPPG MBG</a> menerima beras yang stabil dan tahan simpan lama.
</p>
""",
        "related_links_html": """
<a href="/artikel/cara-menggunakan-moisture-meter-beras" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Panduan Alat QC</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Cara Menggunakan Moisture Meter Beras</span>
    <p class="text-xs text-slate-500 mt-1">Protokol kalibrasi dan pembacaan alat pengukur kelembapan digital.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/artikel/beras-kepala-beras-patah-menir" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Standar Fisik</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Beras Kepala, Beras Patah, dan Menir</span>
    <p class="text-xs text-slate-500 mt-1">Memahami klasifikasi pecahan butir beras menurut standar mutu.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/produk/beras-ladori-25kg" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Produk Resmi</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Beras Premium Ladori 25 Kg</span>
    <p class="text-xs text-slate-500 mt-1">Kadar air terjamin 13.5%, derajat sosoh 95%, dan butir kepala 95%.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Lihat Produk &rarr;</span>
</a>
<a href="/program/sppg-mbg" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Program Institusi</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Pasokan Beras Dapur SPPG MBG</span>
    <p class="text-xs text-slate-500 mt-1">Pengadaan beras bebas klorin dan aman uji lab untuk program gizi.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Pelajari Program &rarr;</span>
</a>
"""
    },

    # --------------------------------------------------------------------------
    # 3. ARTIKEL #010: Apa Itu Beras Kepala, Beras Patah, dan Menir?
    # Merges: #059 (Beras Kepala & Mengapa Harganya Lebih Tinggi)
    # --------------------------------------------------------------------------
    {
        "id": "OLD-010",
        "slug": "beras-kepala-beras-patah-menir",
        "title": "Beras Kepala, Beras Patah, Menir: Panduan Mutu & Standar",
        "h1": "Apa Itu Beras Kepala, Beras Patah, dan Menir?",
        "description": "Pahami perbedaan beras kepala, butir patah (broken), dan menir sesuai SNI. Kenali pengaruhnya terhadap tekstur nasi, rendemen, dan food cost usaha.",
        "keywords": "beras kepala, beras patah broken, menir beras, standar sni beras premium, harga beras kepala",
        "category_badge": "🔬 Mutu, QC & Standar Beras",
        "breadcrumb_title": "Beras Kepala, Patah, Menir",
        "read_time": "8",
        "key_takeaways": "Beras kepala adalah butir utuh hingga minimal 80% panjang utuh. Butir patah (broken) berukuran 20%–80% panjang butir, dan menir berukuran kurang dari 20%. Tingginya persentase beras kepala (min 85–95% pada kelas premium) menentukan harga karena membutuhkan mesin sortir modern dan menghasilkan nasi berbutir rapi, tidak lembek berlendir, serta tidak cepat basi.",
        "body_html": """
<p class="lead text-lg font-medium text-slate-800">
  Saat membaca spesifikasi beras di lembar Certificate of Analysis (COA) atau kemasan resmi, Anda pasti menemukan istilah <strong>butir kepala (head rice)</strong>, <strong>butir patah (broken rice)</strong>, dan <strong>menir (brewers rice)</strong>. Ketiga kategori fraksi ini bukan sekadar istilah pembeda bentuk fisik, melainkan parameter utama yang menentukan kelas mutu, harga jual per kilogram, dan perilaku beras saat ditanak di dapur.
</p>

<p>
  Banyak pengelola dapur komersial tergiur membeli beras berharga miring, namun mengeluh nasinya cepat lembek, berair di warmer, atau menggumpal saat dibuat nasi goreng. Hampir 90% masalah tersebut berpangkal pada tingginya proporsi butir patah dan menir yang tidak disortir secara baik di pabrik penggilingan.
</p>

<h2 class="text-2xl font-bold text-slate-900">Klasifikasi Fraksi Beras Berdasarkan Standar SNI 6128:2020</h2>
<p>
  Standar Nasional Indonesia (SNI) membagi butir beras giling menjadi tiga fraksi ukuran yang sangat presisi:
</p>

<div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-6 not-prose">
  <div class="p-5 bg-white border border-slate-200 rounded-2xl shadow-sm">
    <div class="w-10 h-10 bg-brand-100 text-brand-800 rounded-xl flex items-center justify-center font-bold mb-3">1</div>
    <h3 class="text-base font-bold text-slate-900 mb-1">Beras Kepala (Head Rice)</h3>
    <p class="text-xs text-slate-600 leading-relaxed">
      Butir beras yang utuh sempurna atau bagian butir beras yang memiliki ukuran &ge; 0,8 (80%) dari rata-rata panjang butir utuh. Merupakan fraksi bernilai ekonomis paling tinggi.
    </p>
  </div>
  <div class="p-5 bg-white border border-slate-200 rounded-2xl shadow-sm">
    <div class="w-10 h-10 bg-amber-100 text-amber-800 rounded-xl flex items-center justify-center font-bold mb-3">2</div>
    <h3 class="text-base font-bold text-slate-900 mb-1">Butir Patah (Broken Rice)</h3>
    <p class="text-xs text-slate-600 leading-relaxed">
      Bagian butir beras yang patah dengan ukuran lebih besar dari 0,2 (20%) tetapi lebih kecil dari 0,8 (80%) bagian panjang butir utuh. Umum dijumpai pada beras kelas medium.
    </p>
  </div>
  <div class="p-5 bg-white border border-slate-200 rounded-2xl shadow-sm">
    <div class="w-10 h-10 bg-rose-100 text-rose-800 rounded-xl flex items-center justify-center font-bold mb-3">3</div>
    <h3 class="text-base font-bold text-slate-900 mb-1">Menir (Brewers Rice)</h3>
    <p class="text-xs text-slate-600 leading-relaxed">
      Pecahan butir beras yang sangat kecil berukuran &lt; 0,2 (20%) dari panjang butir utuh. Pada beras konsumsi manusia kelas premium, menir wajib ditekan hingga 0% atau maksimal 0,5%.
    </p>
  </div>
</div>

<h2 class="text-2xl font-bold text-slate-900">Mengapa Beras Kepala Harganya Lebih Tinggi? (Faktor Teknologi Sortir)</h2>
<p>
  Ketika gabah kering giling (GKG) digiling melalui mesin husker dan polisher, benturan mekanis secara alami memecahkan sebagian butir gabah. Pada penggilingan tradisional tanpa alat sortir, hasil gilingan biasanya mengandung 25% hingga 35% butir patah.
</p>
<p>
  Untuk menghasilkan beras berkategori <strong>Premium</strong> dengan beras kepala minimal 85% hingga 95%, pabrik harus mengalirkan beras melalui mesin penyortir canggih:
</p>
<ul class="list-disc pl-6 space-y-2">
  <li>
    <strong>Trieur Cylindrical Length Grader:</strong> Silinder berputar dengan lekukan mikro yang hanya meloloskan butir panjang utuh dan membuang butir patah ke saluran terpisah.
  </li>
  <li>
    <strong>Optical Color Sorter:</strong> Kamera berkecepatan tinggi yang menyortir butir berdasarkan warna dan bentuk mikro detik menggunakan hembusan angin katup pneumatik.
  </li>
</ul>
<p>
  Proses sortir ini mengurangi total bobot beras siap jual (yield susut karena pecahan disalurkan sebagai beras patah/pakan ternak yang bernilai jauh lebih rendah). Biaya investasi mesin dan susut volume inilah yang secara ilmiah menjelaskan mengapa harga beras kepala murni lebih mahal daripada beras asalan.
</p>

<h2 class="text-2xl font-bold text-slate-900">Pengaruh Proporsi Beras Kepala terhadap Kualitas Masakan</h2>
<p>
  Mengapa katering dan restoran sebaiknya memprioritaskan beras dengan butir kepala tinggi?
</p>
<p>
  Pada butir beras yang patah, dinding sel endosperma telah retak dan terbuka. Ketika terkena air panas saat ditanak, butir patah menyerap air jauh lebih cepat daripada butir utuh, melepaskan kandungan amilopektin lengket ke dalam air tanak. Akibatnya:
</p>
<ol class="list-decimal pl-6 space-y-2">
  <li><strong>Nasi Matang Tidak Merata:</strong> Butir patah sudah hancur menjadi bubur lembek, sementara butir utuh baru setengah matang.</li>
  <li><strong>Nasi Cepat Berlendir & Basi:</strong> Pelepasan pati bebas yang berlebih menciptakan lapisan gelatin basah di dasar rice cooker yang memicu fermentasi bakteri dalam waktu kurang dari 8 jam.</li>
  <li><strong>Penampilan Nasi Tidak Estetik:</strong> Butir nasi tidak tampak bulat panjang utuh, melainkan remuk dan saling menempel tidak rapi di piring tamu.</li>
</ol>

<p>
  Dengan memilih <strong><a href="/produk/beras-ladori-25kg" class="text-brand-700 font-bold hover:underline">Beras Premium Ladori 25 kg</a></strong> yang menjamin persentase butir kepala minimal 95%, dapur katering Anda mendapatkan butir nasi yang berpenampilan mewah, mekar maksimal, dan tahan disimpan di magic jar seharian tanpa berubah warna maupun bau.
</p>
""",
        "related_links_html": """
<a href="/artikel/beras-kepala-broken-menir-untuk-purchasing" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Panduan Purchasing</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Analisis Broken Rice untuk Dapur B2B</span>
    <p class="text-xs text-slate-500 mt-1">Teknik uji sampling laboratorium dan toleransi broken rice kontrak pengadaan.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/artikel/kadar-air-beras" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Standar Fisika</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Kadar Air Beras & Angka 14 Persen</span>
    <p class="text-xs text-slate-500 mt-1">Mengapa kelembapan butir sangat mempengaruhi daya simpan dan jamur.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/produk/beras-ladori-25kg" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Spesifikasi Resmi</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Beras Ladori 25 Kg: Butir Kepala 95%</span>
    <p class="text-xs text-slate-500 mt-1">Beras sosoh 95% bebas pemutih untuk katering, restoran, dan hotel.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Lihat Produk &rarr;</span>
</a>
<a href="/program/sppg-mbg" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Program SPPG MBG</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Spesifikasi Beras Dapur Bergizi Gratis</span>
    <p class="text-xs text-slate-500 mt-1">Panduan mutu beras aman dan sehat untuk program pemenuhan gizi anak.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Pelajari Program &rarr;</span>
</a>
"""
    },

    # --------------------------------------------------------------------------
    # 4. ARTIKEL #014: Apa Itu Rendemen Beras? Rumus dan Cara Menghitungnya
    # --------------------------------------------------------------------------
    {
        "id": "OLD-014",
        "slug": "rendemen-beras",
        "title": "Apa Itu Rendemen Beras? Rumus Hitung Gabah ke Beras Putih",
        "h1": "Apa Itu Rendemen Beras? Rumus dan Cara Menghitungnya",
        "description": "Apa itu rendemen beras? Pelajari rumus hitung konversi gabah ke beras giling, faktor varietas, kadar air, dan pengaruhnya pada efisiensi biaya usaha.",
        "keywords": "rendemen beras, rumus rendemen giling, konversi gabah ke beras, gkp ke gkg, rendemen masak nasi",
        "category_badge": "🔬 Mutu, QC & Standar Beras",
        "breadcrumb_title": "Rendemen Beras",
        "read_time": "7",
        "key_takeaways": "Rendemen beras adalah persentase bobot beras giling siap konsumsi yang dihasilkan dari sejumlah bobot gabah awal. Rata-rata rendemen giling gabah kering panen (GKP) ke beras putih berkisar antara 57% hingga 65%. Di tingkat dapur kuliner, rendemen masak (cooking yield) mengukur pemuaian beras menjadi nasi matang (2,2x–2,5x). Keduanya menjadi indikator paling vital dalam menentukan efisiensi biaya produksi.",
        "body_html": """
<p class="lead text-lg font-medium text-slate-800">
  Istilah <strong>rendemen</strong> adalah kata kunci yang paling sering menentukan untung rugi dalam industri perberasan nasional. Baik bagi penggilingan padi modern (rice milling plant) maupun bagi manajer purchasing katering dan restoran, rendemen adalah ukuran efisiensi konversi bahan mentah menjadi produk bernilai guna.
</p>

<p>
  Secara umum, terdapat dua jenis rendemen yang wajib dipahami pelaku usaha: <strong>Rendemen Giling (Milling Recovery)</strong> dari gabah ke beras putih, dan <strong>Rendemen Masak (Cooking Yield)</strong> dari beras mentah ke nasi matang di meja saji.
</p>

<h2 class="text-2xl font-bold text-slate-900">Rumus Rendemen Giling Beras (Pabrik / Penggilingan)</h2>
<p>
  Rendemen giling mengukur berapa kilogram beras putih siap jual yang berhasil diekstraksi dari setiap kilogram gabah kering giling (GKG). Rumusnya adalah:
</p>

<div class="p-4 bg-slate-100 border border-slate-300 rounded-xl my-4 text-center font-mono text-sm sm:text-base font-bold text-slate-900">
  Rendemen Giling (%) = [ Berat Beras Putih Dihasilkan (kg) &divide; Berat Gabah GKG (kg) ] &times; 100%
</div>

<p>
  <strong>Contoh Hitungan:</strong> Jika pabrik menggiling 1.000 kg Gabah Kering Giling (GKG) dan menghasilkan 640 kg beras sosoh putih bersih, maka rendemen gilingnya adalah:
</p>
<p class="font-mono text-sm pl-4 text-slate-700">
  (640 kg &divide; 1.000 kg) &times; 100% = <strong>64,0%</strong>
</p>
<p>
  Sisa 36% dari gabah terkonversi menjadi sekam/kulit gabah (sekitar 20–22%), bekatul/dedak halus (sekitar 8–10%), dan susut kotoran/debu (sekitar 4–6%). Di Indonesia, rendemen giling yang baik umumnya berada di rentang 62% hingga 66%.
</p>

<h2 class="text-2xl font-bold text-slate-900">Faktor yang Mempengaruhi Rendemen Giling</h2>
<ul class="list-disc pl-6 space-y-2">
  <li><strong>Kadar Air Gabah:</strong> Gabah yang terlalu basah (&gt;14%) akan hancur dan gepeng saat masuk rol karet husker. Gabah terlalu kering (&lt;12%) akan rapuh dan banyak pecah. Kadar air ideal penggilingan adalah 13,0%–13,5%.</li>
  <li><strong>Kematangan Panen:</strong> Gabah yang dipanen terlalu dini menghasilkan butir hijau/mengapur yang mudah remuk. Gabah lewat matang banyak retak di batang akibat siklus embun dan panas terik.</li>
  <li><strong>Teknologi Mesin:</strong> Penggilingan modern menggunakan rubber roll husker bertingkat dan polisher berpendingin udara (air-mist polisher) yang meminimalkan gesekan panas penyebab patah.</li>
</ul>

<h2 class="text-2xl font-bold text-slate-900">Rendemen Masak (Cooking Yield) untuk Dapur Katering</h2>
<p>
  Di tingkat dapur katering dan usaha kuliner, angka yang relevan adalah <strong>Rendemen Masak</strong> atau perbandingan berat nasi matang terhadap beras mentah:
</p>

<div class="p-4 bg-brand-50 border border-brand-300 rounded-xl my-4 text-center font-mono text-sm sm:text-base font-bold text-brand-950">
  Cooking Yield (Faktor Pengali) = Berat Nasi Matang (kg) &divide; Berat Beras Mentah (kg)
</div>

<p>
  Beras murah dengan kadar butir patah tinggi dan kadar air basah biasanya hanya memiliki yield 2,0x (1 kg beras jadi 2 kg nasi). Sebaliknya, <strong><a href="/produk/beras-ladori-25kg" class="text-brand-700 font-bold hover:underline">Beras Premium Ladori 25 kg</a></strong> memiliki yield 2,4x hingga 2,5x (1 kg beras jadi 2,4–2,5 kg nasi).
</p>
<p>
  Selisih 400 gram nasi matang per kilogram beras mentah ini menghasilkan tambahan 2 hingga 3 porsi nasi kotak gratis per kilogram beras yang Anda tanak, menurunkan food cost secara signifikan setiap bulannya.
</p>
""",
        "related_links_html": """
<a href="/artikel/cara-menghitung-cooking-yield-beras" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Metodologi Riset</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Cara Menghitung Cooking Yield Beras</span>
    <p class="text-xs text-slate-500 mt-1">Panduan uji tanak laboratorium untuk dapur komersial dan food cost.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/artikel/1-kg-beras-berapa-porsi" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Kalkulasi Porsi</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">1 Kg Beras Jadi Berapa Porsi Nasi?</span>
    <p class="text-xs text-slate-500 mt-1">Simulasi porsi nasi kotak dan prasmanan dengan rasio rendemen tanak.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/produk/beras-ladori-25kg" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Katalog Produk</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Beras Ladori 25 Kg Berkualitas Tinggi</span>
    <p class="text-xs text-slate-500 mt-1">Rendemen mekar 2.4x lipat untuk efisiensi maksimal usaha boga.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Lihat Produk &rarr;</span>
</a>
<a href="/program/sppg-mbg" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Pengadaan SPPG</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Standar Beras Dapur Gizi MBG</span>
    <p class="text-xs text-slate-500 mt-1">Pengadaan beras bersertifikasi dengan stabilitas mutu antar-batch.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Pelajari Program &rarr;</span>
</a>
"""
    },

    # --------------------------------------------------------------------------
    # 5. ARTIKEL #018: Beras untuk Catering: Memilih Tekstur, Rendemen, dan Konsistensi
    # --------------------------------------------------------------------------
    {
        "id": "OLD-018",
        "slug": "beras-untuk-catering",
        "title": "Beras untuk Catering: Tekstur, Rendemen, & Food Cost",
        "h1": "Beras untuk Catering: Memilih Tekstur, Rendemen, dan Konsistensi",
        "description": "Panduan memilih beras untuk catering: cara menjaga tekstur tidak mudah basi, rendemen nasi mekar 2.4x lipat, dan efisiensi food cost per porsi kotak.",
        "keywords": "beras untuk catering, supplier beras katering, beras nasi kotak pulen, rendemen beras katering, beras tidak cepat basi",
        "category_badge": "🍳 Cooking & Horeka",
        "breadcrumb_title": "Beras untuk Catering",
        "read_time": "8",
        "key_takeaways": "Beras untuk catering membutuhkan stabilitas tekstur unik: harus pulen namun butiran tetap terpisah (tidak lembek), rendemen tanak tinggi (min 2.4x), dan tahan disimpan di rice warmer atau box tertutup selama 6–8 jam tanpa mengeluarkan lendir atau aroma apek. Pilihlah beras dengan derajat sosoh 95% dan broken rice di bawah 5%.",
        "body_html": """
<p class="lead text-lg font-medium text-slate-800">
  Bagi pelaku bisnis boga, katering pernikahan, nasi kotak seminar, hingga kantin perusahaan, nasi putih bukan sekadar pelengkap hidangan. Nasi adalah komponen dengan volume piring terbesar (biasanya 50–60% dari total berat sajian) dan merupakan penentu utama apakah konsumen merasa kenyang dan puas dengan rasa masakan Anda.
</p>

<p>
  Namun memilih beras untuk katering jauh lebih kompleks daripada memilih beras konsumsi rumahan. Dapur rumah tangga hanya memasak 1–2 liter beras yang langsung dimakan hangat saat matang. Sebaliknya, dapur katering menanak puluhan kilogram sekaligus, mengemasnya dalam kotak tertutup bersuhu hangat lembap, atau menyajikannya di chafing dish pemanas prasmanan selama berjam-jam.
</p>

<h2 class="text-2xl font-bold text-slate-900">4 Kriteria Krusial Beras Standar Katering Komersial</h2>
<div class="space-y-4 my-6">
  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <h3 class="text-base font-bold text-slate-900 mb-1">1. Toleransi Terhadap Uap Tertutup (Nasi Kotak)</h3>
    <p class="text-sm text-slate-600">
      Saat nasi dimasukkan ke dalam kotak bento atau kardus tertutup, uap panas akan terperangkap. Beras dengan kadar butir patah tinggi atau amilopektin berlebih akan mengalami hidrolisis lanjut dan 'berkeringat', membuat nasi menjadi lembek basah dan basi dalam waktu kurang dari 6 jam. Beras katering yang baik harus memiliki struktur luar butir yang kokoh dan kadar air awal terukur 13,2%–13,8%.
    </p>
  </div>
  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <h3 class="text-base font-bold text-slate-900 mb-1">2. Ketahanan di Pemanas Prasmanan (Chafing Dish / Magic Warmer)</h3>
    <p class="text-sm text-slate-600">
      Pada acara resepsi prasmanan, nasi berada di chafing dish dengan api spirtus pemanas selama 4–6 jam. Beras yang rapuh akan mengering, mengeras seperti kerak di dasar wadah, dan berubah warna menjadi kekuningan. Beras dengan kadar amilosa sedang (20–22%) mempertahankan kelembapan internal tanpa cepat mengering.
    </p>
  </div>
  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <h3 class="text-base font-bold text-slate-900 mb-1">3. Cooking Yield / Daya Mekar (2.4x)</h3>
    <p class="text-sm text-slate-600">
      Beras yang mekar sempurna menghasilkan porsi lebih banyak dari berat mentah yang sama. Beras Ladori dengan yield 2,4x memberikan efisiensi luar biasa: 1 karung 25 kg menghasilkan 60 kg nasi matang, sanggup memenuhi 400 porsi nasi kotak standar 150 gram.
    </p>
  </div>
  <div class="p-4 bg-white border border-slate-200 rounded-xl shadow-sm">
    <h3 class="text-base font-bold text-slate-900 mb-1">4. Konsistensi Antar-Batch Sepanjang Tahun</h3>
    <p class="text-sm text-slate-600">
      Salah satu mimpi buruk juru masak katering adalah takaran air yang harus selalu diubah-ubah karena kualitas beras berubah setiap kali order. Supplier profesional wajib menjamin bahwa beras yang dikirim di musim hujan dan musim kemarau memiliki karakter masak yang identik.
    </p>
  </div>
</div>

<h2 class="text-2xl font-bold text-slate-900">Perbandingan Kebutuhan Nasi Kotak vs Prasmanan</h2>
<div class="overflow-x-auto my-6">
  <table class="w-full text-left border-collapse border border-slate-200 text-sm">
    <thead>
      <tr class="bg-slate-100 text-slate-900 border-b">
        <th class="p-3 border">Parameter</th>
        <th class="p-3 border">Katering Nasi Kotak</th>
        <th class="p-3 border">Prasmanan / Pesta Resepsi</th>
      </tr>
    </thead>
    <tbody>
      <tr class="border-b">
        <td class="p-3 border font-semibold">Gramasi Porsi Nasi</td>
        <td class="p-3 border">130 – 150 gram per porsi</td>
        <td class="p-3 border">180 – 220 gram per porsi</td>
      </tr>
      <tr class="border-b bg-slate-50">
        <td class="p-3 border font-semibold">Toleransi Uap Panas</td>
        <td class="p-3 border">Tinggi (ruang sempit kedap udara)</td>
        <td class="p-3 border">Sedang (ruang terbuka berventilasi)</td>
      </tr>
      <tr class="border-b">
        <td class="p-3 border font-semibold">Kebutuhan Cadangan (Buffer)</td>
        <td class="p-3 border">5% (jumlah kotak terhitung pasti)</td>
        <td class="p-3 border">10% – 15% (tamu mengambil sendiri)</td>
      </tr>
      <tr class="border-b bg-slate-50">
        <td class="p-3 border font-semibold">Rekomendasi Beras Ladori</td>
        <td class="p-3 border font-bold text-brand-800">Beras Premium Ladori 25 Kg</td>
        <td class="p-3 border font-bold text-brand-800">Beras Premium Ladori 25 Kg</td>
      </tr>
    </tbody>
  </table>
</div>

<p>
  Melalui program kemitraan resmi <strong><a href="/program/katering-horeka" class="text-brand-700 font-bold hover:underline">Distributor Beras Katering & Horeka Ladori</a></strong>, kami melayani pengiriman terjadwal langsung ke dapur operasional Anda di wilayah <a href="/wilayah/jogja" class="text-brand-700 font-bold hover:underline">Yogyakarta</a>, Sleman, Muntilan, dan Magelang dengan jaminan sampel tester gratis dan kontinuitas pasokan terpercaya.
</p>
""",
        "related_links_html": """
<a href="/program/katering-horeka" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Layanan B2B</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Pasokan Beras Katering & Horeka</span>
    <p class="text-xs text-slate-500 mt-1">Paket pengadaan beras khusus dapur hotel, restoran, dan katering.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Pelajari Program &rarr;</span>
</a>
<a href="/wilayah/jogja" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Jangkauan Wilayah</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Distributor Beras Katering Jogja</span>
    <p class="text-xs text-slate-500 mt-1">Layanan antar armada langsung ke dapur kuliner Kota Yogyakarta.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Lihat Wilayah &rarr;</span>
</a>
<a href="/artikel/1-kg-beras-berapa-porsi" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Hitung Porsi</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">1 Kg Beras Jadi Berapa Porsi Nasi?</span>
    <p class="text-xs text-slate-500 mt-1">Simulasi akurat porsi nasi kotak dan prasmanan untuk acara boga.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/produk/beras-ladori-25kg" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Produk Unggulan</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Beras Ladori Kemasan 25 Kg</span>
    <p class="text-xs text-slate-500 mt-1">Standar mutu beras premium teruji laboratorium bebas zat kimia.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Lihat Produk &rarr;</span>
</a>
"""
    },

    # --------------------------------------------------------------------------
    # 6. ARTIKEL #022: Beras Berkutu Masih Bisa Dimakan atau Harus Dibuang?
    # Merges: #021 (Apakah Kutu Beras Berbahaya?)
    # --------------------------------------------------------------------------
    {
        "id": "OLD-022",
        "slug": "beras-berkutu-masih-bisa-dimakan",
        "title": "Beras Berkutu Masih Bisa Dimakan? Panduan Keamanan & Cara",
        "h1": "Beras Berkutu Masih Bisa Dimakan atau Harus Dibuang?",
        "description": "Beras berkutu masih bisa dimakan atau harus dibuang? Simak fakta keamanan pangan, siklus Sitophilus oryzae, dan cara mencuci yang benar tanpa rugi.",
        "keywords": "beras berkutu masih bisa dimakan, bahaya kutu beras, cara membersihkan beras berkutu, sitophilus oryzae, beras apek berbubuk",
        "category_badge": "🛡️ Penyimpanan & Problem Solving",
        "breadcrumb_title": "Beras Berkutu",
        "read_time": "7",
        "key_takeaways": "Kutu beras (Sitophilus oryzae) tidak berbisa, tidak menularkan penyakit menular, dan tidak menghasilkan racun kimia mematikan. Namun infestasi berat merusak nilai gizi, menghasilkan serbuk kotoran pemicu alergi pernapasan, dan menurunkan tekstur beras. Jika beras hanya memiliki sedikit kutu, beras masih aman dicuci dan dikonsumsi. Tetapi jika beras sudah berbau apek, berjamur, atau hancur menjadi bubuk, beras wajib dibuang.",
        "body_html": """
<p class="lead text-lg font-medium text-slate-800">
  Membuka karung atau wadah penyimpanan beras dan menemukan serangga hitam kecil merayap di antara butiran beras tentu menimbulkan rasa geli dan panik. Pertanyaan langsung yang muncul di benak setiap ibu rumah tangga dan pengelola dapur adalah: <em>apakah beras berkutu ini masih aman dimakan, atau harus langsung dibuang ke tempat sampah?</em>
</p>

<p>
  Jawaban medis dan sains keamanannya bergantung pada <strong>tingkat kerusakan fisik dan tanda pembusukan sekunder</strong> pada beras tersebut. Menemukan beberapa ekor kutu bukanlah vonis keracunan makanan otomatis, namun membiarkannya berkembang biak tanpa penanganan akan merusak seluruh stok beras Anda.
</p>

<h2 class="text-2xl font-bold text-slate-900">Apakah Kutu Beras Berbahaya bagi Tubuh Manusia?</h2>
<p>
  Kutu beras yang paling umum di Indonesia adalah kumbang moncong bernama ilmiah <em>Sitophilus oryzae</em>. Berikut fakta biologisnya:
</p>
<ul class="list-disc pl-6 space-y-2">
  <li><strong>Tidak Beracun / Tidak Berbisa:</strong> Kutu beras tidak memiliki kelenjar racun, tidak menyengat, dan tidak menggigit manusia. Secara biologis, mereka murni memakan endosperma pati biji-bijian.</li>
  <li><strong>Bukan Vektor Penyakit Menular:</strong> Berbeda dengan lalat atau kecoak yang hinggap di kotoran selokan, kutu beras menghabiskan seluruh hidupnya di lingkungan kering biji-bijian, sehingga tidak membawa kuman tipus atau kolera.</li>
  <li><strong>Risiko Alergi Serbuk & Kotoran (Frass):</strong> Pada infestasi parah, kutu meninggalkan serbuk buangan (frass), bangkai kering, dan partikel kitin mikro. Bagi individu dengan asma atau alergi debu, menghirup atau mengonsumsi serbuk ini tanpa dicuci bersih dapat memicu reaksi iritasi pernapasan dan kulit.</li>
</ul>

<h2 class="text-2xl font-bold text-slate-900">Kapan Beras Berkutu WAJIB Dibuang? (4 Tanda Kritis)</h2>
<p>
  Jika kondisi beras Anda sudah menunjukkan tanda-tanda berikut, jangan dikonsumsi lagi:
</p>
<div class="grid grid-cols-1 sm:grid-cols-2 gap-4 my-6 not-prose">
  <div class="p-4 bg-rose-50 border border-rose-200 rounded-xl">
    <h3 class="text-sm font-bold text-rose-900 mb-1">1. Bau Apek Menyengat / Tengik</h3>
    <p class="text-xs text-rose-800">
      Kutu yang berkoloni meningkatkan kelembapan mikro, memicu jamur dan hidrolisis asam lemak. Nasi yang dimasak dari beras berbau apek akan berasa pahit dan tidak layak makan.
    </p>
  </div>
  <div class="p-4 bg-rose-50 border border-rose-200 rounded-xl">
    <h3 class="text-sm font-bold text-rose-900 mb-1">2. Butir Beras Keropos & Hancur Jadi Bubuk</h3>
    <p class="text-xs text-rose-800">
      Larva kutu melubangi butiran dari dalam hingga tersisa cangkang kopong. Jika diangkat segenggam terasa berdebu seperti tepung rapuh, nilai karbohidrat beras sudah habis.
    </p>
  </div>
  <div class="p-4 bg-rose-50 border border-rose-200 rounded-xl">
    <h3 class="text-sm font-bold text-rose-900 mb-1">3. Terdapat Gumpalan Jaring Jamur</h3>
    <p class="text-xs text-rose-800">
      Jika butiran beras saling menggumpal membentuk sarang dengan benang hifa putih atau keabu-abuan, ini adalah tanda kapang toksik yang memproduksi aflatoksin.
    </p>
  </div>
  <div class="p-4 bg-rose-50 border border-rose-200 rounded-xl">
    <h3 class="text-sm font-bold text-rose-900 mb-1">4. Warna Beras Menguning / Menghitam</h3>
    <p class="text-xs text-rose-800">
      Perubahan warna drastis menunjukkan kerusakan enzimatis dan kimiawi tingkat lanjut yang sudah tidak dapat diselamatkan dengan pencucian biasa.
    </p>
  </div>
</div>

<h2 class="text-2xl font-bold text-slate-900">Cara Membersihkan Beras yang Baru Terinfestasi Kutu Ringan</h2>
<p>
  Jika butiran masih kokoh, tidak apek, dan hanya terlihat beberapa ekor kutu, lakukan langkah penyelamatan higienis ini:
</p>
<ol class="list-decimal pl-6 space-y-2">
  <li><strong>Jemur di Bawah Terik Matahari Tidak Langsung:</strong> Tebarkan beras di atas tampah beralas kain bersih. Kutu sangat sensitif terhadap panas dan udara kering, sehingga mereka akan merayap keluar dari butiran beras dalam 30–45 menit.</li>
  <li><strong>Ayak Serbuk Menir:</strong> Gunakan saringan kawat untuk menyaring serbuk kotoran dan telur kutu mikro yang tertinggal di dasar.</li>
  <li><strong>Cuci Bersih dengan Air Mengalir:</strong> Kutu dan butiran beras kopong yang berlubang akan mengapung ke permukaan air saat dicuci. Buang air lapisan atas tersebut hingga air cucian jernih.</li>
</ol>

<p>
  Untuk pencegahan jangka panjang, simpan beras di tempat sejuk kering berventilasi baik dengan wadah kedap udara. Pelajari panduan lengkap penyimpanan di artikel <a href="/artikel/cara-menyimpan-beras-25-kg" class="text-brand-700 font-bold hover:underline">cara menyimpan beras 25 kg</a> agar stok beras <a href="/produk/beras-ladori-25kg" class="text-brand-700 font-bold hover:underline">Beras Premium Ladori 25 kg</a> Anda di gudang <a href="/wilayah/muntilan" class="text-brand-700 font-bold hover:underline">Muntilan Magelang</a> tetap terlindungi dari serangan hama.
</p>
""",
        "related_links_html": """
<a href="/artikel/cara-menyimpan-beras-25-kg" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Gudang & Rumah</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Cara Menyimpan Beras 25 Kg agar Tidak Apek</span>
    <p class="text-xs text-slate-500 mt-1">Panduan pallet kayu, kontrol suhu, dan wadah kedap udara aman.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/artikel/kadar-air-beras" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Faktor Kelembapan</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Kadar Air Beras & Angka 14 Persen</span>
    <p class="text-xs text-slate-500 mt-1">Mengapa kelembapan butir memicu perkembangan biak serangga gudang.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/produk/beras-ladori-25kg" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Produk Higienis</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Beras Premium Ladori 25 Kg</span>
    <p class="text-xs text-slate-500 mt-1">Bebas kutu, kadar air stabil 13.5%, dan kemasan karung rapi.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Lihat Produk &rarr;</span>
</a>
<a href="/wilayah/muntilan" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Gudang Distribusi</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Distributor Beras Muntilan Magelang</span>
    <p class="text-xs text-slate-500 mt-1">Pusat pasokan logistik beras berkualitas se-Jawa Tengah & DIY.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Lihat Lokasi &rarr;</span>
</a>
"""
    },

    # --------------------------------------------------------------------------
    # 7. ARTIKEL #026: Takaran Air untuk 1 Kg Beras agar Pulen dan Tidak Lembek
    # Merges: #027 (1 Gelas Beras Berapa Gelas Air?)
    # --------------------------------------------------------------------------
    {
        "id": "OLD-026",
        "slug": "takaran-air-untuk-1-kg-beras",
        "title": "Takaran Air untuk 1 Kg Beras agar Pulen & Tidak Lembek",
        "h1": "Takaran Air untuk 1 Kg Beras agar Pulen dan Tidak Lembek",
        "description": "Takaran air untuk 1 kg beras yang tepat agar nasi pulen, matang merata, dan tidak lembek. Panduan rasio air, uji varietas, dan tips rice cooker.",
        "keywords": "takaran air untuk 1 kg beras, 1 gelas beras berapa gelas air, cara memasak beras pulen, rasio air beras, nasi tidak lembek",
        "category_badge": "🍳 Cooking & Dapur",
        "breadcrumb_title": "Takaran Air Beras",
        "read_time": "7",
        "key_takeaways": "Takaran air standar untuk 1 kg beras pulen berkisar antara 1,1 hingga 1,3 liter air (rasio gravimetrik 1 : 1,2). Menggunakan metode tradisional ruas jari sering meleset saat diameter panci berubah. Gunakan rasio gelas (1 gelas beras butuh 1,2–1,3 gelas air untuk pulen, atau 1,5 gelas untuk beras pera) agar hasil tanak konsisten setiap hari.",
        "body_html": """
<p class="lead text-lg font-medium text-slate-800">
  Berapa liter air yang dibutuhkan untuk memasak 1 kg beras agar nasinya pulen pas, tidak lembek berlendir, dan tidak keras pera? Pertanyaan ini terlihat sepele, namun di dapur katering atau warung makan yang menanak nasi berkali-kali setiap hari, ketidaktepatan takaran air adalah penyebab nomor satu nasi terbuang sia-sia.
</p>

<p>
  Banyak orang masih mengandalkan takaran tradisional: mencelupkan jari telunjuk ke dalam air di atas beras hingga batas ruas pertama. Mengapa cara turun-temurun ini sering gagal total saat Anda menanak beras dalam jumlah banyak? Mari kita bedah sains di baliknya.
</p>

<h2 class="text-2xl font-bold text-slate-900">Mengapa Metode 'Ruas Jari' Sering Menipu?</h2>
<p>
  Metode ruas jari mengukur <em>ketinggian vertikal</em> air di atas permukaan beras. Namun secara geometri fisika, volume air adalah luas penampang panci dikalikan tinggi air ($V = \pi r^2 h$).
</p>
<ul class="list-disc pl-6 space-y-2">
  <li>Jika Anda memakai panci kecil berdiameter 16 cm, tinggi air 1 ruas jari setara dengan sekitar 300 ml air.</li>
  <li>Jika Anda memakai panci komersial berdiameter 36 cm, tinggi air 1 ruas jari yang sama setara dengan hampir 1.500 ml (1,5 liter) air!</li>
</ul>
<p>
  Akibatnya, ketika berpindah dari rice cooker kecil ke dandang katering besar, metode ruas jari akan memasukkan air berlebihan hingga nasi menjadi bubur basah. Cara yang benar dan profesional adalah menggunakan <strong>rasio terukur</strong> (bobot timbangan atau perbandingan gelas ukur yang sama).
</p>

<h2 class="text-2xl font-bold text-slate-900">Panduan Takaran Air untuk 1 Kg Beras Berdasarkan Karakter</h2>
<div class="overflow-x-auto my-6">
  <table class="w-full text-left border-collapse border border-slate-200 text-sm">
    <thead>
      <tr class="bg-slate-100 text-slate-900 border-b">
        <th class="p-3 border">Karakter Beras</th>
        <th class="p-3 border">Takaran Air per 1 Kg Beras</th>
        <th class="p-3 border">Hasil Tekstur Nasi</th>
      </tr>
    </thead>
    <tbody>
      <tr class="border-b">
        <td class="p-3 border font-semibold">Beras Pulen Lembut (Kadar Air 13.5%, misal C4/Mentik)</td>
        <td class="p-3 border font-bold text-brand-800">1.1 – 1.2 Liter Air (1.100 – 1.200 ml)</td>
        <td class="p-3 border">Pulen, lembut, butiran mengkilap rapi</td>
      </tr>
      <tr class="border-b bg-slate-50">
        <td class="p-3 border font-semibold">Beras Premium Ladori 25 Kg (All-Rounder Katering)</td>
        <td class="p-3 border font-bold text-brand-800">1.2 – 1.25 Liter Air (1.200 – 1.250 ml)</td>
        <td class="p-3 border">Pulen mekar, tidak lengket, kokoh untuk nasi kotak</td>
      </tr>
      <tr class="border-b">
        <td class="p-3 border font-semibold">Beras Pera Sedang (IR64 / Ciherang kering simpan lama)</td>
        <td class="p-3 border font-bold text-brand-800">1.3 – 1.4 Liter Air (1.300 – 1.400 ml)</td>
        <td class="p-3 border">Butiran terpisah, cocok untuk nasi goreng & padang</td>
      </tr>
      <tr class="border-b bg-slate-50">
        <td class="p-3 border font-semibold">Beras Ketan / Nasi Uduk Gurih Santan</td>
        <td class="p-3 border font-bold text-brand-800">0.9 – 1.0 Liter Cairan (Air + Santan)</td>
        <td class="p-3 border">Kenyal padat, tidak kelembekan</td>
      </tr>
    </tbody>
  </table>
</div>

<h2 class="text-2xl font-bold text-slate-900">Konversi Praktis: 1 Gelas Beras Butuh Berapa Gelas Air?</h2>
<p>
  Jika Anda memasak tanpa timbangan gram, gunakan cangkir atau gelas yang persis sama untuk menakar beras dan air:
</p>
<ul class="list-disc pl-6 space-y-2">
  <li><strong>Rasio Beras Pulen:</strong> 1 gelas beras membutuhkan <strong>1,2 hingga 1,25 gelas air</strong>.</li>
  <li><strong>Rasio Beras Pera / Nasi Goreng:</strong> 1 gelas beras membutuhkan <strong>1,4 hingga 1,5 gelas air</strong>.</li>
</ul>

<h2 class="text-2xl font-bold text-slate-900">3 Tips Emas Menanak Beras di Rice Cooker Komersial</h2>
<ol class="list-decimal pl-6 space-y-2">
  <li><strong>Cuci Maksimal 2–3 Kali:</strong> Jangan meremas beras terlalu kuat saat mencuci. Cukup putar pelan untuk membilas debu sekam luar. Terlalu sering mencuci akan mengikis lapisan vitamin B dan membuat butir beras retak.</li>
  <li><strong>Diamkan 10–15 Menit Sebelum Menekan Tombol Cook:</strong> Biarkan beras terendam sebentar agar molekul air mulai meresap ke inti butir endosperma. Teknik ini menghasilkan kematangan yang merata hingga ke bagian tengah.</li>
  <li><strong>Aduk Segera Saat Berpindah ke Mode 'Warm':</strong> Begitu tombol berpindah ke hangat, buka penutup rice cooker dan aduk nasi perlahan dari bawah ke atas menggunakan centong kayu/plastik bergerigi. Ini melepaskan sisa uap air yang terjebak di dasar panci agar nasi tidak basah berkerak.</li>
</ol>

<p>
  Untuk kebutuhan usaha boga skala besar di wilayah <a href="/wilayah/jogja" class="text-brand-700 font-bold hover:underline">Jogja</a> dan sekitarnya, percayakan pasokan Anda pada <strong><a href="/produk/beras-ladori-25kg" class="text-brand-700 font-bold hover:underline">Beras Premium Ladori 25 kg</a></strong> melalui <a href="/program/katering-horeka" class="text-brand-700 font-bold hover:underline">layanan beras catering dan horeka</a> kami.
</p>
""",
        "related_links_html": """
<a href="/program/katering-horeka" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Layanan B2B</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Pasokan Beras Katering & Horeka</span>
    <p class="text-xs text-slate-500 mt-1">Konsistensi takaran masak untuk usaha katering dan restoran.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Pelajari Program &rarr;</span>
</a>
<a href="/wilayah/jogja" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Jangkauan Armada</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Distributor Beras Jogja & Sekitarnya</span>
    <p class="text-xs text-slate-500 mt-1">Pengiriman rutin ke dapur Horeka di Kota Yogyakarta dan Sleman.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Lihat Wilayah &rarr;</span>
</a>
<a href="/artikel/beras-untuk-catering" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Panduan Kuliner</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Beras untuk Usaha Catering</span>
    <p class="text-xs text-slate-500 mt-1">Memilih tekstur pulen mekar tahan basi seharian di warmer.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Baca Panduan &rarr;</span>
</a>
<a href="/produk/beras-ladori-25kg" class="p-4 rounded-xl border border-slate-200 hover:border-brand-500 hover:bg-brand-50/50 transition flex flex-col justify-between">
  <div>
    <span class="text-xs font-bold text-brand-700 block mb-1">Pilihan Produk</span>
    <span class="text-sm font-bold text-slate-900 block leading-snug">Beras Ladori Kemasan 25 Kg</span>
    <p class="text-xs text-slate-500 mt-1">Beras kualitas konsisten untuk takaran air yang selalu stabil.</p>
  </div>
  <span class="text-xs font-bold text-brand-700 mt-2">Lihat Produk &rarr;</span>
</a>
"""
    }
]

print(f"Loaded {len(p0_part1_articles)} articles in data_p0_part1.py")
