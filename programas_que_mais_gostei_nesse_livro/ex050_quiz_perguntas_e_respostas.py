#    Enunciado: Crie um programa de perguntas e respostas que interage com o usuário, pedindo que o mesmo insira uma resposta.
# Caso a primeira questão esteja correta, exiba em tela uma mensagem de acerto e parta para a próxima pergunta,
# caso incorreta, exiba uma mensagem de erro e pule para a próxima pergunta:

#   Minha primeira versão:

pr = {'Quem descobriu a América? ' : 'Cristovão Colombo', 'Quem descobriu o Brasil? ' : 'Pedro Álvares Cabral', 'Em qual ano o Brasil foi descoberto? ': '1500', 'Qual é o ano da proclamação da República Federativa do Brasil? ': '1889'}
acertos = 0
for respostas in pr.keys():
    r = str(input(respostas)).strip()
    if r == pr[respostas]:
        print('Resposta certa!')
        acertos += 1
    else:
        print('Restosta errada!')
print(f'Você acertou {acertos} questões!')

#   Minha segunda versão (mais caprichada):
#   Obs.: Não apenas pelo capricho, mas gostei mais desse meu segundo código até do que do
# código do professor Feltrin.


print('\033[1m' + '\033[34m-\033[33m=' * 21 + '\033[34m-')
print(f'{'\033[31m> > > \033[35mQUIZ DE HISTÓRIA \033[31m< < <':^59}')
print('\033[34m-\033[33m=' * 21 + '\033[34m-\n')
pr = {'1 - Quem descobriu o Brasil?': ['A: Pero Vaz de Caminha', 'B: Luís de Camões', 'C: Cristóvão Colombo', 'D: Pedro Álvares Cabral'],
      '2 - Quem descobriu a América?': ['A: Pedro Américo', 'B: Cristóvão Colombo', 'C: Pedro Álvares Cabral', 'D: Simón Bolívar'],
      '3 - Nome de nossa terra atribuído por algumas tribos indígenas, no período anterior à chegada dos portugueses ao Brasil:' : ['A: Terra do Pau Brasil', 'B: Terra dos Papagaios', 'C: Pindorama', 'D: Terra de Santa Cruz'],
      '4 - Quando foi firmado o Tradado de Tordesilhas?' : ['A: 1 de janeiro de 1593', 'B: 7 de junho de 1494', 'C: 22 de abril de 1500', 'D: 12 de outubro de 1492'],
      '5 - Qual a data do dia do "Fico", dia em D. Pedro I declarou que não cumpriria as ordens das Cortes portuguesas?': ['A: 9 de janeiro de 1822', 'B: 9 de janeiro de 1832', 'C: 9 de janeiro de 1722', 'D: 9 de janeiro de 1852'],
      '6 - Em que ano foi assinada a Lei Áurea no Brasil?' : ['A: 1889', 'B: 1888', 'C: 1788', 'D: 1887'],
      '7 - Onde ocorreu a Guerra dos Canudos?' : ['A: Interior de São Paulo, entre os anos de 1896 e 1899', 'B: Interior da Bahia, entre os anos de 1896 e 1897', 'C: Interior do Rio de Janeiro, entre os anos de 1897 e 1899', 'D: Interior do Rio Grande do Sul, entre os anos de 1896 e 1899'],
      '8 - Quem foi Napoleão Bonaparte?' : ['A: Imperador francês', 'B: Imperador português', 'C: Imperador polonês', 'D: Imperador grego'],
      '9 - Os principais povos da Mesopotâmia, foram: ' : ['A: Sumérios, Caldeus, Babilônios e Assírios', 'B: Ostrogodos, Burgúndios, Hunos e Visigodos', 'C: Persas, Fenícios, Cananeus e Hititas', 'D: Gregos, Romanos, Gauleses e Cretenses'],
      '10 - Em que ano ocorreu a Revolução Constitucionalista?' : ['A: 1939', 'B: 1833', 'C: 1922', 'D: 1932']}

from time import sleep
gabarito = ('D', 'B', 'C', 'D', 'A', 'B', 'B', 'A', 'A', 'D')
pontos = 0
for c, perguntas in enumerate(pr):
    print(f'\033[36m{perguntas}\n')
    sleep(2)
    print(f'\033[m\033[1m{pr[perguntas][0]}')
    sleep(0.6)
    print(pr[perguntas][1])
    sleep(0.6)
    print(pr[perguntas][2])
    sleep(0.6)
    print(pr[perguntas][3])
    sleep(0.6)
    while True:
        res = str(input(f'\n\033[33mResposta: ')).strip().upper()
        if res not in 'ABCD':
            print('\n\033[31mResposta inválida! Tente novamente.')
        else:
            break
    print('\033[32mAnalisando...')
    sleep(1)
    if res == gabarito[c]:
        print('\033[m\033[1mParabéns, resposta \033[34mCORRETA!\n')
        sleep(1)
        pontos += 1
    else:
        print('\033[m\033[1mQue pena, resposta \033[31mERRADA!\n')
        sleep(1)
print(f'\033[33mVocê acertou {pontos} de 10 questões.')
if pontos < 5:
    print('\033[31mPontuação baixa. Estude mais para melhorar sua pontuação.')
elif pontos < 7:
    print('\033[32mPontuação regular. Estude mais um pouco para melhorar sua pontuação.')
elif pontos < 10:
    print('\033[36mPontuação alta. Parabéns! Com mais um pouco de estudos você pode conseguir 10.')
else:
    print('\033[34mPARABÉNS, você acertou tudo!')



#   Código do professor Feltrin:

base = {
    'Pergunta 01 ': {
        'pergunta':' Quanto é 4 X 4 ?',
        'alternativas':{'a':'12','b':'24','c':'16','d':'20'},
        'resposta_certa':'c',
    },
    'Pergunta 02 ' :{
        'pergunta':' Quanto é 6 / 3 ? ',
        'alternativas':{'a':'2','b':'1','c':'3','d':'4'},
        'resposta_certa':'a',
    },
}

respostas_certas = 0

for pkeys, pvalues in base.items():
    print(f'{pkeys}:{pvalues['pergunta']}')

    for rkeys, rvalues in pvalues['alternativas'].items():
        print(f'[{rkeys}]: {rvalues}')

    resposta = input('Escolha uma alternativa: [a],[b],[c] ou [d]')

    if resposta == pvalues['resposta_certa']:
        print('Resposta Correta!!!')
        respostas_certas += 1
    else:
        print('Resposta Incorreta!!!')

if respostas_certas == 0:
    print('Você não acertou nenhuma questão.')
elif respostas_certas == 1:
    print('Você acertou apenas uma questão.')
else:
    print('Você acertou todas as questões.')
