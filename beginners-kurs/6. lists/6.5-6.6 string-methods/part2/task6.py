# Сортируем песни

n = int(input())
songs = []

for _ in range(n):
    songs.append(input())

songs.sort()
print(*songs, sep="\n")