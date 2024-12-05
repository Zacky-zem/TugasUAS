# Gunakan base image
FROM python:3.9-slim

# Set direktori kerja di dalam container
WORKDIR /app

# Salin file requirements.txt ke container
COPY ./app/requirements.txt /app/requirements.txt

# Salin semua file dari folder app ke container
COPY ./app /app

# Install dependensi dari requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Jalankan aplikasi saat container dijalankan
CMD ["python", "main.py"]
