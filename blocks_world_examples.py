"""
Blocks-world test data for Pyhop 1.1.
Author: Dana Nau <nau@cs.umd.edu>, November 15, 2012
This file should work correctly in both Python 2.7 and Python 3.2.

Update, June 4, 2021:
I've added IPC-2011 problem BW-rand-50 (as transcribed by Éric Jacopin),
and have moved some other examples to a new file.
"""

from __future__ import print_function
from pyhop import *

import blocks_world_operators
print('')
print_operators()

import blocks_world_methods
print('')
print_methods()


#############     beginning of tests     ################


print("""
****************************************
First, test pyhop on some of the operators and smaller tasks
****************************************
""")

print("- Define state1: a on b, b on tale, c on table")

"""
A state is a collection of all of the state variables and their values. Every state variable in the domain should have a value.
"""

state1 = State('state1')
state1.pos={'a':'b', 'b':'table', 'c':'table'}
state1.clear={'c':True, 'b':False,'a':True}
state1.holding=False

print_state(state1)
print('')

print('- these should fail:')
pyhop(state1,[('pickup','a')], verbose=1)
pyhop(state1,[('pickup','b')], verbose=1)
print('- these should succeed:')
pyhop(state1,[('pickup','c')], verbose=1)
pyhop(state1,[('unstack','a','b')], verbose=1)
pyhop(state1,[('get','a')], verbose=1)
print('- this should fail:')
pyhop(state1,[('get','b')], verbose=1)
print('- this should succeed:')
pyhop(state1,[('get','c')], verbose=1)

print("""
****************************************
Run pyhop on two block-stacking problems, both of which start in state1.
The goal for the 2nd problem omits some of the conditions in the goal
of the 1st problemk, but those conditions will need to be achieved
anyway, so both goals should produce the same plan.
****************************************
""")

print("- Define goal1a:")

"""
A goal is a collection of some (but not necessarily all) of the state variables and their desired values. Below, both goal1a and goal1b specify c on b, and b on a. The difference is that goal1a also specifies that a is on table and the hand is empty.
"""

goal1a = Goal('goal1a')
goal1a.pos={'c':'b', 'b':'a', 'a':'table'}
goal1a.clear={'c':True, 'b':False, 'a':False}
goal1a.holding=False

print_goal(goal1a)
print('')

print("- Define goal1b:")

goal1b = Goal('goal1b')
goal1b.pos={'c':'b', 'b':'a'}

print_goal(goal1b)

### goal1b omits some of the conditions of goal1a,
### but those conditions will need to be achieved anyway


pyhop(state1,[('move_blocks', goal1a)], verbose=1)
pyhop(state1,[('move_blocks', goal1b)], verbose=1)

print("""
****************************************
Run pyhop on two more planning problems. As before, the 2nd goal omits
some of the conditions in the 1st goal, but both goals should produce
the same plan.
****************************************
""")

print("- Define state 2:")

state2 = State('state2')
state2.pos={'a':'c', 'b':'d', 'c':'table', 'd':'table'}
state2.clear={'a':True, 'c':False,'b':True, 'd':False}
state2.holding=False

print_state(state2)
print('')

print("- Define goal2a:")

goal2a = Goal('goal2a')
goal2a.pos={'b':'c', 'a':'d', 'c':'table', 'd':'table'}
goal2a.clear={'a':True, 'c':False,'b':True, 'd':False}
goal2a.holding=False

print_goal(goal2a)
print('')

print("- Define goal2b:")

goal2b = Goal('goal2b')
goal2b.pos={'b':'c', 'a':'d'}

print_goal(goal2b)
print('')


### goal2b omits some of the conditions of goal2a,
### but those conditions will need to be achieved anyway.

pyhop(state2,[('move_blocks', goal2a)], verbose=1)
pyhop(state2,[('move_blocks', goal2b)], verbose=1)


print("""
****************************************
Test pyhop on planning problem bw_large_d from the SHOP distribution.
****************************************
""")

print("- Define state3:")

state3 = State('state3')
state3.pos = {1:12, 12:13, 13:'table', 11:10, 10:5, 5:4, 4:14, 14:15, 15:'table', 9:8, 8:7, 7:6, 6:'table', 19:18, 18:17, 17:16, 16:3, 3:2, 2:'table'}
state3.clear = {x:False for x in range(1,20)}
state3.clear.update({1:True, 11:True, 9:True, 19:True})
state3.holding = False

print_state(state3)
print('')

print("- Define goal3:")

goal3 = Goal('goal3')
goal3.pos = {15:13, 13:8, 8:9, 9:4, 4:'table', 12:2, 2:3, 3:16, 16:11, 11:7, 7:6, 6:'table'}
goal3.clear = {17:True, 15:True, 12:True}

print_goal(goal3)
print('')

pyhop(state3,[('move_blocks', goal3)], verbose=1)

print("""
****************************************
Test pyhop on planning problem BW-rand-50 from the IPC 2011 distribution.
****************************************
""")
 
print("- Define initial state for problem IPC2011BWrand50:")
 
IPC2011BWrand50 = State('problem BW-rand-50')
IPC2011BWrand50.pos = {    
        1:48, 2:33, 3:41, 4:37, 5:45, 6:16, 7:31, 8:28, 9:49,
        10:34, 11:15, 12:17, 13:20, 14:2, 15:44, 16:5, 17:32, 18:50, 19:30,
        20:22, 21:27, 22:38, 23:11, 24:'table', 25:46, 26:'table', 27:40, 28:43, 29:19,
        30:39, 31:29, 32:'table', 33:'table', 34:14, 35:36, 36:'table', 37:8, 38:9, 39:18,
        40:3, 41:35, 42:4, 43:24, 44:26, 45:47, 46:42, 47:1, 48:21, 49:25,
        50:6
        }
IPC2011BWrand50.clear = {x:False for x in range(1,50)}
IPC2011BWrand50.clear.update({7:True, 10:True, 12:True, 13:True, 23:True})
IPC2011BWrand50.holding = False
 
print_state(IPC2011BWrand50)
print('')
 
print("- Define goal for problem IPC2011BWrand50:")
 
IPC2011BWrand50Goal = Goal('problem BW-rand-50')
IPC2011BWrand50Goal.pos = {1:33, 3:40, 4:46, 5:21, 6:17, 7:37, 8:15, 9:41,  
        10:26, 11:23, 12:25, 13:47, 14:20, 15:19, 16:31, 17:39, 18:50, 19:1,
        20:45, 21:11, 23:43, 25:42, 26:36, 27:35, 28:29, 29:44,
        30:8, 31:9, 32:6, 33:10, 34:14, 35:2, 36:7, 37:32, 38:28,
        40:24, 41:38, 42:34, 43:12, 44:49, 45:4, 46:18, 47:30, 48:22,
        50:13}
IPC2011BWrand50Goal.clear = {}
 
print_goal(IPC2011BWrand50Goal)
print('')

pyhop(IPC2011BWrand50,[('move_blocks', IPC2011BWrand50Goal)], verbose=1)
