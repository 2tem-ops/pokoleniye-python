from functools import reduce

data = [
    ['Sydney', 5367206, 'primary'], ['Perth', 2384371, 'nan'],
    ['Melbourne', 5159211, 'nan'], ['Canberra', 466566, 'admin'],
    ['Darwin', 127532, 'nan'], ['Jakarta', 41913860, 'admin'],
    ['Kolkata', 22549738, 'primary'], ['Shenzhen', 13878396, 'primary'],
]

print("Cities: " + ", ".join(str(i) for i in sorted([item for sublist in filter(lambda city: city[2] == 'primary' and city[1] > 10_000_000, data) for item in sublist if str(item)[0].isupper()])))