FROM python:3.11-slim

WORKDIR /app
COPY servidor2/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY servidor2/app.py ./
COPY servidor2/templates ./templates
COPY MapReduce ./MapReduce

EXPOSE 5000
CMD ["python", "app.py"]
