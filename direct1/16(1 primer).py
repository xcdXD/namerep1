#region переписывание(один из примеров)

from functools import lru_cache

@lru_cache(maxsize = 500) #ставить 500 или 1000(чтоб комп не взорвался),также увеличение может зарешать
def f(n):
    if n == 1: #переписываем сюда что после при или если
        return 1 #пишется до при или если(здесь f(n) == 1)
    if n > 1:
        return n * f(n - 1)

#endregion

for n in range(3300):f(n)
print((f(3238) // 2 + f(3237)) // f(3236))     #integer division result too large for a float(если вылезла эта ошибка, то нужно за место обычного / поставить //)
