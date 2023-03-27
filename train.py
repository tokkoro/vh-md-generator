import json
import random
import time
import math
import argparse

import valohai

parser = argparse.ArgumentParser()
parser.add_argument('--epochs', type=int, default=10)
parser.add_argument('--how_random', type=float, default=0.05)
parser.add_argument('--wait_time', type=float, default=0.05)
parsed = parser.parse_args()
end_epoch = parsed.epochs
how_random = parsed.how_random
wait_time = parsed.wait_time


for path in valohai.inputs("input_a").path():
    print(f"## input_a {path}")
    with open(path, "r") as f:
        print(f.read())
for path in valohai.inputs("input_b").path():
    print(f"## input_b {path}")
    with open(path, "r") as f:
        print(f.read())


def logMetadata(epoch, loss, accuracy):
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
    logMetadata(epoch + 1, lerp(4.0, 2.0, t) + random.random() * how_random,
                steep_log01(t) + (how_random * random_m1_p1()))
    time.sleep(wait_time * (0.8 + 0.4 * random.random()))  # +- 20 % random

# one in sub folder
output_path = valohai.outputs("output-a").path("department/group/ouput-a.txt", makedirs=True)
with open(output_path, "w") as f:
    f.write("Data A\nis\nin this file\n")

# other in root folder
output_path_b = valohai.outputs("output-b").path("ouput-b.txt", makedirs=True)
with open(output_path_b, "w") as f:
    f.write("Data Root B\nis\nin this file\n")

# other B but in sub folder in root folder
output_path_b_s = valohai.outputs("output-b").path("sub-b/ouput-b.txt", makedirs=True)
with open(output_path_b_s, "w") as f:
    f.write("Data Sub folder B\nis\nin this file\n")
