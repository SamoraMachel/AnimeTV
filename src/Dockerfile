FROM "python3.9"

COPY . src/

COPY ./requirements.txt src/

WORKDIR /src

RUN pip -r install requirements.txt

EXPOSE 8000:5000

CMD ["python", "main.py"]