#  Ex045

'''catálogo = dict(Chuteira = '311,40', Bola_oficial = '159,99', Camisa_da_Seleção = '349,99', Meião = '30,99',Bermuda = '65,99')
print(catálogo.get('Chuteira', 'Objeto não encontrado!'))
catálogo['Bermuda'] = '139,00'
print(catálogo)'''


# Ex046
# Minha solução:

'''lista = ['C','JavaScript','Lua','Python']
if 'Python' in lista:
    print('A linguagem Python consta na lista.')'''

# Solução do livro:

'''linguagens = ['C','JavaScript','Lua', 'Python']
for i in linguagens:
    if i == 'Python':
        print('Python é parte da lista')
    else:
        pass'''

# Ex 047
# Minha tentativa malsucedida:

dicionário = {'Alto Nível':'Python', 'Médio Nível':'C', 'Baixo Nível':'Assembly'}
if 'Python' in dicionário:
    print('Python consta no dicionário.')


#    Resolução do livro (não entendi muito a validade desse código, já que,
# se o ítem buscado não estivesse em primeiro lugar nos valores do dicionário, o programa enviaria
# a cada laço uma mensagem negando a existência de um código negando que o item se encontra no objeto
# para, quando o encontrar, afirmar que sim, ele se encontra no dicionário. Estou levando em  consideração
# que é apenas um exercício. Mesmo assim, acho estranho.

'''d = {'Alto Nível':'Python',
     'Médio Nível':'C',
     'Baixo Nível':'Assembly'}
for i in d.values():
    if not i == 'Python':
        print(f'Python não consta na lista')
    else:
        print(f'Python consta na lista')
        break'''

# Ex 47:

'''lista1 = ['Corínthians', 'Ral Madrid', 'River Plate', 'Milan']
lista2 = ['Brasileirão', 'La Liga', 'Argentino', 'SerieA']
dicionário = dict(keys = lista1, values = lista2)
print(dicionário)
print(type(dicionário))'''

#   Ex 48:

'''cadastro = { 'Nome':'Almeida',
             'Idade':22,
             'Sexo':'Masculino',
             'Estado Civil':'Divorciado',
             'Nacionalidade':'Brasileiro',
             'Faixa de Renda':'3000.00 - 5000.00'}
print(cadastro)'''

#   Ex 49:
#   Minha tentativa:

'''aluno = {'Nome':'João',
         'Primeiro Trimestre':7.6,
         'Segundo Trimestre':9,
         'Terceiro Trimestre':7.2}
média = {'Nome':' ',
         'Média':0}
m = 0
for i in aluno.values():
    if type(i) == float or type(i) == int:
        m += i
print(m/3)'''

#   Resolução do livro:

aluno = [{'Nome':'Fernando','Notas':[62,73,90]}]

def calcula_media(aluno):
    notas = []
    for media in aluno:
        if len(media['Notas']) > 0:
            temp = round(sum(media['Notas']))/len(media['Notas'])
        else:
            temp = 0
        notas.append({'Nome':media['Nome'],'Média das notas':temp})
    print(notas)
    print(type(notas), type(aluno))

media_estudante = calcula_media(aluno)

