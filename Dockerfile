FROM python:3.12-slim
WORKDIR /app
# Cài đặt các thư viện hệ thống cần thiết cho pyodbc và các package khác
COPY requiements.txt .

RUN pip install --no-cache-dir -r requiements.txt
# copy toàn bộ mã nguồn vào container
COPY . .

# 5. Chạy ứng dụng
EXPOSE 5000

CMD ["gunicorn", "-w", "2", "-b", "[::]:5000", "app:app"]

