#frase = 'Curso em Vídeo Python'
#         0123456789........   21
#print(frase.replace('Python','Android'))
#print(frase.split())

## FATIAMENTO de string -- serve para pegar pedaços da str

# [] - é identificador de uma estrutuda de dados chamada -> LISTAS

#frase[9] -- para pegar uma  variável - letra
#print(frase[9:13]) - inclui o 9 e exclui o 13./ex2. [9:] começa no 9 e vai até o fim da str/ ex3. [:13] pega toda a str até o 12 , pois ela exclui o último
#print(frase[:9])
#print(frase[1:])
#print(frase[9:21])
#print(frase[9::3]) -> começa no 9 e vai até o final da str pu7lando de 3 em 3.
#print(frase[2:20])
#print(frase[1:21:2]) -- mostra o 1 e vai até o 20 pulando de dois em dois
#print(frase[9:]) -- quando não se sabe o final da str , deixa com o final :

## ANÁLISE de str --[qual é o tamanho da str , com que letra começa , que letra términa , qual a primeira palavra inteira , etc...]

# FUNÇÃO len() ~tamanho da str~ mostra qts elementos a str possui-vazios ou não- comprimento da str - len(frase)
# FUNÇÃO count('') ~~ conta quantas vezes um elemento está repetido dentro do intervalo especificado('o'0,20)
#print(frase.count('o'))
#print(frase.count('o',0,20)) -> o intervalo analisado é de 0 a 20->inclui 0 início e exclue 20 final.
#obs - caso não saiba o final do intervalo deixa vazio -- ('o',0,) que irá contar até o final da str
#print(len(frase))
#print(frase[9::2])-- começa no 9 e vai até o fim pulando de dois em dois
# FUNÇÃO-starswith('')--print(frase.startswith('P')) -startswith- para testar se começa com um determinado elemento resulta True or False
# FUNÇÃO-endswith('')--print(frase.endswith('n')) - .endswith('') - para testar se términa com um determinadop elemento tbm True or False
# FUNÇÃO  find() --  ele encontra algo dento de uma str --  'onde começou' -- quando/se ele retornar um nºnegativo -1 é pq não existe dentro dessa str
#print(frase.find('deo'))-> ele encontra o início em que começa , ou seja na posição 11
#print(frase.find('Android')) -> qnd se coloca 'um valor que não existe na str' ele retorna -1
#print(frase.find('P'))
#print('Curso' in frase) --- tbm pode usar -in- para testar se existe-> ele retorna True ou False

## TRANSFORMAÇÃO - 'via de regra uma lista de str é imutável'

#pode-se mudá-la através de métodos
# FUNÇÃO replace() -- substitui
#print(frase.replace('Python','Android'))
# FUNÇÕES - upper/lower() - tudo maiúsculo/minúsculo
#print(frase.upper())
#print(frase.lower())
# FUNÇÃO - .capitalize() -- só o primeiro str ficará maiúsculo e o resto da str minúsculo
#print(frase.capitalize())
# FUNÇÃO - .title() -- analisa palavras a str e deixa (Maiúsculas as iniciais das palavras)
#print(frase.title())

#frase2 = ('    Aprenda Python    ')
#print(frase2)
# FUNÇÃO .strip() -- para REMOVER ESPAÇOS VAZIOS excedentes/em branco 'inúteis'
#print(frase2.strip())
# FUNÇÃO  .rstrip()/.lstrip() -- remove  espaços vazios da direita/ esquerda
#print(frase2.rstrip())
#print(frase2.lstrip())


## DIVISÃO ou 'fatiamente de str'

# FUNÇÃO - .split() -- gera uma lista com novas cadeias de caracteres
#frase.split()-> ele gera tecnicamente uma lista com todas as palavras de uma cadeia de caracteres
#print(frase2.split())
# FUNÇÃO - .join() -- juntar um coisa na outra ~~~~! não entendi essa função !~~
#´-`.join(frase)-> ele tbm pode desfazer uma lista que foi feita split - juntando os elementos , mas, colocando um - entre os elementos
#Curso-em-Vídeo-Python
#print(''.join(frase2)) --? dá pra fazer um espaçamento das letras nas palvras da frase danto um ou dois espaços''
#print('  '.join(frase2))
#print(frase2[::-1]) -- inverte a ordem da str - lendo-a de trás pra frente
n = '  Marcelo Estuda Japonês  '
# LISTAS / TUPLAS / DICIONÁRIOS
#print(n[::-1])
#print(len(n))
#print(len(n.strip()))
#print((n.rstrip()))
#print(n.replace('Japonês','Python'))
s = n.split()
#print(s[1][4])
#print(len(s[2]))
print(s[0])
print(s[-1])