import sys, re

sys.stdout.reconfigure(encoding='utf-8')
with open('tools/extracted_master_120.txt', 'r', encoding='utf-8') as f:
    text = f.read()

splits = list(re.finditer(r'ARTIKEL\s+(\d{3})\s*[—\-]\s*([^\n]+)', text))
article_dict = {}
for i, m in enumerate(splits):
    num = int(m.group(1))
    start = m.start()
    end = splits[i+1].start() if i+1 < len(splits) else len(text)
    article_dict[num] = {
        'title': m.group(2).strip(),
        'raw': text[start:end].strip()
    }

p0_ids = [1, 9, 10, 14, 18, 22, 26, 28, 52, 53, 57, 60, 89, 120]
for k in p0_ids:
    raw = article_dict[k]['raw']
    print(f"=== ARTIKEL #{k:03d}: {article_dict[k]['title']} ===")
    lines = raw.split('\n')
    for line in lines:
        if any(line.startswith(prefix) for prefix in ['ARTIKEL', 'Status:', 'Primary keyword:', 'H1 / Judul:', 'Meta description', 'Draft slug:', 'Final URL:', 'Canonical']):
            print('  ', line[:100])
