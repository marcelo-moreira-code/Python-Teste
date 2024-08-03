## TUPLAS SÃO IMUTÁVEIS

# Há 3 tipos de variáveis compostas em python - Tuplas -()- ,Listas-[]- e os Dicionários-{}
## Tuplas


# As TUPLAS são variáveis compostas e IMUTÁVEIS que permitem armazenar vários valores em uma mesma estrutura,acessíveis por chaves individuais.

# Tuplas servem para armazenar informações que não serão alteradas- CPF/RG....

'''tupla = (1,2,3,4,5)
lista = [1,2,3,4,5]

cliente = ('Ana','22','1.65')
clientes = []

# Como é o caso desse exemplo, estamos fazendo um cadastro de um cliente com informações que não serão alteradas e vamos utilizar
# o método - append - da lista para adicionar essa tupla dentro da nossa lista.

clientes.append(cliente)  # adicionando novos ítens / acessando um ítem em uma tupla
print(clientes)

cliente = ('Lucas','21','1.75')
clientes.append(cliente)

cliente = ('Jennifer','20','1.70')
clientes.append(cliente)
print(clientes[0])'''

# Tuplas com Chaves de Dicionários - Tuplas como chave de dicionário
# Aqui estamos colocando os países como chave e as capitais como valores dentro do nosso dicionário.

'''países = {('Brasil') : 'Brasília',('França'):'París',('EUA'):'WD',('Japão') :'Tókio'}
print(países.keys())
print(países.values())'''

# .sorted
# .index
# .count
'''tupla = (2,3,4,5,6,2,2,2,5,9)
print(tupla.index(5))

print(tupla.count(2))'''

# As tuplas -()- são IMUTÁVEIS

lanches = ('sanduíche', 'suco', 'pudim', 'bolo')
lanches.index('suco')
print(lanches.index('suco'))
print(len(lanches))

#for comida in lanches:
#    print(f'Eu vou comer {comida}')
#print('Comi pra caramba!')


#for count in range(0,len(lanches)):
#    print(f'Eu vou comer {lanches[count]} na posição {count}')


#for pos, comida in enumerate(lanches):
#    print(f'Eu vou comer {comida} na posição {pos}')

#print('Comi pra caramba!')

'''a = (1,2,3,4,5,3,5,7)
b = ('a','b','c','d','e')
c = a + b
c1 = b + a
print(c)
print(c1)
#print(c1.index('c'))
print(a)
print(a.index(5, 5))

Para exibir o índice de um elemento de uma tupla em Python, utilizamos o método index(elemento,início,final), que pode conter até três argumentos:

elemento: que será procurado na tupla;
início: índice inicial da pesquisa, que é opcional;
final: índice final da pesquisa, que é opcional.

#print(c1.count(3))'''
#pessoa = ('Gustavo', 39, 'M', 99.40)
