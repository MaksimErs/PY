# задача 34 вариант решения Вини-пух(па папа па)
data = input().split()
print(data)

def funk(D):
    x = [list(D[x]).count('а') for x in range(len(D))]
    if len(list(set(x))) == 1:
        print(' есть такт ')
    else:
        print(' нет такта ')    
    
funk(data) 
     