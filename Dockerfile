FROM python:3.11

WORKDIR /app

COPY requirements.txt .

# Upgrade pip first
RUN pip install --upgrade pip

# Install numpy separately to avoid binary mismatch
RUN pip install numpy==1.26.2

# Then install rest
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
