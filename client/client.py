import time

import msgpack
import numpy as np

from anonymizer_client import AnonymizerClient


def image_get():
    rnd_par = {
        'seed': 12345,
        'min': 0,
        'max': 255,
        'size': 2 * 2 * 3  # 1280 * 768 * 3
    }

    rng = np.random.default_rng(rnd_par['seed'])
    npra = rng.integers(low=rnd_par['min'], high=rnd_par['max'], size=rnd_par['size'])

    image_dict = {
        'meta': rnd_par,
        'image': npra.tobytes(),
    }

    return msgpack.dumps(image_dict)


if __name__ == '__main__':
    config = {
        'server': {
            'host': 'anonymizer',
            'port': 50051
        }
    }

    ac = AnonymizerClient(config)

    while True:
        result = ac.anonymize(image_get())
        print(f'anonymizer server response status => {result.status}')
        print(f'anonymizer server response image => {result.image}')
        time.sleep(2)
