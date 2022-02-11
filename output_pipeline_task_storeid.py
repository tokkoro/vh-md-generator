import json

# Your logic to fetch the right values...
f = open("/valohai/outputs/output_file.txt", "w")
f.write("this is an output!")
f.close()

storeids = [122, 799, 154, 209, 916, 444, 345]  # 209 will error in error task

# Print out a list as metadata
print(json.dumps({
    "storeids": storeids
}))
