FROM python:3.7

RUN apt-get update && apt-get upgrade -y
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

# streamllit
RUN pip install streamlit==0.62.0

EXPOSE 80

CMD ["streamlit", "run", "main.py", "--server.port", "80"]
