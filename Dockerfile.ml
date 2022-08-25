FROM ubuntu:20.04

# Update package manager (apt-get)
# and install (with the yes flag `-y`)
# Python and Pip
RUN apt update \
    && apt install -y build-essential checkinstall\
    && apt-get install -y wget \
    && apt-get -y upgrade
RUN cd /opt/ \
    && wget https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz \
    && tar xzf Python-3.8.3.tgz \
    && cd Python-3.8.3 \
    && apt-get install -y python3-pip \
    && pip install --upgrade pip==21.2.4;

WORKDIR src

COPY src/ .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python3", "-m", "syngen.train"]
