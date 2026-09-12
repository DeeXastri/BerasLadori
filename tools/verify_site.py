import os
import re
import json

base_dir = r"C:\Users\user\Desktop\Project_Antigravity\BERAS LADORI\website"
error_count = 0
checked_pages = 0

print("=== VERIFIKASI JSON-LD & STRUKTUR WEBSITE DISTRIBUTORBERASLADORI.COM ===")

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".html"):
            checked_pages += 1
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, base_dir)
            with open(full_path, "r", encoding="utf-8") as fp:
                html_text = fp.read()
            
            # Find JSON-LD scripts
            pattern = re.compile(r'<script type=["\']application/ld\+json["\']>(.*?)</script>', re.DOTALL)
            matches = pattern.findall(html_text)
            
            if not matches:
                print(f"[INFO] {rel_path}: Tidak ada script JSON-LD terdeteksi.")
            else:
                for idx, block in enumerate(matches):
                    try:
                        parsed = json.loads(block.strip())
                        if "@graph" in parsed:
                            types = [item.get("@type", "Unknown") for item in parsed["@graph"]]
                            print(f"[PASS] {rel_path} block {idx}: Valid @graph -> {types}")
                        else:
                            stype = parsed.get("@type", "Unknown")
                            print(f"[PASS] {rel_path} block {idx}: Valid -> @type: {stype}")
                    except json.JSONDecodeError as err:
                        print(f"[FAIL] {rel_path} block {idx}: JSON ERROR -> {err}")
                        error_count += 1

print(f"\nRingkasan:")
print(f"- Total Halaman HTML Diperiksa: {checked_pages}")
print(f"- Total Kesalahan Sintaks JSON-LD: {error_count}")
if error_count == 0:
    print("STATUS: 100% VALID & SIAP DEPLOY KE VERCEL!")
