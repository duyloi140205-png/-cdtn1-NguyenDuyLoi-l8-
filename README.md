# CDTN1 – Nguyễn Duy Lợi – L8

**Đề tài:** Smart CRM – Mekong Mobile: Khảo sát hài lòng CSAT/NPS
**Track:** SE – Software Engineering
**Sinh viên:** Nguyễn Duy Lợi – 2374802010291
**GitHub:** https://github.com/duyloi140205-png/-cdtn1-NguyenDuyLoi-l8-

## 1. Giới thiệu

Dự án xây dựng hệ thống khảo sát mức độ hài lòng của khách hàng sau bảo hành, thuộc bài toán Smart CRM – Mekong Mobile.

Hệ thống hỗ trợ:
- Xem danh sách khảo sát.
- Xem chi tiết khảo sát.
- Tiếp nhận phản hồi CSAT/NPS.
- Lưu dữ liệu phản hồi vào MySQL.
- Kiểm tra dữ liệu đầu vào và xử lý lỗi nghiệp vụ.

Công nghệ sử dụng:
- Backend: Python, Flask.
- Frontend: React, Vite.
- Database: MySQL.
- Testing: pytest.

## 2. Yêu cầu môi trường

- Python 3.10 trở lên.
- MySQL 8 trở lên.
- Node.js và npm.
- Git.
- VS Code hoặc trình soạn thảo tương đương.

## 3. Kiến trúc và hướng dẫn cài đặt, chạy hệ thống

### 3.1. Kiến trúc

Backend sử dụng kiến trúc ba lớp:

- `src/routes/`: Tiếp nhận yêu cầu HTTP và trả kết quả JSON.
- `src/services/`: Xử lý và kiểm tra quy tắc nghiệp vụ.
- `src/repositories/`: Truy vấn cơ sở dữ liệu MySQL.

Frontend React gồm:

- `frontend/src/pages/`: Các màn hình danh sách khảo sát, chi tiết khảo sát và tiếp nhận phản hồi.
- `frontend/src/components/`: Thành phần dùng chung, gồm xử lý trạng thái tải dữ liệu, rỗng và lỗi.
- `frontend/src/api/client.js`: Gọi API Backend.

### 3.2. Tải mã nguồn

Mở PowerShell và chạy:

```powershell
git clone https://github.com/duyloi140205-png/-cdtn1-NguyenDuyLoi-l8-.git
cd -- -cdtn1-NguyenDuyLoi-l8-
```

### 3.3. Cài đặt Backend

Tạo môi trường Python:

```powershell
python -m venv .venv
```

Kích hoạt môi trường:

```powershell
.\.venv\Scripts\Activate.ps1
```

Cài đặt thư viện:

```powershell
python -m pip install -r requirements-lock.txt
```

### 3.4. Cấu hình MySQL

1. Khởi động MySQL.
2. Mở MySQL Workbench.
3. Thực thi các file SQL trong thư mục `migrations/` theo thứ tự:
   - `001_init.sql`
   - `002_seed.sql`
4. Sao chép `.env.example` thành `.env`.

### Cấu hình đăng nhập demo

Trong file `.env`, cấu hình các biến:

- `SECRET_KEY`: Khóa bí mật dùng để ký phiên đăng nhập Flask.
- `DEMO_USERNAME`: Tên đăng nhập demo.
- `DEMO_PASSWORD`: Mật khẩu đăng nhập demo.

Tạo giá trị `SECRET_KEY` riêng và đặt mật khẩu demo khi cài đặt.

Không commit file `.env`, mật khẩu hoặc khóa bí mật lên GitHub.

5. Cập nhật thông tin kết nối MySQL trong `.env` theo cấu hình máy.

**Lưu ý:** Không đưa file `.env` hoặc mật khẩu MySQL lên GitHub.

### 3.5. Chạy Backend Flask

Tại thư mục gốc dự án:

```powershell
python app.py
```

Backend dự kiến chạy tại:

`http://127.0.0.1:5000/`

Kiểm tra API danh sách khảo sát:

`http://127.0.0.1:5000/api/surveys`

### 3.6. Chạy Frontend React

Mở một Terminal mới:

```powershell
cd frontend
npm install
npm run dev
```

Mở địa chỉ Local do Vite hiển thị, thông thường:

`http://localhost:5173/`

Nếu cổng 5173 đang được sử dụng, Vite có thể chuyển sang cổng khác, chẳng hạn `http://localhost:5174/`.

**Lưu ý:** Cần chạy đồng thời Backend Flask và Frontend React.

### 3.7. Chạy Unit Test

Mở Terminal tại thư mục gốc dự án, kích hoạt `.venv` và chạy:

```powershell
python -m pytest -v
```

Kết quả kiểm thử đã ghi nhận trong quá trình thực hành Buổi 10: **5 Unit Test PASS**.


### 3.8. Kiểm tra luồng tích hợp

1. Khởi động MySQL và Backend Flask.
2. Khởi động Frontend React.
3. Truy cập http://localhost:5173/.
4. Đăng nhập bằng tài khoản demo được cấu hình trong `.env`.
5. Xem danh sách khảo sát.
6. Chọn khảo sát để xem chi tiết.
7. Mở màn hình tiếp nhận phản hồi CSAT/NPS.
8. Nhập mã khảo sát hợp lệ, CSAT từ 1 đến 5 và NPS từ 0 đến 10.
9. Gửi phản hồi và kiểm tra dữ liệu trong MySQL.
10. Nhấn Đăng xuất và xác nhận hệ thống quay về màn hình đăng nhập.

API Survey và Feedback yêu cầu phiên đăng nhập hợp lệ.
Nếu chưa đăng nhập, hệ thống trả về HTTP 401.


## 4. API

| Phương thức | Endpoint | Chức năng |
|---|---|---|
| GET | `/api/surveys` | Danh sách khảo sát |
| GET | `/api/surveys/1` | Chi tiết khảo sát |
| POST | `/api/surveys` | Tạo khảo sát |
| PUT | `/api/surveys/1` | Cập nhật khảo sát |
| DELETE | `/api/surveys/1` | Xóa khảo sát |
| POST | `/api/surveys/1/feedback` | Gửi phản hồi CSAT/NPS |
| POST | `/api/auth/login` | Đăng nhập |
| GET | `/api/auth/me` | Kiểm tra phiên đăng nhập |
| POST | `/api/auth/logout` | Đăng xuất |
| GET | `/api/feedback` | Danh sách phản hồi |
| GET | `/api/feedback/1` | Chi tiết phản hồi |
| PUT | `/api/feedback/1` | Cập nhật phản hồi |
| DELETE | `/api/feedback/1` | Xóa phản hồi |

Ví dụ JSON tạo khảo sát:

```json
{
  "ticket_id": 2,
  "expire_date": "2026-12-31"
}
```

Ví dụ JSON gửi phản hồi:

```json
{
  "csat": 5,
  "nps": 9,
  "comment": "Khách hàng hài lòng với dịch vụ bảo hành."
}
```

Các mã HTTP dự kiến:
- `200`: Truy vấn hoặc cập nhật thành công.
- `201`: Tạo mới thành công.
- `400`: Dữ liệu đầu vào không hợp lệ.
- `404`: Không tìm thấy dữ liệu.
- `409`: Xung đột dữ liệu liên quan.
- `401`: Chưa đăng nhập hoặc phiên đăng nhập không hợp lệ.

## 5. Kiểm thử

Kiểm thử Backend bằng pytest với năm trường hợp:

1. Tạo khảo sát hợp lệ.
2. Từ chối tạo khảo sát đã hết hạn.
3. Cập nhật khảo sát hợp lệ.
4. Kiểm tra giá trị biên CSAT.
5. Từ chối điểm NPS không hợp lệ.

Kết quả đã ghi nhận: **5 passed**.

Kiểm thử tích hợp:
- React lấy danh sách khảo sát từ Flask API.
- Người dùng xem chi tiết khảo sát.
- Người dùng gửi phản hồi.
- Backend xử lý yêu cầu và lưu dữ liệu vào MySQL.

Ảnh minh chứng được lưu trong `docs/minh-chung/`.

## 6. Trạng thái tiến độ hiện tại

### Sprint 1 – Buổi 8

- [x] Xây dựng cấu trúc Backend ba lớp.
- [x] Tạo migration và dữ liệu mẫu.
- [x] Hiện thực CRUD Survey.
- [x] Hiện thực API tiếp nhận Feedback.
- [x] Tạo tài liệu và minh chứng thực hành.

### Sprint 2 – Buổi 10

- [x] Khởi tạo Frontend React/Vite.
- [x] Xây dựng màn hình danh sách khảo sát.
- [x] Xây dựng màn hình chi tiết khảo sát.
- [x] Xây dựng màn hình tiếp nhận phản hồi.
- [x] Kết nối Frontend với Flask API.
- [x] Bổ sung xử lý dữ liệu và kiểm tra đầu vào.
- [x] Viết và chạy thành công 5 Unit Test.
- [x] Lưu ảnh minh chứng giao diện và kết quả kiểm thử.
- [x] Lưu ảnh minh chứng truy vấn phản hồi MySQL.
- [ ] Kiểm tra quy trình cài đặt từ bản clone mới.
- [ ] Hoàn tất commit và push các thay đổi Sprint 2.

### Công việc giai đoạn tiếp theo

- Dashboard thống kê CSAT/NPS.
- Lọc và xuất báo cáo.
- Phân quyền người dùng theo vai trò.
- Quản lý tài khoản người dùng thực tế.
- Kiểm thử hiệu năng.


### Bổ sung BT2 – Buổi 12

- [x] Hoàn thiện CRUD Survey.
- [x] Bổ sung CRUD Feedback.
- [x] Xây dựng giao diện đăng nhập React.
- [x] Tích hợp Flask Session.
- [x] Bảo vệ API Survey và Feedback bằng kiểm tra phiên đăng nhập.
- [x] Kiểm tra API chưa đăng nhập trả về HTTP 401.
- [x] Chạy thành công 5 Unit Test.
- [x] Build Frontend React thành công.
- [x] Chụp ảnh minh chứng BT2.
- [ ] Kiểm tra cài đặt từ bản clone mới.
- [ ] Hoàn thiện báo cáo PDF BT2.
- [ ] Commit, push và tạo Git tag v0.2.

## 7. Git và báo cáo

Sử dụng Conventional Commits với các tiền tố như:

- `feat:` cho chức năng mới.
- `fix:` cho sửa lỗi.
- `test:` cho kiểm thử.
- `docs:` cho tài liệu.

Ảnh minh chứng thực hành các buổi trước được lưu trong `docs/minh-chung/`.

Bộ 7 ảnh minh chứng BT2 – Buổi 12 được lưu trong `docs/screenshots/`, gồm giao diện đăng nhập, danh sách khảo sát, chi tiết khảo sát, biểu mẫu phản hồi, trạng thái lỗi và thử lại, kết quả Unit Test và kiểm tra xác thực API.

## 8. Giới hạn

Hệ thống hiện phục vụ mục đích thực hành và minh chứng Sprint 2.

Hệ thống đã triển khai xác thực cơ bản bằng Flask Session với tài khoản demo. Chưa triển khai phân quyền theo vai trò, quản lý tài khoản người dùng thực tế, dashboard nâng cao và kiểm thử hiệu năng.

Hệ thống cần cấu hình MySQL phù hợp trên từng máy trước khi chạy.