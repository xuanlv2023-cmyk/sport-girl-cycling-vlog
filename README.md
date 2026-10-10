# Sport Girl Cycling & Fitness Vlog Pipeline (V1.0)
### AI Studio Sản Xuất Video Đạp Xe & Fitness Nữ Năng Động Quyến Rũ Chuẩn 9:16 Shorts

---

## Giới Thiệu
Skill **`sport-girl-cycling-vlog`** được thiết kế riêng biệt cho ngách nội dung **Thể Thao & Lối Sống Nữ (Sport, Outdoor Cycling, Home Fitness)** theo phong cách các kênh xu hướng triệu view như *Linh Chi Đi Đạp*.

Skill giải quyết triệt để các thách thức kỹ thuật lớn nhất của AI video vận động:
1. **Khóa nhận diện nhân vật thể thao Uyên Hân (`@_Brand_Sport_Lead`)** 21 tuổi, da thật, má lúm đồng tiền, vóc dáng fit & curvy.
2. **Kỹ thuật quay Dynamic Parallel Tracking** mượt mà, di chuyển song song đồng tốc.
3. **Triệt tiêu 100% lỗi AI cơ khí:** Chống méo bánh xe, chống 3 chân, chống trượt pê-đan.
4. **Tối ưu hóa âm thanh viral 15s:** Đồng bộ beat nhạc remix điện tử hoặc Voice Motivation ngắn gọn.
5. **Xuất xưởng trọn bộ 5 File Word (.docx)** chuyên dụng chuẩn plain text cho tool hàng loạt.

---

## Cấu Trúc Thư Mục Skill
```text
sport-girl-cycling-vlog/
├── SKILL.md                          # Quy trình chỉ dẫn cốt lõi 8 giai đoạn
├── README.md                         # Tài liệu tổng quan & hướng dẫn kích hoạt
├── assets/
│   └── character_turnaround.jpg      # Ảnh Master Model Sheet 4 góc nhìn của Uyên Hân
├── references/                       # 9 Hướng dẫn chuyên sâu độc lập
│   ├── 01-character-sport-sheet.md   # Hồ sơ Uyên Hân & bộ sưu tập đồ tập thể thao
│   ├── 02-bicycle-and-equipment.md   # Quy chuẩn xe đạp địa hình & máy tập thể dục
│   ├── 03-dynamic-tracking-prompts.md# Kỹ thuật quay camera bám đuổi song song
│   ├── 04-mega-prompts-templates.md  # Khung Mega Prompt 5s/10s/15s chuẩn Veo 3.1 & Kling
│   ├── 05-video-generation-rules.md  # Quy tắc render video & QA kiểm định
│   ├── 06-audio-and-editing.md       # Âm nhạc remix viral, beat drop & SFX gió xe
│   ├── 07-assembly-ffmpeg.md         # Quy trình dựng nối tự động bằng FFmpeg
│   ├── 08-lessons-learned.md         # 10 bài học xương máu chống lỗi AI thể thao
│   └── 09-publishing-and-seo.md      # Gói Thumbnail khoe dáng & SEO viral Shorts
├── scripts/
│   └── export_batch_docx.py          # Script tự động kết xuất 5 file Word (.docx)
└── examples/
    └── dap-xe-dem-thanh-pho/         # Dự án mẫu benchmark hoàn chỉnh 15s (3 cảnh)
        ├── FLOW.md
        ├── STORY.md
        ├── CHARACTER_SHEETS.md
        ├── MEGA_PROMPTS.md
        ├── AUDIO_GUIDE.md
        ├── METADATA_SEO.md
        └── export_batch/
            ├── 00_HO_SO_THAM_CHIEU_GOC.docx
            ├── 01_PROMPTS_ANH_HANG_LOAT.docx
            ├── 02_PROMPTS_VIDEO_HANG_LOAT.docx
            ├── 03_PROMPTS_AUDIO_VOICE.docx
            └── 04_METADATA_SEO.docx
```

---

## Lệnh Kích Hoạt Thực Chiến (Quick Start)

### 🔹 Cách 1: Làm video Đạp xe ngoài trời ban đêm (Viral Outdoor Cycling)
```text
Kích hoạt skill /sport-girl-cycling-vlog:
Tôi muốn làm video ngắn đạp xe đêm thành phố cùng Uyên Hân @_Brand_Sport_Lead:
- Thời lượng: 15 giây (3 phân cảnh x 5s ăn khớp nhịp beat drop).
- Định dạng: 9:16 dọc (Shorts/TikTok).
- Trang phục: Áo thun croptop cổ V màu hồng cánh sen ôm dáng, quần short jean trắng lưng cao, giày sneaker trắng.
- Xe đạp: Xe đạp leo núi màu tím pastel @_Bike_Laux_Purple.
- Âm thanh: Nhạc remix viral 15s "Gió cuốn theo chiều xuống" tiết tấu nhanh, hiệu ứng tiếng gió và líp xe đạp.
Yêu cầu: Xuất trọn gói kịch bản STORY.md, MEGA_PROMPTS.md, METADATA_SEO.md và 5 file Word (.docx).
```

### 🔹 Cách 2: Làm video Fitness trong nhà (Home Workout / Trampoline / Vibration Plate)
```text
Kích hoạt skill /sport-girl-cycling-vlog:
Tôi muốn làm video thể dục tại nhà cùng Uyên Hân @_Brand_Sport_Lead:
- Trụ cột: Bạt nhún mini trampoline nhún nhảy theo nhạc.
- Thời lượng: 15 giây.
- Định dạng: 9:16 dọc.
- Âm thanh: Nhạc dance điện tử sôi động.
Yêu cầu: Triển khai trọn bộ kịch bản và mega prompt chống lỗi chuyển động.
```

### 🔹 Cách 3: Clone trực tiếp video đối thủ (Linh Chi Đi Đạp)
```text
Kích hoạt skill /sport-girl-cycling-vlog:
Hãy bóc tách và clone video đối thủ tại đường dẫn: [Đường dẫn video MP4].
Yêu cầu: Chạy Hộp Khám Nghiệm Thị Giác Đa Phương Thức, trích xuất loại xe, trang phục và xây dựng bộ prompt tương ứng cho Uyên Hân.
```
