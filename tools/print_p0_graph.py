import json

data = json.load(open('tools/excel_audit_data.json', encoding='utf-8'))
graph = data['Internal Link Graph'][1:]
p0_nodes = ['OLD-001', 'OLD-009', 'OLD-010', 'OLD-014', 'OLD-018', 'OLD-022', 'OLD-026', 'OLD-028', 'OLD-052', 'OLD-053', 'OLD-057', 'OLD-060', 'OLD-089', 'OLD-120']

for r in graph:
    if r[0] in p0_nodes:
        print(f"{r[0]} | {r[2]} -> Primary: {r[4]} (\"{r[5]}\") | Sec: {r[6]} | Supp1: {r[7]} | Supp2: {r[8]}")
