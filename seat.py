import numpy

def stream_for_actor(actor, max_time):
  gen_time = lambda: actor.sigma * numpy.random.randn() + actor.x_bar
  time = gen_time()
  while time < max_time:
    yield (time, actor.required_state(), actor)
    time += gen_time()

def merge_streams(actor_streams):
  actors = []
  for actor in actor_streams:
    try:
      actor_head = actor.next()
      actors.append((actor_head, actor))
    except StopIteration:
      pass
  while actors:
    actors = sorted(actors)
    min_val, min_actor = actors.pop(0)
    yield min_val
    try:
      actors.append((min_actor.next(), min_actor))
    except StopIteration:
      pass
      
