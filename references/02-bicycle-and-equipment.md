# Giai Đoạn 2 — Quy Chuẩn Xe Đạp, Cung Đường & Thiết Bị Thể Thao
## Skill: `sport-girl-cycling-vlog` • Token Registry: `@_Location_...` & `@_Bike_...`

Tài liệu quy chuẩn về thiết bị xe đạp thể thao và cung đường đạp xe với hệ thống Token đồng bộ, ánh sáng thực tế và loại bỏ triệt để hiệu ứng 3D/CGI nhân tạo.

---

### 1. HỆ THỐNG TOKEN BỐI CẢNH CUNG ĐƯỜNG ĐỒNG BỘ (LOCATION TOKENS)

Khi viết prompt Keyframe và Video, bắt buộc khai báo Token bối cảnh tương ứng trong thẻ `[ENVIRONMENT & LIGHTING]`:

| Token Bối Cảnh | Tên Địa Điểm | Đặc Trưng Không Gian & Ánh Sáng Thực Tế |
| :--- | :--- | :--- |
| `@_Location_City_Highway_Night` | Đại lộ thành phố về đêm | Đường nhựa rộng thênh thang, đèn đường cao áp vàng cam (tungsten), ánh đèn xe lướt nhẹ, mặt đường nhựa phản chiếu êm dịu, vỉa hè hiện đại. |
| `@_Location_Riverside_Path` | Cung đường ven sông lộng gió | Đường dạo bộ ven sông có lan can kim loại, rặng cây xanh, gió thổi tóc bay phất phơ, ánh đèn phản chiếu mặt nước lung linh. |
| `@_Location_Urban_Bridge` | Cầu vượt đô thị hiện đại | Cầu dây văng hoặc cầu thép hiện đại, làn đường dành riêng cho xe đạp, góc nhìn rộng mở ra skyline thành phố. |

---

### 2. NGUYÊN TẮC ÁNH SÁNG ĐƯỜNG PHỐ THỰC TẾ (ANTI-CGI LIGHTING)

> **⚠️ BỘ QUY TẮC ÁNH SÁNG ĐẠP XE ĐỜI THƯỜNG:**
> 1. **Loại bỏ ánh sáng neon Cyberpunk giả tạo:** Cấm dùng `futuristic neon city, cyberpunk glow, unreal engine lighting, volumetric light beams`. Chúng làm video giống game đua xe 3D.
> 2. **Ánh sáng đường phố thực tế (Realistic Municipal Lighting):**
>    - Ánh sáng vàng dịu tự nhiên từ các cột đèn cao áp đường phố (2700K - 3200K tungsten streetlights).
>    - Đèn pha xe đạp phát quầng sáng trắng chiếu xuống mặt đường phía trước bánh xe.
>    - Bóng đổ tiếp xúc của 2 bánh xe trên mặt đường nhựa (Tire contact shadows), tạo cảm giác xe bám chặt trên mặt đường thật.
> 3. **Chất liệu cảm biến máy cơ đời thực:**
>    - Khóa chất máy cơ: `shot on Sony A7S III with 35mm f/1.8 lens (hoặc: captured on iPhone 15 Pro 4K vlog style), natural low-light sensor grain, realistic dynamic range, true-to-life night street ambiance`.

---

### 3. TOKEN XE ĐẠP THỂ THAO CHUẨN CƠ KHÍ (`@_Bike_...`)

#### Dòng xe 1: Xe đạp địa hình khung tím pastel (`@_Bike_Laux_Purple`)
```text
riding @_Bike_Laux_Purple, a sleek modern lavender-purple mountain bike, black suspension fork, flat handlebars with phone mount, water bottle mounted on frame, mechanically accurate dual round wheels with straight spokes, pedals positioned precisely under rider feet, clean tire contact with asphalt road
```

#### Dòng xe 2: Xe đạp thể thao xám titan ánh kim (`@_Bike_Battle_Gray`)
```text
riding @_Bike_Battle_Gray, a metallic gunmetal-gray sport mountain bike, illuminated front LED headlight casting light beam onto the road, dark alloy frame, authentic mechanical gears and chainring, perfectly circular wheels with straight spokes
```
