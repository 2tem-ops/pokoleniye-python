# Строка запроса

def build_query_string(parameters: dict[str, str | int]) -> str:
    res = []
    for key, value in parameters.items():
        res.append(f"{key}={value}&")
    return "".join(sorted(res)).rstrip("&")

print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))