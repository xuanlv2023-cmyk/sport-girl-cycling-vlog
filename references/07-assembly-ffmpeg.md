# Giai Đoạn 7 — Dựng Phim Bằng FFmpeg Chuẩn 9:16 Shorts

## 1. Tiêu Chuẩn Kỹ Thuật Video Master
- **Độ phân giải:** 1080x1920 (9:16 dọc hoàn hảo).
- **Tốc độ khung hình:** 30.0 FPS hoặc 60.0 FPS (tối ưu chuyển động thể thao mượt mắt).
- **Codec:** H.264 (High Profile, level 4.2), YUV420p.
- **Audio:** AAC 320kbps, 48kHz, chuẩn âm lượng YouTube Shorts -14 LUFS.

---

## 2. Quy Trình Dựng Tự Động Bằng FFmpeg

### Bước 1: Chuẩn hóa toàn bộ clip 5s/10s về chuẩn 1080x1920 @ 30fps
```bash
ffmpeg -y -i raw_scene1.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30" -c:v libx264 -preset slow -crf 18 -an scene1_norm.mp4
ffmpeg -y -i raw_scene2.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30" -c:v libx264 -preset slow -crf 18 -an scene2_norm.mp4
ffmpeg -y -i raw_scene3.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30" -c:v libx264 -preset slow -crf 18 -an scene3_norm.mp4
```

### Bước 2: Nối các cảnh (Concatenation)
Tạo file `concat_list.txt`:
```text
file 'scene1_norm.mp4'
file 'scene2_norm.mp4'
file 'scene3_norm.mp4'
```
Chạy lệnh nối:
```bash
ffmpeg -y -f concat -safe 0 -i concat_list.txt -c copy visual_master.mp4
```

### Bước 3: Mix nhạc nền viral và SFX vào video
```bash
ffmpeg -y -i visual_master.mp4 -i viral_music_15s.mp3 -filter_complex "[1:a]volume=1.0[a_out]" -map 0:v -map "[a_out]" -c:v copy -c:a aac -b:a 320k -shortest final_master.mp4
```
