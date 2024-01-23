FROM python:3.9

# EXPOSE 5000 5432

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code/

CMD ["python3" , "src/app.py"]