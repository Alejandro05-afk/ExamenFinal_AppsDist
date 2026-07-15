FROM python:3.11-slim

WORKDIR /app
COPY servidor1/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY servidor1/app.py ./
COPY servidor1/templates ./templates
COPY MapReduce ./MapReduce

EXPOSE 5000
CMD ["python", "app.py"]
