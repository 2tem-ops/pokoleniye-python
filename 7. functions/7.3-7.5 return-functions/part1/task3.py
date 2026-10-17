# Количество дней

def get_days(month: int) -> int:
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        return 28
    else:
        return 31