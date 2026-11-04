def concat(*args, sep: str=" ") -> str:
    return sep.join(str(i) for i in args)