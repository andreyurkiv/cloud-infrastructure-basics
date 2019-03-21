FROM python:3

COPY ./web /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["prime_factorization.py"]

EXPOSE 80
