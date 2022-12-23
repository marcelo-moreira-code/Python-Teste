### Laçoes de repetição p3 -- Interrompendo repetições -while True- com --> break

#StackOverflow

# Normalmente  as linguagens de programação possuem 3 tipos de estruturas de repetição que são
# while , for e o repete ou do while
# No caso do python só existe o for e  o while

#ex1:
# enquanto não maçã:
#    se chão:
#       passo()
#    se buraco:
#       pula()
#    se moeda:
#       pega()
# pega()

#ex2:
# enquanto não maçã:                  while true:
#   se chão:                               if chão:
#     passo()                                 passo()
#   se buraco:                             if buraco:
#     pula()                                  pula()
#   se moeda:                              if moeda:
#     pega()                                  pega()
#   se troféu:                             if troféu:
#     interrompa()                            break()
# pega()                                pega()
#

'''cont = 1
while cont <= 10:
    print(cont, '->', end= '')
    cont += 1
print('Acabou')'''
# para loop infinito é só fazer -- while true --- no lugar de while cont <= 10:
'''cont = 1
while True :
    print(cont,'->',end= '')
    cont += 1
print('Fim')'''

# Gambiarra
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
s -= 999
print('A soma vale {}'.format((s)))

'''n = s = 0
while True:
    n = int(input('Digite um número: '))
    s += n
print('A soma vale {}'.format(s))'''

'''n  = cont = 0
while cont < 3:
    n = int(input('Digite um número: '))
    cont += 1'''


'''n = s = 0
while True :
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')'''

'''n = "Marcelo"
i = 26
print('Meu nome é {} e tenho {} anos.'.format(n,i))
print(f'Meu nome é {n} e tenho {i} anos.')'''

'''n = 'José'
i = 33
s = 987.25
print(f'O {n} tem {i} anos e ganha {s:.2f}.')'''