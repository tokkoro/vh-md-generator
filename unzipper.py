import os
import zipfile

inputs = {
    "package": "https://example.com/package.zip",
}

for p in os.listdir("/valohai/inputs/package/"):
    print(f"will read /valohai/inputs/package/{p}")
    with zipfile.ZipFile(f"/valohai/inputs/package/{p}", 'r') as zip_re:
        zip_re.extractall("/valohai/outputs/")
        for info in zip_re.infolist():
            print(info.filename)