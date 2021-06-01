FROM python:3.7

RUN mkdir /usr/src/app
COPY requirements.txt /usr/src/app/

RUN cd /usr/src/app \
 && pip install --upgrade pip \
 && pip install -r requirements.txt

WORKDIR /usr/src/app
RUN git clone https://github.com/jonfd/icesum.git
WORKDIR /usr/src/app/icesum
RUN git clone https://github.com/kedz/nnsum.git
WORKDIR /usr/src/app/icesum/nnsum
RUN python setup.py install

WORKDIR /usr/src/app
COPY mbl-cnn-s2s.pth icesum/models/mbl-cnn-s2s.pth
COPY main.py main.py

EXPOSE 8080

ENTRYPOINT uvicorn main:app --port 8080 --host 0.0.0.0
