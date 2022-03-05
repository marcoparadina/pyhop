import pyhop
import map
import task_2_operators_and_methods

print('')
pyhop.print_operators()

print('')
pyhop.print_methods()

print('')

###STATE INITIALIZATION###

state1 = pyhop.State('state1')
state1.loc = {'robot': 'p5', 'box1': 'p9', 'box2': 'p6'}
state1.doors_open = {'door1':False, 'door2':False, 'door3':False}
state1.carrying = {'robot': None}


###RUNNING ACTUAL PYHOP###


pyhop.pyhop(state1, [('navigate', 'robot', 'p9')], verbose=1)
pyhop.pyhop(state1, [('navigate', 'robot', 'p4')], verbose=1)
pyhop.pyhop(state1, [('navigate', 'robot', 'p1')], verbose=1)


pyhop.pyhop(state1, [('transport', 'robot', 'box1', 'p1')], verbose=1)
pyhop.pyhop(state1, [('transport', 'robot', 'box2', 'p4')], verbose=1)