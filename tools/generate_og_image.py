# -*- coding: utf-8 -*-
"""
Script to create an ultra-professional 1200x630 Open Graph card
featuring the real Beras Ladori packshot.
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

sys.stdout.reconfigure(encoding='utf-8')

bg_w, bg_h = 1200, 630

# 1. Create canvas with rich brand gradient
canvas = Image.new("RGB", (bg_w, bg_h), "#064e3b")
draw = ImageDraw.Draw(canvas)

# Gradient effect
for y in range(bg_h):
    r = int(6 + (2 - 6) * (y / bg_h))
    g = int(78 + (44 - 78) * (y / bg_h))
    b = int(59 + (34 - 59) * (y / bg_h))
    draw.line([(0, y), (bg_w, y)], fill=(r, g, b))

# Decorative gold top and bottom borders
draw.rectangle([(0, 0), (bg_w, 8)], fill="#f59e0b")
draw.rectangle([(0, bg_h - 8), (bg_w, bg_h)], fill="#f59e0b")

# Outer border accent
draw.rectangle([(20, 20), (bg_w - 20, bg_h - 20)], outline="#047857", width=2)

# Load fonts
try:
    font_badge = ImageFont.truetype("arialbd.ttf", 22)
    font_title = ImageFont.truetype("arialbd.ttf", 52)
    font_sub = ImageFont.truetype("arialbd.ttf", 26)
    font_body = ImageFont.truetype("arial.ttf", 22)
    font_footer = ImageFont.truetype("arialbd.ttf", 20)
except:
    font_badge = font_title = font_sub = font_body = font_footer = ImageFont.load_default()

# 2. Draw Badge
badge_text = "  DISTRIBUTOR RESMI PABRIK  "
draw.rectangle([(60, 55), (420, 95)], fill="#d97706")
draw.text((70, 63), "DISTRIBUTOR RESMI PABRIK", fill="#ffffff", font=font_badge)

# 3. Draw Title
draw.text((60, 115), "BERAS LADORI", fill="#ffffff", font=font_title)
draw.text((60, 185), "Beras Premium Pulen Alami Bebas Pemutih", fill="#fbbf24", font=font_sub)

# Divider line
draw.line([(60, 230), (620, 230)], fill="#059669", width=2)

# 4. Bullet Points
bullets = [
    "• Izin Resmi Kementan RI PD 52.00.33 - 07 / 16",
    "• 100% Bebas Klorin, Pemutih, & Pewangi Kimia",
    "• Kadar Air 13.5% & Butir Kepala Utuh 95%",
    "• Rendemen Mekar 2.4x Lipat (Hemat Food Cost)",
    "• Rute Armada: Sleman, Jogja, Muntilan, Magelang, Temanggung"
]

y_pos = 250
for b in bullets:
    draw.text((60, y_pos), b, fill="#e2e8f0", font=font_body)
    y_pos += 44

# 5. Footer Banner
draw.rectangle([(60, 520), (620, 570)], fill="#042f2e", outline="#0d9488", width=1)
draw.text((80, 532), "🌐 www.berasladori.com  •  📱 WA: 0822-2742-0003", fill="#a7f3d0", font=font_footer)

# 6. Place Packshot Image on Right Side
pack_path = r"C:\Users\user\Desktop\Project_Antigravity\BERAS LADORI\gambar\beras-ladori.png"
if os.path.exists(pack_path):
    pack = Image.open(pack_path)
    # Fit into height approx 520px
    pack_h = 520
    pack_w = int(pack.width * (pack_h / pack.height))
    pack_resized = pack.resize((pack_w, pack_h), Image.Resampling.LANCZOS)
    
    # Calculate position
    pos_x = 720
    pos_y = 55
    
    # Add subtle drop shadow
    shadow = Image.new("RGBA", (pack_w + 30, pack_h + 30), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.rectangle([(15, 15), (pack_w + 15, pack_h + 15)], fill=(0, 0, 0, 160))
    shadow = shadow.filter(ImageFilter.GaussianBlur(15))
    
    # Paste shadow then image
    canvas.paste(shadow, (pos_x - 15, pos_y - 15), shadow)
    canvas.paste(pack_resized, (pos_x, pos_y), pack_resized if pack_resized.mode == 'RGBA' else None)

# Save og-image.jpg
out_path = r"C:\Users\user\Desktop\Project_Antigravity\BERAS LADORI\website\assets\images\og-image.jpg"
canvas.save(out_path, "JPEG", quality=92, optimize=True)
print(f"Generated new og-image.jpg at: {out_path} ({os.path.getsize(out_path) / 1024:.2f} KB)")
