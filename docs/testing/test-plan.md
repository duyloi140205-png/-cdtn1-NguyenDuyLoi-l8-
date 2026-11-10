# TEST PLAN – BUỔI 14

**Đề tài:** Smart CRM – Mekong Mobile
**Luồng nghiệp vụ:** L8 – Khảo sát hài lòng CSAT/NPS
**Track:** SE – Software Engineering
**Sinh viên:** Nguyễn Duy Lợi
**MSSV:** 2374802010291
**Ngày cập nhật:** 10/11/2026

## 1. Mục tiêu kiểm thử

Đánh giá tính đúng đắn của các chức năng thuộc module L8 – CSAT/NPS, phát hiện lỗi và cung cấp minh chứng về chất lượng phần mềm.

Các chức năng nằm trong phạm vi kiểm thử:

- Tạo, cập nhật và quản lý Survey.
- Gửi, cập nhật và quản lý Feedback.
- Kiểm tra thời hạn khảo sát.
- Kiểm tra CSAT hợp lệ từ 1 đến 5.
- Kiểm tra NPS hợp lệ từ 0 đến 10.
- Xác thực người dùng và bảo vệ API.
- Xử lý các trường hợp dữ liệu không hợp lệ.
- Kết nối và truy vấn MySQL.
- Kiểm tra migration, CRUD và rollback.

**Ngoài phạm vi:** Gửi SMS/Email thực tế, kiểm thử tải lớn, phân quyền nhiều vai trò, các chức năng AI và triển khai production.

## 2. Chiến lược kiểm thử

Áp dụng các phương pháp sau:

| Loại kiểm thử | Mục đích | Công cụ |
|---|---|---|
| Service Unit Test | Kiểm tra logic nghiệp vụ độc lập với database | pytest, mock |
| Flask API Test | Kiểm tra xác thực và mã HTTP | pytest, Flask test client |
| MySQL Read Test | Kiểm tra kết nối và đọc dữ liệu thực tế | Python, PyMySQL |
| Migration Test | Kiểm tra tạo cấu trúc database | Python, MySQL |
| CRUD MySQL Test | Kiểm tra thao tác dữ liệu và ràng buộc | Python, PyMySQL |
| Rollback Test | Kiểm tra dữ liệu sau transaction thử nghiệm | MySQL |

Các kỹ thuật lựa chọn dữ liệu:

1. Phân vùng tương đương.
2. Phân tích giá trị biên.
3. Kiểm thử dữ liệu không hợp lệ.
4. Kiểm thử bảo mật và xác thực.
5. Kiểm thử khả năng tái lập.

## 3. Số lượng kiểm thử

Kế hoạch ban đầu dự kiến 12 Test Case. Trong quá trình thực hiện, bộ kiểm thử được mở rộng thành 15 Test Case tự động.

| Nhóm kiểm thử | Số lượng đã thực hiện |
|---|---:|
| Service Unit Test | 10 |
| Flask API Test | 5 |
| **Tổng cộng** | **15** |

Ngoài ra, thực hiện kiểm thử MySQL bằng các script riêng, không tính vào tổng số 15 bài pytest.

## 4. Tiêu chí thành công

- Thực thi tối thiểu 10–12 Test Case.
- Ghi rõ dữ liệu kiểm thử, kết quả mong đợi và kết quả thực tế.
- Xác định trạng thái PASS hoặc FAIL trung thực.
- Có ảnh minh chứng trong `docs/screenshots/`.
- Kiểm tra cả dữ liệu hợp lệ, dữ liệu sai và giá trị biên.
- Kiểm tra kết nối, migration và thao tác dữ liệu MySQL.
- Không làm mất dữ liệu trong database chính.
- Không đưa mật khẩu hoặc secret vào repository.
- Chạy lại bộ kiểm thử sau khi sửa lỗi.

## 5. Môi trường kiểm thử

| Thành phần | Môi trường |
|---|---|
| Hệ điều hành | Windows |
| IDE | Visual Studio Code |
| Backend | Python 3.12, Flask |
| Frontend | React, Vite |
| Database | MySQL |
| Test framework | pytest 9.2.0 |
| Database chính | `csat_nps` |
| Database thử nghiệm | `csat_nps_buoi14_test` |
| Git branch | `master` |

## 6. Dữ liệu kiểm thử

Dữ liệu bao gồm:

- Survey có ngày hết hạn hợp lệ.
- Survey đã hết hạn.
- Survey không tồn tại.
- CSAT hợp lệ: 1 và 5.
- CSAT không hợp lệ: 6.
- NPS hợp lệ: 0 và 10.
- NPS không hợp lệ: 11.
- Thông tin đăng nhập không hợp lệ.
- Feedback hợp lệ và không hợp lệ.

Dữ liệu phục vụ kiểm thử CRUD được thao tác trên database thử nghiệm riêng.

## 7. Quy trình thực hiện

1. Chuẩn bị môi trường Python và MySQL.
2. Xây dựng Test Case cho service và API.
3. Chạy Unit Test bằng pytest.
4. Chạy API Test bằng Flask test client.
5. Kiểm tra kết nối và đọc dữ liệu MySQL.
6. Chạy migration trên database thử nghiệm.
7. Kiểm tra CRUD và rollback.
8. Chụp ảnh minh chứng.
9. Ghi kết quả vào Test Report.
10. Theo dõi lỗi thực tế trong Bug Log.
11. Kiểm tra lại và đưa tài liệu, code kiểm thử lên GitHub.

## 8. Kết quả và công việc tiếp theo

Tại thời điểm cập nhật:

- 10 Service Unit Test: PASS.
- 5 Flask API Test: PASS.
- Migration MySQL: PASS.
- CRUD MySQL: PASS.
- Rollback: PASS.

Các nội dung cần tiếp tục thực hiện:

- Kiểm thử đầy đủ luồng API với MySQL thực tế.
- Kiểm thử giao diện React.
- Kiểm tra file seed và khả năng tái lập trên máy mới.
- Tái hiện, ghi nhận và sửa các lỗi chức năng thực tế nếu phát hiện.

**Báo cáo kết quả chi tiết:** `docs/testing/test-report.md`.