"""
将当前目录下的所有 PDF 合并为一个文件，并以文件名作为书签标题。
依赖：pypdf（pip install pypdf）
用法：python merge_pdfs.py
"""

import glob
import os
from pypdf import PdfWriter, PdfReader

# ── 1. 收集并排序 PDF 文件 ──────────────────────────────────────────
pdf_files = sorted(glob.glob("*.pdf"))

if not pdf_files:
    print("当前目录下没有找到 .pdf 文件。")
    exit(1)

print(f"共找到 {len(pdf_files)} 个 PDF 文件：")
for f in pdf_files:
    print(f"  {f}")

# ── 2. 合并并插入书签 ───────────────────────────────────────────────
writer = PdfWriter()
current_page = 0  # 追踪每个章节起始页

for pdf_path in pdf_files:
    title = os.path.splitext(os.path.basename(pdf_path))[0]  # 去掉 .pdf 后缀

    reader = PdfReader(pdf_path)
    num_pages = len(reader.pages)

    # 添加所有页面
    for page in reader.pages:
        writer.add_page(page)

    # 在该章节第一页插入顶级书签
    writer.add_outline_item(title, current_page)

    print(f"  ✓ {title}  ({num_pages} 页，起始页 {current_page + 1})")
    current_page += num_pages

# ── 3. 写出合并文件 ─────────────────────────────────────────────────
output_path = "merged_output.pdf"
with open(output_path, "wb") as f:
    writer.write(f)

print(f"\n合并完成 → {output_path}（共 {current_page} 页）")
