/**
 * DistributorBerasLadori.com - Main Application Script
 * Features: B2B Tonase Calculator, Dynamic WhatsApp Link Generator, FAQ Accordion, Mobile Menu
 */

const CONFIG = {
  // Default WhatsApp Business number (dapat diubah sesuai nomor riil Kak Bodro)
  waNumber: "6282227420003",
  defaultMsg: "Halo Distributor Beras Ladori, saya ingin konsultasi pasokan beras partai besar untuk katering/institusi di Jawa Tengah - DIY."
};

document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();
  initCalculator();
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

    const type = typeSelect ? typeSelect.value : 'mbg';
    // Standar porsi: 80 - 85 gram beras mentah per porsi
    const gramPerPortion = type === 'prasmanan' ? 85 : 80;
    const dailyKg = Math.ceil((portions * gramPerPortion) / 1000);
    const weeklyKg = dailyKg * 7;
    const weeklySacks = Math.ceil(weeklyKg / 25);

    if (dailyKgDisplay) dailyKgDisplay.textContent = dailyKg.toLocaleString('id-ID') + ' kg / hari';
    if (weeklySacksDisplay) weeklySacksDisplay.textContent = weeklySacks.toLocaleString('id-ID') + ' karung (25 kg) / pekan';

    let productRec = '';
    let benefit = '';

    if (type === 'prasmanan') {
      productRec = 'Beras Premium Ladori (25 kg / 50 kg)';
      benefit = 'Pulen alami, aroma wangi pandan alami, putih bersih tanpa bahan kimia pemutih. Standar tertinggi prasmanan & hajatan.';
    } else {
      productRec = 'Beras DiHorein Spesialis MBG & Horeka (25 kg)';
      benefit = 'Rendemen mekar tinggi, tahan basi >20 jam di pemanas/warmer. Sangat hemat modal katering & porsi melimpah.';
    }

    if (productRecDisplay) productRecDisplay.textContent = productRec;
    if (benefitDisplay) benefitDisplay.textContent = benefit;

    if (waCalcBtn) {
      const text = `Halo Distributor Beras Ladori, saya ingin mengajukan penawaran pasokan beras partai besar:%0A` +
        `- Estimasi Porsi: ${portions} porsi/hari%0A` +
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
