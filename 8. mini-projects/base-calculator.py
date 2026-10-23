def BOH(num: int):
    return bin(num)[2:], oct(num)[2:], hex(num)[2:].upper()

def convert_to_any_base(num: int, base: int):
    res = ""
    while num != 0:
        remainder = num % base
        if remainder >= 10:
            remainder = chr(65 + (remainder - 10))
        num //= base
        res += str(remainder)
    return res[::-1]

if __name__ == "__main__":
    n = int(input())
    for num in BOH(n):
        print(num)