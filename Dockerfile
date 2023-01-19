FROM python:3.9

WORKDIR /
 
COPY . .

RUN pip install -r reqs.txt

ENV PORT 8080

CMD ["python", "main.py"]