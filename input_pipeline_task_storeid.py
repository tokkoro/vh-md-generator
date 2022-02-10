import valohai
import json

f = open("/valohai/outputs/output_file.txt", "w")
f.write("this is an output!")
f.close()

storeid = valohai.parameters('id').value

print(json.dumps({
    'storeid': storeid,
}))