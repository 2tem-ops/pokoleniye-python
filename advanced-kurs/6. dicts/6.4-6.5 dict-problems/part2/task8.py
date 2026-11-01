# Банковские операции

vault = {}

def bank(operation: str, id: str, amount: int | None) -> None:

    if id not in vault: vault[id] = 0

    if operation == "top up": vault[id] += amount
    elif operation == "withdraw" or operation == "pay": vault[id] -= amount
    elif operation == "show balance" and not amount: print(vault[id])



arthur = 'id-1004'
tony = 'id-78923'
bank('top up', tony, 500)
bank('show balance', arthur, None)
bank('pay', tony, 120)
bank('top up', arthur, 1000)
bank('show balance', arthur, None)
bank('withdraw', tony, 200)
bank('show balance', tony, None)