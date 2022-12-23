## CONDIÇÕES ANINHADAS

#OBS==> ESTUDAR ANÁLISE DE ALGORITMO E ANÁLISE ASSINTÓTICA => BIG O Notation

# if carro.esquerda():
#      bloco1
# elif carro.direita():
#      bloco2
# elife carro.ré():
#      bloco3
#else:
#      bloco4

nome = str(input('Qual é seu nome? '))
if nome == 'Marcelo':
    print('Que nome lindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Helena Sófia Jéssica Júlia':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))