is_non_negative_num = lambda s: float(s) >= 0 if s.replace(".", "", 1).count(".") == 0 and s.replace(".", "").isdigit()  else False

print(is_non_negative_num('a.58'))