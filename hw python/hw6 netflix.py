import random


COST = random.randint(50, 101)

personalMoney = { "Alice":random.randint(0, 80),
        "Bob":random.randint(0, 80),
        "Charley":random.randint(0, 80) }
#создаю список в котором будет генерироваться баланс ребят

while (personalMoney["Alice"] + personalMoney["Bob"] + personalMoney["Charley"] < COST):
    personalMoney["Alice"]: random.randint(0, 80)
    personalMoney["Bob"]: random.randint(0, 80)
    personalMoney["Charley"]: random.randint(0, 80)

    print(personalMoney)
#создаю цикл для того, чтобы соблюдалось условие x+y+z > COST
personalMoney.pop(min(personalMoney))
#убираю наименьшее значение из списка, тем самым остаются двое с наибольшими значениями, которые будут скидываться на подписку

print("На подписку будут скидываться: " ''.join(map(str, personalMoney)))