"""
Blocks-world test data for Pyhop 1.1.
Author: Dana Nau <nau@cs.umd.edu>, November 15, 2012.
This file should work correctly in both Python 2.7 and Python 3.2.

Update, June 4, 2021:
I've separated these examples from the ones in blocks_world_examples.py,
which use a different set of methods and produce very long output.
"""

from __future__ import print_function
from pyhop import *

print("""
****************************************
Load the usual blocks-world operators, and then a modified version
of the blocks_world methods in which the method for 'get' is
replaced with two methods that will sometimes cause backtracking.
****************************************
""")

import blocks_world_operators
print_operators()
print('')


import blocks_world_methods2
print_methods()
print('')


print("""
****************************************
Do the backtracking examples.
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

print("""\n=== In the next call to pyhop, it should backtrack:
the recursion depth should go up, then down, then up again.===\n""")

# verbose=2 tells pyhop to print out a message at each recursion depth

pyhop(state1,[('get', 'a')], verbose=2)

print("""\n=== This time it shouldn't backtrack.===\n""")


pyhop(state1,[('get', 'c')], verbose=2)

print("""\n=== This time it should fail.===\n""")

pyhop(state1,[('get', 'b')], verbose=2)



print("""
****************************************
demonstrate different levels of verbosity
****************************************
""")

print('- verbosity 0:')
pyhop(state1,[('get','a')], verbose=0)
print('- verbosity 1:')
pyhop(state1,[('get','a')], verbose=1)
print('- verbosity 2:')
pyhop(state1,[('get','a')], verbose=2)
print('- verbosity 3:')
pyhop(state1,[('get','a')], verbose=3)
