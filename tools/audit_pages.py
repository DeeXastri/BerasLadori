import os
import glob
import re
import json

html_files = glob.glob('website/**/*.html', recursive=True)
print(f"Auditing {len(html_files)} HTML files...\n")

all_pass = True

for path in sorted(html_files):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Title
    m_title = re.search(r'<title>(.*?)</title>', content)
    title = m_title.group(1) if m_title else 'MISSING'
    title_len = len(title)
    title_ok = 0 < title_len <= 60

    # Meta desc
    m_desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content)
    desc = m_desc.group(1) if m_desc else 'MISSING'
    desc_len = len(desc)
    desc_ok = 130 <= desc_len <= 165

    # Canonical
    m_canon = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](https://www\.berasladori\.com/.*?)["\']', content)
    canon_ok = bool(m_canon)

    # Robots
    robots_ok = 'max-image-preview:large' in content

    # Schema
    schema_ok = '<script type="application/ld+json">' in content

    status = 'OK' if (title_ok and desc_ok and canon_ok and robots_ok and schema_ok) else 'FAIL'
    if status == 'FAIL':
        all_pass = False
    print(f"[{status}] {path}")
    print(f"     Title ({title_len} chars): {title}")
    print(f"     Desc  ({desc_len} chars): {desc[:60]}...")
    if not title_ok:
        print(f"     [!] Title length warning ({title_len} chars)")
    if not desc_ok:
        print(f"     [!] Desc length warning ({desc_len} chars)")
    if not canon_ok:
        print(f"     [!] Canonical issue!")
    if not robots_ok:
        print(f"     [!] Robots issue!")
    if not schema_ok:
        print(f"     [!] Schema issue!")

print('\n' + ('='*50))
if all_pass:
    print('ALL 12 PAGES PASSED 100% AUDIT CHECKS!')
else:
    print('SOME PAGES FAILED AUDIT!')
print('='*50)
