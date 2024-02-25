# Operadores lógicos And, Or, Not pt1 - And

# x > y > z  --> x==z
x = input('Insira o primeiro valor: ')
y = input('Insira o segundo valor: ')
z = input('Insira o  terceiro valor: ')

#nome = input('Digite o seu nome: ')
x, y, z = int(x), int(y), int(z)

#bloco condicional
if x>y and y>z:
    print('sequência de ordem decrescente inserida')
elif x<y and y<z:
    print('Sequência de ordem crescente digitada') 
else:
    print('Outra sequência que não ordem crescente ou decrescente')
       
#fora do condicional
print('%i, %i, %i.' %(x, y, z))
