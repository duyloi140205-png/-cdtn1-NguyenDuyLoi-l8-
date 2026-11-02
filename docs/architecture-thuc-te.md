# KIẾN TRÚC THỰC TẾ – BÀI TẬP 2

**Đề tài:** Smart CRM – Mekong Mobile
**Luồng nghiệp vụ:** L8 – Khảo sát hài lòng CSAT/NPS
**Track:** SE – Software Engineering
**Sinh viên:** Nguyễn Duy Lợi
**MSSV:** 2374802010291

## 1. Tổng quan hệ thống

Hệ thống được xây dựng nhằm hỗ trợ Mekong Mobile quản lý khảo sát và thu thập phản hồi của khách hàng sau quá trình bảo hành.

Công nghệ sử dụng:

- Frontend: React và Vite.
- Backend: Python và Flask.
- Cơ sở dữ liệu: MySQL.
- Kiểm thử: pytest.
- Xác thực cơ bản: Flask Session.

## 2. Kiến trúc hệ thống

Hệ thống được tổ chức theo mô hình Frontend – Backend – Database.

**Luồng xử lý:**

React Frontend → Flask Routes → Services → Repositories → MySQL

Các thành phần:

**Frontend:** Hiển thị giao diện, tiếp nhận thao tác của người dùng và gửi yêu cầu đến API.

**Routes:** Tiếp nhận yêu cầu HTTP, kiểm tra phiên đăng nhập và trả về kết quả JSON.

**Services:** Xử lý logic và các quy tắc nghiệp vụ.

**Repositories:** Thực hiện các thao tác truy vấn và cập nhật dữ liệu trong MySQL.

**MySQL:** Lưu trữ thông tin khảo sát, phản hồi và các dữ liệu liên quan.

## 3. Các thực thể nghiệp vụ chính

### 3.1. Survey

Thực thể Survey quản lý thông tin khảo sát sau bảo hành.

Các chức năng đã triển khai:

- Tạo khảo sát.
- Xem danh sách khảo sát.
- Xem chi tiết khảo sát.
- Cập nhật khảo sát.
- Xóa khảo sát.

### 3.2. Feedback

Thực thể Feedback lưu phản hồi của khách hàng đối với khảo sát.

Các chức năng đã triển khai:

- Tạo phản hồi.
- Xem danh sách phản hồi.
- Xem chi tiết phản hồi.
- Cập nhật phản hồi.
- Xóa phản hồi.

## 4. Quy tắc nghiệp vụ

**Quy tắc 1 – Thời hạn khảo sát:** Hệ thống kiểm tra thời hạn khảo sát và từ chối các thao tác không hợp lệ theo quy tắc đã triển khai.

**Quy tắc 2 – Điểm CSAT:** Điểm CSAT phải nằm trong khoảng từ 1 đến 5.

**Quy tắc 3 – Điểm NPS:** Điểm NPS phải nằm trong khoảng từ 0 đến 10.

Khi dữ liệu đầu vào không hợp lệ, Backend trả về thông báo lỗi để Frontend hiển thị cho người dùng.

## 5. Xác thực và bảo vệ API

Hệ thống sử dụng cơ chế đăng nhập demo với Flask Session.

Các API xác thực:

- `POST /api/auth/login`
- `GET /api/auth/me`
- `POST /api/auth/logout`

Các API Survey và Feedback được bảo vệ bằng kiểm tra phiên đăng nhập.

Khi chưa đăng nhập, hệ thống trả về HTTP `401 UNAUTHORIZED`.

Hệ thống hiện chưa triển khai phân quyền người dùng theo vai trò.

## 6. Giao diện Frontend

Các màn hình đã xây dựng:

1. Đăng nhập.
2. Danh sách khảo sát.
3. Chi tiết khảo sát.
4. Biểu mẫu gửi phản hồi CSAT/NPS.

Frontend sử dụng API client riêng để giao tiếp với Backend.

Hệ thống có xử lý các trạng thái tải dữ liệu, dữ liệu rỗng và lỗi kết nối, đồng thời cung cấp thao tác thử lại khi tải dữ liệu thất bại.

## 7. Kiểm thử

Dự án sử dụng pytest để kiểm thử các quy tắc nghiệp vụ.

Lệnh thực hiện:

`python -m pytest -v`

Kết quả đã ghi nhận: **5 Unit Test PASS**.

Các nhóm kiểm thử bao gồm dữ liệu hợp lệ, giá trị biên và dữ liệu không hợp lệ.

Frontend React cũng đã được kiểm tra bằng lệnh:

`npm run build`

## 8. Minh chứng

Các ảnh minh chứng BT2 được lưu tại `docs/screenshots/`:

- `01-login.png`
- `02-survey-list.png`
- `03-survey-detail.png`
- `04-feedback.png`
- `05-error-retry.png`
- `06-tests.png`
- `07-api-auth.png`

## 9. Giới hạn và hướng phát triển

Hệ thống hiện sử dụng tài khoản demo và chưa có phân quyền theo vai trò.

Các hướng phát triển tiếp theo gồm:

- Quản lý tài khoản người dùng.
- Phân quyền theo vai trò.
- Dashboard thống kê CSAT/NPS.
- Xuất báo cáo khảo sát.
- Bổ sung kiểm thử tích hợp và kiểm thử hiệu năng.

## 10. Kết luận

Dự án đã triển khai các chức năng cốt lõi của hệ thống khảo sát CSAT/NPS theo kiến trúc ba lớp Backend, tích hợp giao diện React và cơ sở dữ liệu MySQL.

Các chức năng chính đã được kiểm tra trong quá trình thực hành và có ảnh minh chứng phục vụ đánh giá Bài tập 2.