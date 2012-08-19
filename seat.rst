Haldean's Conjecture
===============================================
*Definition*: An *object* is defined to be in one of three states, *A*, *B* or
*C*.

*Definition*: An *actor* can be one of two types; type *F* can only use objects
in state *A*. Type *M* uses objects in state *A* with a probability of 0.2, and
objects in state *B* with a probability of 0.8. Actors may switch the state of
an object before and after use. Switching the state of an object requires a
work coefficient of 1. All actors use an object every X seconds, where X is a
random variable taken from a Gaussian distribution with parameters x_bar and
sigma.

*Problem*: Given a configuration *Q = (N_F, N_M, x_bar_F, x_bar_M, sigma_F,
sigma_M)*, what is the optimal strategy for each of the actors to reduce the
total work coefficient?

*Haldean's Conjecture*: The optimal strategy is for each actor is as follows:

* On using the object, the actor changes its state to whatever state is
  required for the actor to use the object.
* After using the object, the actor leaves the object in the state in which it
  was used.

Simulation
-----------------------------------------------
We construct a simulation which takes a time limit, a configuration and a
strategy for each class of actor, runs 1000 trials and outputs the mean work
coefficient incurred by the given strategy. Strategies are functions
*f: State -> State -> State* , which map initial state and required state to
"output state", where the "output state" is defined as the state in which the
actor leaves the object.

Each trial consists of two phases. First, for each actor, a stream of events
is calculated with associated timestamps and state requirements. Each element
in the stream is a 3-tuple of *(time, required_state, actor)* . The duration
between events is taken from the associated Gaussian distribution for each
actor.

These event streams are then merge-sorted and the second phase begins, in which 
the total work coefficient for the trial is calculated. During merging, if any
two actors attempt to use the object at the same time, a random actor is picked
to go first. The initial state of the object *q_0* is defined to be the
required state of the first actor to use the object.  Then, for each element in
the stream *(t, r, A)*:

* If the current state *q* and the required state *r* differ, add 1 to the work
  coefficient.
* Let *f* be the strategy for actor *A*. Apply *f* to *q, r* to get *q'*. Let
  *q = q'*

Repeat until all elements in the stream have been exhausted. The result of this
trial will be the work coefficient, or the number of times the state of the
object was changed out of necessity.
