lst = []
while True:
    try:
        K = int(input('Введите кол-во чисел, для счёта: '))
        if K < 3:
            raise Exception()
        break
    except Exception as e:
        print('Неверное значение, попробуйте снова')
K += 1
for z in range(1, K):
    while True:
        try:
            lst_add = int(input("Введите число: "))
            if lst_add < 1:
                raise Exception()
            lst.append(lst_add)
            break
        except Exception as e:
            print('Число не утерждает условию, попробуйте снова')

a = 0
b = 0
c = 0
p = 0
s = 0
ms = 0

for i in range(len(lst) - 3):
    a = lst[i]
    b = lst[i + 1]
    c = lst[i + 2]
    if a < b + c and b < a + c and c < b + a:
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        if  s > ms:
            ms = s
            print(a, b, c, 'вход был')
print(ms, a, b, c, 'end')