#!/bin/sh
set -e

python -c "
import os
import time
import pymysql

host = os.getenv('MYSQL_HOST', 'mysql')
port = int(os.getenv('MYSQL_PORT', '3306'))
user = os.getenv('MYSQL_USER', 'sibp_user')
password = os.getenv('MYSQL_PASSWORD', 'sibp_pass')
database = os.getenv('MYSQL_DATABASE', 'sibp_db')

for attempt in range(30):
    try:
        conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            connect_timeout=3,
        )
        conn.close()
        print('MySQL conectado.')
        break
    except Exception as exc:
        print(f'Aguardando MySQL... tentativa {attempt + 1}/30 ({exc})')
        time.sleep(2)
else:
    raise SystemExit('Nao foi possivel conectar ao MySQL.')
"

python manage.py migrate --noinput

python manage.py shell -c "
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'rootsib')
email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'rootsib@dev.com')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'rootsib2026')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print('Superuser padrao criado.')
else:
    print('Superuser padrao ja existe.')
"

python manage.py runserver 0.0.0.0:8000
