def print_products(*args) -> None:
    products = [arg for arg in args if type(arg) is str and arg]
    res = []

    if products:
        for idx, product in enumerate(products, start=1):
            res.append(f"{idx}) {product}")
        print("\n".join(res))
    else:
        print("Нет продуктов")

print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)