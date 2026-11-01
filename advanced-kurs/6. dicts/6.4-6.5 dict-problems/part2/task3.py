# Доступ к ресурсу заблокирован



def is_access_allowed(ip_address: str, mode: int, ip_access_lists: dict[str, list[str]]) -> str:
    if mode == 1:
        return "ДА" if ip_address not in ip_access_lists["black list"] else "НЕТ"
    return "ДА" if ip_address in ip_access_lists["white list"] else "НЕТ"


black_list = [
    '45.34.12.200', '78.91.204.34',
    '78.94.127.35', '96.124.37.82',
]
white_list = [
    '14.231.64.173', '75.34.2.179',
]
ip_access_lists = {
    'black list': black_list,
    'white list': white_list,
}
print(
    is_access_allowed(
        '224.27.189.35',
        1,
        ip_access_lists,
    )
)
