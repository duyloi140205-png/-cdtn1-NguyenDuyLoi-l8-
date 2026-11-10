# Nhật ký thay đổi thiết kế sau BT1
- **Đề tài:** L8 - Khảo sát hài lòng CSAT/NPS (Track SE)
- **Điểm BT1:** 6.5/10; đầy đủ 8.5/10, kỹ thuật 4.5/10, nhất quán 6/10, trình bày 6.5/10.
- **Nguồn phản hồi:** Ảnh chụp màn hình E-learning do sinh viên cung cấp. Ảnh chưa hiển thị nhận xét chi tiết; các quyết định sau là đề xuất kỹ thuật, không phải nguyên văn giảng viên.

| Vấn đề | Quyết định | Lý do |
|---|---|---|
| Kỹ thuật cần cải thiện | Tách routes/services/repositories | Phân định HTTP, nghiệp vụ, truy cập DB rõ ràng |
| BT1 nêu quan hệ WarrantyTicket - Survey là 1-1 nhưng SQL chưa ràng buộc | Thêm UNIQUE(Survey.TicketID) | Đồng bộ ERD và DDL |
| BT1 nêu điểm CSAT/NPS nhưng DDL chưa có CHECK | Thêm CHECK và validation tại service | Ngăn dữ liệu sai ở cả API và DB |
| DDL BT1 dùng khóa chính INT nhập tay | Đổi sang AUTO_INCREMENT | Thuận tiện tạo mới qua API |
| UC2 yêu cầu kiểm tra hết hạn | Kiểm tra ExpireDate ở service | Từ chối phản hồi sau hạn |
| BT1 có Survey -> Feedback 1-N | Giữ quan hệ 1-N | Tuân thủ BT1; cần xem xét chống gửi lặp ở phiên sau |
| Phạm vi ngoài SMS/Email/AI | Giữ ngoài phạm vi | Đúng Scope BT1 |

**Cần bổ sung:** Phản hồi chi tiết nếu giảng viên có cung cấp ở nguồn khác; ghi nhận các thay đổi sau khi tự chạy thử.
## Phản hồi Bài tập 2 – Buổi 14

- **Điểm BT2:** 8.5/10.
- **Ngày chấm:** 07/11/2026.
- **Giảng viên:** Thầy Trần Công Thanh.
- **Nhận xét hiển thị trên LMS:** "Điểm mạnh: Flask + MySQL + React tách ..."
- **Lưu ý:** Nội dung nhận xét bị rút gọn bằng dấu ba chấm, không có thông tin chi tiết về các điểm cần cải thiện.

### Kế hoạch cải tiến sau BT2

1. Bổ sung Test Plan cho module L8 CSAT/NPS.
2. Thiết kế và chạy 10–12 test case, bao gồm giá trị biên, dữ liệu sai, bảo mật và tái lập.
3. Ghi nhận kết quả PASS/FAIL thực tế trong Test Report.
4. Phát hiện và ghi lại lỗi thực tế trong Bug Log.
5. Sửa lỗi bằng các commit riêng và chạy lại toàn bộ test.

Các mục cải tiến trên là kế hoạch kiểm thử của sinh viên, không phải nguyên văn nhận xét của giảng viên.