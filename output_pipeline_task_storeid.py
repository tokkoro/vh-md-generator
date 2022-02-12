import json
import argparse

# Your logic to fetch the right values...
f = open("/valohai/outputs/output_file.txt", "w")
f.write("this is an output!")
f.close()


parser = argparse.ArgumentParser()
parser.add_argument('--node_count', type=int, default=5)
parsed = parser.parse_args()
node_count = parsed.node_count

sets = node_count // 5

storeids = [122, 799, 154, 209, 916, 444, 345] * (sets+1)  # id=209 will error in error task

while len(storeids) > node_count:
    storeids.pop()

# Print out a list as metadata
print(json.dumps({
    "storeids": storeids
}))
