list1 = [[7, 15], [2, 3, 5, 10], [4]]

print(max(max(list1, key=lambda lst: max(lst))))