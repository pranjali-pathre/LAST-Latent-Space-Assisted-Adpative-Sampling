FROM ubuntu:18.04
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
RUN apt-get update

RUN apt-get install -y wget && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get upgrade -y && apt-get install git python-pip -y
RUN apt-get install wget curl -y

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 git mercurial subversion

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh
RUN conda --version

RUN conda create -n last python=3.7 -y
WORKDIR /opt/
RUN activate last

RUN pip install psutil
RUN pip install scikit-learn --no-cache-dir
RUN pip install mdtraj --no-cache-dir
RUN pip install MDAnalysis --no-cache-dir
RUN pip install tensorflow --no-cache-dir
RUN pip install statsmodels --no-cache-dir
RUN conda install -c conda-forge openmm
RUN pip install fastapi --no-cache-dir
RUN pip install uvicorn --no-cache-dir
RUN pip install python-multipart
COPY LAST /opt/
# WORKDIR /opt/

RUN chmod +x ./src/run.sh
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
