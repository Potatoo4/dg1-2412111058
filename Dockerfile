FROM python:3.12-slim

WORKDIR /srv/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    && useradd -m -u 1000 -s /bin/bash appuser

COPY app ./app

RUN chown -R appuser:appuser /srv/app

USER appuser

EXPOSE 5000

CMD ["python", "app/app.py"]
