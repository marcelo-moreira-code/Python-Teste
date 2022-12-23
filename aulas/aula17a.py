### Listas

#num = (2,4,6,8)
#num[0] = 0
#print(num)

#num = [3,1,9,7,5]
#num[1] = 11
#num[5] = 13   # para adicionar um elemento no final da lista  .append()
#num.append(13)
#num.sort() # coloca em ordem numérica / alfabética
#num.sort(reverse=True)  # inverte a ordem
#print(num)
#num.insert(0, 15) # colocar um elem. numa posição específica .insert(posição, elemento)
#print(num)
#num.pop() # remove o último elemnto da lista  .pop()
#print(num)
#num.pop(2) # tbm remove pelo index indicado
#print(num)
#print(f'Essa lista tem {len(num)} elementos.')
#num.insert(1, 7)
#if 4 in num:
#    num.remove(2)
#else:
#    print('Não achei o número 4')

#print(num)
#num.remove(7) # remove do inícia da lista o primeiro elemento que ele achar
#print(num)

'''valores = []
valores.append(1)
valores.append(3)
valores.append(5)

#for v in valores:
#    print(f'{v}...', end='')


for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''


'''valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')'''

### Cuidado com as listas     duplicação /  cópia

'''a = [2, 3, 4, 7]
b = a # Cria um ligação entre as duas listas , assim , se uma for alterada, as duas são modificadas
b = a[:] # Faz uma cópia da lista a , e fica independente de a / podendo alterá-la
b[2] = 5 # Ao alterar um elemento de uma lista que foi Igualada a outra, o Python faz uma ligação entre elas
# Assim, ao alterar um elemento em uma das listas, acaba-se alterando das duas listas
print(f'A lista A: {a}')
print(f'A lista B: {b}')'''

### 6 tips for loops

## 1) Don't use loops at all

'''
numbers = [10,20,30,40,50,60]
result = 0
for num in numbers:
    result += num

print(result)

result = sum(numbers)
print(result)'''

## 2) Use enumerate

'''numbers = [13,15,24,16,50]

#for index in range(len(numbers)):
#    print(index, numbers[index])

for index , valor in enumerate(numbers):
    print(index, valor)'''

## 3) Use zip

'''# Essa abordagem pode dar muita merda , se uma das listas tiver mais elementos que a outra!
a = [1,2,3]
b = ['a','b','c']

for index in range(len(a)):
    print(a[index], b[index])'''

'''a = [1,2,3,4]
b = ['a','b','c']
#for index in range(len(a)):
#    print(a[index], b[index])
#
for val1 , val2 in zip(a, b): # Para ver o erro nesse arg : for val1,val2 in zip(a, b, strict=True)
    print(val1 , val2)'''

## 4) Think lazy! Use a generator

'''events = [('learn', 5), ('learn', 10), ('relaxed', 20)]
minutes_studied = 0
for event in events:
    if event[0] == 'learn':
        minutes_studied += event[1]
print(minutes_studied)
#
study_times = (event[1] for event in events if event[0] == 'learn')
minutes_studied = sum(study_times)
print(minutes_studied)'''

# 5) Use itertools

'''lines = ['line1','line2','line3','line4','line5','line6','line7','line8','lin9','line10']

for i, line in enumerate(lines):
    if i >= 5:
        break
    print(line)

print()

#for itertools import islice

first_five_lines = islice(lines, 5)

for line in first_five_lines:
    print(line)'''

