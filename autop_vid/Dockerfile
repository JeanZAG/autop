FROM openpose:latest


RUN apt-get install python-pip -y
RUN pip install pandas

RUN pip install argparse

COPY data_proc.py scrpy.py ./

CMD  python scrpy.py && /bin/bash



