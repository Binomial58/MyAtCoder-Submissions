from functools import lru_cache

mod = 998244353


@lru_cache
def Fc(n):
    if n > 4:
        return (Fc(n // 2) % mod * Fc((n + 1) // 2) % mod) % mod
    else:
        return n


x = int(input())
print(Fc(x))
