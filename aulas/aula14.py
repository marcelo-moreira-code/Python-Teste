## ESTRUTURA DE REPETIÇÃO,LACOS- while -

#- for - é uma ESTRUTURA DE REPETIÇÃO COM VARIÁVEL DE CONTROLE

# A estrutura  de repetição - for -É usada qnd se sabe +- quantas repetições serão feitas- precisa de um limite ou precisa-se saber o intervalo ex :(1,100)/(2,200,2) ...

# Já quando tem-se uma estrutura que não se sabe o limite do intervalo a ser executado , é preferível
# Usar a estrutura de repetição - while - enquanto não fizer tal coisa ,continua repetindo.

#-while- é uma ESTRUTURA DE REPETIÇÃO COM TESTE LÓGICO

# enquanto não maça:              while not apple:
#      passo()                        passo()
# pega()                          pega()

# ou seja se vc sabe o limite (onde inicia e onde términa) do intervalo usa o -for-
# se não sabe o limite usa o -while-
# -while - serve para quando se sabe o limte e tbm para quando ção se sabe o lim.

# while not apple:
#    if chão:
#       passo()
#    if buraco:
#       pule()
#    if moeda:
#       pega()
# pega()

'''for c in range (1,10):
    print(c)
print('Fim') '''

# c += 1 é =  c = c +1

'''c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')'''

#Ex1 de Flag ou condição de parada ->while n!=0:
# Enquanto n não for 0  ele continua pedido valores
'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')'''

#Ex2
'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S?N] ')).upper()
print('Fim')'''

#Ex3
'''n = 1
par = impar = 0
s = 0
while n != 0:
    n = int(input('Digite um valor: '))

    if n != 0:
        if n % 2 == 0:
            par += 1
            s += n
        else:
            impar += 1
print('Você digitou {} números pares  e {} números ímpares. {}'.format(par,impar,s))
 '''

# Programa para ler a quantidade de palavras em um texto


'''name = (input('Enter file: '))
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)'''