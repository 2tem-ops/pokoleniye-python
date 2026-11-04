# Отличники

data = []
res = []

for _ in range(int(input())):
    partition = []
    for _ in range(int(input())):
        student, name = input().split()
        partition.append((student, name))
    data.append(partition)

for sublist in data:
    res.append(any(map(lambda x: x[1] == "5", sublist)))

print("YES" if all(res) else "NO")