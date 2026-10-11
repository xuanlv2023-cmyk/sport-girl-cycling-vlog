#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script tự động kết xuất trọn bộ 5 File Word (.docx) chuyên dụng cho sản xuất hàng loạt
Dự án: Đạp Xe Đêm Thành Phố (Skill: sport-girl-cycling-vlog)
1. 00_HO_SO_THAM_CHIEU_GOC.docx
2. 01_PROMPTS_ANH_HANG_LOAT.docx
3. 02_PROMPTS_VIDEO_HANG_LOAT.docx
4. 03_PROMPTS_VOICE_HANG_LOAT.docx
5. 04_METADATA_SEO.docx

Quy chuẩn Tool Batch:
- 100% văn bản thuần túy (Plain Text Paragraphs), KHÔNG sử dụng Table ở bất kỳ file nào.
- 01_PROMPTS_ANH: Mỗi cảnh là đúng 1 đoạn văn liên tục xuống dòng (3 cảnh = đúng 3 đoạn văn).
- 02_PROMPTS_VIDEO: Mỗi cảnh là đúng 1 đoạn văn liên tục không ngắt dòng bên trong (3 cảnh = đúng 3 đoạn văn).
- 03_PROMPTS_VOICE: Lời thoại sạch 100%, không kèm tên cảnh, không nhãn người nói, không kèm chú thích SFX (3 cảnh = đúng 3 đoạn văn).
"""

import os
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def add_styled_title(doc, title_text, subtitle_text, note_text=None):
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run_title = p_title.add_run(title_text)
    run_title.font.name = 'Segoe UI'
    run_title.font.size = Pt(17)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(219, 39, 119) # Pink Magenta Sport
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(2)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run_sub = p_sub.add_run(subtitle_text)
    run_sub.font.name = 'Segoe UI'
    run_sub.font.size = Pt(10)
    run_sub.font.italic = True
    run_sub.font.color.rgb = RGBColor(100, 116, 139)

    if note_text:
        p_sub.paragraph_format.space_after = Pt(4)
        p_note = doc.add_paragraph()
        p_note.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run_note = p_note.add_run(note_text)
        run_note.font.name = 'Segoe UI'
        run_note.font.size = Pt(9.5)
        run_note.font.color.rgb = RGBColor(190, 24, 93)
        p_note.paragraph_format.space_after = Pt(16)
    else:
        p_sub.paragraph_format.space_after = Pt(14)

def add_clean_paragraph(doc, text_content, font_name='Consolas', font_size=10, is_bold=False):
    """Thêm đúng 1 đoạn văn liên tục không nhãn thừa cho tool batch"""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(14)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text_content)
    run.font.name = font_name
    run.font.size = Pt(font_size)
    run.font.bold = is_bold
    run.font.color.rgb = RGBColor(30, 41, 59)

def export_file_00(output_dir):
    doc = Document()
    add_styled_title(doc, "HỒ SƠ THAM CHIẾU GỐC (MASTER REFERENCE ASSETS)",
                     "Dự án: Đạp Xe Đêm Thành Phố • Nhân vật: Uyên Hân Sport @_Brand_Sport_Lead • Phương tiện: @_Bike_Laux_Purple",
                     "⚠️ BƯỚC 0 BẮT BUỘC: Nạp ảnh Turnaround làm Character Reference cho Tool AI tạo ảnh/video.")

    p_h1 = doc.add_heading(level=2)
    p_h1.add_run("1. Master Character Model Sheet @_Brand_Sport_Lead")
    p_c_desc = doc.add_paragraph()
    p_c_desc.add_run("• Tên: ").bold = True
    p_c_desc.add_run("Uyên Hân Sport @_Brand_Sport_Lead (21 tuổi, nữ VĐV/vlogger thể thao người thật 100%).\n")
    p_c_desc.add_run("• Đặc điểm: ").bold = True
    p_c_desc.add_run("Mặt trái xoan, má lúm đồng tiền, mắt to tròn rạng rỡ, tóc đuôi ngựa cao thể thao, vóc dáng săn chắc quyến rũ.\n")
    p_c_desc.add_run("• Trang phục tham chiếu: ").bold = True
    p_c_desc.add_run("Áo croptop hồng magenta ôm sát + Quần short denim trắng cạp cao, không khuyên tai/dây chuyền.")
    p_c_desc.paragraph_format.space_after = Pt(4)

    prompt_char = "A professional four-view character turnaround model sheet of @_Brand_Sport_Lead, an attractive 21-year-old East Asian athletic woman, displaying front view, three-quarter view, profile side view, and radiant joyful smiling expression close-up. Authentic natural Asian beauty, delicate oval face, charming dimples, luminous deep dark brown eyes, natural soft matte skin with visible micro-pores, sleek sporty high ponytail. Athletic toned hourglass physique, full bust, flat slim waist, long toned legs. Wearing a fitted magenta-pink athletic low-cut crop top, high-waisted white denim shorts, clean neckline, no jewelry. Stationary hands-free mounted camera, eye-level portrait, both hands relaxed naturally. Soft diffused daylight, neutral studio background, pristine clean sensor image, unretouched real human photography, zero AI plastic look, zero waxy shine, zero CGI rendering --ar 16:9 --style raw"
    add_clean_paragraph(doc, prompt_char)

    p_h2 = doc.add_heading(level=2)
    p_h2.add_run("2. Master Vehicle & Avenue Sheet")
    p_l_desc = doc.add_paragraph()
    p_l_desc.add_run("• Xe đạp: ").bold = True
    p_l_desc.add_run("Xe đạp địa hình thể thao màu tím lavender @_Bike_Laux_Purple, bánh tròn nan hoa thẳng, bàn đạp cơ học chuẩn xác.\n")
    p_l_desc.add_run("• Cung đường: ").bold = True
    p_l_desc.add_run("Đại lộ thành phố về đêm @_Location_Night_City_Avenue, đèn đường ánh vàng ấm, cây xanh ven đường lung linh ánh đèn fairy lights.")
    p_l_desc.paragraph_format.space_after = Pt(4)

    prompt_loc = "A cinematic establishing shot of @_Location_Night_City_Avenue, a wide modern city boulevard at dusk, wet asphalt road reflecting golden streetlights, tree-lined sidewalks adorned with delicate fairy lights, modern architecture in soft bokeh background, 35mm film photography aesthetic, pristine clean sensor image, zero UI graphics, no watermark --ar 9:16 --style raw"
    add_clean_paragraph(doc, prompt_loc)

    doc.save(os.path.join(output_dir, "00_HO_SO_THAM_CHIEU_GOC.docx"))

def export_file_01(output_dir):
    doc = Document()
    add_styled_title(doc, "PROMPTS TẠO ẢNH HÀNG LOẠT (BATCH IMAGE PROMPTS)",
                     "Dự án: Đạp Xe Đêm Thành Phố • Chuẩn 9:16 Real Human Sports Photography",
                     "Định dạng Tool Batch: 100% văn bản thuần túy không nhãn thừa. Mỗi cảnh là đúng 1 đoạn văn liên tục xuống dòng (3 cảnh = đúng 3 đoạn văn sạch).")

    prompts = [
        "unretouched candid sports photography, raw 8k DSLR camera capture, @_Brand_Sport_Lead, authentic 21-year-old Vietnamese athletic woman, 100% living human, delicate oval face, charming dimples on cheeks, large bright expressive dark brown eyes, radiant cheerful smile, soft wispy bangs, long dark brown hair neatly tied in a sporty ponytail flying backwards in wind, realistic healthy skin texture with visible natural micro-pores and soft matte finish, athletic hourglass figure, wearing fitted magenta-pink athletic crop top, high-waisted white denim shorts, riding @_Bike_Laux_Purple lavender mountain bike on @_Location_Night_City_Avenue, warm golden tungsten streetlamps lighting, authentic tire contact shadows, shot on Sony A7S III with 35mm f/1.8 lens, natural optical bokeh, zero AI plastic wax smoothing, zero CGI look --ar 9:16 --v 6.1 --style raw",
        "candid live-action sport snapshot, unedited real DSLR photograph, @_Brand_Sport_Lead, 21-year-old Vietnamese sporty woman, ponytailed hair flying in breeze, authentic skin pores and subtle natural workout flush, radiant smile, side-view 3/4 angle pedaling smoothly on lavender mountain bike @_Bike_Laux_Purple along tree-lined avenue at night @_Location_Night_City_Avenue, warm city streetlights glowing overhead, clean asphalt road, sharp focus on rider, natural optical motion blur on road surface, 50mm f/1.4 lens, 1/500s shutter speed, zero airbrushed skin, zero mannequin look --ar 9:16 --v 6.1 --style raw",
        "heartwarming sports portrait, gorgeous 21-year-old Vietnamese sporty woman @_Brand_Sport_Lead, glowing fair skin with natural soft matte texture and delicate micro-pores, joyful dimpled smile, breathless happy laugh after night cycling, brushing stray hair strands behind ear, bike decelerated safely beside curb pavement on modern avenue plaza @_Location_Night_City_Avenue, warm architectural bokeh lights in background, shallow depth of field, 85mm f/1.4 lens, unretouched real human photography, zero waxy doll face, zero CGI --ar 9:16 --v 6.1 --style raw"
    ]
    for p in prompts:
        add_clean_paragraph(doc, p)
    doc.save(os.path.join(output_dir, "01_PROMPTS_ANH_HANG_LOAT.docx"))

def export_file_02(output_dir):
    doc = Document()
    add_styled_title(doc, "PROMPTS TẠO VIDEO HÀNG LOẠT (BATCH MEGA PROMPTS)",
                     "Dự án: Đạp Xe Đêm Thành Phố • Chuẩn Tagged Blocks Bắt Buộc 1:1",
                     "Định dạng Tool Batch: 100% văn bản thuần túy không nhãn thừa. Mỗi cảnh là đúng 1 đoạn văn liên tục không ngắt dòng bên trong (3 cảnh = đúng 3 đoạn văn sạch).")

    video_prompts = [
        "[SPECIFICATION]: Exactly 10.0 seconds, 9:16 vertical 1080x1920, 30 FPS, authentic dynamic sport vlog realism, unretouched real human photography. [CAMERA DYNAMICS]: Parallel tracking camera moving smoothly alongside subject at identical matching speed from 3/4 front angle, eye-level framing, subject centered in 9:16 frame. Continuous unbroken single-take video throughout all 10.0 seconds with zero camera shake, stabilized gimbal glide. Crisp tack-sharp subject with realistic cinematic motion blur on surrounding road surface and passing streetlights. [CHARACTER ANCHOR]: @_Brand_Sport_Lead, authentic 21-year-old Vietnamese athletic woman, 100% living human, natural soft matte skin finish with visible micro-pores, natural workout flush, radiant joyful smile with charming dimples, lively dark eyes, high ponytail fluttering backwards in wind, wearing fitted magenta-pink athletic crop top and high-waisted white denim shorts, clean neckline, bare collarbone, black smartwatch on left wrist, strictly no earrings, no necklace. [VEHICLE & EQUIPMENT]: Riding @_Bike_Laux_Purple, sleek lavender mountain bike with black suspension fork, mechanically precise pedals rotating smoothly under her feet, circular wheels with straight spokes, clean tire contact with road. [ENVIRONMENT]: Positioned in @_Location_Night_City_Avenue, broad city avenue at night, municipal warm golden tungsten streetlamps, modern architecture bokeh in background, natural road reflections, shot on Sony A7S III with 35mm f/1.8 lens. [INITIAL STATE]: Inherits Keyframe K1: cycling smoothly on the avenue, hands gripped comfortably on handlebars, looking forward with bright enthusiastic eyes. [ACTION & KINETIC TIMELINE]: - [0.0s - 3.0s]: Cycling smoothly forward into the cool night breeze, focused joyful gaze looking ahead, high ponytail billowing backwards in natural wind, smooth rhythmic pedal cadence. - [3.0s - 7.0s]: Turns head toward camera lens with an infectious dazzling smile, left hand releases handlebar to wave enthusiastically at the camera, delivers lively greeting with natural Vietnamese lip-sync. - [7.0s - 10.0s]: Hand lowers back comfortably onto the handlebar, radiant smile lingering warmly into the lens, accelerating gracefully as avenue widens, smoothly settling into Keyframe K2. [AUDIO BGM & SFX]: Upbeat viral remix intro with accelerating percussion, soft wind rushing sfx and gentle bicycle freehub ticking, cheerful spoken Vietnamese voice (16 từ/10s): \"Đạp xe dạo phố đêm cùng Linh nha cả nhà ơi! Không khí mát mẻ chill xỉu luôn á!\" [FINAL STATE]: Hand lowering back to handlebar, radiant smile lingering, smoothly settling into Keyframe K2. [NEGATIVE CONSTRAINTS]: Strictly NO extra legs, NO slipping feet, NO waxy face, NO AI plastic doll skin, NO porcelain shine, NO CGI rendering, NO warped wheels.",
        "[SPECIFICATION]: Exactly 10.0 seconds, 9:16 vertical 1080x1920, 30 FPS, authentic dynamic sport vlog realism, unretouched real human photography. [CAMERA DYNAMICS]: Side-view parallel tracking shot at bike level, smooth gimbal glide keeping rider in razor-sharp focus while asphalt road and roadside greenery streak smoothly with motion blur. Continuous unbroken single-take video throughout all 10.0 seconds. [CHARACTER ANCHOR]: @_Brand_Sport_Lead, the identical 21-year-old athlete, natural skin pores, ponytailed hair, wearing fitted magenta crop top and white shorts, toned legs pedaling with graceful cadence, happy glowing facial expression, full bust, slim waist. [VEHICLE & EQUIPMENT]: Riding @_Bike_Laux_Purple lavender mountain bike in sharp focus, both feet firmly planted on pedals rotating in perfect mechanical harmony, straight spokes. [ENVIRONMENT]: Inside @_Location_Night_City_Avenue, tree-lined boulevard at night, decorative warm city lamps glowing overhead, clean asphalt road, authentic tire shadows. [INITIAL STATE]: Seamlessly matching Keyframe K2: side-profile tracking, continuous fluid pedaling cadence. [ACTION & KINETIC TIMELINE]: - [0.0s - 3.0s]: Steady rhythmic pedaling along the shimmering boulevard, body leaning slightly forward with natural athletic grace, enjoying the crisp evening breeze. - [3.0s - 7.0s]: Playful head tilt toward the tracking lens, laughing joyfully, one hand flashes a cute peace sign directly at the camera, chest rising and falling with healthy athletic respiration. - [7.0s - 10.0s]: Replaces hand on bike grip, smoothly gliding past the final row of golden streetlamps as the central plaza approaches in the distance, matching Keyframe K3. [AUDIO BGM & SFX]: Peak upbeat remix melody, vibrant bassline drop, rhythmic pedal swish, happy breathless laugh. [FINAL STATE]: Lowering peace sign gesture, decelerating slightly as plaza approaches, matching Keyframe K3. [NEGATIVE CONSTRAINTS]: Strictly NO three feet, NO deformed bike parts, NO AI plastic skin, NO waxy doll shine, NO camera UI overlays.",
        "[SPECIFICATION]: Exactly 10.0 seconds, 9:16 vertical 1080x1920, 30 FPS, authentic dynamic sport vlog realism, unretouched real human photography. [CAMERA DYNAMICS]: Tracking camera smoothly slows down and transitions into medium close-up portrait, perfectly stabilized front angle. Continuous unbroken single-take video throughout all 10.0 seconds with unwavering composure. [CHARACTER ANCHOR]: @_Brand_Sport_Lead, the identical 21-year-old athlete, glowing face with visible pores, cute dimples, looking directly into camera with pure radiant happiness, chest breathing naturally after cardio ride, bare neckline. [VEHICLE & EQUIPMENT]: @_Bike_Laux_Purple decelerating safely to a stop, one foot gracefully resting on the curb pavement. [ENVIRONMENT]: Positioned at plaza edge of @_Location_Night_City_Avenue, well-lit urban plaza background with luminous architectural lighting and lush green hedges, natural optical depth of field, shot on Sony A7S III. [INITIAL STATE]: Inherits Keyframe K3: bike coasting to a gentle stop beside plaza curb. [ACTION & KINETIC TIMELINE]: - [0.0s - 3.0s]: Smoothly coming to a gentle stop beside the illuminated flower beds, brushing stray hair strands behind ear with a bright luminous smile. - [3.0s - 7.0s]: Beaming directly at viewer with heartfelt warmth, two hands shaping a cute glowing heart gesture over her chest, delivering enthusiastic closing sign-off with synchronized lip-sync. - [7.0s - 10.0s]: Hands lower into a friendly energetic farewell wave, charming dimples deepening under the plaza lights, chest settling into peaceful breathing rhythm as video reaches conclusion. [AUDIO BGM & SFX]: Final musical beat cadence lingering softly, ambient evening breeze, cheerful spoken Vietnamese voice (20 từ/10s): \"Một vòng thành phố mười lăm cây số xong rồi nè! Chúc cả nhà ngủ ngon và nhớ tập thể dục cùng Linh nghen!\", happy vocal chuckle. [FINAL STATE]: Holding sweet farewell smile and hand wave, eyes sparkling with sporting joy, completing the video loop. [NEGATIVE CONSTRAINTS]: Strictly NO extra fingers, NO morphing eyes, NO AI plastic doll skin, NO porcelain shine, NO camera UI overlays."
    ]
    for vp in video_prompts:
        add_clean_paragraph(doc, vp)
    doc.save(os.path.join(output_dir, "02_PROMPTS_VIDEO_HANG_LOAT.docx"))

def export_file_03(output_dir):
    doc = Document()
    add_styled_title(doc, "KỊCH BẢN LỜI THOẠI HÀNG LOẠT (BATCH TTS SCRIPTS)",
                     "Dự án: Đạp Xe Đêm Thành Phố • BGM Remix 128 BPM & Giọng Nữ Trẻ Trung",
                     "Định dạng Tool Batch: Lời thoại tiếng Việt sạch 100%, không nhãn thừa, không chú thích SFX. Mỗi cảnh là đúng 1 đoạn văn liên tục xuống dòng (3 cảnh = đúng 3 đoạn văn sạch).")

    voice_lines = [
        "Đạp xe dạo phố đêm cùng Linh nha cả nhà ơi! Không khí mát mẻ chill xỉu luôn á!",
        "Gió đêm lướt nhẹ qua tóc, cảm giác tự do và tràn đầy năng lượng tích cực.",
        "Một vòng thành phố mười lăm cây số xong rồi nè! Chúc cả nhà ngủ ngon và nhớ tập thể dục cùng Linh nghen!"
    ]
    for vl in voice_lines:
        add_clean_paragraph(doc, vl, font_name='Segoe UI', font_size=11.5)
    doc.save(os.path.join(output_dir, "03_PROMPTS_VOICE_HANG_LOAT.docx"))

def export_file_04(output_dir):
    doc = Document()
    add_styled_title(doc, "GÓI TỐI ƯU SEO & ĐĂNG TẢI VIRAL ĐA KÊNH",
                     "Dự án: Đạp Xe Đêm Thành Phố • Chuẩn Đăng Tải Shorts / TikTok / Reels")

    p_h1 = doc.add_heading(level=2)
    p_h1.add_run("1. Prompt Tạo Ảnh Bìa Thumbnail (9:16)")
    thumb_prompt = "A hyper-realistic cinematic thumbnail photo, 9:16 vertical framing, @_Brand_Sport_Lead, 21-year-old athletic Vietnamese woman, radiant smile with cute dimples, sporty high ponytail, wearing fitted magenta crop top and white denim shorts, sitting on lavender mountain bike under warm glowing city streetlamps, dreamy urban bokeh, masterpiece, 8k resolution, raw photography, zero AI wax smoothing --ar 9:16 --v 6.1 --style raw"
    add_clean_paragraph(doc, thumb_prompt)

    p_h2 = doc.add_heading(level=2)
    p_h2.add_run("2. Chữ Dán Thumbnail (Overlay Text)")
    add_clean_paragraph(doc, "ĐẠP XE ĐÊM CỰC MÊ! 🚲✨\nLƯỚT GIÓ PHỐ THỊ! 🌆\nTHẢ CẢM XÚC BAY XA! 💖", font_name='Segoe UI', font_size=11)

    p_h3 = doc.add_heading(level=2)
    p_h3.add_run("3. Tiêu Đề Đa Nền Tảng (A/B Testing Headlines)")
    add_clean_paragraph(doc, "A: Đạp xe lướt gió đêm ngắm thành phố lung linh cùng Uyên Hân 🚲✨ #Shorts\nB: Buổi tối giải tỏa stress tuyệt vời nhất chính là đạp xe 🌆💨 #TikTokSports\nC: Năng lượng tích cực mỗi tối cùng cô nàng yêu thể thao! 💖 #Reels", font_name='Segoe UI', font_size=11)

    p_h4 = doc.add_heading(level=2)
    p_h4.add_run("4. Caption & Hashtag 3 Tầng")
    add_clean_paragraph(doc, "Sau một ngày bận rộn, cảm giác được đạp xe lướt trong gió đêm mát rượi thật sự chữa lành tâm hồn! Cả nhà có thích đạp xe ban đêm như Hân không nè? Thả tim cho Hân nhé! 🚲✨\n\n#Shorts #TikTokSports #ReelsViral #CyclingVlog #DapXeDem #GaiXinhDapXe #FitnessMotivation #HealthyLifestyle #UyenHanCycling #SportGirl", font_name='Segoe UI', font_size=10.5)

    doc.save(os.path.join(output_dir, "04_METADATA_SEO.docx"))

def export_all():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "export_batch")
    os.makedirs(output_dir, exist_ok=True)
    export_file_00(output_dir)
    export_file_01(output_dir)
    export_file_02(output_dir)
    export_file_03(output_dir)
    export_file_04(output_dir)
    print(f"[OK] Đã xuất thành công trọn bộ 5 file .docx chuẩn Tool Batch tại: {output_dir}")

if __name__ == '__main__':
    export_all()
