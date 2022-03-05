import pyhop
import task_2_operators_and_methods
import map 

print('')
pyhop.print_operators()

print('')
pyhop.print_methods()

print('')

#############     beginning of tests     ################

print("""
****************************************
Simple tests for the operators
****************************************
""")

state1 = pyhop.State('state1')
state1.loc = {'robot': 'p5', 'box1': 'p5', 'box2': 'p5'}
state1.doors_open = {'door1':False, 'door2':False, 'door3':False}
state1.carrying = {'robot': None}

print("- this should fail because I'm using the moveto method to move across rooms:")
pyhop.pyhop(state1, [('moveto', 'robot', 'p9')], verbose=1)
print("- this should fail because I'm trying to pick up a box while the robot already carrying another box:")
pyhop.pyhop(state1, [('pickup', 'robot', 'box1'), ('pickup', 'robot', 'box2')], verbose=1)
print('- these should succeed:')
pyhop.pyhop(state1, [('moveto', 'robot', 'p4')])
pyhop.pyhop(state1, [('pickup', 'robot', 'box1'), ('putdown', 'robot', 'box1'), ('pickup', 'robot', 'box2')], verbose=1)


print("""
****************************************
Tests for the whole planning domain, using the 'transport' task, 
which also calls 'navigate' and 'fetch' tasks, so they are tested too
****************************************
""")

state2 = pyhop.State('state2')
state2.loc = {'robot2': 'p1', 'box3': 'p9', 'box4': 'p2'}
state2.doors_open = {'door1':False, 'door2':False, 'door3':False}
state2.carrying = {'robot2': None}

print("""- Transportation of a box across different rooms,
and thus also navigation across rooms:""")
pyhop.pyhop(state2, [('transport', 'robot2', 'box3', 'p4')], verbose=1)

print("""- Transportation of a box within a room, 
and thus also navigation within a room:""")
pyhop.pyhop(state2, [('transport', 'robot2', 'box4', 'p3')], verbose=1)