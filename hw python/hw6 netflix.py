import random

COST = random.randint(50, 101)

personalMoney = { "Alice":random.randint(0, 80),
        "Bob":random.randint(0, 80),
        "Charley":random.randint(0, 80) }



while (personalMoney["Alice"] + personalMoney["Bob"] + personalMoney["Charley"] < COST):
    personalMoney["Alice"]: random.randint(0, 80)
    personalMoney["Bob"]: random.randint(0, 80)
    personalMoney["Charley"]: random.randint(0, 80)

max_value = max(personalMoney.values())
finalPersonalMoney = {k: v for k, v in personalMoney.items() if v == max_value}
print(finalPersonalMoney)

if personalMoney["Bob"] < personalMoney["Alice"] < personalMoney["Charley"] or personalMoney["Charley"] < personalMoney["Alice"] < personalMoney["Bob"]:
    finalPersonalMoney.update(personalMoney["Alice"])
elif personalMoney["Alice"] < personalMoney["Bob"] < personalMoney["Charley"] or personalMoney["Charley"] < personalMoney["Bob"] < personalMoney["Alice"]:
    finalPersonalMoney.update(personalMoney["Bob"])
else:
    finalPersonalMoney.update(personalMoney["Charley"])

print(finalPersonalMoney)
