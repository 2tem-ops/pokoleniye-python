# 2 часа
from datetime import datetime, timedelta

data = {}

def process_time(hhmm: str) -> datetime:
    return datetime.strptime(hhmm, "%H:%M")

for _ in range(int(input())):
    hm = input().split(": ")
    data[hm[0]] = process_time(hm[1])

for _ in range(int(input())):
    hm = input().split(": ")
    start, end = data[hm[0]], process_time(hm[1])

    if end < start:
        end += timedelta(days=1)

    difference = end - start
    extra_minutes = int((difference - timedelta(hours=2)).total_seconds() // 60)
    opp = extra_minutes * 3
    if difference >= timedelta(hours=2) and opp > 0:
        print(f"{hm[0]}: {opp}₽")
    else:
        print(f"{hm[0]}: плата не взимается")



