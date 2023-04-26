# задача 28
def sumas(a,b):
    if b == 0:
        return a
    else:
        return sumas(a + 1, b -1)
g = int(input())
f = int(input())
print(sumas(g, f))
    