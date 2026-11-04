# По низкой цене

def get_file(filename: str):
    with open(filename, "r", encoding="utf-8") as file:
        return [[int(i) if i.isdigit() else i for i in line.strip().split(": ") ] for line in file.readlines()]

requested = [input() for _ in range(int(input()))]
filenames = ["desyatochka.txt", "kubit.txt", "polosa.txt"]

all_products = {}

for filename in filenames:
    for product in get_file(filename):
        all_products.setdefault(product[0], []).append(product[1])

best_products = {product: min(prices) for product, prices in all_products.items() if product in requested}
res = []

best_des, best_kub, best_pol = [], [], []

for product in requested:
    if product not in best_products:
        continue

    price = best_products[product]

    for filename in filenames:
        for info in get_file(filename):
            if info[0] == product and info[1] == price:
                if filename == "desyatochka.txt":
                    best_des.append(info[0])
                elif filename == "kubit.txt":
                    best_kub.append(info[0])
                else:
                    best_pol.append(info[0])

print("Десяточка:")
if best_des:
    print(*best_des, sep=", ")
else:
    print("–")

print("Кубит:")
if best_kub:
    print(*best_kub, sep=", ")
else:
    print("–")

print("Полоса:")
if best_pol:
    print(*best_pol, sep=", ")
else:
    print("–")




