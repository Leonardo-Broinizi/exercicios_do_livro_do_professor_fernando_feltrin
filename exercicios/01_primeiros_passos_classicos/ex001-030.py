# Esses exercícios iniciais do livro são bem simples, por isso não realizarei todos,
#já que algumas práticas apresentam temas que já domino.

nome = 'Leonardo'
ano = 1991
valor = 19.91

# Isso é o exercício 2, um comentário simples

'''Isso é o exercício 3, um comentário mais complexo,
podendo usar mais linhas só com o símbolo inicial de três aspas, que, 
assim como no caso anterior, da forquilha, o que estiver dentro das aspas será ignorado
(no caso da forquilha, basta estar na frente dela'''

""""Também pode ser feito com três aspas duplas"""


'''num = int(input('Digite um número: ')) # Ex008
num = float(num)
print(num,type(num))

nome_idade = ['Leonardo',32,'Thais',32,'Matheus',7, 'Giovanna',0, 'Julia',13]
print(nome_idade[4:7]) # Exercício 009, que me fez atentar ao fato de que uma lista pode conter elementos de vários tipos (str, int, float)

nome = ['Leonardo','Thais','Matheus', 'Giovanna', 'Julia']# Ex010
print(len(nome),nome[2])

num1 = 103
num2 = 89
print(num1 > num2) # Ex017, gerará True

# Ex021: Duas formas de escrever uma estrutura condicional composta:
num1 = 100
num2 = 89
print(num1 <= 100 and num2 <= 100)
print(num1 and num2 <= 100)

# Ex023, enunciado: Verifique se o valor de num1 consta nos elementos de lista1. 
Sendo num1 = 100 e lista = [10, 100, 1000, 10000, 100000]

num1 = 100
lista1 = [10,100,1000,10000,100000]
print(num1 in lista1) # O operador 'in' nos é útil para verificar se um determinado dado/valor consta dentro de uma variável/objeto.

# Ex027, enunciado: Cria uma estrutura de repetição que percorra a string 'Nikola Tesla',
# exibindo em tela letra por letra desse nome:
for i in 'Nikola Tesla':
    print(i)
# Aqui fiz uso pela primeira vez (que me lembre) da estrutura de repetição 'for'.
lista = ['arroz','feijão','leite','ovos','pão','sabonete','macarrão','banana']
for i in lista:
    print(i)

# Ex029, enunciado: Crie um programa que lê um valor de início e um valor de fim,
#exibindo um tela a contagem dos números dentro desse intervalo.
# Minnha tentaviva:
vi = int(input('Digite o valor inicial: '))
vf = int(input('Digite o valor final: '))
while vi <= vf:
    print(vi)
    vi += 1
#A resolução do livro:
início = int(input('Digite a número onde começa a contagem: '))
fim = int(input('Digite o número onde termina a contagem: '))
for i in range(início, fim + 1):
    print(i)
#Eu não consegui usar a estrutura 'for'. Preciso treinar a função 'range' e o laço 'for'.

# Ex030, enunciado: Crie um programa que realiza a contagem de 0 a 20,
#exibindo apenas números pares:
# Minha tentativa:
for i in range(0, 20, 2):
    print(i)
# Resolução do livro:
for i in range(0, 21):
    if i % 2 == 0:
        print(i)
# Segunda resolução do livro (se parece com a minha):
for i in range(0, 21, 2):
    print(i)'''

