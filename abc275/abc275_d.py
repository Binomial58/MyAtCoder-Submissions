# pythonでメモ化再帰を行う方法
from functools import lru_cache


@lru_cache
def yet(t):
    if t == 0:
        return 1
    else:
        return yet(t // 2) + yet(t // 3)


n = int(input())
print(yet(n))
