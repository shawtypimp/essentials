def eqv(a,b,c):
    return((max (a,b) * 0.01)==(c-(a+b)))
a = float(input("Введите число а"))
b = float(input("Введите число б"))
c = float(input("Введите их сумму"))

print(eqv(a, b, c))