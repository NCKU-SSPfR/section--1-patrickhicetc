# 使用 Python 3.11 作為基礎鏡像
FROM python:3.11

# 創建非 root 用戶，確保 /app 目錄存在
RUN adduser --disabled-password --gecos '' appuser \
    && mkdir -p /app \
    && chown -R appuser /app

# 切換到非 root 用戶
USER appuser

# 設置工作目錄
WORKDIR /app

# 複製 requirements.txt，安裝安全依賴
COPY requirements.txt .
RUN pip install --no-cache-dir --require-hashes -r requirements.txt

# 避免拷貝敏感文件
COPY src /app/src
COPY config /app/config

# 啟動應用，避免使用 --reload
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
