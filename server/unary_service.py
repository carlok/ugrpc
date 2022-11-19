import json

import msgpack
import numpy as np

import mlib.grpc.unary_pb2_grpc as pb2_grpc
import mlib.grpc.unary_pb2 as pb2


class UnaryService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass

    def _image_get(self):
        rnd_par = {
            'seed': 54321,
            'min': 0,
            'max': 255,
            'size': 2 * 2 * 3  # 1280 * 768 * 3
        }

        rng = np.random.default_rng(rnd_par['seed'])
        npra = rng.integers(low=rnd_par['min'], high=rnd_par['max'], size=rnd_par['size'])

        return npra.tobytes()

    def GetServerResponse(self, request, context):
        message = msgpack.loads(request.message)

        status = {
            'a': 1,
            'b': message['meta']['min'] + 1
        }

        print(f"client meta => {message['meta']}")
        print(f"client image => {message['image']}")
        result = {'status': json.dumps(status), 'image': self._image_get()}

        return pb2.MessageResponse(**result)