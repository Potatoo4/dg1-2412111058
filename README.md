# DG1 – Hoàng Đức Anh – 2412111058

## Chạy trên máy khác bằng Docker

Cài Git và Docker Desktop (Windows/macOS) hoặc Docker Engine cùng Docker Compose
(Linux), sau đó chạy trong terminal:

```bash
git clone https://github.com/Potatoo4/dg1-2412111058.git
cd dg1_2412111058
docker compose up --build -d
```

Mở <http://localhost:5000>. Kiểm tra API tại <http://localhost:5000/api/health>.

Compose dùng volume `students-data` để giữ dữ liệu sinh viên khi container được
tạo lại. Dừng ứng dụng bằng:

```bash
docker compose down
```

Không thêm `-v` nếu muốn giữ dữ liệu; `docker compose down -v` sẽ xóa volume.

## Chạy trực tiếp bằng Python

Cần Python 3.12 trở lên. Cài dependencies và chạy ứng dụng:

```bash
python -m venv .venv
```

Kích hoạt môi trường ảo (`.venv\Scripts\activate` trên Windows hoặc
`source .venv/bin/activate` trên macOS/Linux), sau đó:

```bash
pip install -r requirements.txt
python app/app.py
```
