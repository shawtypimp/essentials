S = [23, 51, 70, 44, 95, 67, 88]
#спрос
D = [11, 24, 70, 38, 95, 22, 88]
#предложение
N =[]
#список в котором будут храниться моменты времени, когда рынок находился в равновесии
for i in S:
    if i in D:
        N.append(i)
#цикл, который находит совпавшие элементы в двух массивах 
numbersOfMoments = len(N)
#получаю количество элементов в массиве
print("Количество моментов времени когда рынок был в рановесии: ", numbersOfMoments)
