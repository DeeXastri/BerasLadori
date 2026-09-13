# -*- coding: utf-8 -*-
"""
Script to copy and optimize beras-ladori.png into website/assets/images/
Generates:
- website/assets/images/beras-ladori.png (clean master copy)
- website/assets/images/beras-ladori.webp (optimized high-res WebP)
- website/assets/images/beras-ladori-600.webp (mobile-optimized WebP)
"""

import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

src_path = r"C:\Users\user\Desktop\Project_Antigravity\BERAS LADORI\gambar\beras-ladori.png"
out_dir = r"C:\Users\user\Desktop\Project_Antigravity\BERAS LADORI\website\assets\images"
os.makedirs(out_dir, exist_ok=True)

print(f"Reading source image from: {src_path}")
im = Image.open(src_path)
orig_w, orig_h = im.size
print(f"Original format: {im.format}, Dimensions: {orig_w}x{orig_h}, Mode: {im.mode}")

# 1. Save master PNG in website assets
dest_png = os.path.join(out_dir, "beras-ladori.png")
im.save(dest_png, "PNG", optimize=True)
png_size = os.path.getsize(dest_png)
print(f"Saved: {dest_png} ({png_size / 1024:.2f} KB)")

# 2. Convert and save high-res WebP
dest_webp = os.path.join(out_dir, "beras-ladori.webp")
im.save(dest_webp, "WEBP", quality=90, method=6)
webp_size = os.path.getsize(dest_webp)
print(f"Saved: {dest_webp} ({webp_size / 1024:.2f} KB) -> Compression: {(1 - webp_size/png_size)*100:.1f}% savings!")

# 3. Save scaled 600w WebP for mobile / responsive srcset
dest_webp_600 = os.path.join(out_dir, "beras-ladori-600.webp")
target_w = 600
target_h = int(orig_h * (target_w / orig_w))
im_600 = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
im_600.save(dest_webp_600, "WEBP", quality=85, method=6)
webp_600_size = os.path.getsize(dest_webp_600)
print(f"Saved: {dest_webp_600} ({target_w}x{target_h}, {webp_600_size / 1024:.2f} KB)")

print("\nImage processing completed successfully!")
