list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]

print(sum([sum(lst) for lst in list1]) / sum(len(lst) for lst in list1))