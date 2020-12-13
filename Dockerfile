# Docker file for the project: Prediction of Wine Quality based on Physicochemical Tests  
# Mark Wang, Dec, 2020

# use rocker/tidyverse as the base image and
FROM rocker/tidyverse

# install the anaconda distribution of python
RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy && \
    /opt/conda/bin/conda update -n base -c defaults conda

# put anaconda python in path
ENV PATH="/opt/conda/bin:${PATH}"

# install docopt python package
RUN conda update conda

RUN conda install -y -c anaconda \ 
    docopt \
    requests

RUN conda install -y -c conda-forge feather-format

# install altair-related packages
RUN conda install altair

RUN conda install -c conda-forge altair_saver

# Adapted from https://github.com/ttimbers/breast_cancer_predictor/blob/master/Dockerfile by Tiffany Timbers
