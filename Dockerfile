FROM python:3.7.6-alpine3.10
LABEL maintainer="Dawn Ho <dawn.ho@gmail.com>"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY . ./

CMD ["python", "ctrl-temp.py"]
