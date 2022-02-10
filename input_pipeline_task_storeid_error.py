import valohai
import json

f = open("/valohai/outputs/output_file.txt", "w")
f.write("this is an output!")
f.close()

storeid = valohai.parameters('id').value
if str(storeid) == "209":
    raise RuntimeError("STORE ID 209 is evil")

print(json.dumps({
    'storeid': storeid,
}))