import grpc

import mlib.grpc.unary_pb2_grpc as pb2_grpc
import mlib.grpc.unary_pb2 as pb2


class AnonymizerClient(object):
    def __init__(self, config):
        self.server = {
            'host': config['server']['host'],
            'port': config['server']['port'],
        }

        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.server['host'], self.server['port']))
        self.stub = pb2_grpc.UnaryStub(self.channel)


    def anonymize(self, message):
        message = pb2.Message(message=message)
        return self.stub.GetServerResponse(message)