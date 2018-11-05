# Readme for gRPC and ProtoBuf

Use the following command to generate the python protobuf files, based on scorereader.proto definition:

python -m grpc_tools.protoc  -I. --python_out=. --grpc_python_out=. scorereader.proto

Example at: https://grpc.io/docs/quickstart/python.html