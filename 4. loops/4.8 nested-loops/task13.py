n, m = int(input()), int(input())
flag = False

for b in range(1, n):
    for d in range(1, n):
        for c in range(1, n):
            if b + 3 * d + 2 * c == m:
                flag = True
                if flag:
                    print(f"{b} + 3×{d} + 2×{c} = {m}")

if flag == False:
    print("При заданных n и m решений не существует.")