from operator import add, sub, mul, truediv
from typing import Callable

def arithmetic_operation(operation: str) -> Callable:
    return {"+": add, "-": sub, "*": mul, "/": truediv}[operation]