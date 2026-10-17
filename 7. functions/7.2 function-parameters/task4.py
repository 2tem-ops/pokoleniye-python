# Отсортируй и выведи

def print_sorted_hyphen(s: str):
    lst = s.split("-")
    lst.sort()
    print("-".join(lst))

print_sorted_hyphen("orange-apple-avocado-plum-cherry")