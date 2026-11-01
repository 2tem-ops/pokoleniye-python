# Исправление дубликатов

s = input().split()
duplicates = {}

for char in s:
    if char not in duplicates:
        print(char, end=" ")
    else:
        print(f"{char}_{duplicates[char]}", end=" ")
    duplicates[char] = duplicates.get(char, 0) + 1

