is_num = lambda s: True if s.replace(".", "", 1).count(".") == 0 and s.replace("-", "", 1).count("-") == 0 and s.replace(".", "").replace("-", "").isdigit() and "-" not in s[1:-1] else False

print(is_num('0.0'))