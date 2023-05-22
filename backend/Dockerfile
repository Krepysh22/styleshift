FROM python:3-slim-buster

WORKDIR /backend

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH /backend

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
