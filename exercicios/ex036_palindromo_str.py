# Minha resolução:

nome = str(input('Digite uma frase para saber se é ou não palíndromo: ')).upper().strip().replace(' ', '')
invertido = ''
for i in range(len(nome) -1, -1, -1):
    invertido += nome[i]
print(invertido)
print('Essa frase é um palíndromo!' if nome == invertido else 'Essa frase não é um palíndromo!')

# Resolução do professor Feltrin:

'''frase = str(input('Digite uma palavra ou frase: ')).strip().upper()

palavras = frase.split()
caracteres = ''.join(palavras) # lembrando que 'join' é um método que substitui todos os espaços em branco pelo que estiver destro das aspas (se não tiver nada lá dentro, ele elimina esses espaços).
fraseinvertida = ''

for i in range(len(caracteres) -1, -1, -1):
    fraseinvertida += caracteres[i]

print(caracteres, fraseinvertida)

if fraseinvertida == caracteres:
    print('É um palíndromo!!!')
else:
    print('Não é um palíndromo...')'''
