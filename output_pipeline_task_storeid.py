import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--node_count', type=int, default=5)
parsed = parser.parse_args()
node_count = parsed.node_count

storeids = list(range(node_count))

# Print out a list as metadata
print(json.dumps({
    "storeids": storeids
}))
