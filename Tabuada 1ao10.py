#Faça um programa que printe no console a tabuda do UM ao DEZ.

n1 = 0
n2 = 0

while n1 < 10:
    n1 += 1
    while n2 < 10:
        n2 += 1
        m = n1 * n2
        print(f"{n1} * {n2} = {m}")
    n2 = 0
