FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    if [ -f "requirements.txt" ]; then pip install -r requirements.txt; fi

COPY . .

RUN pip install -e .

CMD ["python"]
