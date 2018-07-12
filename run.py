from lru_cache.utils import cache

@cache
def some_func(a, b, c):
    print (a, b, c)
    return '{0}-{1}-{2}'.format(a, b, c)

if __name__ == "__main__":
    print(some_func(1, 1, 1))
    print(some_func(2, 2, 2))
    print(some_func(1, 1, 1))