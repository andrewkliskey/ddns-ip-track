FROM python:3
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ddns-ip-track.py .

CMD [ "python", "./ddns-ip-track.py" ]
