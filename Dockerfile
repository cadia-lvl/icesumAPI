FROM python:3.7

RUN mkdir /usr/src/app
COPY requirements.txt /usr/src/app/


RUN cd /usr/src/app \
 && pip install --upgrade pip \
 && pip install -r requirements.txt
#RUN pip install --use-deprecated=html5lib torch==0.4.1 -f https://download.pytorch.org/whl/torch_stable.html


WORKDIR /usr/src/app
RUN git clone https://github.com/jonfd/icesum.git
RUN pip install pandas==1.3.5
RUN pip install --use-deprecated=html5lib torch==0.4.1 -f https://download.pytorch.org/whl/cpu/torch_stable.html
RUN pip install pytorch-ignite==0.3.0
RUN pip install tokenizer
WORKDIR /usr/src/app/icesum
RUN git clone https://github.com/kedz/nnsum.git
RUN cd nnsum && python setup.py install


WORKDIR /usr/src/app
COPY mbl-cnn-s2s.pth icesum/models/mbl-cnn-s2s.pth
COPY main.py main.py

EXPOSE 8080

ENTRYPOINT uvicorn main:app --port 8080 --host 0.0.0.0
