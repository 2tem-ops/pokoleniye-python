# Анаграммы 2

print("YES" if (sorted([i for i in input().lower() if i.isalpha()]) == sorted([i for i in input().lower() if i.isalpha()])) else "NO")