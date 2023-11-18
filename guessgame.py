import random
from tkinter import *
from tkinter import messagebox 
import time

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

class JogoEducacional:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Jogo Educacional")
        self.janela.configure(bg="black")
        self.janela.geometry("800x600")  # Cor de fundo preta

        self.pontuacao = 0
        self.pontos_por_pergunta = 10
        self.pergunta_atual = None
        self.resposta_correta = None
        self.perguntas_feitas = 0

        self.iniciar_jogo()

    def iniciar_jogo(self):
        self.label_pergunta = Label(self.janela, text="Pergunta:", font=("Arial", 12), fg="white", bg="black")
        self.label_pergunta.pack()

        self.entry_resposta = Entry(self.janela)
        self.entry_resposta.pack()

        self.botao_resposta = Button(self.janela, text="Responder", command=self.verificar_resposta)
        self.botao_resposta.pack()

        self.label_resultado = Label(self.janela, text="", fg="white", bg="black")
        self.label_resultado.pack()

        self.label_hora = Label(self.janela, text="", font=("Arial", 12), fg="white", bg="black")
        self.label_hora.pack()

        self.nova_pergunta()

    def nova_pergunta(self):
        if self.perguntas_feitas < len(perguntas_respostas):
            self.pergunta_atual, self.resposta_correta = random.choice(list(perguntas_respostas.items()))
            self.label_pergunta.config(text=self.pergunta_atual)
            self.entry_resposta.delete(0, END)
            self.botao_resposta.config(state="active")
        else:
            self.finalizar_jogo()

    def verificar_resposta(self):
        resposta = self.entry_resposta.get()
        if str(resposta).strip().lower() == str(self.resposta_correta).strip().lower():
            self.pontuacao += self.pontos_por_pergunta
            self.label_resultado.config(text="Resposta correta! Parabéns!", fg="green")
        else:
            self.label_resultado.config(text=f"Resposta incorreta. A resposta correta é: {self.resposta_correta}", fg="red")
        self.botao_resposta.config(state="disabled")
        self.perguntas_feitas += 1
        self.janela.after(2000, self.nova_pergunta)

    def finalizar_jogo(self):
        self.label_pergunta.config(text=f"Fim do jogo! Sua pontuação final é: {self.pontuacao} pontos")
        self.botao_resposta.config(state="disabled")
        messagebox.showinfo("Fim do jogo", f"Sua pontuação final é: {self.pontuacao} pontos")

    def atualizar_hora(self):
        hora_atual = time.strftime("%H:%M:%S")
        self.label_hora.config(text=hora_atual)
        self.janela.after(1000, self.atualizar_hora)

if __name__ == "__main__":
    janela = Tk()
    jogo = JogoEducacional(janela)
    jogo.atualizar_hora()  # Iniciar a atualização da hora
    janela.mainloop()