import random

secretNumber = random.randint(1, 101)
print(secretNumber)

userName = input("Напишите ваше имя: ")

f = open("name&guesses.txt", "w")
print("Компьютер загадал число от 1 до 100, ваша задача угадать его ")
guessesMade = 0
answer = 0

while answer != secretNumber:
    answer = int(input("Введите число: "))
    guessesMade += 1
    if answer < secretNumber:
        print("Загаданное число больше ")
    if answer > secretNumber:
        print("Загаданное число меньше ")
    if answer == secretNumber:
        print("Вы угадали число!")
        print("Количество попыток: ", guessesMade)
 
f = open("name&guesses.txt", "w")
f.write(userName)
f.write(str(guessesMade))
f.close()