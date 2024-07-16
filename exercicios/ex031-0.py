# Ex 031, minha tentativa:
'''pt = int(input('Digite o primeiro termo da Progressão Aritmética: '))
razão = int(input('Agora digite a razão: '))
for i in range(pt, 20, razão-1):
    print(i)

# Resolução do livro:
termo =  int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: ' ))

pa = termo + (20 - 1) * razão

for i in range(termo,pa + razão, razão):
    print(i)


# Ex32:
n = int(input('Digite um número para saber sua tabuada: '))
x = 1
for i in range(10):
    print(n, ' x ', x, ' = ', n * x)
    x += 1

# Ex33, enunciado: Crie um programa que realiza a contagem regressiva de 20 segundos:

from time import sleep
for i in range(20, -1, -1):
    print(i)
    sleep(1)
print('Contagem Terminada!!!')

#Ex 34
c = s = 0
for i in range(101):
    if i%2 == 1:#No livro, o cálculo realizado é 'i % 3 == 0', o que daria no final 33 números no intervalo proposto. Mas o enunciado pediu números ímpares, e não apenas múltiplos de 3. Foi um equívoco.
        print(i)
        c += 1
        s += i

print(f'Entre 1 e 100 foram encontrados {c} números ímpares.\nA soma de todos esses números é: {s}.')


# Ex 35, enunciado: Crie um programa que pede ao usuário que o mesmo digite um número qualquer,
#em seguida retorne se esse número é primo ou não, caso não, retorne também quantas vezes ele é divisível:
p = 0
base = n = int(input('Digite um número para saber se é primo ou não: '))
while base >= 1:
    if n%base == 0:
        p += 1
    base -= 1
if p == 2:
    print(f'{n} é um número primo.')
else:
    print(f'{n} não é um número primo, é divisível {p} vezes.')

# resolução do livro:

numero = int(input('Digite um número: '))
divisoes = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisoes += 1

if divisoes == 2:
    print(f'{numero} é primo!!!')
    print(f'{numero} é divisível por 1 ou por {numero}')
else:
    print(f'{numero} não é primo!!!')
    print(f'{numero} é divisível {divisoes} vezes...')
'''


