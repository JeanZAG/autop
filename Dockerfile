#FROM nvidia/cuda:8.0-cudnn5-devel
FROM nvidia/cuda:10.0-cudnn7-devel

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y git 
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libopencv-dev
RUN apt-get install -y cmake

RUN apt-get install -y libprotobuf-dev

RUN apt-get install -y libgoogle-glog-dev

RUN apt-get install -y  protobuf-compiler libatlas-base-dev libboost-all-dev libhdf5-serial-dev 




# RUN chmod +x /scripts/ubuntu/install_deps_and_cuda.sh

# RUN bash  ./scripts/ubuntu/install_deps_and_cuda.sh


RUN apt purge --auto-remove cmake

RUN apt-get install -y software-properties-common wget unzip

RUN  wget http://www.cmake.org/files/v3.12/cmake-3.12.2.tar.gz 
# RUN unzip cmake-3.12.1.tar.gz
RUN ls 
RUN tar -xvzf cmake-3.12.2.tar.gz
WORKDIR cmake-3.12.2/
RUN ./bootstrap
RUN make -j8
RUN make install 

RUN cmake --version

WORKDIR ..


RUN git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose

WORKDIR openpose

RUN mkdir build

WORKDIR build 


RUN cmake ..


# WORKDIR build

RUN make -j8

WORKDIR ..

