# Калькулятор доставки

def get_shipping_cost(quantity: int) -> int:
    if quantity == 1:
        return 1000
    else:
        return 1000 + 120 * (quantity - 1)

print(get_shipping_cost(1))
print(get_shipping_cost(100))
