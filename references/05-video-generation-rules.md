# Giai Đoạn 5 — Quy Trình Render Video & Kiểm Soát Chất Lượng AI

## 1. Các Nền Tảng AI Video Tối Ưu Cho Thể Loại Vận Động
- **Google Veo 3.1 (Omni 1.1 Flash):** Số 1 về độ mượt mà chuyển động, xử lý tracking camera và gió thổi tóc tự nhiên nhất thế giới hiện nay.
- **Kling AI (v1.5 / v2.0):** Khả năng mô phỏng chân đạp xe và giữ on-model khuôn mặt cực tốt khi dùng tính năng First Frame + Last Frame.
- **Runway Gen-3 Alpha:** Rất mạnh về camera motion prompt (`[Camera: Tracking forward-right at 15mph]`).
- **Hailuo AI (Minimax):** Diễn xuất khuôn mặt tươi tắn, biểu cảm nụ cười tự nhiên, không bị đơ cứng.

---

## 2. Kỹ Thuật First Frame & Last Frame Cho Video Đạp Xe
Khi chuyển cảnh giữa các phân đoạn đạp xe:
- **Nguyên tắc Match-Motion:** Khung hình kết thúc của cảnh trước ($K_x$) và khung bắt đầu cảnh sau ($K_{x+1}$) phải cùng chung vector vận tốc chuyển động (xe đang tiến về phía trước).
- Không match-cut từ trạng thái đang đạp xe 20km/h đột ngột sang đứng yên tại chỗ trong cùng 1 cảnh liên tục, mà phải có nhịp giảm tốc (*deceleration beat*).

---

## 3. Checklist Kiểm Định Chất Lượng Video (QA Checklist)
Trước khi đưa vào dựng:
- [ ] Khuôn mặt nhân vật đúng nhận diện Uyên Hân (má lúm, mắt to, không sáp nhựa).
- [ ] Không có hiện tượng 3 chân, chân lơ lửng hoặc xuyên qua nan hoa.
- [ ] Bánh xe đạp giữ hình tròn, không méo hình elip hoặc tan biến khi quay nhanh.
- [ ] Gió thổi tóc và áo quần bay tự nhiên, không bị giật cục (zero frame stuttering).
- [ ] Camera tracking di chuyển mượt mà, không rung lắc chóng mặt.
