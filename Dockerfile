FROM python:3.9

WORKDIR /app

COPY ./main.py /app/main.py
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD ["python3", "main.py"]