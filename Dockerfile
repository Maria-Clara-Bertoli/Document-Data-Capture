FROM python:3.12.3

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

EXPOSE 80

EXPOSE 27017

CMD ["fastapi", "run", "app/required_files/routes.py", "--port", "80"]