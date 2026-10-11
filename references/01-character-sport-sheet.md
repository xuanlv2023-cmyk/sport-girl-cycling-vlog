# Giai Đoạn 1 — Master Character & Sport Outfit Sheet (Uyên Hân Sport)
## Skill: `sport-girl-cycling-vlog` • Token Registry & Anti-AI Photorealism

Tài liệu này xác lập tiêu chuẩn nhận diện hình ảnh nhân vật thương hiệu độc quyền cho kênh **Uyên Hân Đạp Xe / Sport Vlog**, lấy cảm hứng từ năng lượng thể thao đời thực, tươi tắn, quyến rũ của các video đối thủ hot trend (như Vòng Quay Nắng Mai) nhưng mang tính **nguyên bản 100%**, đạt tiêu chuẩn **CHỤP ẢNH NGƯỜI THẬT THỂ THAO 100% (REAL HUMAN SPORTS PHOTOGRAPHY)**, loại bỏ hoàn toàn cảm giác tượng sáp đơ hoặc mặt nhựa AI.

---

## 1. HỆ THỐNG TOKEN THAM CHIẾU ĐỒNG BỘ (DYNAMIC TOKEN REGISTRY)

Để đảm bảo tính nhất quán tuyệt đối giữa ảnh (Keyframe) và video (I2V/T2V), bắt buộc dùng Token định danh theo cấu trúc `@_`:

### A. Quy chuẩn Token Nhân vật (`@_Char_...` / `@_Brand_...`):
- **Đơn nhân vật chính (Mặc định):** `@_Brand_Sport_Lead` (Uyên Hân Sport 21 tuổi).
- **Kịch bản đạp xe theo nhóm / Đa nhân vật:**
  - `@_Char_Sport_Lead`: Nữ chính Uyên Hân.
  - `@_Char_Cycling_Buddy`: Bạn đồng hành đạp xe cùng (chạy song song hoặc phía sau).
  - Mỗi nhân vật đều có ảnh Turnaround Sheet riêng biệt để nạp làm Image Reference.

### B. Quy chuẩn Token Bối cảnh (`@_Loc_...`):
- **Đơn bối cảnh:** `@_Location_City_Highway_Night` (Đại lộ thành phố về đêm).
- **Đa bối cảnh trong 1 video cycling vlog:**
  - `@_Location_Apartment_Lobby`: Khu sảnh chung cư dắt xe ra.
  - `@_Location_City_Highway_Night`: Cung đường đại lộ đêm lung linh ánh đèn.
  - `@_Location_Riverside_Path`: Đường ven sông lộng gió đón bình minh / hóng gió đêm.
- **Quy tắc gán trong Mega Prompt:** Mọi thẻ `[ENVIRONMENT & LIGHTING]` đều phải bắt đầu bằng Token bối cảnh tương ứng để giữ tính cố định của ánh sáng đường phố và mặt đường nhựa.

### C. Cơ chế 2 Chế độ (Tự Sáng Tạo vs Clone Đối Thủ):
1. **Chế độ Tự Sáng Tạo:** Khai báo `@_Brand_Sport_Lead` kết hợp trang phục thể thao động `[DYNAMIC_OUTFIT_STRING]` và xe đạp `[DYNAMIC_BIKE_STRING]`.
2. **Chế độ Clone Đối Thủ (Multimodal Video Audit):**
   - Quét video đối thủ qua thị giác máy tính.
   - Bóc tách nhân vật đối thủ thành `@_Cloned_Cyclist` $\rightarrow$ ánh xạ sang `@_Brand_Sport_Lead`.
   - Bóc tách loại xe (xe đạp mini Nhật, Fixed Gear, Road Bike) và ánh sáng đường phố thành `@_Cloned_Bike_Setting`.

---

## 2. BỘ QUY TẮC TRIỆT TIÊU CHẤT AI (ANTI-AI PHOTOREALISM SYSTEM)

> **⚠️ BỘ QUY TẮC PHÒNG CHỐNG "MẶT SÁP AI":**
> 1. **Cấm tuyệt đối từ khóa làm mịn bệt da:** `porcelain, flawless skin, plastic, airbrushed, supermodel, perfect face, 3D render, CGI`.
> 2. **Bắt buộc dùng da thật thể thao có lỗ chân lông:** `unretouched candid cycling photography, authentic living 21-year-old Vietnamese athletic girl, natural soft matte skin finish with visible micro-pores and fine skin texture, subtle natural workout flush on cheeks, windblown hair strands, lively engaging dark brown almond eyes`.
> 3. **Ánh sáng đường phố đời thường chân thực:** `authentic municipal street lamp tungsten glow, realistic night ambiance with natural sensor low-light dynamic range, authentic road reflections, realistic bicycle headlight beam, natural tire contact shadows, zero artificial neon glow, zero CGI bloom`.
> 4. **Khóa ngũ quan - Giải phóng trang phục & xe:** Ảnh Turnaround chỉ khóa gương mặt và vóc dáng. Quần áo thể thao, dòng xe đạp và cung đường biến thiên 100% theo kịch bản.

---

## 3. ĐẶC ĐIỂM NHẬN DIỆN DIỆN MẠO NGƯỜI THẬT 100%

| Thuộc Tính | Chi Tiết Nhận Diện Thực Tế | Từ Khóa Prompt Tiếng Anh Chuẩn (Raw Cycling) |
| :--- | :--- | :--- |
| **Độ tuổi & Nguồn gốc** | Nữ thanh niên Việt Nam 21-23 tuổi, năng động, thanh tú, yêu thể thao ngoài trời | `authentic candid sports vlog photography of @_Brand_Sport_Lead, a 21-year-old Vietnamese sporty woman, 100% living human, raw capture` |
| **Làn da thể thao** | Da sáng khỏe khoắn tự nhiên có lỗ chân lông thật, ửng hồng hào thể thao (outdoor flush), độ phản chiếu ánh sáng tự nhiên | `natural soft matte skin finish, visible delicate micro-pores and fine skin texture, subtle natural rosy workout flush, realistic skin translucency` |
| **Đôi mắt & Nụ cười** | Mắt to tròn đen láy sáng linh hoạt, nụ cười rạng rỡ má lúm đồng tiền nhẹ duyên dáng, biểu cảm thư giãn ngắm phố | `lively dark brown eyes with genuine emotional warmth, authentic eyelid creases, cheerful dimpled half-smile with natural lip texture` |
| **Mái tóc** | Tóc đuôi ngựa buộc cao/lửng năng động, mái thưa bay phất phơ tự nhiên trong gió đêm khi đạp xe | `sporty high ponytail with loose wispy bangs fluttering naturally in the breeze, dynamic windblown flyaway hair strands` |
| **Vóc dáng (Physique)** | Thân hình đồng hồ cát thể thao săn chắc, eo thon phẳng lì, đôi chân thon dài nuột nà khi đạp pê-đan | `fit toned athletic hourglass physique, slender defined shoulders, flat toned midriff, long shapely legs, healthy sporty curve` |
| **Phụ kiện cho phép** | Đồng hồ thông minh thể thao (smartwatch) ở cổ tay trái; tuyệt đối không đeo khuyên tai hay dây chuyền rườm rà | `sleek sports smartwatch on left wrist, unobstructed clean neckline, strictly no earrings, no necklace` |

---

## 4. MASTER PROMPT TURNAROUND 4 GÓC NHÌN (CHUẨN SENSOR MÁY CƠ)

Prompt chuẩn dùng để tạo ảnh Character Turnaround Sheet hoặc nạp làm Image Reference:

```text
A professional four-view character turnaround model sheet of @_Brand_Sport_Lead, an authentic 21-year-old Vietnamese athletic woman, displaying front view, three-quarter view, profile side view, and charming close-up smiling facial expression with subtle dimples. Delicate oval face, subtle natural dimples on cheeks, large bright expressive dark brown eyes, radiant cheerful smile, soft wispy bangs, long dark brown hair neatly tied in a sporty ponytail. Realistic healthy glowing skin texture with natural soft matte finish, visible natural micropores, athletic hourglass figure, full natural bust, delicate bare collarbones, slim toned waist. Wearing a minimalist white fitted scoop-neck short-sleeved t-shirt, unobstructed natural neckline, clean chest area, strictly no earrings, no necklace. Captured on Sony A7 IV with 50mm f/1.4 lens, clean neutral studio lighting, natural floor shadows, pristine camera sensor quality, unretouched real human photography, zero AI plastic wax smoothing, zero CGI look --ar 16:9 --style raw
```

---

## 5. BỘ SƯU TẬP TRANG PHỤC THỂ THAO BIẾN THIÊN (`[DYNAMIC_OUTFIT_STRING]`)

- **Set 1 (Đạp Xe Đêm Quyến Rũ):** `wearing an authentic fitted white short-sleeve athletic crop top, paired with high-waisted denim shorts, white athletic sneakers, clean neckline, bare collarbone, strictly no necklace, no earrings`
- **Set 2 (Bộ Đồ Tập Đồng Bộ):** `wearing a matching two-piece athletic summer set with a cream-beige short-sleeved sporty shirt with dark contrast collar piping and matching relaxed flare athletic shorts, white running shoes`
- **Set 3 (Chống Nắng Dã Ngoại):** `wearing a light mint-green sun-protection zip-up athletic jacket over a sports top, dark gray high-waisted compressive athletic yoga leggings, black baseball cap, white sneakers`
