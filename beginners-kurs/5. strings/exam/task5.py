# Переворот

s = input()

first, second = s.find("h"), s.rfind("h")

sub1 = s[first + 1:second]
sub2 = s[second - 1:first:-1]

print(s.replace(sub1, sub2))