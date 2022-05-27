import argparse
import json


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--parameter_id', type=int, default=1337)
    return parser.parse_args()


args = parse_args()

print(json.dumps({
    'parameter_id': args.parameter_id,
}))
