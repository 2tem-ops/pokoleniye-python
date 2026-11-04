# Сортировка IP-адресов

from ipaddress import ip_address

ips = [input() for _ in range(int(input()))]

print(*sorted(ips, key=lambda ip: int(ip_address(ip))), sep="\n")