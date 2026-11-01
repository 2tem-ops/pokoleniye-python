# В чем отличие

def dict_diff(data1: dict[str, int | float], data2: dict[str, int | float]) -> dict[str, str]:
    comparison = {}
    for i in data1:
        if i not in data2:
            comparison[i] = "deleted"
        elif i in data2 and data2[i] == data1[i]:
            comparison[i] = "unchanged"
        else:
            comparison[i] = "changed"
    for i in data2:
        if i not in data1:
            comparison[i] = "added"
    return comparison

data1 = {'one': 1, 'two': 2, 'four': 4}
data2 = {'four': 4}
print(dict_diff(data1, data2))
