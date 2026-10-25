# L8 - Khảo sát hài lòng CSAT/NPS (Track SE)
Nguyễn Duy Lợi - 2374802010291. Mẫu BT2 Buổi 8 xây dựng từ thiết kế BT1.

## 1. Giới thiệu
Backend REST API cho Survey và Feedback sau bảo hành, dùng kiến trúc routes/services/repositories, MySQL.

## 2. Yêu cầu môi trường
- Python 3.10+; MySQL 8+; Git; VS Code (khuyến nghị).
- Tạo môi trường: `python -m venv .venv` rồi kích hoạt.
- Cài thư viện: `pip install -r requirements.txt`.
- Sao chép `.env.example` thành `.env`, sửa thông tin MySQL (không commit `.env`).
- Chạy lần lượt `migrations/001_init.sql` và `migrations/002_seed.sql` trong MySQL Workbench.
- Khởi chạy: `python app.py` rồi truy cập `http://127.0.0.1:5000/`.

## 3. Kiến trúc
- `src/routes`: API HTTP; `src/services`: kiểm tra nghiệp vụ; `src/repositories`: truy vấn MySQL.
- `migrations/`: DDL và seed; `docs/`: nhật ký thiết kế và ảnh minh chứng.

## 4. API
- `GET /api/surveys` - danh sách khảo sát.
- `GET /api/surveys/1` - xem khảo sát.
- `POST /api/surveys` - JSON `{"ticket_id":2,"expire_date":"2026-12-31"}` (cần ticket tồn tại).
- `PUT /api/surveys/1` - JSON `{"expire_date":"2026-12-31"}`.
- `DELETE /api/surveys/1` - xóa khảo sát (xóa kèm phản hồi).
- `POST /api/surveys/1/feedback` - JSON `{"csat_score":5,"nps_score":9,"comment":"Hài lòng"}`.

## 5. Kiểm thử thủ công
1. `GET /` phải trả JSON status `running`.
2. `GET /api/surveys` sau seed phải có khảo sát mẫu.
3. `POST /api/surveys/1/feedback` với CSAT 5, NPS 9 phải trả mã 201.
4. Gửi CSAT 6 phải nhận lỗi 400.
5. Chụp ảnh kết quả thực tế vào `docs/minh-chung/`.

## 6. Trạng thái tiến độ hiện tại
- [x] Chuẩn bị cấu trúc 3 lớp, migration, seed, CRUD Survey, ghi nhận Feedback.
- [x] Soạn nhật ký điều chỉnh thiết kế BT1.
- [ ] Kiểm thử kết nối MySQL và API trên máy sinh viên.
- [ ] Bổ sung ảnh minh chứng chạy thực tế.
- [ ] Commit ít nhất 2 lần và push GitHub; cập nhật link commit cuối buổi.
- [ ] Dashboard, lọc/xuất báo cáo, bảo mật phân quyền và kiểm thử hiệu năng (giai đoạn tiếp theo).

## 7. Git và báo cáo
Trong repository của bạn, chia ít nhất 2 commit thực tế, ví dụ:
`git add src migrations app.py requirements.txt .gitignore .env.example && git commit -m "feat: implement survey CRUD and feedback API"`
`git add README.md docs && git commit -m "docs: document architecture and BT1 design changes"`
Sau đó `git push` và lấy URL commit mới nhất trên GitHub. Không commit mật khẩu hoặc file `.env`.

## 8. Giới hạn
Đây là mã nguồn mẫu chưa chạy với MySQL của sinh viên. Không có ảnh chạy thực tế, không có commit GitHub được tạo thay sinh viên. API quản trị chưa có xác thực; chỉ chạy trong môi trường phát triển cục bộ.
