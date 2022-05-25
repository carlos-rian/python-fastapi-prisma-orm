FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app

COPY /app /app

COPY requirements.txt /app

RUN pip install --upgrade --user --no-warn-script-location pip 

RUN pip install -r requirements.txt 