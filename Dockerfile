
FROM python:3.12.2-alpine3.19

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY ./testProject /app/
COPY .env /app/
RUN ls -la /app

RUN chmod +x starter.sh

EXPOSE 8000

CMD ["./starter.sh"]
