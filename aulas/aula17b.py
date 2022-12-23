### LISTAS []

# O que é uma lista em Python

# Nada mais é do que uma lista comum, é isso mesmo, uma lista comum!

# Quando você faz uma lista de compras, por exemplo, isso é uma lista, e no Python é a mesma coisa!

# Vamos poder listar todas as informações dentro de uma única variável e depois utilizar essas informações dentro do nosso código.

# Para criar listas no Python é necessário:

# Utilizar o símbolo [] (colchetes) para as listas;
# Armazenar a lista em uma VARIÁVEL;
# Separa itens da lista pela vírgula;

#lista_frutas = ['maça','banana','melancia','abacate']
#print(lista_frutas[0])

## Métodos do Python para utilizar nas listas
# Agora vamos analisar alguns métodos do Python como: append e insert (para inserir informações na lista); del, pop e remove (para remover itens da lista).

## Para ADICIONAR um item a lista:

# .append(): adiciona o item ao final da lista;
# .insert(): insere um item na lista na posição indicada

## Para DELETAR um item da lista:

# .del: remove um item da lista baseado na posição indicada;
# .remove(): remove um item baseado no seu valor e não na sua posição;
# .pop(): remove da lista_compras o último item, mas não o exclui.

'''Como criar uma lista do zero no Python?
Podemos também criar uma lista do zero e trazer itens de outras listas para dentro dele com a utilização do pop que vai pegar essa informação e armazenar em outra variável.

Outra opção para criar uma lista é utilizar a função input para que o próprio usuário possa inserir as informações de forma manual através de uma caixa!

# Criando a lista tarefas
tarefas = []

# Usando o Input() vamos coletar do usuário qual a tarefa a ser adicionada.

atividade = input('Insira uma atividade: ')

#Adiciona a tarefa indicada pelo usuário a lista de tarefas

tarefas.append(atividade)
Insira uma atividade: Curtir o video de listas da Hashtag

print(tarefas)
['Curtir o video de listas da Hashtag']
Inserindo vários itens na lista
Outra forma de criar uma lista é utilizando o while + input, então até que a informação da caixa de entrada seja vazia o programa irá armazenar as informações em uma lista.

while atividade:
   atividade = input(Insira uma atividade: ')
   tarefas.append(atividade)
Insira uma atividade: Me inscrever no canal da Hashtag
Insira uma atividade: Fazer o download do minicurso de Python
Insira uma atividade: Compartilhar o vídeo da Hashtag
Insira uma atividade
A estrutura abaixo indica que pegará os itens da posição [0] até o penúltimo item da lista [-2]:

print(tarefas[:-2])
['Curtir o video de listas da Hashtag', 'Me inscrever no canal da Hashtag', 'Fazer o download do minicurso de Python']
Já no exemplo a seguir temos a utilização da estrutura FOR para percorrer todos os elementos e fazer o print de cada um deles.

for tarefa in tarefas:
   print(tarefa)
Curtir o video de listas da Hashtag
Me inscrever no canal da Hashtag
Fazer o download do minicurso de Python
Compartilhar o vídeo da Hashtag
Criando uma lista com valores numéricos
Até agora todas nossas listas foram compostas por textos, mas é possível ter listas com valores numéricos.

Claro que não podemos criar listas apenas com textos, podemos ter valores armazenados, mas como foi mostrado no exemplo é importante saber o que vai fazer para não ter problemas!

Pois, nesse exemplo temos duas listas em uma determinada ordem e ao utilizar o sort para ordenar elas, essa sequência é desfeita, então a ordem inicial foi modificada.

Então se você estava pegando cada nome e relacionando ao número pela posição isso não poderá mais ser feito. No exemplo abaixo temos 3 lojas e seu volume em vendas.

lojas = ['Rio de Janeiro','São Paulo', 'Curitiba']
vendas = [10000, 20000, 50000]
O .sort() ordena os valores do maior para o menor. Atenção: as duas listas não estão conectadas.

lojas.sort()
vendas.sort()
Perceba que ao mudarmos a ordem, não temos mais a Rio de Janeiro -> 10000 / São Paulo -> 20000 / Curitiba -> 50000:

print(lojas)
print(vendas)
['Curitiba', 'Rio de Janeiro', 'São Paulo']
[10000, 20000, 50000]
Unindo listas no Python
Para unir duas listas podemos simplesmente utilizar o símbolo de +:

print(lojas+vendas)
['Curitiba', 'Rio de Janeiro', 'São Paulo', 10000, 20000, 50000]
Não é o que queremos. Vamos tentar inverter a ordem:

print(lojas+vendas)
['Curitiba', 'Rio de Janeiro', 'São Paulo', 10000, 20000, 50000]
Ainda não é o que queremos. Neste caso unir as listas com o símbolo de + não atende a nossa necessidade, pois queremos relacionar o nome ao valor!

Já estamos quase finalizando, agora vamos a uma parte importante: utilizar um Tupla para unir listas e conseguir relacionar o nome ao valor.

## Unindo listas com tupla

Tupla é um objeto assim como as listas. Ao invés de usarmos o [] usaremos () para criar uma dupla.

No exemplo, precisamos relacionar o nome ao valor, e com a Tupla será possível fazer a união das listas dessa forma.

Utilizando o for para passar por todos os elementos como vimos anteriormente vamos conseguir esse resultado, mas veja, que precisamos colocar o elemento i primeira lista e o elemento i da segunda lista.

Dessa forma temos uma tupla que nada mais é do que do que um objeto que nos permite armazenar várias informações associadas.

Neste caso estamos armazenando a loja com a sua respectiva venda para que essas informações fiquem sempre vinculadas.

Veja o código com o processo descrito acima:

lojas = ['Rio de Janeiro','São Paulo', 'Curitiba']
vendas = [10000,20000,50000]
resultados=[]
Usando range para rodar o for. i é uma variável auxiliar que irá percorrer a posição 0, 1 e 2 da nossas listas. Range(3) indica serem 3 iterações:

for i in range(3):
   tupla=(lojas[i],vendas[i])
   resultados.append(tupla)
print(resultados)
[('Rio de Janeiro', 10000), ('São Paulo', 20000), ('Curitiba', 50000) ]
Para finalizar vamos te mostrar como acessar um item dentro dessa tupla, pois temos um argumento a mais do que temos na lista.

O primeiro é a posição do conjunto e depois será a posição no conjunto, então nesse exemplo temos resultados [1][0].

Isso significa que vamos pegar o conjunto na posição 1 que é referente a São Paulo e 20000. Em seguida pegamos a posição 0 desse conjunto, que corresponde ao nome São Paulo.

Ou seja, primeiro informamos o conjunto que vamos analisar e em seguida qual elemento queremos desse conjunto!

print(resultados[1][0])
São Paulo
Ao fazermos resultados[1][0] acessamos o primeiro item da tupla, ou seja: São Paulo,

Resumo dos principais operadores de lista
Para que você não se perca em meio a tanta informação, resumimos aqui os principais operadores de listas Python.

## Acessar os dados de uma lista (operador [])
A expressão dentro dos colchetes é o índice. Lembre-se de que o índice do primeiro elemento é 0. Na nossa lista de compras:

print(lista_compras[1])

laranja

## Concatenar lista Python (operador +)

Em um exemplo, [2, 4, 6] + [3, 5] retorna [2, 3, 4, 5, 6]

## Multiplicação (operador *)

Esse operador repete (replica) uma lista diversas vezes. Se multiplicarmos nossa lista_compras por 3, teremos:

[‘banana’,’laranja’,’maçã’,’banana’,’laranja’,’maçã’,’banana’,’laranja’,’maçã’]

## Descobrindo o tamanho das listas Python (operador len() )

A função len() retorna a quantidade de elementos existentes. Na nossa lista_compras, teríamos:

print(len(lista_compras))

3

## Verificando a existência de itens nas listas Python (operador in)

Esse operador percorre todos os itens e retorna “True”, se houver equivalência, e “False”, se não houver o valor. Veja:

lista_compras = [‘banana’,’laranja’,’maçã’]

‘banana’ in lista_compras

True

‘mamão’ in lista_compras

False

## Descobrindo os valores Mínimos, Máximos e Soma (operadores min(), max() e sum())

Veja o exemplo com uma lista numérica:

numeros = [1, 3, 5, 7, 9]

print(min(numeros))

#Resultado: 1

print(max(numeros))

#Resultado: 9

print(sum(numeros))

#Resultado: 25

Veja outros métodos de listas Python importantes

extend: serve para prolongar a lista, pois adiciona no fim todos os elementos do argumento iterable passado como parâmetro.
index: devolve o índice base-zero do primeiro item cujo valor é igual a x. Se o valor não existir, o retorno será ValueError.
count: retorna o número de vezes em que um elemento aparece na lista.
sort: coloca em ordem alfabética os itens na lista.
reverse: inverte a ordem dos elementos na lista.
copy: devolve uma cópia rasa da lista.
clear: remove todos os itens da lista.'''
