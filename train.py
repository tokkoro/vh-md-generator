import json
import random
import time
import math
import argparse

end_epoch = 10

parser = argparse.ArgumentParser()
parser.add_argument('--how_random', type=float, default=0.05)
how_random = parser.parse_args().how_random

def logMetadata(epoch, loss, accuracy):
    print()
    print(json.dumps({
        'epoch': epoch,
        'loss': loss,
        'acc': accuracy,
    }))


for epoch in range(1, end_epoch + 1):
    logMetadata(epoch, 4 - 2 * epoch / end_epoch + random.random() * how_random,
                max(0.0, (1 + math.log10(max(0.000000001, (epoch - 1) / end_epoch)) / 10) + (
                            how_random * 2.0 * (random.random() - 0.5))))
    time.sleep(0.8 + 0.4 * random.random())
