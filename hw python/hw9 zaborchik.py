def zaborchik(line) :
    tmp = ''
    i = 0
    for w in line.lower() :
        if w.isalpha() :
            if i % 2:
                w = w.upper()
            i += 1
        elif w == ' ':
            i = 0
        tmp += w
    return tmp
 
print(zaborchik("заборчик, заборчик"))