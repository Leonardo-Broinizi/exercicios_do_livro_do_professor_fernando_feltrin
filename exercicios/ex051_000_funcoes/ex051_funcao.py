#    ex051: Crie uma função de nome 'funcao1', que por sua vez não realiza nenhuma ação:
#    Obs.: Eu não sabia nem isso, então apenas copiei o resultado do livro.
#    Obs.2: Voltei depois de um tempo, e já aprendi algumas coisas sobre funções
# em Python, então agora ficou mais fácil rs.:
#    Ex. 51 e 52:
'''def funcao1():
    pass

var1 = funcao1()

#    Ex. 53 e 54:
def funcao2():
    print('Bem-vindo!')
    return 0

var2 = funcao2()

print(var2)

#    Ex. 55:
def funcao3(nome):
    print(f'Seja bem-vindo(a) {nome}!')

n = str(input('Digite seu nome: '))
funcao3(n)
print(n)'''

#    Ex. 56:
'''def quadrado(n):
    print(n ** 2)

num = float(input('Digite um número para saber o seu quadrado: '))
quadrado(num)'''

#    Ex. 57:
'''def nomeCompleto(nome, sobrenome):
    print(f'Seja bem-vindo(a) {nome} {sobrenome}!')

nome = str(input('Digite seu primeiro nome: '))
sobrenome = str(input('Digite seu sobrenome: '))
nomeCompleto(nome, sobrenome)'''

#    Ex. 58:
'''def calcula(n1, n2=5):
    print(n1 * n2)

num = int(input('Digite um número: '))
calcula(num)'''

#    Ex. 59:
'''def boasVindas(nome, nacionalidade='Brasileiro', sobrenome='Farias'):
    print(f'Seja bem-vindo(a) {nome} {sobrenome}, {nacionalidade}!')

nome1 = str(input('Digite seu nome: '))
boasVindas(nome1)'''

#    Ex. 60:
'''def pontos(*n):
    for c in n:
        print(f'{c}')



pontos(4,5,3,23,1,32,66)'''

#    Ex. 61:
'''def somador(*n):
    soma = 0
    for c in n:
        soma += c
    print(f'A soma dos números {n} é: {soma}')

somador(1, 4, 8, 3, 5, 2, 9, 6)'''

#    Ex. 62:
'''def func(*args, **kwargs):
    kwargs['dois'] = 22
    print(f'args: {args}, type(args): {type(args)}\nkwargs: {kwargs}, type(kargs): {type(kwargs)}')

func(1,3,5,7,9, dois=2,quatro=4,seis=6,oito=8)'''

