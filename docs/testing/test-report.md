# TEST REPORT – BUỔI 14

**Đề tài:** Smart CRM – Mekong Mobile
**Luồng nghiệp vụ:** L8 – Khảo sát hài lòng khách hàng CSAT/NPS
**Track:** SE – Software Engineering
**Sinh viên:** Nguyễn Duy Lợi
**MSSV:** 2374802010291
**Ngày kiểm thử:** 10/11/2026
**Trạng thái:** Đã thực hiện kiểm thử tự động, kiểm thử API bằng Flask test client và kiểm thử cơ sở dữ liệu MySQL.

---

## 1. Mục tiêu kiểm thử

Mục tiêu của hoạt động kiểm thử Buổi 14 là đánh giá tính đúng đắn của các chức năng thuộc luồng L8 – CSAT/NPS, bao gồm:

- Tạo và cập nhật khảo sát (Survey).
- Gửi phản hồi đánh giá CSAT/NPS.
- Kiểm tra giới hạn dữ liệu đầu vào.
- Xử lý khảo sát hết hạn hoặc không tồn tại.
- Kiểm tra xác thực người dùng khi truy cập API.
- Kiểm tra mã trạng thái HTTP của API.
- Kiểm tra kết nối và truy vấn MySQL.
- Kiểm tra khả năng khởi tạo cấu trúc cơ sở dữ liệu.
- Kiểm tra thao tác CRUD và rollback trên cơ sở dữ liệu thử nghiệm.

Kết quả kiểm thử được sử dụng để đánh giá tiến độ phát triển hệ thống và xác định các vấn đề cần khắc phục trước khi hoàn thiện sản phẩm.

## 2. Môi trường và công cụ kiểm thử

| Thành phần | Công nghệ / Công cụ |
|---|---|
| Hệ điều hành | Windows |
| Ngôn ngữ lập trình | Python 3.12.0 |
| Backend | Flask |
| Frontend | React / Vite |
| Cơ sở dữ liệu | MySQL |
| Công cụ kiểm thử | pytest 9.2.0 |
| Thư viện kết nối MySQL | PyMySQL |
| Môi trường lập trình | Visual Studio Code |
| Cơ sở dữ liệu chính | `csat_nps` |
| Cơ sở dữ liệu thử nghiệm | `csat_nps_buoi14_test` |

**Lệnh chạy toàn bộ kiểm thử tự động:**

```powershell
python -m pytest -v
```

**Kết quả thực tế:**

```text
15 passed in 0.27s
```

Các bài kiểm thử service sử dụng mock repository. Một số bài kiểm thử API sử dụng mock service nhằm kiểm tra phản hồi HTTP mà không thay đổi dữ liệu MySQL.

Ngoài pytest, dự án còn có các script kiểm thử MySQL trực tiếp để xác minh cấu trúc và thao tác dữ liệu trên cơ sở dữ liệu thử nghiệm.

## 3. Danh sách Test Case

### 3.1. Kiểm thử nghiệp vụ Service – 10 Test Case

| ID | Chức năng | Dữ liệu kiểm thử | Kết quả mong đợi | Kết quả thực tế | Trạng thái |
|---|---|---|---|---|---|
| TC-01 | Tạo Survey hợp lệ | TicketID=1, hết hạn sau 7 ngày | Tạo khảo sát và trả ID | Repository mock trả ID=1 | PASS |
| TC-02 | Tạo Survey hết hạn | Ngày hết hạn trước hôm nay | Phát sinh ValueError | ValueError như mong đợi | PASS |
| TC-03 | Cập nhật Survey | Ngày hết hạn sau 7 ngày | Cập nhật thành công | Repository mock trả kết quả thành công | PASS |
| TC-04 | Gửi Feedback biên trên | CSAT=5, NPS=10 | Chấp nhận phản hồi | Tạo Feedback thành công qua mock | PASS |
| TC-05 | Gửi Feedback NPS sai | CSAT=5, NPS=11 | Từ chối dữ liệu | ValueError; không gọi hàm tạo Feedback | PASS |
| TC-06 | Gửi Feedback biên dưới | CSAT=1, NPS=0 | Chấp nhận phản hồi | Tạo Feedback thành công qua mock | PASS |
| TC-07 | Gửi Feedback CSAT sai | CSAT=6, NPS=5 | Từ chối dữ liệu | ValueError; không gọi hàm tạo Feedback | PASS |
| TC-08 | Survey hết hạn | Ngày hết hạn trước hôm nay | Không cho gửi Feedback | ValueError như mong đợi | PASS |
| TC-09 | Survey không tồn tại | Repository trả None | Thông báo không tìm thấy | LookupError như mong đợi | PASS |
| TC-10 | Cập nhật Feedback NPS sai | NPS=11 | Không cho cập nhật | ValueError; không gọi hàm cập nhật | PASS |

**Kết quả:** 10/10 Test Case PASS.

**File kiểm thử:** `tests/test_survey_service.py`

**Minh chứng:** `../screenshots/buoi14-unit-tests.png`

### 3.2. Kiểm thử Flask API – 5 Test Case

| ID | Chức năng | Dữ liệu / thao tác | Kết quả mong đợi | Kết quả thực tế | Trạng thái |
|---|---|---|---|---|---|
| TC-11 | Bảo vệ API Survey | GET `/api/surveys` khi chưa đăng nhập | HTTP 401 | HTTP 401 | PASS |
| TC-12 | Đăng nhập sai mật khẩu | POST `/api/auth/login` với thông tin sai | HTTP 401 | HTTP 401 | PASS |
| TC-13 | Gửi Feedback thành công | POST `/api/surveys/3/feedback`, mock service trả ID=123 | HTTP 201 và JSON chứa ID=123 | HTTP 201, JSON `{"id":123}` | PASS |
| TC-14 | Survey không tồn tại | POST Feedback, mock service phát sinh LookupError | HTTP 404 và JSON có trường error | HTTP 404, có trường error | PASS |
| TC-15 | NPS không hợp lệ | POST Feedback, mock service phát sinh ValueError | HTTP 400 và JSON có trường error | HTTP 400, có trường error | PASS |

**Kết quả:** 5/5 Test Case PASS.

**File kiểm thử:** `tests/test_auth_api.py`

**Lệnh thực hiện:**

```powershell
python -m pytest tests/test_auth_api.py -v
```

**Kết quả thực tế:**

```text
5 passed in 0.27s
```

**Minh chứng:** `../screenshots/buoi14-api-tests.png`

**Nhận xét:** Các bài kiểm thử xác nhận Flask trả về mã HTTP phù hợp trong các tình huống đã thiết lập. Đối với TC-13 đến TC-15, service được mock nên kết quả chưa chứng minh toàn bộ quy trình ghi dữ liệu qua API vào MySQL thực tế.

## 4. Tổng hợp kết quả kiểm thử tự động

| Nhóm kiểm thử | Tổng số | PASS | FAIL | Tỷ lệ PASS |
|---|---:|---:|---:|---:|
| Service Unit Tests | 10 | 10 | 0 | 100% |
| Flask API Tests | 5 | 5 | 0 | 100% |
| **Tổng cộng** | **15** | **15** | **0** | **100%** |

**Kết quả chạy toàn bộ pytest ngày 10/11/2026:**

```text
==================== 15 passed in 0.27s ====================
```

**Đánh giá:** Tất cả 15 bài kiểm thử tự động hiện có đều đạt yêu cầu.

Tỷ lệ PASS 100% chỉ phản ánh bộ kiểm thử đã thực hiện, không có nghĩa toàn bộ hệ thống không còn lỗi.

## 5. Kiểm thử tích hợp MySQL – Kết nối và đọc dữ liệu

**Mục tiêu:** Xác minh backend có thể kết nối và truy vấn dữ liệu từ MySQL thực tế.

**Cơ sở dữ liệu:** `csat_nps`

**Phương pháp:** Chạy Python, nạp cấu hình từ `.env` bằng `load_dotenv()` và sử dụng các hàm repository hiện có.

| Nội dung kiểm tra | Kết quả thực tế | Trạng thái |
|---|---|---|
| Kết nối MySQL | Kết nối thành công | PASS |
| Kiểm tra cấu trúc database | Có 5 bảng: Customer, Store, WarrantyTicket, Survey, Feedback | PASS |
| `repo.list_surveys()` | Trả về 2 bản ghi | PASS |
| Kiểm tra Survey | Bản ghi đầu có SurveyID=3 | PASS |
| `repo.list_feedback()` | Trả về 2 bản ghi | PASS |

**Kết luận:** Các thao tác kết nối và đọc dữ liệu hoạt động thành công với MySQL thực tế.

Hoạt động này chỉ đọc dữ liệu, không thực hiện thay đổi dữ liệu trong cơ sở dữ liệu chính.

**Minh chứng:** `../screenshots/buoi14-mysql-read.png`

## 6. Kiểm thử khả năng tái lập cấu trúc cơ sở dữ liệu

**Mục tiêu:** Kiểm tra file migration có thể tạo cấu trúc cơ sở dữ liệu trên môi trường thử nghiệm.

**File migration:** `migrations/001_init.sql`

**Script kiểm thử:** `tests/check_migration.py`

**Database thử nghiệm:** `csat_nps_buoi14_test`

**Lệnh thực hiện:**

```powershell
python tests/check_migration.py
```

**Kết quả thực tế:**

```text
MIGRATION PASS
So bang: 5
```

Các bảng được xác nhận:

1. Customer
2. Store
3. WarrantyTicket
4. Survey
5. Feedback

| Nội dung | Kết quả |
|---|---|
| Kết nối MySQL | PASS |
| Chạy migration trên database thử nghiệm | PASS |
| Kiểm tra số lượng bảng | 5 bảng |
| Kiểm tra danh sách bảng | Đủ 5 bảng |
| Bảo vệ dữ liệu database chính | Script sử dụng database thử nghiệm riêng |

**Kết luận:** Kiểm thử khởi tạo cấu trúc cơ sở dữ liệu bằng `001_init.sql` thành công.

**Giới hạn:** Chưa xác minh đầy đủ file `002_seed.sql` và toàn bộ quy trình cài đặt trên một máy mới hoàn toàn.

**Minh chứng:** `../screenshots/buoi14-migration-test.png`

## 7. Kiểm thử CRUD MySQL và ràng buộc dữ liệu

**Mục tiêu:** Xác minh các thao tác tạo, đọc, cập nhật, xóa Survey/Feedback và kiểm tra ràng buộc NPS trên MySQL.

**Script kiểm thử:** `tests/check_crud_mysql.py`

**Database thử nghiệm:** `csat_nps_buoi14_test`

**Lệnh thực hiện:**

```powershell
python tests/check_crud_mysql.py
```

### 7.1. Kết quả kiểm thử CRUD

| ID | Nội dung | Kết quả thực tế | Trạng thái |
|---|---|---|---|
| DB-01 | Tạo Survey | Tạo thành công SurveyID=1 | PASS |
| DB-02 | Tạo Feedback | Tạo thành công FeedbackID=1 | PASS |
| DB-03 | Đọc Feedback | Đọc đúng CSAT=5, NPS=9 | PASS |
| DB-04 | Cập nhật Feedback | Cập nhật thành công CSAT=4, NPS=8 | PASS |
| DB-05 | Kiểm tra NPS=11 | MySQL từ chối dữ liệu không hợp lệ | PASS |
| DB-06 | Xóa Feedback | Xóa thành công | PASS |
| DB-07 | Xóa Survey | Xóa thành công | PASS |

**Kết quả Terminal:**

```text
CREATE SURVEY PASS: 1
CREATE FEEDBACK PASS: 1
READ FEEDBACK PASS
UPDATE FEEDBACK PASS
INVALID NPS REJECTED PASS
DELETE FEEDBACK PASS
DELETE SURVEY PASS
CRUD MYSQL TEST PASS
ROLLBACK DONE
```

### 7.2. Kiểm tra rollback

Sau khi chạy kiểm thử CRUD, hệ thống thực hiện rollback transaction.

Tiến hành truy vấn lại hai bảng Survey và Feedback trong database thử nghiệm.

**Kết quả thực tế:**

```text
Survey after rollback: 0
Feedback after rollback: 0
```

**Kết luận:** Sau kiểm thử, hai bảng Survey và Feedback trong database thử nghiệm không có bản ghi được lưu lại.

Các thao tác CRUD và kiểm tra ràng buộc dữ liệu đạt yêu cầu trong phạm vi script đã thực hiện.

**Giới hạn:** Đây là kiểm thử SQL trực tiếp, chưa phải kiểm thử toàn bộ quy trình CRUD thông qua Flask API và giao diện React.

**Minh chứng:** `../screenshots/buoi14-crud-mysql.png`

## 8. Theo dõi lỗi – Bug Log

**File theo dõi:** `docs/testing/bug-log.md`

Trong phạm vi các bài kiểm thử đã thực hiện, chưa xác nhận được lỗi chức năng có thể tái hiện.

Quá trình kiểm tra API gửi Feedback đã xác nhận endpoint:

`POST /api/surveys/<int:sid>/feedback`

trả về HTTP 201 và JSON chứa ID trong trường hợp service mock thành công.

Do đó, không ghi nhận lỗi thiếu HTTP response ở endpoint này.

**Trạng thái Bug Log:** Tiếp tục theo dõi, bổ sung khi phát hiện lỗi thực tế.

Khi phát hiện lỗi, cần ghi rõ:

- Mã lỗi và mức độ nghiêm trọng.
- Các bước tái hiện.
- Kết quả mong đợi và kết quả thực tế.
- Ảnh minh chứng.
- Commit sửa lỗi, nếu đã sửa.
- Kết quả kiểm thử lại.

Không ghi lỗi giả hoặc đánh dấu đã sửa khi chưa có bằng chứng.

## 9. Danh sách minh chứng kiểm thử

| STT | Tên file | Nội dung |
|---|---|---|
| 1 | `buoi14-unit-tests.png` | Kết quả Unit Test |
| 2 | `buoi14-all-tests.png` | Kết quả chạy pytest |
| 3 | `buoi14-api-tests.png` | Kết quả 5 API Test |
| 4 | `buoi14-mysql-read.png` | Kết nối và đọc dữ liệu MySQL |
| 5 | `buoi14-migration-test.png` | Kết quả migration PASS |
| 6 | `buoi14-crud-mysql.png` | Kết quả CRUD MySQL PASS |

**Thư mục lưu minh chứng:** `docs/screenshots/`

Các ảnh được sử dụng để đối chiếu với kết quả kiểm thử đã ghi trong báo cáo.

## 10. Giới hạn và công việc cần bổ sung

Mặc dù các bài kiểm thử hiện tại đều PASS, hệ thống vẫn còn một số phạm vi cần tiếp tục xác minh:

1. Kiểm thử tích hợp Flask API với MySQL thực tế cho toàn bộ luồng tạo Survey và gửi Feedback.
2. Kiểm thử thao tác trên giao diện React và khả năng hiển thị thông báo lỗi.
3. Kiểm thử quy trình chạy migration và seed trên môi trường mới.
4. Kiểm thử thêm các trường hợp dữ liệu trùng lặp và lỗi kết nối cơ sở dữ liệu.
5. Tiếp tục tìm, tái hiện và ghi nhận các lỗi thực tế trong Bug Log.
6. Kiểm tra và lưu các thay đổi bằng Git commit, sau đó push lên GitHub.

## 11. Kết luận chung

Trong Buổi 14, dự án Smart CRM – Mekong Mobile đã đạt được các kết quả:

- **15/15 bài kiểm thử pytest PASS**, gồm 10 Service Unit Test và 5 Flask API Test.
- Kết nối và truy vấn dữ liệu MySQL thành công.
- Kiểm thử migration thành công với 5 bảng.
- Kiểm thử CRUD Survey/Feedback bằng SQL trực tiếp thành công.
- Kiểm tra NPS không hợp lệ được MySQL từ chối.
- Xác nhận Survey và Feedback trong database thử nghiệm có 0 bản ghi sau rollback.
- Đã lưu các ảnh minh chứng tương ứng.

**Đánh giá:** Các chức năng và tình huống đã kiểm thử hoạt động đúng với kết quả mong đợi. Dự án có bằng chứng kiểm thử tự động và kiểm thử cơ sở dữ liệu phục vụ báo cáo tiến độ Buổi 14.

Tuy nhiên, kết quả hiện tại chưa chứng minh toàn bộ hệ thống không có lỗi. Các yêu cầu còn thiếu về kiểm thử tích hợp, Bug Log và lịch sử commit cần tiếp tục hoàn thiện theo tiêu chí của giảng viên.