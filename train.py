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


def lerp(a, b, t):
    return a * (1 - t) + b * t


def steep_log01(t):
    return max(0.0, (1 + math.log10(max(0.000000001, t)) / 10))


def random_m1_p1():
    return 2.0 * (random.random() - 0.5)


for epoch in range(0, end_epoch):
    t = epoch / end_epoch
    print(t)
    logMetadata(epoch + 1, lerp(4.0, 2.0, t) + random.random() * how_random, steep_log01(t) + (how_random * random_m1_p1()))
    time.sleep(0.8 + 0.4 * random.random())
