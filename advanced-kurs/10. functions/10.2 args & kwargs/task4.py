def greet(*args: str) -> str:
    return f"Hello, {" and ".join(args)}!"

print(greet('Timur', 'Roman'))