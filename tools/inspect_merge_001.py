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
    article_dict[num] = text[start:end].strip()

def get_body(raw_text):
    copy_idx = raw_text.find('Copy Artikel')
    linking_idx = raw_text.find('Internal Linking Saat Publish')
    if copy_idx != -1 and linking_idx != -1:
        return raw_text[copy_idx+len('Copy Artikel'):linking_idx].strip()
    return raw_text

print("=== ARTICLE #001 BODY ===")
print(get_body(article_dict[1])[:600])

print("\n=== ARTICLE #003 BODY (Merge into #001) ===")
print(get_body(article_dict[3])[:600])

print("\n=== ARTICLE #004 BODY (Merge into #001) ===")
print(get_body(article_dict[4])[:600])

print("\n=== ARTICLE #054 BODY (Merge into #001) ===")
print(get_body(article_dict[54])[:600])

print("\n=== ARTICLE #055 BODY (Merge into #001) ===")
print(get_body(article_dict[55])[:600])

print("\n=== ARTICLE #056 BODY (Merge into #001) ===")
print(get_body(article_dict[56])[:600])
