# api_final
api final
# API для проекта Yatube

## 📌 Описание

**Yatube API** — это REST API для социальной сети блогеров.  
С помощью него можно:
- публиковать посты;
- подписываться на других пользователей;
- оставлять комментарии;
- просматривать записи по группам.

Проект реализован с использованием Django REST Framework и позволяет взаимодействовать с платформой через HTTP-запросы (GET, POST, PUT, DELETE).

---

## 🚀 Установка и запуск

1. **Клонируйте репозиторий:**

```bash
git clone https://github.com/AltoKlef/api_final_yatube.git
cd api_final_yatube
```
2. **Создайте и активируйте виртуальное окружение:**

```bash
python -m venv venv
source venv/bin/activate        # для Linux/MacOS
venv\Scripts\activate           # для Windows
```
3. **Установите зависимости:**
```bash
pip install -r requirements.txt
```
4. **Примените миграции и запустите сервер:**
```bash
python manage.py migrate
python manage.py runserver
```