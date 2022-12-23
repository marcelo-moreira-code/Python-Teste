# CORES NO TERMINAL
#\033[STYLE;TEXT;BACK
#EX: \033;33;44m

#STYLE                         TEXT(cor da letra)    BACK(cores de fundo)
# 0 none(nenhum)               30 white              40
# 1 bold(negrito)              31 red                41
# 4 underline(sublinhado)      32 green              42
# 7negative(inverte)           33 yellow             43
#                              34 blue               44
#                              35 purple             45
#                              36 ciano              46
#                              37 gray               47

# PARA CANCELAR AS CORES  BASTA     \033[m
#print('\033[34;40mOlá pessoal , bom dia a todos !\033[m')
a = 4
b = 6
c = a+b
#print('A soma de {}{}{} + {}{}{} é igual a {}{}{}.'.format('\033[34;40m',a,'\033[m','\033[33;40m',b,'\033[m','\033[31;40m',c,'\033[m'))
cores = {'limpa':'\033[m',
         'blue':'\033[34m',
         'red':'\033[31m',
         'green':'\033[32m',
         'yellow':'\033[33m'}

print('Oi, bom dia {} minha Deusa!{}'.format(cores['yellow'],cores['limpa']))