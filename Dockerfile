FROM python:3-alpine3.15 
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5010 
CMD python ./app.py
