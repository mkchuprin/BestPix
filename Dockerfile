from jfloff/alpine-python

COPY . /opt
WORKDIR /opt
RUN apk add libffi libheif-dev libde265-dev x265-dev
RUN pip install --upgrade pip
RUN pip install git+https://github.com/david-poirier-csn/pyheif.git
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps
RUN pip install -r requirements.txt

ENTRYPOINT python BestPix/application.py