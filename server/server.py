from concurrent import futures

import grpc

import mlib.grpc.unary_pb2_grpc as pb2_grpc

from unary_service import UnaryService


def serve(config):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=config['server']['max_workers']))
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
    server.add_insecure_port(f"[::]:{config['server']['port']}")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    config = {
        'server': {
            'port': '50051',
            'max_workers': 10
        }
    }
    serve(config)
