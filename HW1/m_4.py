# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками 

print("введите количество долек с одной стороны m")
m = int(input())
print("введите количество долек с одной стороны n")
n = int(input())
print("введите сколько долек отламываем k")
k = int(input())
if n * m > k:
    if k % n == 0 or k % m == 0:
        print("можно отломить")
    else:
        print("невозможно отломить k долек")
else:
    print("невозможно отломить k долек")
             
         