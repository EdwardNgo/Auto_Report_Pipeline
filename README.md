# tla_thanh_pham

Danh sách chức năng:
- Tự động trích xuất thông tin từ anh Chúc,chị Nga, đội sale
- Gửi mail cho khách hàng

Luồng chạy cronjob:
 1. Gmail_attachment: Lấy các file excel từ khách hàng (ie: anh Chúc)
 2. Component db dump: Đẩy dữ liệu từ các file excel lấy được vào trong database
 3. Tự động gửi mail .
 4. Thiết lập cronjob: cronjob.py
 - lấy file excel: một ngày một lần
 - Gửi mail: Tùy thời gian - 5 ngày 1 lần
 
Để cài đặt các chương trình cần thiết:
- pip install -r requirements.txt

Để chạy cronjob:
- python cronjob.py
 