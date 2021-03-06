from jfloff/alpine-python

COPY . /opt
WORKDIR /opt

RUN apk update 
RUN pip install --upgrade pip

RUN pip install Flask

RUN apk add build-base jpeg-dev zlib-dev
RUN pip install Pillow

RUN apk add libffi libheif-dev libde265-dev x265-dev
RUN pip install git+https://github.com/david-poirier-csn/pyheif.git

ENTRYPOINT python bestpix/application.py
