n, z1, z2 = int(input()), complex(input()), complex(input())
z1_conj, z2_conj = z1.conjugate(), z2.conjugate()

print(z1 ** n + z2 ** n + z1_conj ** n + z2_conj ** (n + 1))