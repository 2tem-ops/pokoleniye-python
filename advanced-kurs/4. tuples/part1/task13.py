tuples = [(46, 82), (75,), (3, -4, -10)]

print([i[:-1] + (100,) for i in tuples])