# задача 36 вычисление элемента по номеру строки и столбца(вариант)
def print_oper(op,x,y):
    print(op(x,y))
def fors(rows,columns):    
    rows = 6
    columns = 6
    d = []    
    for a in range(1,rows + 1):
        d.append(list(map(lambda f:a*f,range(1,columns+1))))
    return d  
print_oper(fors,6,6) 