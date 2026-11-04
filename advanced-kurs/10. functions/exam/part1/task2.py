def pretty_print(data: list, side: str="-", delimiter: str="|"):
    print(side * (len(data) * 3 + sum(len(str(x)) for x in data) + 1))
    for element in data:
        print(f"{delimiter} {element}", end=" ")
    print(delimiter)
    print(side * (len(data) * 3 + sum(len(str(x)) for x in data) + 1))

pretty_print([1, 2, 10, 23, 123, 3000])