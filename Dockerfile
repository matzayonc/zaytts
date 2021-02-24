FROM python

COPY . /app

RUN pip install -r /app/freeze
EXPOSE 5000

CMD [ "python", "/app/main.py" ]