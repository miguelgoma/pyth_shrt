FROM python:3.8
RUN pip3 install fastapi unicorn
COPY ./app /app
CMD ["uvicorn","short_app.main:app","--host", "137.184.84.221","--port","15000"]