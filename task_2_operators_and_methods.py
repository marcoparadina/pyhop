import pyhop
import map

###OPERATORS###

"""
Moves the robot 'a' from it current position to position 'x'. If the robot 
is carrying a box, the position of that box changes together with the 
position of the robot
"""
def moveto(state, a, x):
    if map.room_of(state.loc[a])==map.room_of(x):
        state.loc[a] = x
        if state.carrying[a]:
            state.loc[state.carrying[a]]=x
        return state
    return False

"""
Operator that makes robot cross doors:
a=name of the robot
d= door that is being crossed
x=position of the robot after having crossed the door, which must be on one of the sides of the door 'd'
Again if the robot is carrying a box, the position of the box will change
with the position of the robot
"""
def cross(state, a, d, x):
    curr_room=map.room_of(state.loc[a])
    if curr_room!=map.room_of(x) and map.side_of(d, curr_room)==state.loc[a] and map.other_side_of(d, curr_room)==x:
        state.loc[a]=x
        if state.carrying[a]:
            state.loc[state.carrying[a]]=x
        return state
    return False

"""
Operator that opens a closed door 'd' when robot 'a' is in front of that door
"""
def open(state, a, d):
    if state.doors_open[d]==False and state.loc[a]==map.side_of(d, map.room_of(state.loc[a])):
        state.doors_open[d]=True
        return state
    return False

"""
Operator that closes an open door 'd' when robot 'a' is in front of that door
"""
def close(state, a, d):
    if state.doors_open[d] and state.loc[a]==map.side_of(d, map.room_of(state.loc[a])):
        state.doors_open[d]=False
        return state
    return False

"""
Picks up the box 'box' when if the robot 'a' is in the same position as the box
"""
def pickup(state, a, box):
    if state.carrying[a]==None:
        state.carrying[a]=box
        return state
    return False

"""
Puts down the box 'box' in the position where the robot currently is
"""
def putdown(state, a, box):
    if state.carrying[a]==box:
        state.carrying[a]=None
        return state
    return False

pyhop.declare_operators(moveto, cross, open, close, pickup, putdown)


###METHODS###
"""
Top-level-method 'navigate' will use this method if the robot 'a' is in the same room as 
the target location 'x'
"""
def navigate_within_room(state, a, x):
    if map.room_of(x)==map.room_of(state.loc[a]):
        return [('moveto', a, x)]
    return False

"""
Top-level-method 'navigate' will use this method if the robot 'a' is in a different room than 
the target location 'x'
"""
def navigate_across_rooms(state, a, x):
    curr_pos=state.loc[a]
    if map.room_of(x)!=map.room_of(curr_pos):
        #This cycle looks for a door that connects the current room with the room where we are headed. It always finds one
        for d in map.doors_of(map.room_of(curr_pos)):
            if d in map.doors_of(map.room_of(x)):
                if state.doors_open[d]==True:
                    return [('moveto', a, map.side_of(d, map.room_of(curr_pos))), 
                            ('cross', a, d, map.other_side_of(d, map.room_of(curr_pos))),
                            ('moveto', a, x)
                            ]
                else: 
                    return [('moveto', a, map.side_of(d, map.room_of(curr_pos))),
                            ('open', a, d),
                            ('cross', a, d, map.other_side_of(d, map.room_of(curr_pos))),
                            ('close', a, d),
                            ('moveto', a, x)
                            ]
    return False

"""
Method that navigates the robot 'a' to the position where the box 'box' is and picks it up
"""
def fetch_box(state, a, box):
    if state.carrying[a]==None:
        return [('navigate', a, state.loc[box]), ('pickup', a, box)]
    return False

"""
Method that makes the robot 'a' carry the box 'box' from where it is located to a 
new location 'x'. This method uses the top-level-method 'fetch'
"""
def transport_box(state, a, box, x):
    if state.carrying[a]!=box:
        return [('fetch', a, box), ('navigate', a, x), ('putdown', a, box)]
    return False

pyhop.declare_methods('navigate', navigate_within_room, navigate_across_rooms)
pyhop.declare_methods('fetch', fetch_box)
pyhop.declare_methods('transport', transport_box)