# найдите сумму цифр трехзнаяного числа

print("введите трехзначное число")
m = int(input())
c = m // 100
b = m % 100
t = m // 10 - c * 10
d = m % 10
Resalt = c + d + t
print("сумма цифр введенного числа равна")
print(Resalt)
