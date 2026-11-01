# Строка запроса

def add_query_string(url: str, query: dict[str | None, str | int | None]) -> str:
    if query:
        res = url + "?"
        for k, v in query.items():
            res += f"{k}={v}&"
        return res.rstrip("&")
    return url

print(add_query_string('pygen.ru', {'page': 1}))