from random import randint

def generate_lottery_ticket() -> str:
    lst = set()
    ticket = ""
    while True:
        lst.add(randint(1, 49))
        if len(lst) == 7:
            ticket += " ".join([str(i) for i in (sorted(list(lst)))])
            lst.clear()
            break
    return ticket.rstrip()


print(generate_lottery_ticket())
print(generate_lottery_ticket())
print(generate_lottery_ticket())