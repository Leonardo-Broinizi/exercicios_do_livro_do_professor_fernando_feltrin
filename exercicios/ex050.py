#    Enunciado: Crie um programa de perguntas e respostas que interage com o usuário, pedindo que o mesmo insira uma resposta.
# Caso a primeira questão esteja correta, exiba em tela uma mensagem de acerto e parta para a próxima pergunta,
# caso incorreta, exiba uma mensagem de erro e pule para a próxima pergunta:

#   Minha primeira versão:

'''pr = {'Quem descobriu a América? ' : 'Cristovão Colombo', 'Quem descobriu o Brasil? ' : 'Pedro Álvares Cabral', 'Em qual ano o Brasil foi descoberto? ': '1500', 'Qual é o ano da proclamação da República Federativa do Brasil? ': '1889'}
acertos = 0
for respostas in pr.keys():
    r = str(input(respostas)).strip()
    if r == pr[respostas]:
        print('Resposta certa!')
        acertos += 1
    else:
        print('Restosta errada!')
print(f'Você acertou {acertos} questões!')'''

#   Minha segunda versão:


#   Código do professor Feltrin: 