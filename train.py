import json


def logMetadata(epoch, loss, accuracy, gain, num, arr, json_obj):
    print(json.dumps({
        'epoch': epoch,
        'loss': loss,
        'acc': accuracy,
        'gain': gain,
        'numberi': num,
        'arrrrray': arr,
        'obj': json_obj
    }))


logMetadata(1, "teksti",    "3",    '1970-01-01T00:00:00.000000', 1,        [[10, 2, 3], [4, 5, 6], [7, 8, 9]], {'what':'a dict'})
logMetadata(2, -1,          4,      '2020-01-01T00:00:00.000000', "2",      [[11, 2, 3], [4, 5, 6], [7, 8, 9]], {'what':'a dict'})
logMetadata(3, "teksti",    5,      '2020-01-01T00:00:00.000000', 3,        [[12, 2, 3], [4, 5, 6], [7, 8, 9]], {'what':'a dict'})
logMetadata(4, 3,           6,      '2020-01-01T00:00:00.000000', "5",      [[13, 2, 3], [4, 5, 6], [7, 8, 9]], {'what':'a dict'})
logMetadata(5, "teksti",    6,      '2020-01-01T00:00:00.000000', "5",      [[14, 2, 3], [4, 5, 6], [7, 8, 9]], {'what':'a dict'})
