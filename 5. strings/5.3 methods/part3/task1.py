# Плохие комментарии

n = int(input())
s = ""

for i in range(1, n + 1):
    comment = input()
    if comment.isspace() or len(comment) == 0:
        s += f"{i}: COMMENT SHOULD BE DELETED\n"
    else:
        s += f"{i}: {comment}\n"

print(s)
