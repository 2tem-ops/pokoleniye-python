numbers = [5, 46, 47, 8, 12, 95, 32]

res = map(lambda x: x // 2 if x % 2 == 0 else x,
          filter(lambda x: x % 2 == 0 or x <= 47, numbers))

print(*res)