from random import randint
usuario = []
i = 0
amazon = 0
americanas = 0
casas_bahia = 0
extra = 0
magazina_luiza = 0
ponto_frio = 0
submarino = 0
outros = 0
numero = 3000

while i <= numero:
    usuario.append(randint(1,8))
    i += 1
for i in range(numero):
    if usuario[i] == 1:
        amazon += 1
    elif usuario[i] == 2:
        americanas += 1
    elif usuario[i] == 3:
        casas_bahia += 1
    elif usuario[i] == 4:
        extra += 1
    elif usuario[i] == 5:
        magazina_luiza += 1
    elif usuario[i] == 6:
        ponto_frio += 1
    elif usuario[i] == 7:
        submarino += 1
    elif usuario[i] == 8:
        outros += 1


n1 = amazon * randint(1, 20)
n2 = americanas * randint(1, 20)
n3 = casas_bahia * randint(1, 20)
n4 = extra * randint(1, 20)
n5 = magazina_luiza * randint(1, 20)
n6 = ponto_frio * randint(1, 20)
n7 = submarino * randint(1,20)
n8 = outros * randint(1, 20)

soma = n1+n2+n3+n4+n5+n6+n7+n8

print(soma)
print('---------------------------------------------------------')
print('                        ESTATíSTICA                      ')
print('---------------------------------------------------------')
print('Qual a sua loja de departamento favorita?')
print('')
print('Amazon: ', n1)
print('Americanas: ', n2)
print('Casas Bahia: ', n3)
print('Extra: ', n4)
print('Magazine Luiza: ', n5)
print('Ponto Frio: ', n6)
print('Submarino: ', n7)
print('Outros: ', n8)
print('---------------------------------------------------------')
print('')
print('---------------------------------------------------------')

n1 = float((n1 / soma)*100)
n2 = float((n2 / soma)*100)
n3 = float((n3 / soma)*100)
n4 = float((n4 / soma)*100)
n5 = float((n5 / soma)*100)
n6 = float((n6 / soma)*100)
n7 = float((n7 / soma)*100)
n8 = float((n8 / soma)*100)


print('a porcentagem dos usuários que preferem a Amazon é: ', round(n1, 2), '%')
print('a porcentagem dos usuários que preferem a Americanas é: ', round(n2, 2), '%')
print('a porcentagem dos usuários que preferem a Casas Bahia é: ', round(n3, 2), '%')
print('a porcentagem dos usuários que preferem a Extra: ', round(n4, 2), '%')
print('a porcentagem dos usuários que preferem a Magazine Luiza: ', round(n5, 2), '%')
print('a porcentagem dos usuários que preferem a Ponto Frio: ', round(n6, 2), '%')
print('a porcentagem dos usuários que preferem a Submarino: ', round(n7, 2), '%')
print('a porcentagem dos usuários que preferem a Outros: ', round(n8, 2), '%')
print(round(n1+n2+n3+n4+n5+n6+n7+n8, 0))
