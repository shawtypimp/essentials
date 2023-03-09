tomspeed = int(input("Введите скорость движения Тома"))
jerryspeed = int(input("Введите скорость движения Джерри"))
distance = int(input("Введите расстояние между Томом и Джерри"))
formula = float(distance/(tomspeed-jerryspeed))
if jerryspeed >= tomspeed :
    print("Том никогда не догонит Джерри")
else: 
    print ("Том настигнет Джерри за: ", formula, "секунд" ) 