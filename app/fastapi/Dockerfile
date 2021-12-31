FROM python:3.7

RUN apt-get update && apt-get upgrade -y
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

# FastAPI
RUN pip install fastapi uvicorn

# Camera
ENV READTHEDOCS=True
RUN pip install picamera


EXPOSE 8000

#COPY ./app /app

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
