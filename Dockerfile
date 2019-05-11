FROM python:3.7
WORKDIR /app
COPY requirements.txt /app
COPY filter.py /app
RUN pip install -r /app/requirements.txt

CMD ["python", "filter.py"]