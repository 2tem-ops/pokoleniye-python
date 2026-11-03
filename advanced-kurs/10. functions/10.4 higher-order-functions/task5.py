from typing import Callable

def func_apply(func: Callable, lst: list) -> list:
    return list(map(func, lst))
