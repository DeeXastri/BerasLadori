import json

with open('tools/excel_audit_data.json', 'r', encoding='utf-8') as f:
    wb = json.load(f)

audit_rows = wb['Audit 120']
header = audit_rows[0]

print('=== 14 ARTIKEL PRIORITAS P0 (KEEP) ===')
for r in audit_rows[1:]:
    row_dict = {header[i]: r[i] if i < len(r) else '' for i in range(len(header))}
    if row_dict.get('Status', '').strip() == 'KEEP' and row_dict.get('Priority', '').strip() == 'P0':
        aid = int(float(row_dict['ID']))
        print(f"#{aid:03d} | {row_dict['Cluster']:<20} | {row_dict['Judul'][:48]:<50} | Slug: {row_dict['Draft Slug']}")
        print(f"     KW: {row_dict['Primary Keyword']:<30} | Target1: {row_dict['Money Target 1']} | Target2: {row_dict['Money/Local Target 2']}")
