#region c 2-я буквами(т.е с f и g)

from functools import *

@lru_cache(maxsize = 500)
def f(n):
    return 3 * g(n - 3) + 7

@lru_cache(maxsize = 500)
def g(n):
    if n <= 20:
        return n + 2
    if n > 20:
        return g(n - 3) + 1
for n in range(38000):f(n)
print(f(37811))
