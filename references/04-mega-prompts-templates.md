# Giai Đoạn 4 — Khung Mega Prompts Đạp Xe & Fitness (Chuẩn Thẻ Phân Rã & Timeline Động Lực Học)

## Mục đích
Soạn thảo trọn bộ Mega Prompts độc lập (**Standalone Tagged Blocks**) cho từng phân cảnh thể thao đạp xe của nhân vật Uyên Hân Sport `@_Brand_Sport_Lead`, tối ưu tuyệt đối cho **Google Veo 3.1**, **Kling AI (1.6)**, **Luma Dream Machine**, **Hailuo Minimax**, **Wan 2.1**.

Cấu trúc thẻ phân rã giúp khóa chặt vẻ đẹp thể thao quyến rũ, cơ thể săn chắc, chuyển động cơ học chính xác (bàn đạp quay tròn, bánh xe không méo) và chuyển giao trạng thái match-cut mượt mà giữa các cảnh.

---

## 1. Cấu Trúc Khối Thẻ Mega Prompt Chuẩn Thể Thao (Tagged Blocks Bắt Buộc)

Mỗi phân cảnh là một khối kỹ thuật độc lập gồm các thẻ định danh `[...]`:

```text
[SPECIFICATION]: Exactly [5.0s / 10.0s], 9:16 vertical 1080x1920, [30 / 60 FPS], unretouched real human photography, authentic dynamic sport vlog realism.
[CAMERA DYNAMICS]: Parallel tracking shot moving smoothly alongside subject at identical speed from 3/4 front angle, eye level, subject centered in 9:16 frame. Crisp tack-sharp subject with realistic cinematic motion blur on surrounding road surface and passing streetlights. Strictly NO camera shake, stabilized gimbal glide.
[CHARACTER ANCHOR]: @_Brand_Sport_Lead, an attractive 21-year-old East Asian athletic woman, delicate oval face, charming dimples, radiant joyful smile, long dark hair tied in a high sporty ponytail flying backwards in wind, wearing [DYNAMIC_SPORT_OUTFIT], unobstructed bare neckline, delicate collarbones, athletic toned hourglass physique, full bust, flat slim waist, shapely legs, strictly no earrings, no necklace.
[VEHICLE & EQUIPMENT]: Riding @_Bike_Asset, sleek mountain bike with mechanically precise pedals rotating smoothly under her feet, circular wheels with straight spokes, flat black handlebars.
[ENVIRONMENT]: Positioned on @_Location_ID, [mô tả đường phố / cảnh quan / ánh sáng], soft ambient streetlamps casting warm streaks, modern skyscrapers in soft bokeh background.
[INITIAL STATE]: First frame strictly inherits Keyframe K_x: [vị trí đạp xe, hướng nhìn, tốc độ ban đầu].
[ACTION & KINETIC TIMELINE]:
- [0-2s]: Cycling cadence & wind flow — Cycling smoothly forward, focused joyful gaze looking ahead, hair billowing backwards in natural wind.
- [2-4s]: Lens engagement & charm — Turns head toward camera lens with an infectious dazzling smile, releases one hand from handlebar to wave / gesture happily.
- [4-5s]: Pose settling & road tracking — Hands return smoothly to handle / holds gesture, gaze shifting forward or maintaining eye contact, settling into Keyframe K_{x+1}.
[AUDIO BGM & SFX]: Upbeat viral remix beat with punchy bass drops, layered with organic sounds of bicycle chain clicking, whirring freewheel, soft wind gust.
[FINAL STATE]: Final frame settles seamlessly into Keyframe K_{x+1} for invisible match-cut.
[NEGATIVE CONSTRAINTS]: Strictly NO extra limbs, NO three legs, NO feet slipping off pedals, NO distorted wheels, NO bent bike frame, NO waxy plastic skin, NO CGI 3D doll face, NO camera UI overlays.
```

---

## 2. ⚠️ Kỷ Luật Sắt Của Dòng Video Đạp Xe Thể Thao

1. **KHÓA CHUYỂN ĐỘNG CƠ HỌC BÀN ĐẠP & BÁNH XE (MECHANICAL CADENCE LOCK):**
   - Bàn chân luôn bám chắc trên pedal, nhịp đạp tròn đều, bánh xe tròn hoàn hảo không bị méo lệch thành hình bầu dục.
2. **KỶ LUẬT GÓC QUAY TRACKING SONG SONG (PARALLEL TRACKING):**
   - Camera di chuyển tịnh tiến cùng vận tốc với xe đạp, giữ chủ thể sắc nét trong khi hậu cảnh và mặt đường lướt mờ (motion blur) tự nhiên.
3. **LIÊN KẾT TRẠNG THÁI MATCH-CUT:**
   - Sử dụng thẻ `[INITIAL STATE]` và `[FINAL STATE]` để kết nối các đoạn đường khác nhau một cách liền mạch.
