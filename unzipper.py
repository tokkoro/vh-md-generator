import itertools
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