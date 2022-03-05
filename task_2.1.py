import pyhop
import map

def moveto(state, a, x):
    if map.room_of(state.loc[a])==map.room_of(x):
        state.loc[a] = x
        return state
    return False

def cross(state, a, d, x):
    curr_room=map.room_of(state.loc[a])
    if curr_room!=map.room_of(x) and map.side_of(d, curr_room)==state.loc[a] and map.other_side_of(d, curr_room)==x:
        state.loc[a]=x
        return state
    return False

pyhop.declare_operators(moveto, cross)

def navigate_within_room(state, a, x):
    if map.room_of(x)==map.room_of(state.loc[a]):
        return [('moveto', a, x)]
    return False

def navigate_across_rooms(state, a, x):
    curr_pos=state.loc[a]
    if map.room_of(x)!=map.room_of(curr_pos):
        for d in map.doors_of(map.room_of(curr_pos)):
            if d in map.doors_of(map.room_of(x)):
                return [('moveto', a, map.side_of(d, map.room_of(curr_pos))), 
                        ('cross', a, d, map.other_side_of(d, map.room_of(curr_pos))),
                        ('moveto', a, x)
                       ]
    return False

pyhop.declare_methods('navigate', navigate_within_room, navigate_across_rooms)

state1 = pyhop.State('state1')
state1.loc = {'robot': 'p5'}

pyhop.pyhop(state1, [('navigate', 'robot', 'p1')], verbose=1)