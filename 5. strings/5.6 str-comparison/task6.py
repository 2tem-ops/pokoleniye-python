# Порядок книг

orig_n = int(input())
n = orig_n
flag = True

book = input()

name_start = book.find("«") + 1
surname_end = book.find(".")

surname = book[:surname_end - 2]
name = book[name_start:-1]

while n != 0:
    old_book = book
    if n != orig_n:
        book = input()
        if old_book[:old_book.find(".") - 2] == book[:book.find(".") - 2]:
            if old_book[book.find("«") + 1:-1] > book[book.find("«") + 1:-1]:
                flag = False
        else:
            if old_book[:old_book.find(".") - 2] > book[:book.find(".") - 2]:
                flag = False
    n -= 1

if flag:
    print("YES")
else:
    print("NO")
