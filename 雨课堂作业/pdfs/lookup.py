"""
输入合并后的页码，查询它原属于哪个 PDF 文件。
用法：python lookup_page.py
"""

import glob
import os
from pypdf import PdfReader

# ── 1. 读取所有 PDF 的页数，建立映射表 ─────────────────────────────
pdf_files = sorted(glob.glob("*.pdf"))

if not pdf_files:
    print("当前目录下没有找到 .pdf 文件。")
    exit(1)

# [(起始页, 结束页, 文件名), ...]  页码从 1 开始
mapping = []
current = 1

print("正在读取各 PDF 页数...")
for pdf_path in pdf_files:
    reader = PdfReader(pdf_path)
    n = len(reader.pages)
    mapping.append((current, current + n - 1, os.path.basename(pdf_path)))
    print(f"  {os.path.basename(pdf_path):20s}  第 {current:>4} ~ {current + n - 1:<4} 页  ({n} 页)")
    current += n

total = current - 1
print(f"\n合并后共 {total} 页，可开始查询。输入 q 退出。\n")

# ── 2. 查询循环 ─────────────────────────────────────────────────────
while True:
    raw = input("请输入页码：").strip()

    if raw.lower() == "q":
        print("退出。")
        break

    if not raw.isdigit():
        print("  请输入有效的正整数。\n")
        continue

    page_num = int(raw)

    if page_num < 1 or page_num > total:
        print(f"  页码超出范围，合并后共 {total} 页。\n")
        continue

    for start, end, name in mapping:
        if start <= page_num <= end:
            local = page_num - start + 1  # 在原文件中的页码
            print(f"  第 {page_num} 页 → {name}（该文件第 {local} 页，共 {end - start + 1} 页）\n")
            break
