FROM python:3.13-slim 

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev pkg-config && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN pip install --upgrade pip

RUN pip install  --no-cache-dir -r requirements.txt



COPY . .

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
