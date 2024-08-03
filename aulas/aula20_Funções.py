### Funções - def

# Rotina / repetição
# def -> as funções criam comandos personalizados  / tbm pode-se usar parametros

'''
print() / input() / int() / len() ...

def enfeite():
    print('</>'*16)

enfeite()
print('          SISTEMA DE ALUNOS          ^.^')
enfeite()

##

def mensagem(msg):
    print('-'*20)
    print(msg)
    print('-'*20)

mensagem('Olá, tudo bem?')


def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'E a soma de A + B é {s}')




def mult(a,b):
    m = a * b
    print(m)


print(f'A soma dos números 4 e 9 é {soma(4,9)}  e a multiplicação deles é {mult(4,9)} ')
soma(4,9)
mult(4,9)'''

# Empacotamento de parâmetros -> * para desenpacotar

'''def soma(* números):
    s = 0
    for num in números:
        s += num
    print(f'Somando os números {números} temos {s}')

soma(2,4,6,8,3,5,7,9)
soma(13,23,37,77)'''


'''def contador(*num):
    print(num)
    for valor in num:
        print(f'{valor} -> ', end='')
    print(' Fim!')'''

# Pode usar todos os métodos das tuplas e listas na def

'''def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


contador(5,3,7,8,9)
contador(5,7,8,9,12,3,4,5)
contador(3,5)'''

# Nas listas

'''def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1


valores = [3,5,7,9,11]
dobra(valores)
print(valores)'''




