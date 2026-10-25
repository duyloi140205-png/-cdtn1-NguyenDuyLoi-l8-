# Báo cáo Buổi 8 – BT2

**Họ tên:** Nguyễn Duy Lợi  
**MSSV:** 2374802010291  
**Track:** SE – Software Engineering  
**Đề tài:** L8 – Khảo sát hài lòng CSAT/NPS

## 1. Link commit cuối buổi

[Cập nhật đường dẫn GitHub sau khi push thành công]

## 2. Phản hồi BT1 và cải tiến

Đã đọc phản hồi BT1 với điểm số 6.5/10.

- Đầy đủ: 8.5
- Kỹ thuật: 4.5
- Nhất quán: 6
- Trình bày: 6.5

Đã chuẩn bị tài liệu `docs/thay-doi-thiet-ke.md`, đề xuất bổ sung ràng buộc UNIQUE, CHECK, validation và phân tách các lớp xử lý.

## 3. Cấu trúc dự án

Đã tổ chức mã nguồn theo các thành phần:

- `src/routes/`: Xử lý các API endpoint.
- `src/repositories/`: Truy cập cơ sở dữ liệu MySQL.
- `src/services/`: Thư mục dành cho logic nghiệp vụ.
- `migrations/`: Các script cơ sở dữ liệu.
- `docs/`: Báo cáo và minh chứng thực hành.

Đã kiểm thử thực tế các API bằng PowerShell và trình duyệt.

## 4. Module đầu tiên – CRUD Survey và Feedback

**Các chức năng đã kiểm thử:**

- GET: Lấy danh sách khảo sát.
- POST: Tạo khảo sát mới, API trả về ID = 4.
- PUT: Cập nhật ngày hết hạn của khảo sát ID = 4 thành 2027-02-15.
- DELETE: Xóa khảo sát ID = 1.
- Feedback: Gửi đánh giá CSAT = 5, NPS = 9 và nội dung nhận xét.

**Cơ sở dữ liệu:** MySQL, schema `csat_nps`.

Đã xác nhận dữ liệu khảo sát và đánh giá được lưu trong MySQL. Kiểm tra sau thao tác PUT cho thấy SurveyID = 4, TicketID = 3, ExpireDate = 2027-02-15.

## 5. Minh chứng chạy thực tế

- [GET – Danh sách khảo sát](minh-chung/01-get.png)
- [POST – Tạo khảo sát](minh-chung/02-post.png)
- [PUT – Cập nhật khảo sát](minh-chung/03-put.png)
- [POST Feedback – Gửi đánh giá](minh-chung/04-feedback.png)
- [DELETE – Xóa khảo sát](minh-chung/05-delete.png)
- [MySQL – Dữ liệu Feedback](minh-chung/06-mysql-feedback.png)
- [MySQL – Kiểm tra PUT](minh-chung/07-mysql-put.png)

## 6. Số commit trong buổi

[Cập nhật sau khi kiểm tra lịch sử Git; yêu cầu tối thiểu 2 commit]

## 7. README và bảo mật

Đã chuẩn bị `README.md`, `.gitignore` và `.env.example`.

Cần kiểm tra trạng thái Git trước khi push, đảm bảo file `.env` và dữ liệu nhạy cảm không được đưa lên GitHub.

## 8. Kết quả và hướng phát triển

**Kết quả:** Đã triển khai và kiểm thử module CRUD Survey, API Feedback CSAT/NPS, kết nối MySQL và lưu ảnh minh chứng.

**Hướng phát triển:** Hoàn thiện validation, xử lý lỗi API, kiểm thử tự động và bổ sung các ràng buộc dữ liệu.