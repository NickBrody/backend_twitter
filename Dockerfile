FROM python:3.9-slim

WORKDIR /app/
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY app.py /app/
COPY database.py /app/
COPY models.py /app/
COPY schemas.py /app/
COPY static/ /app/static/
COPY templates/ /app/templates/
CMD ["uvicorn", "app:app"]