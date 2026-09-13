import glob
import os
import re

files = glob.glob('website/**/*.html', recursive=True)
updated_subpages = 0
homepage_checked = False

for f in sorted(files):
    f_norm = f.replace('\\', '/')
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    if f_norm == 'website/index.html':
        assert 'index, follow' in content, "Homepage should be index, follow"
        homepage_checked = True
        print(f"[HOMEPAGE KEPT INDEXABLE] {f_norm}")
        continue
    
    new_content = re.sub(
        r'<meta\s+name=["\']robots["\']\s+content=["\'].*?["\']>',
        '<meta name="robots" content="noindex, follow">',
        content
    )
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(new_content)
        updated_subpages += 1
        print(f"[SUBPAGE SET NOINDEX, FOLLOW] {f_norm}")

print(f"\nDone! Homepage verified: {homepage_checked}. Total subpages updated: {updated_subpages}")
