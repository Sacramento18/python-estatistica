from random import randint
usuario = []
i = 0
xiaomi = 0
apple = 0
samsung = 0
lg = 0
motorola = 0
asus = 0
outros = 0
numero = 3000

while i <= numero:
    usuario.append(randint(1,7))
    i += 1
for i in range(numero):
    if usuario[i] == 1:
        xiaomi += 1
    elif usuario[i] == 2:
        apple += 1
    elif usuario[i] == 3:
        samsung += 1
    elif usuario[i] == 4:
        lg += 1
    elif usuario[i] == 5:
        motorola += 1
    elif usuario[i] == 6:
        asus += 1
    elif usuario[i] == 7:
        outros += 1


n1 = xiaomi * randint(1, 20)
n2 = apple * randint(1, 20)
n3 = samsung * randint(1, 20)
n4 = lg * randint(1, 20)
n5 = motorola * randint(1, 20)
n6 = asus * randint(1, 20)
n7 = outros * randint(1, 20)

soma = n1+n2+n3+n4+n5+n6+n7

print(soma)
print('#########################################################')
print('                        ESTATíSTICA                      ')
print('#########################################################')
print('Qual a marca de smartphone favorita??')
print('')
print('xiaomi: ', n1)
print('apple: ', n2)
print('samsung: ', n3)
print('lg: ', n4)
print('motorola: ', n5)
print('asus: ', n6)
print('outros: ', n7)
print('#########################################################')
print('')
print('#########################################################')

n1 = float((n1 / soma)*100)
n2 = float((n2 / soma)*100)
n3 = float((n3 / soma)*100)
n4 = float((n4 / soma)*100)
n5 = float((n5 / soma)*100)
n6 = float((n6 / soma)*100)
n7 = float((n7 / soma)*100)


print('a porcentagem dos usuários do xiaomi é: ', round(n1, 2), '%')
print('a porcentagem dos usuários do apple é: ', round(n2, 2), '%')
print('a porcentagem dos usuários do samsung é: ', round(n3, 2), '%')
print('a porcentagem dos usuários do lg: ', round(n4, 2), '%')
print('a porcentagem dos usuários do motorola: ', round(n5, 2), '%')
print('a porcentagem dos usuários do asus: ', round(n6, 2), '%')
print('a porcentagem dos usuários de outros: ', round(n7, 2), '%')
print(round(n1+n2+n3+n4+n5+n6+n7, 0))