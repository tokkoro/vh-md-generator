import valohai

storeid = valohai.parameters('id').value
if storeid == "209":
    raise RuntimeError("STORE ID 209 is evil")
