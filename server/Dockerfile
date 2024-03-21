FROM python:alpine3.19

WORKDIR /app

COPY ./protos /app/protos
COPY ./greet_server.py /app/greet_server.py
COPY ./greet_pb2_grpc.py /app/greet_pb2_grpc.py
COPY ./greet_pb2.py /app/greet_pb2.py
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 50051

CMD ["python", "greet_server.py"]