# Is the Triangle Valid?

def is_valid_triangle(side1, side2, side3):
    if side1 < side2 + side3 and side2 < side3 + side1 and side3 < side1 + side2:
        return True
    else:
        return False

print(is_valid_triangle(12, 10, 11))
print(is_valid_triangle(2, 2, 2))
print(is_valid_triangle(2, 3, 10))
print(is_valid_triangle(3, 4, 5))