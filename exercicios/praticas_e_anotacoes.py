#   Daqui até a linha ? eu fiz para testar se como era possível colocar listas e dicionários
# dentro de dicionários.

lista1 = ['Corínthians', 'Ral Madrid', 'River Plate', 'Milan']
lista2 = ['Brasileirão', 'La Liga', 'Argentino', 'SerieA']
d = {'Alto Nível':'Python',
     'Médio Nível':'C',
     'Baixo Nível':'Assembly'}

cadastro = { 'Nome':'Almeida',
             'Idade':22,
             'Sexo':'Masculino',
             'Estado Civil':'Divorciado',
             'Nacionalidade':'Brasileiro',
             'Faixa de Renda':'3000.00 - 5000.00'}

dicionários_recebem_quaisquer_dados_incluindo_listas_e_outros_dicionários = {'lista1':lista1,'lista2':lista2, 'Cadastro':cadastro}
print(dicionários_recebem_quaisquer_dados_incluindo_listas_e_outros_dicionários)