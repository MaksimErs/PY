# счастливый билет проверка

print("введите шестизначное число билета")
v = int(input())
m = v // 1000
c = m // 100
b = m % 100
t = m // 10 - c * 10
d = m % 10
Resalt1 = c + d + t
print(Resalt1)
n = v % 1000
c1 = n // 100
b1 = n % 100
t1 = n // 10 - c1 * 10
d1 = n % 10
Resalt2 = c1 + d1 + t1
print(Resalt2)
if Resalt1 == Resalt2:
    print("билет счастливый")
else:
    print("билет не счастливый")
    
