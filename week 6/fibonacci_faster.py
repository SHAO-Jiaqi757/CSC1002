from functools import lru_cache

@lru_cache(None)  # memorize what have computed
def fibonacci_faster(n):
    if n <= 1:
        return 1

    else:
        return fibonacci_faster(n-1) + fibonacci_faster(n-2)