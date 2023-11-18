import random
from tkinter import *

perguntas_respostas = {
    "Quanto é 2 + 2?": 4,
    "Qual é a raiz quadrada de 9?": 3,
    "Quanto é 5 x 8?": 40,
    "Quanto é 12 / 3?": 4,
    "Quem proclamou a independência do Brasil em 1822?": "Dom Pedro I",
    "Em que ano a República foi proclamada no Brasil?": 1889,
    "Quem liderou a Revolução Constitucionalista de 1932?": "M.M.D.C",
    "Quem e o professor de pca da turma 2 unigranrio turma ADS?": "professor Oswaldo",
    "Quem e o atual presidente do Brasil?": "LUIS INACIO LULA DA SILVA",
    "Normalmente, quantos litros de sangue uma pessoa tem? Em média, quantos são retirados numa doação de sangue?" : "450 mililitros",
    "De quem é a famosa frase Penso, logo existo?": "Descartes",
    "De onde é a invenção do chuveiro elétrico?": "Brasil",
    "Quais o menor país do mundo": "Vaticano",
    "Qual o nome do presidente do Brasil que ficou conhecido como Jango?": "João Goulart",
    "Quantas casas decimais tem o número pi?": "Infinitas",
    "Qual o número mínimo de jogadores em cada time numa partida de futebol?": 7,
}

def fazer_pergunta():
    pergunta, resposta_correta = random.choice(list(perguntas_respostas.items()))
    print(pergunta)
    resposta = input("Sua resposta: ")
    
    if str(resposta).strip().lower() == str(resposta_correta).strip().lower():
        print("Resposta correta! Parabéns!\n")
        return True
    else:
        print("Resposta incorreta. A resposta correta é:", resposta_correta, "\n")
        return False

def jogar_jogo():
    pontuacao = 0
    numero_de_perguntas = 7
    
    print("Bem-vindo ao Jogo Educacional!")
    
    for _ in range(numero_de_perguntas):
        if fazer_pergunta():
            pontuacao += 1
    
    print("Fim do jogo! Sua pontuação final é:", pontuacao, "de", numero_de_perguntas)

jogar_jogo()





