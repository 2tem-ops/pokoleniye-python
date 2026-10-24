# Камень, ножницы, бумага

steps = {"камень": 0, "бумага": 1, "ножницы": 2}
p1, p2 = input(), input()

opp = (steps[p1] - steps[p2]) % 3
if opp == 0:
    print("ничья")
elif opp == 1:
    print("Тимур")
else:
    print("Руслан")