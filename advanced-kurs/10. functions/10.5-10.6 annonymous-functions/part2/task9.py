mixed_list = ['cow', 12, 'chicken', 'sand', 75]

print(max(mixed_list, key=lambda x: (type(x) is int, x)))