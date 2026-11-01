users = [
    {'name': 'Andrew', 'email': 'and@gmail.com'},
    {'name': 'Tim', 'phone': '555-1618', 'email': 'tim-tim@yandex.ru'},
    {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
    {'name': 'Vika', 'phone': '547-2123', 'email': 'Viko4ka@gmail.com'},
    {'name': 'Kate', 'surname': 'Maltseva', 'city': 'Vologda'},
]

print(*sorted(user["name"] for user in users if user.get("email", "") == ""))