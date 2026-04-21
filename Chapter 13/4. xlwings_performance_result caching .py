# Run each block one by one and notice wall time
# else use start time and end time to see performance difference

import time
from functools import cache

def slow_double(x):
    """Pretend this is slow (e.g., heavy pandas calculation)."""
    time.sleep(2)     # Simulate slow processing
    return x * 2

#%%
# Calling twice → slow both times
%%time
print(slow_double(10))   # waits 2 sec

#%%
%%time
print(slow_double(10))   # waits 2 sec again


#%%
@cache
def slow_double_cached(x):
    """Same function, but cached."""
    time.sleep(2)     # Simulate heavy work
    return x * 2

#%%
# First call → slow (2 sec)
%%time
print(slow_double_cached(10))

#%%
# Second call → Instant!
%%time
print(slow_double_cached(10))
