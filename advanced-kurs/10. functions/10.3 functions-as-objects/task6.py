# Интересная сортировка-1

nums = list(map(int, input().split()))

print(*sorted(nums, key=lambda x: sum(int(i) for i in str(x))))

