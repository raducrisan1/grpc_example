# Readme for gRPC and ProtoBuf

Use the following command to generate the python protobuf files, based on scorereader.proto definition:

python -m grpc_tools.protoc  -I. --python_out=. --grpc_python_out=. scorereader.proto

Example at: https://grpc.io/docs/quickstart/python.html

for the server, use the following command to generate the proxy:
~/.nuget/packages/grpc.tools/1.16.0/tools/linux_x64/protoc -I. --csharp_out . --grpc_out . scorereader.proto --plugin=protoc-gen-grpc=${HOME}/.nuget/packages/grpc.tools/1.16.0/tools/linux_x64/grpc_csharp_plugin