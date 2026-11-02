tuples = [(26, 1, 30), (47, 5, 4), (11, 7, 9)]

print({tpl[0]: tpl[1:] for tpl in tuples})