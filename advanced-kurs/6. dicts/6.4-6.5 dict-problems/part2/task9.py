# По категориям

def show_top_categories(spendings: list[tuple[str, int]], num: int) -> None:
    data = {}

    for product, price in spendings:
        data[product] = data.get(product, 0) + price

    categories = sorted(data.items(), key=lambda x: (x[1], x[0].lower()), reverse=True)[:num]

    for category, spending in sorted(categories, key=lambda x: x[0].casefold()):
        print(category)


spendings = [
    ('продукты', 780), ('фитнес', 3000),
    ('ЖКХ', 11500), ('продукты', 1200),
    ('такси', 420), ('продукты', 230),
    ('аптека', 900), ('сантехника', 700),
    ('товары для дома', 1750),
]
show_top_categories(spendings, 3)