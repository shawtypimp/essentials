import random

array1 = []

for i in range(random.randint(4, 100)):
    array1.append(random.randint(-1, 9999))
numbers = [array1]
total = 0
for numbers in array1:
    total += numbers
print(total)

x = random.randint(0, 9999)
print(x)

if total%x == 0:
    print(True)
else :
    print(False)


    