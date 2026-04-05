# NODEFIRE — GPU Cloud Landing

Лендинг с формой заявок и уведомлениями в Telegram.

## Стек
- **Фронт:** HTML/CSS/JS (один файл)
- **Бэк:** Python + FastAPI
- **Деплой:** Render.com (бесплатно)

---

## 🚀 Деплой на Render.com

### 1. Залить на GitHub

```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ВАШ_ЮЗЕР/gpulanding.git
git push -u origin main
```

### 2. Создать Telegram бота

1. Напиши @BotFather в Telegram
2. Отправь `/newbot`
3. Дай имя и юзернейм боту
4. Скопируй токен

Узнать свой chat_id:
- Напиши что-нибудь своему боту
- Открой: `https://api.telegram.org/botТВОЙ_ТОКЕН/getUpdates`
- Найди `"id"` в поле `"chat"`

### 3. Задеплоить на Render

1. Зайди на [render.com](https://render.com)
2. New → Web Service
3. Подключи свой GitHub репозиторий
4. Настройки:
   - **Runtime:** Docker
   - **Build Command:** (оставь пустым — Docker сам)
   - **Start Command:** (оставь пустым)
5. В разделе **Environment Variables** добавь:
   - `TELEGRAM_TOKEN` = твой токен от BotFather
   - `TELEGRAM_CHAT_ID` = твой chat id
6. Нажми **Deploy**

### 4. Привязать домен (опционально)

В настройках сервиса на Render: Settings → Custom Domain → добавь свой домен.

---

## 💻 Локальный запуск

```bash
# Установи зависимости
pip install -r backend/requirements.txt

# Скопируй и заполни .env
cp .env.example .env

# Запусти
cd backend
uvicorn main:app --reload --port 8000
```

Открой: http://localhost:8000

---

## 🐳 Через Docker

```bash
cp .env.example .env
# Заполни .env своими данными

docker-compose up --build
```
