dict1 = {'apple': 7, 'orange': 2, 'peach': 5}
dict2 = {'kiwi': 1, 'apple': 6, 'orange': 2}

dict1 = {k: (dict1[k] + dict2[k] if k in dict2 else dict1[k]) for k in dict1.keys()}
dict2.update(dict1)

print(dict2)