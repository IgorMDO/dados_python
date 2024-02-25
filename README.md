# Interpolação de dados

# declaração de variáveis e atribuição de valores
nome = input('Insira o seu nome: ')
idade = input('Digite a sua idade: ')
sal = input('Digite seu salário: ')

# conversão de dados
idade = int(idade)
sal = float(sal)

# saída de dados via interpolação

#com S-Strings
print(f'O seu nome é {nome}, sua idade é {idade} anos e seu salário é igual a R$ {sal}.')

#com %
print('O seu nome é %s, sua idade é de %i anos e o seu salário é de R$%.2f' %(nome, idade, sal))
