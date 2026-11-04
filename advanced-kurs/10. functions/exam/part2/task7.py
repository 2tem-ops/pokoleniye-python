from typing import Callable

def compose(f: Callable, g: Callable) -> Callable:
    def h(x) -> Callable:
        return f(g(x))
    return h