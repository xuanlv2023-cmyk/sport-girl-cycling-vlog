# Sport Girl Cycling & Fitness Vlog Pipeline (V10 Production)
### AI Studio Sản Xuất Video Đạp Xe & Kinetic Fitness Nữ Năng Động Quyến Rũ Chuẩn 9:16 Shorts

---

## Giới Thiệu
Skill **`sport-girl-cycling-vlog`** được thiết kế riêng biệt cho ngách nội dung **Nữ Thần Thể Thao Đạp Xe & Lifestyle Fitness (Sport Girl Cycling, Outdoor & Home Workout Vlog)**, lấy cảm hứng và đối chuẩn trực tiếp từ kênh triệu view **"Linh Chi Đi Đạp"**.

Skill giải quyết triệt để vấn đề video AI bị đơn điệu, đơ cứng và thiếu sức hút thị giác:
1. **Khóa nhận diện nhân vật thể thao Uyên Hân (`@_Brand_Sport_Lead`)** 21 tuổi, má lúm đồng tiền sâu, da thật có lỗ chân lông và mồ hôi tập luyện.
2. **Khóa vóc dáng thể thao quyến rũ (`@_Body_Athletic_Cleavage_Curves`):** Vòng 1 đầy đặn lộ rãnh ngực tự nhiên (`tasteful prominent cleavage`), eo thon lộ cơ bụng số 11, hông quả táo và đôi chân dài miên man.
3. **Kỹ thuật quay Low-Angle Upward Tracking Cam:** Góc máy thấp dưới ghi-đông hất nhẹ lên 35 độ, chạy đồng tốc song song, tôn trọn vẹn vóc dáng và chân dài.
4. **Timeline Diễn xuất Vi mô Micro-Acting 15.0s:** Nhân vật liên tục biến hóa biểu cảm từng 3-4s (tập trung đạp xe $\rightarrow$ cười bừng sáng má lúm $\rightarrow$ nháy mắt tinh nghịch `flirty wink` $\rightarrow$ buông tay thả dáng/bắn tim).
5. **Hỗ trợ 2 Chế Độ Độc Lập:**
   - **Chế độ 1 — AI Gợi Ý (AI Ideation Mode):** Kho 10 kịch bản mẫu thể thao độc quyền chia 3 nhánh: Đạp xe dạo phố đêm, Bạt nhún Trampoline nảy lửa, Fitness phòng khách sang trọng. 100% Giọng Miền Nam / Sài Gòn tự nhiên.
   - **Chế độ 2 — Clone Đối Thủ 1:1 (Linh Chi Clone Mode):** Bóc tách 1:1 từ 91 video thực tế của kênh Linh Chi Đi Đạp thông qua [`references/10-competitor-clone-matrix.md`](references/10-competitor-clone-matrix.md).
6. **Xuất xưởng Trọn gói 5 File Word (.docx):** 100% plain text paragraphs, 0 table, 1 đoạn văn liên tục per scene cho tool batch.

---

## Cấu Trúc Thư Mục Skill
```text
sport-girl-cycling-vlog/
├── SKILL.md                          # Quy trình chỉ dẫn cốt lõi 10 giai đoạn chuẩn V10
├── README.md                         # Tài liệu tổng quan & hướng dẫn kích hoạt nhanh
├── assets/
│   └── character_turnaround.jpg      # Ảnh Master Model Sheet 4 góc nhìn của Uyên Hân
├── references/                       # 10 Hướng dẫn chuyên sâu độc lập
│   ├── 01-character-sport-sheet.md   # Hồ sơ Uyên Hân, vóc dáng vòng 1 & 6 set đồ gợi cảm
│   ├── 02-bicycle-and-equipment.md   # Quy chuẩn xe đạp địa hình, bạt nhún, máy rung & bối cảnh
│   ├── 03-dynamic-tracking-prompts.md# Kỹ thuật quay góc thấp & Timeline Micro-Acting 15s
│   ├── 04-mega-prompts-templates.md  # 3 mẫu Mega Prompt Tagged Blocks cho 3 phân nhánh
│   ├── 05-video-generation-rules.md  # Quy tắc render video & QA kiểm định chất lượng
│   ├── 06-audio-and-editing.md       # Âm nhạc remix viral TikTok, beat drop & SFX gió xe
│   ├── 07-assembly-ffmpeg.md         # Quy trình dựng nối tự động bằng FFmpeg chuẩn 15.0s
│   ├── 08-lessons-learned.md         # 6 bài học kinh nghiệm xương máu chống video đơn điệu
│   ├── 09-publishing-and-seo.md      # Gói Thumbnail khoe dáng & SEO viral Shorts
│   └── 10-competitor-clone-matrix.md # Ma trận bóc tách 1:1 từ 91 video Linh Chi Đi Đạp
├── scripts/
│   └── export_batch_docx.py          # Script tự động kết xuất 5 file Word (.docx) zero-table
└── examples/
    └── dap-xe-dem-thanh-pho/         # Dự án mẫu benchmark hoàn chỉnh 15s
        ├── FLOW.md
        ├── STORY.md
        ├── CHARACTER_SHEETS.md
        ├── MEGA_PROMPTS.md
        ├── VO_SCRIPT.md
        ├── METADATA_SEO.md
        └── export_batch/
            ├── 00_HO_SO_THAM_CHIEU_GOC.docx
            ├── 01_PROMPTS_ANH_HANG_LOAT.docx
            ├── 02_PROMPTS_VIDEO_HANG_LOAT.docx
            ├── 03_PROMPTS_VOICE_HANG_LOAT.docx
            └── 04_METADATA_SEO.docx
```

---

## Hướng Dẫn Kích Hoạt Thực Chiến

### 🔹 Cách 1: Sử dụng Chế độ AI Gợi Ý (AI Ideation Mode)
```text
Kích hoạt skill /sport-girl-cycling-vlog ở Chế độ AI Gợi Ý:
Tôi muốn làm video 15s đạp xe dạo phố đêm Sài Gòn cùng Uyên Hân @_Brand_Sport_Lead:
- Phân nhánh: Outdoor Night Cycling (Đạp xe đại lộ đêm lung linh ánh đèn).
- Thời lượng: 15.0 giây (Single Master Take).
- Vóc dáng & Trang phục: @_Body_Athletic_Cleavage_Curves, áo croptop sọc ngang ôm sát tôn ngực, quần short jean trắng cạp cao.
- Xe đạp: Xe đạp leo núi sườn tím pastel @_Bike_Laux_Purple.
- Yêu cầu: Diễn xuất vi mô sống động (cười má lúm, nháy mắt tinh nghịch, buông tay thả dáng), nhạc EDM remix viral, xuất kịch bản Giọng Sài Gòn và 5 file Word (.docx).
```

### 🔹 Cách 2: Sử dụng Chế độ Clone Đối Thủ 1:1 (Linh Chi Clone Mode)
```text
Kích hoạt skill /sport-girl-cycling-vlog ở Chế độ Clone Đối Thủ:
Hãy bóc tách và clone Video 10 (hoặc Video 14 / Video 22) từ folder đối thủ "Linh Chi Đi Đạp":
- Đạo cụ: Bạt nhún mini trampoline (hoặc máy rung ban công / xe đạp hoàng hôn).
- Nhân vật đích: Uyên Hân Sport @_Brand_Sport_Lead, chuẩn da thật có lỗ chân lông, tôn vóc dáng vòng 1 và đường cong đồng hồ cát.
- Yêu cầu: Giữ nguyên 100% bố cục góc máy và cử động nảy của đối thủ, xuất trọn gói Keyframe, Mega Prompt và 5 file Word (.docx).
```
