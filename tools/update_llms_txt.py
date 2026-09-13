# -*- coding: utf-8 -*-
"""
Update website/llms.txt and website/llms-full.txt with all 34 B2B articles.
"""

from data_cluster1 import cluster1_articles
from data_cluster2 import cluster2_articles
from data_cluster3 import cluster3_articles
from data_cluster4 import cluster4_articles
from data_cluster5 import cluster5_articles

all_30 = (
    cluster1_articles +
    cluster2_articles +
    cluster3_articles +
    cluster4_articles +
    cluster5_articles
)

# Read current llms.txt
with open("website/llms.txt", "r", encoding="utf-8") as f:
    llms_txt = f.read()

article_links_markdown = "\n## Arsip Panduan Sains Pengadaan Beras B2B (34 Panduan)\n"
for a in all_30:
    article_links_markdown += f"- [{a['title']}](https://www.berasladori.com/artikel/{a['slug']}): {a['description']}\n"

# Check if section already exists
if "## Arsip Panduan Sains Pengadaan Beras B2B" not in llms_txt:
    llms_txt = llms_txt.strip() + "\n" + article_links_markdown
    with open("website/llms.txt", "w", encoding="utf-8") as f:
        f.write(llms_txt)
    print("Updated website/llms.txt")

# Read current llms-full.txt
with open("website/llms-full.txt", "r", encoding="utf-8") as f:
    llms_full_txt = f.read()

if "## Arsip Panduan Sains Pengadaan Beras B2B" not in llms_full_txt:
    llms_full_txt = llms_full_txt.strip() + "\n" + article_links_markdown
    with open("website/llms-full.txt", "w", encoding="utf-8") as f:
        f.write(llms_full_txt)
    print("Updated website/llms-full.txt")
