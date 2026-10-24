# Merge lists 1

def merge(list1: list, list2: list) -> list:
    list1.extend(list2)
    return sorted(list1)

print(merge([1, 2, 3], [5, 6, 7, 8]))
print(merge([1, 7, 10, 16], [5, 6, 13, 20]))