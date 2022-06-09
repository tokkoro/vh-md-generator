import valohai
import json


how_many = valohai.parameters('how_many').value

for i in range(how_many):
    f = open("/valohai/outputs/output_file"+str(i)+".txt", "w")
    f.write("this is an output! " + str(i))
    f.close()


print(json.dumps({
    'how_many': how_many,
}))
