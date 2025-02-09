FROM python:3.12-alpine

ADD . ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]
