### LAÇOS,REPETIÇÕES OU ITERAÇÕES

## ESTRUTURA DE REPETIÇÃO OU LAÇO -for- LAÇO COM VARIÁVEL DE CONTROLE

# laço c no intervalo(0,3):          for c in range(0,3):
#       passo()                            passo()
#       pega()                             pega()
# passo()                            passo()
# pega()                             pega()


# laço c no intervalo(0,3):          for c in range(0,3):
#       se @:                              if @:
#          pega()                             pega()
#       passo()                            passo()
#       pula()                             pula()
# passo()                            passo()
# pega()                             pega()

#for c in range(1,6):
#    print('Oi')
#print('Fim')

#for c in range(0,10):
#    print(c**2)

# se quiser que conte do maior para o menor é só fazer
for c in range(6,0,-1):
    print(c)
print('Fim')

'''n = int(input('Digite um número: '))
for c in range(0,n+1):
    print(c)
print('Fim')'''

'''i = int(input('início: '))
f = int(input('Fim: '))
p = int(input('Passos: '))
for c in range(i,f+1, p):
    print(c)
print('Fim')'''
# Para fazer o somatório de uma sequência pode-se fazer:
'''s = 0
for c in range(0,6):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}.'.format(s))'''

'''s = 0
for c in range(0,101):
    s += c
print('O somatório de todos os números de 0 a 100 é {}.'.format(s))'''

'''Q47 - for c in range(1,26):
    print(c*2)'''


'''s = 0
for c in range(0,101):
    s += c
print(s)'''
#    if c % 2 != 0:
#        print(c)
#    s += c
#print(s)
'''s = 0
for c in range(0,501,5):
    s += c
    print(c)'''
#print(s)