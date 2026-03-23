FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir "django>=6.0.3,<7.0.0" "djangorestframework>=3.16.1,<4.0.0" "pymysql>=1.1.1,<2.0.0" "cryptography>=45.0.0,<46.0.0"

COPY . .

RUN chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]
