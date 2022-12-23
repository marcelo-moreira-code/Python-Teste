## CONDIÇÕES SIMPLES, COMPOSTAS E SIMPLIFICADA
#carro.siga()
#se carro.esquerda()
#   carro.siga()       | BLOCO VERDADEIRO
#   carro.direita()    |
#   carro.siga()       |
#   carro.direita()
#   carro.esquerda()
#   carro.siga()
#   carro.direita()
#   carro.siga()
#senão
#   carro.siga()
#   carro.esquerda()
#   carro.siga()
#   carro.esquerda()
#   carro.siga()
#carro.pare()

# indetação na tecla TAB --- Condição ou estrutura condicional
# Numa Condição ou o bloco True é executado ou o bloco False é executado. Nunca serão executados os dois!
#se carro.esquerda()        if carro.esquerda():
#     bloco_V_                 bloco True
#senão                      else:
#     bloco_F_                   bloco False
#ex:
#tempo = int(input('Quantos anos tem seu carro?'))
#if tempo <= 3:
#    print('Carro Novo')
#else:
#    print('Carro Velho')
#print('--Fim--')

# Condição Simplificada - invés da parte de cima
#tempo = int(input('Quantos anos tem seu carro? '))
#print('carro novo' if tempo <= 3 else 'carro velho')
#print('--FIM--')

# A estrutura Condicional Simples é formada somente pela parte if .
# Já uma estrutura Condicional Composta possui tanto o if quanto o else e elife
'''nome = str(input('Qual seu nome? '))
if nome == 'Marcelo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão feio!')
print('Bom dia, {}!'.format(nome))'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {:.1f}'.format(m))
'''if m >= 6.0 :
    print('Sua média foi boa! Parabêns')
else:
    print('Sua média foi ruim! Estude Mais')'''
print('Parabêns' if m >= 6 else 'Estude Mais')
















#n = str(input('Escreva seu nome completo: ')).strip()
#print('Analisando seu nome ....')
#print('Seu nome em maiúsculas é {}'.format(n.upper()))
#print('Seu nome em minúsculas é {}'.format(n.lower()))
#print('O seu nome possui um total de {} letras.'.format(len(n)-n.count(' ',0,)))
#s = n.split()
#print('O seu primeiro nome possui {} letras.'.format(len(s[0])))
