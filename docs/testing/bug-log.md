# BUG LOG – BUỔI 14

**Đề tài:** Smart CRM – Mekong Mobile
**Luồng nghiệp vụ:** L8 – CSAT/NPS
**Track:** SE – Software Engineering
**Sinh viên:** Nguyễn Duy Lợi
**MSSV:** 2374802010291
**Ngày cập nhật:** 10/11/2026

## 1. Mục đích

Theo dõi các lỗi thực tế phát hiện trong quá trình kiểm thử phần mềm, ghi nhận mức độ ảnh hưởng, các bước tái hiện, phương án xử lý và kết quả kiểm thử lại.

## 2. Danh sách lỗi

| Bug ID | Chức năng | Mô tả lỗi | Mức độ | Trạng thái | Commit sửa lỗi | Minh chứng |
|---|---|---|---|---|---|---|
| Chưa có | — | Chưa xác nhận được lỗi chức năng trong phạm vi kiểm thử hiện tại | — | Tiếp tục kiểm thử | — | — |

## 3. Kết quả kiểm thử đã thực hiện

| Hạng mục | Kết quả |
|---|---|
| Service Unit Test | 10 PASS |
| Flask API Test | 5 PASS |
| Migration MySQL | PASS |
| CRUD MySQL | PASS |
| Kiểm tra rollback | PASS |
| Tổng pytest | 19 PASS, 0 FAIL |

Các bài kiểm thử hiện tại chưa phát hiện lỗi chức năng được tái hiện và xác nhận.

## 4. Các tình huống cần kiểm thử bổ sung

- Tạo Survey qua API với dữ liệu không hợp lệ.
- Cập nhật Survey không tồn tại.
- Xóa Survey không tồn tại.
- Gửi Feedback khi Survey hết hạn.
- Kiểm tra lỗi khi MySQL không khả dụng.
- Kiểm tra dữ liệu trùng lặp.
- Kiểm tra xử lý lỗi trên giao diện React.
- Kiểm thử luồng gửi Feedback với MySQL thực tế.

## 5. Quy trình ghi nhận và xử lý lỗi

Khi phát hiện lỗi, thực hiện:

1. Ghi lại các bước tái hiện.
2. Xác định kết quả mong đợi.
3. Ghi kết quả thực tế.
4. Phân loại mức độ Critical, Major, Minor hoặc Trivial.
5. Chụp ảnh hoặc lưu log minh chứng.
6. Sửa lỗi trong source code.
7. Chạy lại bài kiểm thử liên quan.
8. Ghi mã commit sửa lỗi.
9. Cập nhật trạng thái lỗi.

## 6. Ghi chú

Chỉ ghi nhận lỗi khi có bằng chứng tái hiện thực tế.

Không tự tạo lỗi giả hoặc ghi nhận commit sửa lỗi chưa tồn tại.

Nếu phát hiện lỗi mới, bổ sung vào bảng ở Mục 2 và cập nhật kết quả kiểm thử lại.
## 7. Kết quả rà soát bổ sung ngày 11/11/2026

- Đã bổ sung 4 bài kiểm thử, tổng cộng 19/19 PASS.
- Kiểm tra SQL cập nhật Survey: PASS.
- Kiểm tra độ dài nhận xét Feedback: PASS.
- Kiểm tra giới hạn NPS khi cập nhật Feedback: PASS.
- Kiểm tra đăng ký IntegrityError handler: PASS.

### Rà soát thay đổi liên quan IntegrityError

Commit: 19e9638

Nội dung thực tế:
- Chỉnh sửa thông báo lỗi dữ liệu tham chiếu không hợp lệ hoặc trùng lặp.
- Định dạng lại hàm xử lý IntegrityError.

Kết quả:
- Kiểm thử đăng ký handler PASS.
- Chưa xác nhận được lỗi thiếu đăng ký handler trong phiên bản trước.
- Chưa thực hiện kiểm thử HTTP 409 tích hợp với MySQL thực tế.

Không ghi nhận BUG-01, BUG-02 hoặc BUG-03 là lỗi đã khắc phục nếu chưa có bằng chứng tương ứng.