from typing import Callable

def call(func: Callable, *args):
    return func(*args)