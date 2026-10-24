# Разбиение на чанки

s = input().split()
n = int(input())

def chunked(lst: list[str], chunk_size: int) -> list:
    res = []

    if len(lst) <= chunk_size:
        return [lst]

    lst = "".join(lst)
    chunks = len(lst) // chunk_size

    k = 0

    for i in range(chunks):
        chunk = []
        while len(chunk) < chunk_size:
            chunk.append(lst[k])
            k += 1
        res.append(chunk)

    if len(lst) % chunk_size != 0:
        res.append([lst[-1]])

    return res

print(chunked(s, n))