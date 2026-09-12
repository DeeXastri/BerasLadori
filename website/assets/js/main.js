/**
 * DistributorBerasLadori.com - Main Application Script
 * Features: B2B Tonase Calculator, Dynamic WhatsApp Link Generator, FAQ Accordion, Mobile Menu
 */

const CONFIG = {
  // Default WhatsApp Business number (dapat diubah sesuai nomor riil Kak Bodro)
  waNumber: "6282227420003",
  defaultMsg: "Halo Distributor Beras Ladori, saya ingin konsultasi pasokan beras partai besar untuk katering/institusi di area Sleman, Jogja, atau Magelang Raya."
};

document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();
  initCalculator();
  initKateringCalculator();
  initPesantrenCalculator();
  initFaqAccordion();
  initWhatsAppLinks();
});

/**
 * Mobile Menu Toggle
 */
function initMobileMenu() {
  const btn = document.getElementById('mobile-menu-btn');
  const menu = document.getElementById('mobile-menu');
  if (!btn || !menu) return;

  btn.addEventListener('click', () => {
    const isHidden = menu.classList.contains('hidden');
    if (isHidden) {
      menu.classList.remove('hidden');
    } else {
      menu.classList.add('hidden');
    }
  });
}

/**
 * B2B Tonase & Rice Consumption Calculator
 */
function initCalculator() {
  const portionsInput = document.getElementById('calc-portions');
  const portionsDisplay = document.getElementById('calc-portions-val');
  const typeSelect = document.getElementById('calc-type');
  
  const dailyKgDisplay = document.getElementById('calc-daily-kg');
  const weeklySacksDisplay = document.getElementById('calc-weekly-sacks');
  const productRecDisplay = document.getElementById('calc-recommendation');
  const benefitDisplay = document.getElementById('calc-benefit');
  const waCalcBtn = document.getElementById('calc-wa-btn');

  if (!portionsInput || !portionsDisplay) return;

  function recalculate() {
    const portions = parseInt(portionsInput.value, 10) || 500;
    portionsDisplay.textContent = portions.toLocaleString('id-ID');

    const type = typeSelect ? typeSelect.value : 'ladori';
    // Standar porsi: 85 gram beras mentah per porsi
    const gramPerPortion = type === 'pesantren' ? 80 : 85;
    const dailyKg = Math.ceil((portions * gramPerPortion) / 1000);
    const weeklyKg = dailyKg * 7;
    const weeklySacks = Math.ceil(weeklyKg / 25);

    if (dailyKgDisplay) dailyKgDisplay.textContent = dailyKg.toLocaleString('id-ID') + ' kg / hari';
    if (weeklySacksDisplay) weeklySacksDisplay.textContent = weeklySacks.toLocaleString('id-ID') + ' karung (25 kg) / pekan';

    let productRec = '';
    let benefit = '';

    if (type === 'pesantren') {
      productRec = 'Beras DiHorein Spesialis Pondok Pesantren (25 kg)';
      benefit = 'Diformulasikan khusus untuk dapur santri. Rendemen tanak mekar melimpah (1:2.4), mengenyangkan lebih lama, dan hemat biaya anggaran santri.';
    } else {
      productRec = 'Beras Premium Ladori (25 kg / 50 kg) - Rekomendasi Resmi SPPG MBG & Horeka';
      benefit = 'Beras putih bersih mutu premium tanpa pemutih sintetis, pulen lezat, dan tahan lama sesuai rekomendasi standar SPPG MBG, katering, rumah makan, dan hotel.';
    }

    if (productRecDisplay) productRecDisplay.textContent = productRec;
    if (benefitDisplay) benefitDisplay.textContent = benefit;

    if (waCalcBtn) {
      const area = waCalcBtn.getAttribute('data-wilayah') || 'wilayah koridor Magelang-Jogja';
      const text = `Halo Distributor Beras Ladori, saya ingin mengajukan penawaran pasokan beras di ${area}:%0A` +
        `- Estimasi Porsi/Kebutuhan: ${portions} porsi/hari%0A` +
        `- Kebutuhan Harian: ~${dailyKg} kg/hari%0A` +
        `- Kebutuhan Mingguan: ~${weeklySacks} karung (25kg)%0A` +
        `- Rekomendasi Pilihan: ${productRec}%0A` +
        `Mohon info harga khusus tonase dan jadwal armada kirim ke lokasi kami.`;
      
      waCalcBtn.href = `https://wa.me/${CONFIG.waNumber}?text=${text}`;
    }
  }

  portionsInput.addEventListener('input', recalculate);
  if (typeSelect) typeSelect.addEventListener('change', recalculate);
  recalculate();
}

/**
 * Interactive FAQ Accordion
 */
function initFaqAccordion() {
  const faqButtons = document.querySelectorAll('.faq-accordion-btn');
  faqButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const content = btn.nextElementSibling;
      const icon = btn.querySelector('.faq-icon');
      
      const isOpen = !content.classList.contains('hidden');
      
      // Close other accordions
      document.querySelectorAll('.faq-accordion-content').forEach(c => c.classList.add('hidden'));
      document.querySelectorAll('.faq-icon').forEach(i => i.classList.remove('rotate-180'));

      if (!isOpen) {
        content.classList.remove('hidden');
        if (icon) icon.classList.add('rotate-180');
      }
    });
  });
}

/**
 * Dynamic WhatsApp Pre-filled Links
 */
function initWhatsAppLinks() {
  const waLinks = document.querySelectorAll('.dynamic-wa-link');
  waLinks.forEach(link => {
    const customText = link.getAttribute('data-wa-text') || CONFIG.defaultMsg;
    link.href = `https://wa.me/${CONFIG.waNumber}?text=${encodeURIComponent(customText)}`;
  });
}

/**
 * Kalkulator Kebutuhan Beras Khusus Katering Hajatan & Prasmanan
 */
function initKateringCalculator() {
  const portionsInput = document.getElementById('katering-portions');
  const portionsDisplay = document.getElementById('katering-portions-val');
  const typeSelect = document.getElementById('katering-type');
  const totalKgDisplay = document.getElementById('katering-total-kg');
  const sacks25Display = document.getElementById('katering-sacks-25');
  const savingsDisplay = document.getElementById('katering-savings');
  const waBtn = document.getElementById('katering-calc-wa-btn');

  if (!portionsInput) return;

  function calcKatering() {
    const portions = parseInt(portionsInput.value, 10) || 1000;
    if (portionsDisplay) portionsDisplay.textContent = portions.toLocaleString('id-ID');

    const type = typeSelect ? typeSelect.value : 'prasmanan';
    // Standar gram beras mentah: Prasmanan 100g, Nasi Box 125g
    const gram = type === 'box' ? 125 : 100;
    const typeLabel = type === 'box' ? 'Nasi Kotak / Box (125g/porsi)' : 'Prasmanan / Buffet (100g/porsi)';
    
    // Beras Ladori mekar 10%-15% lebih banyak, efisiensi takaran
    const totalKg = Math.ceil((portions * gram) / 1000);
    const sacks25 = Math.ceil(totalKg / 25);
    const savedKg = Math.ceil(totalKg * 0.12); // estimasi efisiensi mekar 12%

    if (totalKgDisplay) totalKgDisplay.textContent = totalKg.toLocaleString('id-ID') + ' kg';
    if (sacks25Display) sacks25Display.textContent = sacks25.toLocaleString('id-ID') + ' karung (25 kg)';
    if (savingsDisplay) savingsDisplay.textContent = `Hemat ~${savedKg} kg beras berkat daya mekar tinggi Ladori`;

    if (waBtn) {
      const text = `Halo Distributor Beras Ladori, saya ingin booking kuota beras untuk katering acara:%0A` +
        `- Jumlah Tamu: ${portions.toLocaleString('id-ID')} Porsi%0A` +
        `- Format Sajian: ${typeLabel}%0A` +
        `- Estimasi Kebutuhan: ~${totalKg} kg (${sacks25} Karung 25kg Beras Ladori)%0A` +
        `Mohon konfirmasi ketersediaan kuota jadwal dan fasilitas garansi hari-H ke dapur kami.`;
      waBtn.href = `https://wa.me/${CONFIG.waNumber}?text=${text}`;
    }
  }

  portionsInput.addEventListener('input', calcKatering);
  if (typeSelect) typeSelect.addEventListener('change', calcKatering);
  calcKatering();
}

/**
 * Kalkulator Kebutuhan Beras Khusus Dapur Pondok Pesantren
 */
function initPesantrenCalculator() {
  const santriInput = document.getElementById('pesantren-santri');
  const santriDisplay = document.getElementById('pesantren-santri-val');
  const dailyKgDisplay = document.getElementById('pesantren-daily-kg');
  const monthlyKgDisplay = document.getElementById('pesantren-monthly-kg');
  const monthlySacks25Display = document.getElementById('pesantren-sacks-25');
  const monthlySacks50Display = document.getElementById('pesantren-sacks-50');
  const waBtn = document.getElementById('pesantren-calc-wa-btn');

  if (!santriInput) return;

  function calcPesantren() {
    const santri = parseInt(santriInput.value, 10) || 500;
    if (santriDisplay) santriDisplay.textContent = santri.toLocaleString('id-ID');

    // Asumsi 3x makan sehari santri @80 gram beras mentah DiHorein (rendemen mekar 1:2.4) = 240 gram/santri/hari
    const dailyKg = Math.ceil((santri * 240) / 1000);
    const monthlyKg = dailyKg * 30;
    const sacks25 = Math.ceil(monthlyKg / 25);
    const sacks50 = Math.ceil(monthlyKg / 50);

    if (dailyKgDisplay) dailyKgDisplay.textContent = dailyKg.toLocaleString('id-ID') + ' kg / hari';
    if (monthlyKgDisplay) monthlyKgDisplay.textContent = (monthlyKg / 1000).toFixed(1) + ' Ton / bulan (' + monthlyKg.toLocaleString('id-ID') + ' kg)';
    if (monthlySacks25Display) monthlySacks25Display.textContent = sacks25.toLocaleString('id-ID') + ' sak (25 kg)';
    if (monthlySacks50Display) monthlySacks50Display.textContent = sacks50.toLocaleString('id-ID') + ' sak (50 kg)';

    if (waBtn) {
      const text = `Halo Distributor Beras DiHorein, kami pengurus dapur Pondok Pesantren ingin mengajukan pasokan rutin:%0A` +
        `- Jumlah Santri: ${santri.toLocaleString('id-ID')} santri (3x makan sehari)%0A` +
        `- Estimasi Kebutuhan Bulanan: ~${(monthlyKg/1000).toFixed(1)} Ton / bulan (${sacks25} sak 25kg atau ${sacks50} sak 50kg)%0A` +
        `- Produk Pilihan: Beras DiHorein Khusus Pesantren%0A` +
        `Mohon info daftar harga grosir pasokan pondok dan pengajuan sampel uji tanak ke lokasi kami.`;
      waBtn.href = `https://wa.me/${CONFIG.waNumber}?text=${text}`;
    }
  }

  santriInput.addEventListener('input', calcPesantren);
  calcPesantren();
}
