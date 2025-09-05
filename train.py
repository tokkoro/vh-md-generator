import json
import argparse
import random
from datetime import timedelta, datetime


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)


parser = argparse.ArgumentParser()
parser.add_argument('--files', type=int, default=10)
parser.add_argument('--prefix', type=str, default="price_TOMI")
parsed = parser.parse_args()
file_count = parsed.files
prefix = parsed.prefix
version_name = f"{random_date(datetime(2020, 1, 1), datetime.now())}".replace(" ", "-").replace(":", "-")

metadata = {
    "valohai.dataset-versions": [f"dataset://like-ap/{version_name}"]
}

for i in range(file_count):
    f = open(f"/valohai/outputs/{prefix}" + str(i) + ".csv", "w")
    f.write(f"timestamp,price_TOMI_{i+1}\n{random_date(datetime(2020, 1, 1), datetime.now())},{random.random() * 100}\n")
    f.close()
    fmd = open(f"/valohai/outputs/{prefix}" + str(i) + ".csv.metadata.json", "w")
    fmd.write(json.dumps(metadata))
    fmd.close()

print(json.dumps({
    'file_count': file_count,
}))
