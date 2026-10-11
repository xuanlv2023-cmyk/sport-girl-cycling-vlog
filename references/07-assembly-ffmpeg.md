# Giai Đoạn 7 — Dựng Phim Bằng FFmpeg Chuẩn 9:16 Shorts (Khung Phân Cảnh 10.0s)
## Skill: `sport-girl-cycling-vlog` • Ghép Nối Các Phân Cảnh 10s Từ Google Veo 3.1 & Muse

---

## 1. TIÊU CHUẨN KỸ THUẬT VIDEO MASTER
- **Khung phân cảnh thành phần:** Đúng **10.0 giây** mỗi cảnh (chuẩn giới hạn render tối đa của Google Veo 3.1 & Muse).
- **Tổng thời lượng video hoàn chỉnh:** 
  - 2 phân cảnh x 10s = **20.0 giây** (Fast Viral Shorts).
  - 3 phân cảnh x 10s = **30.0 giây** (Standard Viral Shorts).
  - 6 phân cảnh x 10s = **60.0 giây** (Full-Length YouTube Shorts).
- **Độ phân giải:** 1080x1920 (9:16 dọc hoàn hảo).
- **Tốc độ khung hình:** 30.0 FPS.
- **Codec:** H.264 (High Profile, level 4.2), YUV420p.
- **Audio:** AAC 320kbps, 48kHz, chuẩn âm lượng YouTube Shorts -14 LUFS.

---

## 2. QUY TRÌNH DỰNG TỰ ĐỘNG BẰNG FFMPEG

### Bước 1: Chuẩn hóa toàn bộ clip 10.0s về chuẩn 1080x1920 @ 30fps
```bash
ffmpeg -y -i raw_scene1.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30" -t 10.0 -c:v libx264 -preset slow -crf 18 -an scene1_10s.mp4
ffmpeg -y -i raw_scene2.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30" -t 10.0 -c:v libx264 -preset slow -crf 18 -an scene2_10s.mp4
ffmpeg -y -i raw_scene3.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30" -t 10.0 -c:v libx264 -preset slow -crf 18 -an scene3_10s.mp4
```

### Bước 2: Nối các cảnh (Concatenation)
Tạo file `concat_list.txt`:
```text
file 'scene1_10s.mp4'
file 'scene2_10s.mp4'
file 'scene3_10s.mp4'
```

Lệnh ghép nối video không giật khung:
```bash
ffmpeg -y -f concat -safe 0 -i concat_list.txt -c copy video_merged_30s.mp4
```

### Bước 3: Lồng âm thanh Remix & Thoại đã mix
```bash
ffmpeg -y -i video_merged_30s.mp4 -i audio_master.mp3 -c:v copy -c:a aac -b:a 320k -shortest final_short_30s.mp4
```
