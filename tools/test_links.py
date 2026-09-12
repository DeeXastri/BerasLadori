import os
import re

base_dir = r"C:\Users\user\Desktop\Project_Antigravity\BERAS LADORI\website"
broken_links = []
checked_links = 0

# Map of existing files/routes
# On Vercel with cleanUrls: true:
# "/" -> index.html
# "/program/sppg-mbg" -> program/sppg-mbg.html
# "/artikel" -> artikel/index.html
# "/artikel/daftar-harga-beras-ladori-25kg" -> artikel/daftar-harga-beras-ladori-25kg.html
# "/wilayah/magelang" -> wilayah/magelang.html etc.

def route_exists(route):
    if route.startswith("#") or route.startswith("http") or route.startswith("mailto:") or route.startswith("tel:"):
        return True
    clean = route.split("?")[0].split("#")[0]
    if clean == "" or clean == "/":
        return True
    
    # Remove leading slash
    path = clean.lstrip("/")
    
    # Check direct html file
    f_html = os.path.join(base_dir, path + ".html")
    if os.path.isfile(f_html):
        return True
    
    # Check directory index.html
    f_dir_index = os.path.join(base_dir, path, "index.html")
    if os.path.isfile(f_dir_index):
        return True
    
    # Check exact file
    f_exact = os.path.join(base_dir, path)
    if os.path.isfile(f_exact):
        return True

    return False

print("=== VERIFIKASI TAUTAN INTERNAL (LINK INTEGRITY CHECK) ===")
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".html"):
            p = os.path.join(root, f)
            rel = os.path.relpath(p, base_dir)
            with open(p, "r", encoding="utf-8") as fp:
                html = fp.read()
            
            hrefs = re.findall(r'href=["\'](.*?)["\']', html)
            for href in hrefs:
                checked_links += 1
                if not route_exists(href):
                    broken_links.append((rel, href))

print(f"Total Tautan Diperiksa: {checked_links}")
print(f"Total Tautan Rusak / Broken Links: {len(broken_links)}")
if broken_links:
    for src, target in broken_links:
        print(f"[BROKEN] In {src} -> {target}")
else:
    print("STATUS: ZERO BROKEN LINKS! Seluruh rute tautan internal 100% terhubung sempurna.")
