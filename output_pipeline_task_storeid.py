import json

# Your logic to fetch the right values...

storeids = [122, 154, 209, 916, 345] # 209 will error in error task

# Print out a list as metadata
print(json.dumps({
    "storeids": storeids
}))
