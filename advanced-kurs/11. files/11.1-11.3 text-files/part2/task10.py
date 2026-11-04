# Размер не имеет значение

files = {(file := input()): len(open(file).read()) + open(file).read().count("\n") for _ in range(int(input()))}

print(*[f"{file} {size}B" for file, size in sorted(files.items(), key=lambda x: (-x[1], x[0]))], sep="\n")

