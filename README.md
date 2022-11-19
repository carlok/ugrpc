# ugrpc
Unary gRPC based on Manchanda example

```
docker-compose --file grpc.yml rm -f; docker-compose --file grpc.yml up stop; docker-compose --file grpc.yml up --build --remove-orphans
```

```
python -m grpc_tools.protoc --proto_path=./mlib/grpc/ ./mlib/grpc/unary.proto --python_out=./mlib/grpc/ --grpc_python_out=./mlib/grpc/
```

## Important

changed `unary_pb2_grpc.py` as

```
import mlib.grpc.unary_pb2 as unary__pb2
```