from string import punctuation
 
text = str(input("Введите текст содержащий не менее 5 слов"))
 
tbl = str.maketrans('', '', punctuation)
words = text.translate(tbl).lower().split()
print(max(words, key=len))
print(max(set(words), key=lambda x: words.count(x)))