from python

MAINTAINER Nicolas Marie-Magdelaine <nikos.mm.e AT gmail.com>

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

CMD [ "export FLASK_APP=node.py" ]

CMD [ "flask run" ]
