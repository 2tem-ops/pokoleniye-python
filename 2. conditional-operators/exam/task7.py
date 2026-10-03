x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 - x2 == 2 and (y1 - y2 == 1 or y2 - y1 == 1)) or (x2 - x1 == 1 and y1 - y2 == 2):
    print("YES")
elif (x2 - x1 == 2 and y2 - y1 == 1) or (x2 - x1 == 1 and y2 - y1 == 2):
    print("YES")
elif x1 - x2 == 1 and (y2 - y1 == 2 or y1 - y2 == 2):
    print("YES")
elif x2 - x1 == 2 and (y1 - y2 == 1 or y2 - y1 == 1):
    print("YES")
else:
    print("NO")