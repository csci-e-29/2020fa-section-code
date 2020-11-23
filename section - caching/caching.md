## Administrivia

Schedule:
- 11/18: memoization, caching; pset 5 due tomorrow
- 11/25: schedule next week
- 12/2 Visualization
- 12/9 Science Fair
- 12/16 Final

outstanding: pset 6, final project, final exam

## Caching

#### Django Caching
https://docs.djangoproject.com/en/3.1/topics/cache/

The cache system requires a small amount of setup. Namely, you have to tell it where your cached 
data should live – whether in a database, on the filesystem or directly in memory. This is an 
important decision that affects your cache’s performance; yes, some cache types are faster than others.

local memory, which is like a lightweight memcached, is the default

#### Popular strategies that describe the mechanism for keeping and evicting data from the cache.
FIFO, LIFO, LRU, MRU, LFU

#### Memoization in Python
https://towardsdatascience.com/memoization-in-python-57c0a738179a

#### LRU Cache
https://docs.python.org/3.4/library/functools.html?highlight=lru_cache
t.ly/3GOV

#### Timeit
https://docs.python.org/3/library/timeit.html


### LRU strategy

@functools.lru_cache(maxsize=128, typed=False)

Decorator to wrap a function with a memoizing callable that saves up to the maxsize
most recent calls. It can save time when an expensive or I/O bound function is
periodically called with the same arguments.

Since a dictionary is used to cache results, the positional and keyword arguments
to the function must be hashable.

If maxsize is set to None, the LRU feature is disabled and the cache can grow without
bound. The LRU feature performs best when maxsize is a power-of-two.

If typed is set to True, function arguments of different types will be cached separately.
For example, f(3) and f(3.0) will be treated as distinct calls with distinct results.

---

A cache implemented using the LRU strategy organizes its items in order of use.
Every time you access an entry, the LRU algorithm will move it to the top of the
cache. This way, the algorithm can quickly identify the entry that’s gone unused
the longest by looking at the bottom of the list.

@lru_cache uses a dictionary behind the scenes. It caches the function’s result under a
key that consists of the call to the function, including the supplied arguments.

