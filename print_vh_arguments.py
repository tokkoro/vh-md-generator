from valohai.internals import global_state, global_state_loader

global_state_loader.load_global_state_if_necessary()
print(global_state.parameters)
