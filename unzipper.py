import itertools
import json
import os
import shutil
import zipfile
import valohai

inputs = {
    "package": "https://example.com/package.zip",
}

params = {
    "flat-directory": True,
}

valohai.prepare(
    step='unzip-step',
    default_parameters=params,
)



for p in os.listdir("/valohai/inputs/package/"):
    print(f"will read /valohai/inputs/package/{p}")
    with zipfile.ZipFile(f"/valohai/inputs/package/{p}", 'r') as zip_re:
        zip_re.extractall("/valohai/outputs/")
        for info in zip_re.infolist():
            print(info.filename)

if valohai.parameters('flat-directory').value:
    all_files = []
    for root, _dirs, files in itertools.islice(os.walk('/valohai/outputs/'), 1, None):
        for filename in files:
            all_files.append(os.path.join(root, filename))
    for filename in all_files:
        shutil.move(filename, '/valohai/outputs/')



# add metadata for images
for root, _sub_dirs, files in os.walk("/valohai/outputs/"):
    for file_full_path in [os.path.join(root, f) for f in files]:
        print(f"will add metadata for {file_full_path} if *.png file")
        file_name = os.path.basename(file_full_path)
        if file_name.endswith(".png"):
            metadata = {
                "vhic_group": "/".join(file_name.split("_")[:-1]),
            }
            if file_name.endswith("_confidence.png"):
                metadata["vhic_truth"] = file_name.replace("_confidence.png", "_class.png")
            if file_name.endswith(".png"):
                metadata["vhic_truth"] = file_name.replace("_binary.png", "_class.png")
            if not file_name.endswith("_rgb.png"):
                metadata["vhic_base"] = "_".join(file_name.split("_")[:-1]) + "_rgb.png"
            metadata_path = file_full_path.replace(file_name, file_name + ".metadata.json")
            with open(metadata_path, "w") as f:
                f.write(json.dumps(metadata))
