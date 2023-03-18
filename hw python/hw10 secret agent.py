codeWords = ["Мавпродош", "Лорнектиф", "Древерол", "Фиригарпиг", "Клодобродыч"]
codeWord = str(input("Введите кодовое словое с большой буквы"))
c = []

for i in codeWords:
    if i in codeWord and i in codeWords:
        c.append(i)
       
result = any(i in codeWord for i in codeWords)

if result == True:
    print("Ты – свой. Приветствую, любезный", "".join(c),"!")
else:
    print("Тут ничего нет. Еще есть вопросы?")
   
