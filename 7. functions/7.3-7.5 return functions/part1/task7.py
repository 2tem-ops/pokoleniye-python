# С каждого по одному

def get_unique(numbers: list) -> list:
    lst = []
    [lst.append(i) for i in numbers if i not in lst]
    return lst


print(get_unique([1, 2, 4, 3, 4]))
print(get_unique([0, -2, 1, -2, -3, 0]))
print(get_unique([5, 6, 7]))