# README #

### What is this repository for? ###

* Pyhop, version 1.2.2
* A simple HTN planning system written in Python. 

### How do I get set up? ###

Pyhop is a simple HTN planner written in Python. 
It works in both Python 2 and 3. 
For examples of how to use it, see the example files that come with it.

Pyhop was easy to implement (less than 150 lines of code), and if you understand the basic ideas of HTN planning ([this presentation](http://www.cs.umd.edu/~nau/papers/nau2013game.pdf) contains a quick summary),
Pyhop should be easy to understand.

Pyhop's planning algorithm is like the one in [SHOP](http://www.cs.umd.edu/projects/shop/), but with several differences that should make it easier to integrate it with ordinary computer programs:

  - Pyhop represents states of the world using ordinary variable bindings, not logical propositions. A state is just a Python object that contains the variable bindings.  For example, you might write s.loc['v'] = 'd' to say that vehicle v is at location d in state s.
  
  - To write HTN operators and methods for Pyhop, you don't need to learn a specialized planning language. Instead, you write them as ordinary Python functions. The current state (e.g., s in the above example) is passed to them as an argument.


### Contribution guidelines ###

* I am not currently accepting contributions.

### Who do I talk to? ###

* [Dana S. Nau](http://www.cs.umd.edu/~nau)