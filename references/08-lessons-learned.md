# BÀI HỌC KINH NGHIỆM & BỘ LỌC PHÒNG CHỐNG "CHẤT AI" CYCLING VLOG
## Skill: `sport-girl-cycling-vlog` • Phiên bản: V10 Production

Tổng hợp các bẫy lỗi khiến video đạp xe AI trông đơ sáp, bối cảnh giả tạo và giải pháp xử lý triệt để:

---

### 1. BẪY MẶT ĐƠ SÁP BÚP BÊ (AI PLASTIC DOLL FACE TRAP)
- **Hiện tượng:** Gương mặt bóng nhờn như tượng sáp, da láng mịn như búp bê silicon, mắt vô hồn, không có cảm giác gió thổi tự nhiên.
- **Nguyên nhân:** Dùng các từ khóa `flawless skin, porcelain face, gorgeous, supermodel, perfect, 3D render`.
- **Giải pháp dứt điểm:** Bắt buộc dùng:
  `unretouched candid cycling vlog photography, authentic living 21-year-old Vietnamese athletic girl, natural soft matte skin finish with visible micro-pores and fine skin texture, subtle natural workout flush on cheeks, windblown hair tendrils fluttering naturally in night breeze, lively expressive dark eyes`.
  Negative prompt: `airbrushed, plastic skin, porcelain doll, waxy shine, mannequin, CGI, 3D render`.

---

### 2. BẪY LỖI CƠ KHÍ XE ĐẠP (BICYCLE MECHANICAL MUTATION)
- **Hiện tượng:** Bàn đạp quay ngược chiều, xích lơ lửng, bánh xe bị méo ovan, chân không chạm pê-đan.
- **Giải pháp dứt điểm:**
  - Trong video prompt, luôn ghi: `feet firmly planted on pedals, realistic forward pedaling cadence in continuous circular rhythm, dual perfectly circular wheels with straight spokes, stable straight chain`.
  - Giữ mức Motion level an toàn `0.40 - 0.45` trên Kling AI / Wan để tránh biến dạng khung xe.

---

### 3. BẪY ÁNH SÁNG ĐÊM CYBERPUNK GIẢ TẠO (CGI NEON NIGHT TRAP)
- **Hiện tượng:** Đường phố tối mịt với ánh sáng viền xanh/hồng neon rực rỡ như phim viễn tưởng, không giống một buổi đạp xe đời thực.
- **Giải pháp dứt điểm:**
  - Khóa ánh sáng thực tế: `authentic municipal street lamp tungsten glow, realistic night road ambiance with natural sensor low-light grain, authentic tire contact shadows on asphalt road`.
  - Khóa cảm biến máy cơ: `captured on Sony A7S III with 35mm f/1.8 prime lens or iPhone 15 Pro 4K vlog style, natural optical depth of field, realistic dynamic range`.

---

### 4. BẪY MẤT ĐỒNG BỘ ĐẠP XE NHÓM HOẶC ĐỔI CUNG ĐƯỜNG (IDENTITY & ROUTE DRIFT)
- **Hiện tượng:** Cảnh 1 đạp xe trên đại lộ, cảnh 2 bị nhảy sang khu rừng hoang vu hoặc đổi màu xe đạp.
- **Giải pháp dứt điểm:**
  - Khai báo Token cố định: `@_Brand_Sport_Lead`, `@_Bike_Laux_Purple` và `@_Location_City_Highway_Night` xuyên suốt các phân cảnh.
  - Luôn đính kèm ảnh Turnaround Sheet của nhân vật và xe đạp khi tạo Keyframe.
