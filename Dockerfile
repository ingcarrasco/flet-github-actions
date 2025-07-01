FROM python:3.13.5-slim

WORKDIR /app

COPY ./app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

EXPOSE 8500
CMD ["python", "main.py"]