import valohai
from valohai.internals import global_state, global_state_loader

import sys
print(sys.argv[1:])

global_state_loader.load_global_state_if_necessary()
print(global_state.parameters)

mylist = valohai.parameters('mylist-separated').value
print(type(mylist))
print(mylist)
print(mylist[0])

mylist_non = valohai.parameters('mylist-non-separated').value
print(type(mylist_non))
print(mylist_non)
print(mylist_non[0])

