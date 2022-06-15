import json


def logMetadata(epoch, loss, accuracy, gain, num):
    print(json.dumps({
        'epoch': epoch,
        'loss': loss,
        'acc': accuracy,
        'gain': gain,
        'numberi': num,
    }))


logMetadata(1, "teksti",    "3",    '1970-01-01T00:00:00.000000', 1)
logMetadata(2, -1,          4,      '2020-01-01T00:00:00.000000', "2")
logMetadata(3, "teksti",    5,      '2020-01-01T00:00:00.000000', 3)
logMetadata(4, 3,           6,      '2020-01-01T00:00:00.000000', "5")
logMetadata(4, "teksti",    6,      '2020-01-01T00:00:00.000000', "5")
