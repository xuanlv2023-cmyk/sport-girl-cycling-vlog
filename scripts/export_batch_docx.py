# -*- coding: utf-8 -*-
"""
Script tự động kết xuất trọn bộ 5 File Word (.docx) chuyên dụng cho sản xuất hàng loạt
Skill: sport-girl-cycling-vlog
Quy chuẩn: 100% văn bản thuần túy (Plain Text Paragraphs), KHÔNG sử dụng Table ở bất kỳ file nào.
"""

import os
import sys
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def add_styled_title(doc, title_text, subtitle_text, note_text=None):
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run_title = p_title.add_run(title_text)
    run_title.font.name = "Segoe UI"
    run_title.font.size = Pt(17)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(194, 24, 91) # Berry pink sporty
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(2)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run_sub = p_sub.add_run(subtitle_text)
    run_sub.font.name = "Segoe UI"
    run_sub.font.size = Pt(10)
    run_sub.font.italic = True
    run_sub.font.color.rgb = RGBColor(113, 128, 150)

    if note_text:
        p_sub.paragraph_format.space_after = Pt(4)
        p_note = doc.add_paragraph()
        p_note.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run_note = p_note.add_run(note_text)
        run_note.font.name = "Segoe UI"
        run_note.font.size = Pt(9.5)
        run_note.font.color.rgb = RGBColor(225, 29, 72)
        p_note.paragraph_format.space_after = Pt(16)
    else:
        p_sub.paragraph_format.space_after = Pt(14)

def add_prompt_paragraph(doc, text_content, label=None, font_name="Consolas", font_size=10, is_bold=False):
    if label:
        p_label = doc.add_paragraph()
        run_lbl = p_label.add_run(label)
        run_lbl.font.name = "Segoe UI"
        run_lbl.font.size = Pt(10.5)
        run_lbl.font.bold = True
        run_lbl.font.color.rgb = RGBColor(194, 24, 91)
        p_label.paragraph_format.space_before = Pt(8)
        p_label.paragraph_format.space_after = Pt(2)

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(14)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text_content)
    run.font.name = font_name
    run.font.size = Pt(font_size)
    run.font.bold = is_bold
    run.font.color.rgb = RGBColor(33, 37, 41)

def export_5_files(output_dir, project_data):
    os.makedirs(output_dir, exist_ok=True)
    
    # 00_HO_SO_THAM_CHIEU_GOC.docx
    doc0 = Document()
    add_styled_title(doc0, "HỒ SƠ THAM CHIẾU GỐC (MASTER REFERENCE ASSETS)",
                     f"Dự án: {project_data['title']} • Nhân vật: @_Brand_Sport_Lead Uyên Hân",
                     "⚠️ BƯỚC 0: Nạp ảnh Turnaround 4 góc nhìn làm Character/Face Reference:")
    
    p_h1 = doc0.add_heading(level=2)
    p_h1.add_run("1. Master Character Model Sheet @_Brand_Sport_Lead").font.name = "Segoe UI"
    p_c_desc = doc0.add_paragraph()
    p_c_desc.add_run("• Tên: Uyên Hân @_Brand_Sport_Lead (21 tuổi, Á Đông, năng động, quyến rũ thể thao fit & curvy).\n")
    p_c_desc.add_run("• Đặc điểm: Mặt trái xoan, má lúm đồng tiền duyên dáng, mắt sáng, tóc đuôi ngựa bay trong gió.\n")
    p_c_desc.add_run("• Kỷ luật: KHÔNG hoa tai, KHÔNG dây chuyền, chỉ đeo smartwatch thể thao.\n")
    add_prompt_paragraph(doc0, project_data['char_prompt'], "Prompt Midjourney / Flux Turnaround 4 góc nhìn:")

    p_h2 = doc0.add_heading(level=2)
    p_h2.add_run("2. Master Vehicle & Environment Reference").font.name = "Segoe UI"
    add_prompt_paragraph(doc0, project_data['env_prompt'], "Prompt Tạo Ảnh Bối Cảnh & Xe Đạp Chuẩn:")
    doc0.save(os.path.join(output_dir, "00_HO_SO_THAM_CHIEU_GOC.docx"))

    # 01_PROMPTS_ANH_HANG_LOAT.docx
    doc1 = Document()
    add_styled_title(doc1, "DANH SÁCH PROMPTS ẢNH ĐỘC LẬP (IMAGE KEYFRAMES)",
                     f"Dự án: {project_data['title']} • Tỷ lệ khóa: 9:16 Dọc",
                     "Mỗi phân cảnh là 1 đoạn văn thuần túy. Copy-paste trực tiếp vào Midjourney / Flux:")
    for lbl, p_txt in project_data['img_prompts']:
        add_prompt_paragraph(doc1, p_txt, lbl)
    doc1.save(os.path.join(output_dir, "01_PROMPTS_ANH_HANG_LOAT.docx"))

    # 02_PROMPTS_VIDEO_HANG_LOAT.docx
    doc2 = Document()
    add_styled_title(doc2, "DANH SÁCH MEGA PROMPTS VIDEO DYNAMIC TRACKING",
                     f"Chuẩn Google Veo 3.1 & Kling AI • Camera Tracking Song Song • {len(project_data['video_prompts'])} Phân Cảnh",
                     "Mỗi phân cảnh là 1 khối thẻ kỹ thuật hoàn chỉnh. Copy-paste trực tiếp vào AI Video Generator:")
    for lbl, p_txt in project_data['video_prompts']:
        add_prompt_paragraph(doc2, p_txt, lbl, font_size=9)
    doc2.save(os.path.join(output_dir, "02_PROMPTS_VIDEO_HANG_LOAT.docx"))

    # 03_PROMPTS_AUDIO_VOICE.docx
    doc3 = Document()
    add_styled_title(doc3, "HƯỚNG DẪN ÂM NHẠC VIRAL & LỜI THOẠI MOTIVATION",
                     f"Dự án: {project_data['title']} • Chuẩn Âm Thanh 15s / 30s",
                     "Đồng bộ beat drop cho CapCut / Premiere / ElevenLabs:")
    for lbl, a_txt in project_data['audio_guide']:
        add_prompt_paragraph(doc3, a_txt, lbl, font_name="Segoe UI", font_size=10.5)
    doc3.save(os.path.join(output_dir, "03_PROMPTS_AUDIO_VOICE.docx"))

    # 04_METADATA_SEO.docx
    doc4 = Document()
    add_styled_title(doc4, "GÓI METADATA SEO & THUMBNAIL KHOE DÁNG",
                     f"Dự án: {project_data['title']} • Tối ưu hóa CTR Shorts / TikTok",
                     "Chữ dán 2-3 từ, Ma trận 4 Prompt Thumbnail A/B, 3 Tiêu đề A/B, Caption & Hashtags:")
    add_prompt_paragraph(doc4, project_data['text_overlay'], "1. Chữ Dán Thumbnail Động (Text Overlay - 2 đến 3 Từ):", font_name="Segoe UI", font_size=13, is_bold=True)
    for lbl, tp_txt in project_data['thumb_prompts']:
        add_prompt_paragraph(doc4, tp_txt, lbl)
    add_prompt_paragraph(doc4, project_data['titles_ab'], "3. Bộ 3 Tiêu Đề A/B Testing Chuẩn Thuật Toán:", font_name="Segoe UI", font_size=10.5)
    add_prompt_paragraph(doc4, project_data['caption_hashtag'], "4. Caption Xuất Bản & Cây Hashtag 3 Tầng:", font_name="Segoe UI", font_size=10.5)
    doc4.save(os.path.join(output_dir, "04_METADATA_SEO.docx"))
    print("Exported 5 .docx files successfully!")
