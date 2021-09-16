import json
import random
import time
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--epochs', type=int, default=10)
parser.add_argument('--how_random', type=float, default=0.05)
parser.add_argument('--wait_time', type=float, default=0.05)
parsed = parser.parse_args()
end_epoch = parsed.epochs
how_random = parsed.how_random
wait_time = parsed.wait_time

words = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum".split();

long_name = "Long_metrics_name_that_has_multiple_important_parts_123456";

def random_words(length):
    result = ""
    for i in range(length):
        result += words[random.randrange(len(words))] + " "
    return result;
    

def logMetadata(epoch, loss, accuracy):
    data = {
        'epoch': epoch,
        'loss': -loss,
        'acc': accuracy,
    }
    for i in range(20):
        data[long_name[:-2*i]] = accuracy
    print(json.dumps(data))


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
