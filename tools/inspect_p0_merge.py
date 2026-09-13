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
        'content': text[start:end].strip()
    }

p0_ids = [1, 9, 10, 14, 18, 22, 26, 28, 52, 53, 57, 60, 89, 120]
merge_ids = [3, 4, 54, 55, 56, 21, 27, 59, 96]

print('Found P0 articles:', [k for k in p0_ids if k in article_dict])
print('Found Merge articles:', [k for k in merge_ids if k in article_dict])
for k in p0_ids:
    c = article_dict[k]['content']
    print(f"P0 #{k:03d}: {article_dict[k]['title']} ({len(c)} chars)")

for k in merge_ids:
    c = article_dict[k]['content']
    print(f"MERGE #{k:03d}: {article_dict[k]['title']} ({len(c)} chars)")
