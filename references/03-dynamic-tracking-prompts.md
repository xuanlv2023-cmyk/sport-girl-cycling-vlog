# Giai Đoạn 3 — Kỹ Thuật Quay Dynamic Parallel Tracking & Chống Méo AI

## 1. Bản Chất Của Kỹ Thuật Parallel Tracking Trong Video Đạp Xe
Khác với thể loại vlog ngồi tĩnh, video đạp xe đạt triệu view nhờ vào **Cảm Giác Tốc Độ Mượt Mà (Smooth Kinetic Flow)**:
- Chủ thể di chuyển về phía trước nhưng **giữ vị trí ổn định ở tâm khung hình (Center Framing)**.
- Hậu cảnh xung quanh (hàng cây, đèn đường, mặt đường nhựa, tòa nhà) lướt về phía sau với độ nhòe chuyển động tự nhiên (*cinematic motion blur*).
- Máy quay đồng tốc (chạy xe theo kèm bên cạnh hoặc phía trước) tạo góc nhìn như khán giả đang đạp xe lướt đi cùng nhân vật.

---

## 2. Ma Trận 4 Góc Máy Đạp Xe Chuẩn Studio (Multi-Angle Cycling Camera Matrix)

### 🔹 Góc 1: 3/4 Front Parallel Tracking (Góc Vàng Hút Triệu View)
- **Vị trí:** Camera đặt chếch 45 độ phía trước bên hông, chạy song song cùng tốc độ xe đạp.
- **Khung hình:** Thấy rõ khuôn mặt rạng rỡ của Uyên Hân, mái tóc bay phấp phới, tay lái, thân trên thon gọn và chuyển động của chân đạp.
- **Cú pháp Prompt:**
  ```text
  Smooth parallel tracking camera moving alongside at exact matching speed, medium-full shot framed from 3/4 front angle, subject centered in 9:16 vertical frame. Beautiful motion blur on city road and passing streetlights, crisp sharp focus on subject face and upper body.
  ```

### 🔹 Góc 2: Side-Profile Full Tracking (Góc Khoe Đường Cong & Vóc Dáng)
- **Vị trí:** Camera đặt vuông góc 90 độ ngang tầm hông, di chuyển song song.
- **Khung hình:** Thấy toàn bộ dáng xe đạp ngang, chuyển động guồng chân đạp pê-đan đều đặn, đường cong chữ S quyến rũ, lưng thẳng tự nhiên.
- **Cú pháp Prompt:**
  ```text
  Smooth side-view tracking shot at bike level, capturing full horizontal profile of woman cycling smoothly, mechanically synchronized pedaling motion, shapely athletic silhouette, dynamic motion blur streaks on passing background trees and pavement.
  ```

### 🔹 Góc 3: Rear Over-the-Shoulder Tracking (Góc Nhìn Khám Phá & Tự Do)
- **Vị trí:** Camera chạy bám đuổi từ phía sau lệch một bên vai hoặc trực diện đuôi xe.
- **Khung hình:** Thấy mái tóc bồng bềnh tung bay trong gió, tấm lưng thon, ba lô nhỏ thể thao và con đường thênh thang phía trước.
- **Cú pháp Prompt:**
  ```text
  Rear tracking camera chasing smoothly behind rider, showing windblown flowing ponytail, athletic posture, expansive open road receding ahead under twilight sky, camera maintains stable distance.
  ```

### 🔹 Góc 4: Stop & Pose / Dancing on Bike Beat (Điểm Dừng Nhấn Beat)
- **Vị trí:** Cận trung (MCU), xe giảm tốc độ hoặc dừng chân chạm đất, nhân vật nhìn thẳng vào camera làm cử chỉ vẫy tay, làm dấu chữ V, bắn tim hoặc nhún nhảy nhẹ theo điệu nhạc.
- **Cú pháp Prompt:**
  ```text
  Smooth camera decelerates into medium close-up, subject slowing down with one foot lightly tapping the ground, turning warmly toward lens with dazzling genuine smile, playful hand wave to viewer, joyful carefree demeanor.
  ```

---

## 3. Bộ Từ Khóa Chống Méo Khuyết Tật AI (Negative Constraints for Cycling)
Khi tạo prompt cho Veo 3.1, Kling, Runway Gen-3, Luma:
- **Chân & Cơ thể:** `strictly no phantom limbs, no third leg, no disconnected legs, feet firmly touching pedals at all times, no morphing knees, no rubbery thighs`.
- **Xe đạp:** `mechanically accurate bicycle frame, perfectly round wheels, rigid straight spokes, no melting chain, no duplicate handlebars, no detached seat`.
- **Mặt & Da:** `real unretouched Asian beauty, natural matte glowing skin, visible micropores, no waxy shine, no CGI anime rendering, no airbrushed mannequin face`.
