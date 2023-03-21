start = int(input("Введите начальное число"))
end = int(input("Введите конечное число"))

if start > end:
    start = start + end
    end = start - end
    start = start - end 
else:
    None

array = list(range(start, end + 1))

total = 0
for i in array:
    total += i
    
print(total)



    
 

