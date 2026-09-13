import json

with open('tools/excel_audit_data.json', 'r', encoding='utf-8') as f:
    wb = json.load(f)

audit_rows = wb['Audit 120']
header = audit_rows[0]

keep_articles = []
for r in audit_rows[1:]:
    row_dict = {header[i]: r[i] if i < len(r) else '' for i in range(len(header))}
    if row_dict.get('Status', '').strip() == 'KEEP':
        keep_articles.append(row_dict)

print(f'Total KEEP articles: {len(keep_articles)}')

# Group by priority
by_prio = {'P0': [], 'P1': [], 'P2': []}
for a in keep_articles:
    p = a.get('Priority', '').strip()
    if p in by_prio:
        by_prio[p].append(a)

for p, arts in by_prio.items():
    print(f'\n=== PRIORITY {p} ({len(arts)} Artikel) ===')
    for a in arts:
        aid = int(float(a['ID']))
        cluster = a.get('Cluster', '')[:18]
        judul = a.get('Judul', '')[:48]
        slug = a.get('Draft Slug', '')
        kw = a.get('Primary Keyword', '')
        target1 = a.get('Money Target 1', '')
        target2 = a.get('Money/Local Target 2', '')
        print(f"#{aid:03d} | {p} | {cluster:<18} | {judul:<50} | Slug: {slug}")
        print(f"     KW: {kw:<30} | T1: {target1} | T2: {target2}")
