FROM python:3.13.7

WORKDIR /tgbot

COPY . /tgbot

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "tg_bot_start.py"]