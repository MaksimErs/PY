# задача 26
def pow(a,b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return pow(a*a,b // 2)
    else:
        return a * pow(a * a, (b - 1) // 2)
a = int(input())
b = int(input())
print(pow(a,b))
    