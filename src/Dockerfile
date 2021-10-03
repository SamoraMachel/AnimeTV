FROM python:3.9

COPY . src/

COPY ./requirements.txt src/

WORKDIR /src

RUN pip install -r requirements.txt

EXPOSE 8000:5000

CMD ["python", "main.py"]