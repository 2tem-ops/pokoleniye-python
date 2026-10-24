# Кремниевая долина

n = int(input())

res = []
for i in range(1, n + 1):
    s = input()
    word = "anton"
    j = 0

    for ltr in s:
        if ltr == word[j]:
            j += 1
            if j == len(word):
                break

    if j == len(word):
        res.append(str(i))

print(" ".join(res))
