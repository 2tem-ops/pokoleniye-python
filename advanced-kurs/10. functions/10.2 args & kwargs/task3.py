def mean(*args) -> int | float:
    nums = [arg for arg in args if type(arg) is int or type(arg) is float]
    if nums:
        return sum(nums) / len(nums)
    return 0

print(mean(-1, 2, 3, 10, ('5')))