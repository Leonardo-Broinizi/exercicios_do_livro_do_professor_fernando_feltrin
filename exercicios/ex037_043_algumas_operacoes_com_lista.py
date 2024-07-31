# ex037 f'string:

'''nome = str(input('Digite o seu nome: ')).strip()
print(f'Olá, {nome}!')'''

# ex038 Operação dentro da máscara de substituição (com f'string):

'''n = int(input('Digite um número: '))
print(f'O quadrado de {n} é {n**2}.')'''

# ex039 Substituição de ítem de uma lista:

'''lista = ['Ana', 'Carlos', 'Daiane', 'Fernando', 'Maria']
print(lista)
lista[2] = 'Jamile'
print(lista)'''

# ex040 Adicionando elementos ao fim da lista:

'''lista = ['Ana', 'Carlos', 'Jamile', 'Fernando', 'Maria']
print(lista)
lista.append('Paulo') # Se o método 'extend' fosse utilizado (ou o uso de lista += 'Paulo'), cada digito do elemento (Paulo, nesse exemplo) seria adicionado como um novo elemento, ficando assim nesse exemplo: ['Ana', 'Carlos', 'Jamile', 'Fernando', 'Maria', 'P', 'a', 'u', 'l', 'o'].
print(lista)'''

# ex041 Adicionando elementos em qualquer posição da lista (com o uso do método INSERT):

'''lista = ['Ana', 'Carlos', 'Jamile', 'Fernando', 'Maria']
print(lista)
lista.insert(2,'Eliana') # Primeiro declaro o índice (nesse caso, 2), depois o dado/valor a ser inserido ('Eliana').
print(lista)'''

# ex042 Removendo ítens em qualquer posição na lista pelo seu nome (e não pelo índice) com o método REMOVE):

'''lista = ['Ana', 'Carlos', 'Eliana', 'Jamile', 'Fernando', 'Maria']
print(lista)
lista.remove('Carlos')
print(lista)

# Minha modificação do exercício para ver se poderia usar uma variável contendo o nome que precisaria ser removido (e confirmei que sim): 
lista = ['Ana', 'Carlos', 'Eliana', 'Jamile', 'Fernando', 'Maria']
print(lista)
nome = 'Jamile'
lista.remove(nome)
print(lista)'''

# ex043 Exibindo apenas determinados índices da lista:

'''lista = ['Ana', 'Carlos', 'Eliana', 'Jamile', 'Fernando', 'Maria']
print(lista[1:4])
print(lista[-1])'''
