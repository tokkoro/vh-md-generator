import json
import math
import random
import time

end_epoch = 10


def logMetadata(epoch, loss, accuracy):
    print()
    print(json.dumps({
        'epoch': epoch,
        'loss': loss,
        'acc': accuracy,
    }))


for epoch in range(0, end_epoch + 1):
    logMetadata(epoch, 4 - 0.1 * epoch / end_epoch + random.random() * 0.3,
                math.sqrt(max(0.0, epoch / end_epoch - 0.1 * random.random())))
    time.sleep(0.8 + 0.4 * random.random())
