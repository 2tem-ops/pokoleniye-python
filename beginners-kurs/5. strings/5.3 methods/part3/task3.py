# Автомобильный номер

plate = input()

flag = False

valid_letters = "АВЕКМНОРСТУХ"
valid_length = len(plate) == 10 or len(plate) == 9

if valid_length:
    if plate[:1].isalpha() and plate[:1] in valid_letters:
        if plate[1:4].isdigit():
            if plate[4:6].isalpha() and plate[4] in valid_letters and plate[5] in valid_letters:
                if plate[6] == "_":
                    if plate[7:].isdigit():
                        flag = True

if flag:
    print("YES")
else:
    print("NO")



