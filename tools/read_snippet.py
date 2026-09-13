import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('tools/extracted_master_120.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pos = 13731
# print next 2500 characters
print(text[pos+1000:pos+3500])
