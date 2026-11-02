# Покупки в интернет-магазине

purchases = {}

for _ in range(int(input())):
    buyer, product, amount = input().split()
    amount = int(amount)

    purchases.setdefault(buyer, {})
    purchases[buyer][product] = purchases[buyer].get(product, 0) + amount

for name, purchase in sorted(purchases.items()):
    print(name + ":")
    for product, amount in sorted(purchase.items()):
        print(product, amount)