### Funções p2

## Interactive Help
## Docstrings
## Argumentos opcionais
## Escopo de Variáveis
## Retorno de resultados

## Ajuda Interativa - Interactive help   -> no Python Console digite -> help() + que queres pesquisa

# help()
#help(input)
#print(input.__doc__)

## Docstrings - string de documentação/ manual

'''def contador(i,f,p):
    """ É uma docstring.
    -> Faz uma contagem e mostra na tela.
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    -> Função criada por Gustavo Guanaba do canal Cursoemvideo.

    """

    c = 1
    while c <= f:
        print(f' {c} ',end='')
        c += p
    print('Fim!')


contador(2,100,5)

help(contador)'''

## Parâmetros Opcionais -> usada para tratar de erros qnd se esquece de preencher algum dos parâmetros da função.

'''def somar(a,b,c=0): # somar(a=0,b=0,c=0)
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    :return: Sem retorno
    -> Função criada por Gustavo Guanabara do canal Cursoemvideo.
    """
    s = a + b + c
    print(f'A soma vale {s}')



somar(3,5,9)
somar(2,6)'''

## Escopo de Variáveis - Escopo é o local onde uma variável vai existir , e onde ela não vai mais existir.
# variável global x local
'''def teste():
    x = 8 # Escopo local, pois, foi declarada dentro da função. Só vale qnd a função for chamada.
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


# Programa Principal
n = 2 # Escopo global , pois , foi declarada fora do função e está valendo para todas as vezes
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal , x vale {x}')'''

# global
'''def teste2(b):
    #global a --> global define o valor da variável durante todo o programa , ignora o 
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')



a = 5
teste2(a)
print(f'A fora vale {a}')
#print(f'B fora vale {b}')
#print(f'C fora vale {c}')'''

## Retornando Valores - return

'''def somar(a=0,b=0,c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3,5,8)
somar(6)
somar(3,6,9)

## 
def somar(a=0,b=0,c=0):
    s = a + b + c
    #print(f'A soma vale {s}')
    return s

r1 = somar(3,5,8)
r2 = somar(6)
r3 = somar(3,6,9)

print(f'Meus cálculos deram {r1}, {r2} e {r3}')'''

'''def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


#n = int(input(('Digite um número: ')))
#print(f'O fatorial de 6 é {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f"Os resultados são {f1} , {f2} e {f3}")'''

# Par ou Ímpar
'''def Par_ou_Impar(n=0):
    if n % 2 == 0:
        return 'Par!'
    else:
        return 'Ímpar!'


n = int(input('Digite um número: '))
print(f'O número {n} é {Par_ou_Impar(n)}')'''

def par (n=0):
    if n % 2 == 0:
        return True
    else:
        return False
        

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É ímpar!')