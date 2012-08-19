Haldean's Conjecture
===============================================
*Definition*: An *object* is defined to be in one of three states, *A*, *B* or
*C*.

*Definition*: An *actor* can be one of two types; type *F* can only use objects
in state *A*. Type *M* uses objects in state *A* with a probability of 0.2, and
objects in state *B* with a probability of 0.8. Actors may switch the state of
an object before and after use. Switching the state of an object requires a
work factor of 1. All actors use an object every X seconds, where X is a random
variable taken from a Gaussian distribution with parameters x_bar and sigma.

*Problem*: Given a configuration *Q = (N_F, N_M, x_bar_F, x_bar_M, sigma_F,
sigma_M)*, what is the optimal strategy for each of the actors to reduce the
total work factor?

*Haldean's Conjecture*: The optimal strategy is for each actor is as follows:

* On using the object, the actor changes its state to whatever state is
  required for the actor to use the object.
* After using the object, the actor leaves the object in the state in which it
  was used.

