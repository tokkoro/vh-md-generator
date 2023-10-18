import valohai
import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('--epochs', type=int, default=10)
parser.add_argument('--how_random', type=float, default=0.05)
parser.add_argument('--wait_time', type=float, default=0.05)
parsed = parser.parse_args()
end_epoch = parsed.epochs
how_random = parsed.how_random
wait_time = parsed.wait_time

out_path = valohai.outputs().path('filu.txt')

Path(out_path).touch()
