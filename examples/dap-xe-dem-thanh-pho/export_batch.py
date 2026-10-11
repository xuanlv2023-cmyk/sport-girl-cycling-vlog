#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script tự động kết xuất trọn bộ 5 File Word (.docx) chuyên dụng cho sản xuất hàng loạt
Dự án: Đạp Xe Đêm Sài Gòn (Skill: sport-girl-cycling-vlog V10 Production)
Khung phân cảnh: Chuẩn 3 phân cảnh x 10.0s = 30.0s tối ưu cho Google Veo 3.1 & Muse
1. 00_HO_SO_THAM_CHIEU_GOC.docx
2. 01_PROMPTS_ANH_HANG_LOAT.docx
3. 02_PROMPTS_VIDEO_HANG_LOAT.docx
4. 03_PROMPTS_VOICE_HANG_LOAT.docx
5. 04_METADATA_SEO.docx

Quy chuẩn Tool Batch:
- 100% văn bản thuần túy (Plain Text Paragraphs), KHÔNG sử dụng Table ở bất kỳ file nào.
- 01_PROMPTS_ANH: Mỗi cảnh là đúng 1 đoạn văn liên tục xuống dòng (3 cảnh = đúng 3 đoạn văn).
- 02_PROMPTS_VIDEO: Mỗi cảnh là đúng 1 đoạn văn liên tục không ngắt dòng bên trong (3 cảnh = đúng 3 đoạn văn).
- 03_PROMPTS_VOICE: Lời thoại sạch 100% Giọng Miền Nam/Sài Gòn, không kèm tên cảnh, không nhãn người nói, không kèm chú thích SFX (3 cảnh = đúng 3 đoạn văn).
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
                     "Dự án: Đạp Xe Đêm Sài Gòn • Nhân vật: Uyên Hân Sport @_Brand_Sport_Lead • Phương tiện: @_Bike_Laux_Purple",
                     "⚠️ BƯỚC 0 BẮT BUỘC: Nạp ảnh Turnaround làm Character Reference cho Tool AI tạo ảnh/video.")

    p_h1 = doc.add_heading(level=2)
    p_h1.add_run("1. Master Character Model Sheet @_Brand_Sport_Lead")
    p_c_desc = doc.add_paragraph()
    p_c_desc.add_run("• Tên: ").bold = True
    p_c_desc.add_run("Uyên Hân Sport @_Brand_Sport_Lead (21 tuổi, nữ thần thể thao người thật 100%).\n")
    p_c_desc.add_run("• Vóc dáng: ").bold = True
    p_c_desc.add_run("@_Body_Athletic_Cleavage_Curves (Thân hình đồng hồ cát thể thao, vòng 1 đầy đặn quyến rũ lộ rãnh ngực tự nhiên, eo thon cơ bụng số 11, chân dài miên man).\n")
    p_c_desc.add_run("• Trang phục tham chiếu: ").bold = True
    p_c_desc.add_run("Áo croptop cổ vuông trễ ôm sát màu kem viền đen + Quần short denim trắng cạp cao, đồng hồ thông minh tay trái, dây chuyền mặt tròn mảnh.")
    p_c_desc.paragraph_format.space_after = Pt(4)

    prompt_char = "A professional four-view character turnaround model sheet of @_Brand_Sport_Lead, an authentic 21-year-old Vietnamese athletic woman, displaying front view, three-quarter view, profile side view, and charming close-up smiling facial expression with distinct cheek dimples. Delicate oval face, large bright expressive dark brown eyes, radiant cheerful smile, soft wispy bangs, long dark brown hair neatly tied in a sporty high ponytail. Realistic healthy glowing skin texture with natural soft matte finish, visible natural micropores, delicate workout flush. Athletic curvy hourglass figure featuring generous natural bust with tasteful prominent cleavage, bare collarbones, slim toned waist with faint ab lines, shapely hips and toned thighs. Wearing a tight-fitting cream-white ribbed scoop-neck athletic crop top with dark contrast collar piping, high-waisted white denim shorts, clean neckline, minimal dainty necklace, sports smartwatch on left wrist, strictly no earrings. Captured on Sony A7 IV with 50mm f/1.4 lens, clean neutral studio lighting, natural floor shadows, pristine camera sensor quality, unretouched real human photography, zero AI plastic wax smoothing, zero CGI look --ar 16:9 --style raw"
    add_clean_paragraph(doc, prompt_char)

    p_h2 = doc.add_heading(level=2)
    p_h2.add_run("2. Master Vehicle & Boulevard Sheet")
    p_l_desc = doc.add_paragraph()
    p_l_desc.add_run("• Xe đạp: ").bold = True
    p_l_desc.add_run("Xe đạp địa hình thể thao màu tím lavender @_Bike_Laux_Purple, bánh tròn nan hoa thẳng, bàn đạp cơ học chuẩn xác.\n")
    p_l_desc.add_run("• Cung đường: ").bold = True
    p_l_desc.add_run("Đại lộ đô thị Sài Gòn về đêm @_Location_City_Highway_Night, đèn đường ánh vàng ấm 3000K, cây xanh ven đường lung linh ánh đèn phố.")
    p_l_desc.paragraph_format.space_after = Pt(4)

    prompt_loc = "A cinematic establishing shot of @_Location_City_Highway_Night, a wide modern boulevard in Saigon at night, asphalt road reflecting golden streetlights, tree-lined sidewalks, illuminated modern high-rises in soft bokeh background, 35mm film photography aesthetic, pristine clean sensor image, zero UI graphics, no watermark --ar 9:16 --style raw"
    add_clean_paragraph(doc, prompt_loc)

    doc.save(os.path.join(output_dir, "00_HO_SO_THAM_CHIEU_GOC.docx"))

def export_file_01(output_dir):
    doc = Document()
    add_styled_title(doc, "PROMPTS TẠO ẢNH HÀNG LOẠT (BATCH IMAGE PROMPTS)",
                     "Dự án: Đạp Xe Đêm Sài Gòn • Chuẩn 9:16 Real Human Sports Photography",
                     "Định dạng Tool Batch: 100% văn bản thuần túy không nhãn thừa. Mỗi cảnh là đúng 1 đoạn văn liên tục xuống dòng (3 cảnh = đúng 3 đoạn văn sạch).")

    prompts = [
        "unretouched candid sports photography, raw 8k DSLR camera capture, @_Brand_Sport_Lead, authentic 21-year-old Vietnamese athletic woman, 100% living human, delicate oval face, charming dimples on cheeks, large bright expressive dark brown eyes, radiant cheerful smile, soft wispy bangs, long dark brown hair neatly tied in a sporty ponytail flying backwards in wind, realistic healthy skin texture with visible natural micro-pores and soft matte finish, delicate perspiration sheen, athletic curvy hourglass figure with prominent natural cleavage, bare toned midriff, wearing fitted cream-white athletic crop top with dark contrast piping, high-waisted white denim shorts, riding lavender mountain bike @_Bike_Laux_Purple on @_Location_City_Highway_Night, low-angle 3/4 front view looking slightly upward, warm golden tungsten streetlamps, authentic tire contact shadows, shot on Sony A7 IV with 35mm f/1.8 lens, natural optical bokeh, zero AI plastic wax smoothing, zero CGI look --ar 9:16 --v 6.1 --style raw",
        "candid live-action sport snapshot, unedited real DSLR photograph, @_Brand_Sport_Lead, 21-year-old Vietnamese sporty woman, ponytailed hair flying in night breeze, authentic skin pores and subtle natural workout flush, radiant dimpled smile, side-view 3/4 angle pedaling smoothly on lavender mountain bike @_Bike_Laux_Purple along tree-lined boulevard @_Location_City_Highway_Night, shapely athletic curves, generous bust with prominent neckline, flat toned waist, flashing playful peace sign and flirty wink toward camera, warm streetlights glowing overhead, clean asphalt road, sharp focus on rider, natural optical motion blur on road surface, 50mm f/1.4 lens, zero airbrushed skin, zero mannequin look --ar 9:16 --v 6.1 --style raw",
        "heartwarming sports portrait, gorgeous 21-year-old Vietnamese sporty woman @_Brand_Sport_Lead, glowing skin with natural soft matte texture and visible micro-pores, joyful dimpled smile, breathless happy laugh after night cycling, shaped glowing heart hands over chest, bike decelerated safely beside curb pavement on modern avenue plaza @_Location_City_Highway_Night, bare collarbones, warm architectural bokeh lights in background, shallow depth of field, 85mm f/1.4 lens, unretouched real human photography, zero waxy doll face, zero CGI --ar 9:16 --v 6.1 --style raw"
    ]
    for p in prompts:
        add_clean_paragraph(doc, p)
    doc.save(os.path.join(output_dir, "01_PROMPTS_ANH_HANG_LOAT.docx"))

def export_file_02(output_dir):
    doc = Document()
    add_styled_title(doc, "PROMPTS TẠO VIDEO HÀNG LOẠT (BATCH MEGA PROMPTS)",
                     "Dự án: Đạp Xe Đêm Sài Gòn • Chuẩn Tagged Blocks Khung 10.0s Cho Google Veo 3.1 & Muse",
                     "Định dạng Tool Batch: 100% văn bản thuần túy không nhãn thừa. Mỗi cảnh là đúng 1 đoạn văn liên tục không ngắt dòng bên trong (3 cảnh = đúng 3 đoạn văn sạch).")

    video_prompts = [
        "[SPECIFICATION]: Exactly 10.0 seconds, 9:16 vertical 1080x1920, 30 FPS, authentic dynamic sport vlog realism, unretouched real human photography. [CAMERA DYNAMICS]: Dynamic low-angle parallel tracking camera gliding smoothly at matching 15km/h speed alongside subject from 3/4 front angle, lens positioned slightly below handlebar level looking upward at 35-degree angle, accentuating long shapely legs and prominent chest curves. Subject centered tack-sharp in 9:16 frame with cinematic motion blur on asphalt road and golden municipal streetlights. Continuous unbroken take with stabilized gimbal glide. [CHARACTER ANCHOR]: @_Brand_Sport_Lead, authentic 21-year-old Vietnamese athletic woman, delicate oval face, large dark eyes, high ponytail fluttering backwards in night breeze. Athletic curvy hourglass figure featuring generous natural bust with tasteful visible cleavage, bare toned midriff, sculpted thighs. Wearing a form-fitting cream-white athletic crop top with dark contrast collar piping, high-waisted white denim booty shorts, white sneakers. Genuine living skin with visible micro-pores, natural rosy workout flush and delicate sweat sheen, strictly NO waxy skin, NO CGI. [VEHICLE & EQUIPMENT]: Riding lavender-purple mountain bike @_Bike_Laux_Purple, hands lightly gripping handlebars, synchronized smooth circular pedaling with feet locked to pedals, mechanically precise straight spokes and round wheels. [ENVIRONMENT]: Cruising on @_Location_City_Highway_Night under warm 3000K municipal tungsten streetlamps, modern skyscrapers in soft bokeh background, authentic tire contact shadows on asphalt road. [INITIAL STATE]: Inherits Keyframe K1: cycling smoothly forward, focused joyful gaze looking ahead. [ACTION & KINETIC TIMELINE]: - [0.0s - 3.0s]: Cycling smoothly forward into cool night breeze, high ponytail billowing backwards, chest rising and falling naturally with athletic breath. - [3.0s - 7.0s]: Turns head directly toward camera lens, breaking into a dazzling radiant smile with cute dimples, waving left hand enthusiastically to viewer while delivering cheerful greeting. - [7.0s - 10.0s]: Hand lowers back comfortably onto handlebar, radiant smile lingering warmly into lens, accelerating gracefully as avenue widens, settling smoothly into Keyframe K2. [AUDIO BGM & SFX]: Upbeat viral EDM remix intro with accelerating percussion, bicycle freewheel ticking, rush of night breeze, cheerful spoken Vietnamese voice (20 từ/10s): \"Hít hà không khí mát rượi của Sài Gòn về đêm cùng Uyên Hân nè cả nhà ơi! Đạp xe đêm vừa chill vừa khỏe người nữa nè!\" [FINAL STATE]: Hand lowering back to handlebar, radiant smile lingering, smoothly settling into Keyframe K2. [NEGATIVE CONSTRAINTS]: Strictly NO extra legs, NO slipping feet, NO waxy face, NO AI plastic doll skin, NO porcelain shine, NO CGI rendering, NO warped wheels.",
        "[SPECIFICATION]: Exactly 10.0 seconds, 9:16 vertical 1080x1920, 30 FPS, authentic dynamic sport vlog realism, unretouched real human photography. [CAMERA DYNAMICS]: Side-view 3/4 parallel tracking shot at bike level moving smoothly alongside rider, lens tilted slightly upward, keeping subject in razor-sharp focus while dark road and roadside greenery streak smoothly with motion blur. Continuous unbroken single take. [CHARACTER ANCHOR]: @_Brand_Sport_Lead, the identical 21-year-old athlete, natural skin pores, ponytail hair fluttering, wearing cream crop top with dark piping and white shorts, sculpted athletic hourglass curves, generous bust with prominent neckline, flat toned midriff, long toned legs pedaling with graceful cadence. [VEHICLE & EQUIPMENT]: Riding @_Bike_Laux_Purple lavender mountain bike in sharp focus, both feet firmly planted on pedals rotating in perfect mechanical harmony, straight spokes, rigid frame. [ENVIRONMENT]: Cruising inside @_Location_City_Highway_Night, broad tree-lined boulevard at night, golden streetlamps glowing overhead, authentic tire contact shadows. [INITIAL STATE]: Seamlessly matching Keyframe K2: side-profile tracking, continuous fluid pedaling cadence. [ACTION & KINETIC TIMELINE]: - [0.0s - 3.0s]: Steady rhythmic pedaling along shimmering boulevard, body leaning slightly forward with athletic grace, wind fluttering clothes. - [3.0s - 7.0s]: Playful head tilt toward tracking lens, laughing joyfully, left hand flashes cute peace sign beside cheek, winking right eye with magnetic flirty charm, upper body swaying to music. - [7.0s - 10.0s]: Replaces hand on bike grip, smoothly gliding past the final row of golden streetlamps as illuminated plaza approaches in distance, matching Keyframe K3. [AUDIO BGM & SFX]: Peak upbeat remix bass drop, vibrant kick drums, rhythmic pedal swish, happy breathless laugh, cheerful spoken Vietnamese voice (19 từ/10s): \"Gió đêm lướt qua tóc mát rượi luôn á, đạp xe kiểu vầy nó đã gì đâu, bao nhiêu mệt mỏi tan biến hết trơn!\" [FINAL STATE]: Lowering peace sign gesture, smoothly decelerating as illuminated plaza approaches, matching Keyframe K3. [NEGATIVE CONSTRAINTS]: Strictly NO three feet, NO deformed bike parts, NO AI plastic skin, NO waxy doll shine, NO camera UI overlays.",
        "[SPECIFICATION]: Exactly 10.0 seconds, 9:16 vertical 1080x1920, 30 FPS, authentic dynamic sport vlog realism, unretouched real human photography. [CAMERA DYNAMICS]: Tracking camera smoothly slows down and transitions into medium close-up portrait at eye level, perfectly stabilized front angle. Continuous unbroken take with pristine optical depth of field. [CHARACTER ANCHOR]: @_Brand_Sport_Lead, the identical 21-year-old athlete, glowing skin with visible micropores, charming dimples deepening, looking directly into camera with pure radiant joy, chest rising and falling with natural athletic respiration after cardio ride, bare collarbones, clean neckline. [VEHICLE & EQUIPMENT]: @_Bike_Laux_Purple decelerating smoothly to a stop, one foot gracefully resting on the curb pavement, maintaining bicycle balance. [ENVIRONMENT]: Positioned at plaza edge of @_Location_City_Highway_Night, luminous architectural plaza background with modern ambient lighting and lush greenery, shot on Sony A7 IV. [INITIAL STATE]: Inherits Keyframe K3: bike coasting to a gentle stop beside plaza curb. [ACTION & KINETIC TIMELINE]: - [0.0s - 3.0s]: Bike comes to a gentle stop, one foot planted firmly on pavement, brushing stray hair strand behind ear with bright luminous smile. - [3.0s - 7.0s]: Beaming directly at viewer with heartfelt warmth, two hands shaping a cute glowing heart gesture over her chest, delivering enthusiastic closing sign-off with synchronized lip-sync. - [7.0s - 10.0s]: Hands lower into a friendly energetic farewell wave, charming dimples deepening under plaza lights, chest settling into peaceful breathing rhythm, completing video loop. [AUDIO BGM & SFX]: Final musical beat cadence lingering softly, ambient evening breeze, cheerful spoken Vietnamese voice (16 từ/10s): \"Đạp xe đêm mê xỉu luôn đó cả nhà! Thấy cưng thì nhớ thả tim và theo dõi Uyên Hân nghen, mãi yêu!\", happy vocal chuckle. [FINAL STATE]: Holding sweet farewell smile and hand wave, eyes sparkling with sporting joy, completing the video loop. [NEGATIVE CONSTRAINTS]: Strictly NO extra fingers, NO morphing eyes, NO AI plastic doll skin, NO porcelain shine, NO camera UI overlays."
    ]
    for vp in video_prompts:
        add_clean_paragraph(doc, vp)
    doc.save(os.path.join(output_dir, "02_PROMPTS_VIDEO_HANG_LOAT.docx"))

def export_file_03(output_dir):
    doc = Document()
    add_styled_title(doc, "KỊCH BẢN LỜI THOẠI HÀNG LOẠT (BATCH TTS SCRIPTS)",
                     "Dự án: Đạp Xe Đêm Sài Gòn • Chuẩn 3 Phân Cảnh x 10.0s • 100% Giọng Sài Gòn",
                     "Định dạng Tool Batch: Lời thoại tiếng Việt sạch 100%, không nhãn thừa, không chú thích SFX. Mỗi cảnh là đúng 1 đoạn văn liên tục xuống dòng (3 cảnh = đúng 3 đoạn văn sạch).")

    voice_lines = [
        "Hít hà không khí mát rượi của Sài Gòn về đêm cùng Uyên Hân nè cả nhà ơi! Đạp xe đêm vừa chill vừa khỏe người nữa nè!",
        "Gió đêm lướt qua tóc mát rượi luôn á, đạp xe kiểu vầy nó đã gì đâu, bao nhiêu mệt mỏi tan biến hết trơn!",
        "Đạp xe đêm mê xỉu luôn đó cả nhà! Thấy cưng thì nhớ thả tim và theo dõi Uyên Hân nghen, mãi yêu!"
    ]
    for vl in voice_lines:
        add_clean_paragraph(doc, vl, font_name='Segoe UI', font_size=11.5)
    doc.save(os.path.join(output_dir, "03_PROMPTS_VOICE_HANG_LOAT.docx"))

def export_file_04(output_dir):
    doc = Document()
    add_styled_title(doc, "GÓI TỐI ƯU SEO & ĐĂNG TẢI VIRAL ĐA KÊNH",
                     "Dự án: Đạp Xe Đêm Sài Gòn • Chuẩn Đăng Tải Shorts / TikTok / Reels")

    p_h1 = doc.add_heading(level=2)
    p_h1.add_run("1. Prompt Tạo Ảnh Bìa Thumbnail (9:16)")
    thumb_prompt = "A hyper-realistic cinematic thumbnail photo, 9:16 vertical framing, @_Brand_Sport_Lead, 21-year-old athletic Vietnamese woman, radiant smile with deep cute dimples, sporty high ponytail, athletic hourglass curves featuring prominent natural cleavage, wearing fitted cream-white crop top with dark piping and white denim shorts, sitting on lavender mountain bike under warm glowing city streetlamps, dreamy urban bokeh, masterpiece, 8k resolution, raw photography, zero AI wax smoothing --ar 9:16 --v 6.1 --style raw"
    add_clean_paragraph(doc, thumb_prompt)

    p_h2 = doc.add_heading(level=2)
    p_h2.add_run("2. Chữ Dán Thumbnail (Overlay Text)")
    add_clean_paragraph(doc, "ĐẠP XE ĐÊM SÀI GÒN! 🚲✨\nNỤ CƯỜI ĐỐN TIM! 💖\nCHILL HẾT NẤC! 🌆", font_name='Segoe UI', font_size=11)

    p_h3 = doc.add_heading(level=2)
    p_h3.add_run("3. Tiêu Đề Đa Nền Tảng (A/B Testing Headlines)")
    add_clean_paragraph(doc, "A: Đạp xe lướt gió đêm ngắm Sài Gòn lung linh cùng Uyên Hân 🚲✨ #Shorts\nB: Buổi tối giải tỏa stress tuyệt vời nhất chính là đạp xe dạo phố 🌆💨 #TikTokSports\nC: Năng lượng tích cực và nụ cười tỏa nắng mỗi tối cùng Uyên Hân! 💖 #Reels", font_name='Segoe UI', font_size=11)

    p_h4 = doc.add_heading(level=2)
    p_h4.add_run("4. Caption & Hashtag 3 Tầng")
    add_clean_paragraph(doc, "Sau một ngày bận rộn, cảm giác được đạp xe lướt trong gió đêm mát rượi của Sài Gòn thật sự chữa lành tâm hồn! Cả nhà có thích đạp xe ban đêm như Hân không nè? Thả tim cho Hân nhé! 🚲✨\n\n#Shorts #TikTokSports #ReelsViral #CyclingVlog #DapXeDem #UyenHanSport #LinhChiDiDap #GaiXinhDapXe #FitnessMotivation #HealthyLifestyle #SportGirl", font_name='Segoe UI', font_size=10.5)

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
