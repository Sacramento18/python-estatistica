from random import randint
usuario = []
i = 0
aliexpress = 0
banggood = 0
wish = 0
outros = 0
numero = 3000

while i <= numero:
    usuario.append(randint(1, 4))
    i += 1
for i in range(numero):
    if usuario[i] == 1:
        aliexpress += 1

    elif usuario[i] == 2:
        banggood += 1

    elif usuario[i] == 3:
        wish += 1

    elif usuario[i] == 4:
        outros += 1

n1 = aliexpress * randint(1, 20)
n2 = banggood * randint(1, 20)
n3 = wish * randint(1, 15)
n4 = outros * randint(1, 20)
soma = n1+n2+n3+n4


print('#########################################################')
print('                        ESTATíSTICA                      ')
print('#########################################################')
print('Qual Loja de produtos importados possui maior confiança dos usuários?')
print('Em uma amostra de ', soma, 'pessoas tem-se o resultado de: ')
print('')
print('   AliExpress: ', n1)
print('     Banggood: ', n2)
print('         Wish: ', n3)
print('       Outros: ', n4)
print('#########################################################')
print('')
print('#########################################################')

n1 = float((n1 / soma)*100)
n2 = float((n2 / soma)*100)
n3 = float((n3 / soma)*100)
n4 = float((n4 / soma)*100)

print('a porcentagem dos usuários do AliExpress é: ', round(n1, 2), '%')
print('a porcentagem dos usuários do Banggood é: ', round(n2, 2), '%')
print('a porcentagem dos usuários do Wish é: ', round(n3, 2), '%')
print('a porcentagem dos usuários do outras lojas é: ', round(n4, 2), '%')

print(n1+n2+n3+n4)