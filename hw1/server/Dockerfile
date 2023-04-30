FROM python:3.9

COPY protocol_serializers/base_serializer.py .
COPY requirements.txt .
RUN pip install --upgrade pip wheel setuptools requests
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install protobuf grpcio grpcio-tools

COPY ./protocol_serializers ./protocol_serializers
COPY ./protocol_serializers/protobuf/train_pb2.py .
RUN python -m grpc_tools.protoc -I./protocol_serializers/protobuf --python_out=. --grpc_python_out=. train.proto
COPY . .


CMD ["python", "-u", "server.py"]