#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import tkinter as tk

# ===========================
# Configuração dos símbolos
# ===========================
simbolos = ["moeda", "caveira", "sete", "cereja", "2x"]
pesos = [0.5, 0.2, 0.1, 0.1, 0.1]

icones = {
    "moeda": "🪙",
    "caveira": "💀",
    "sete": "7️⃣",
    "cereja": "🍒",
    "2x": "✖️2"
}

# ===========================
# Estado do jogo
# ===========================
saldo = 100
rodadas = 0

# ===========================
# Funções do jogo
# ===========================
def girar():
    return random.choices(simbolos, pesos, k=3)

def calcular_premio(giro):
    if "caveira" in giro or giro.count("2x") >= 2:
        return 0

    moeda = giro.count("moeda")
    sete = giro.count("sete")
    cereja = giro.count("cereja")
    doisx = giro.count("2x")

    if moeda == 3:
        return 3
    if sete == 3:
        return 7
    if cereja == 3:
        return 30

    if doisx == 1:
        if moeda == 2:
            return 6
        if sete == 2:
            return 14
        if cereja == 2:
            return 60

    if sete == 2 or cereja == 2:
        return 1

    return 0

def atualizar_tela(giro=None):
    saldo_label.config(text=f"Saldo: R$ {saldo}")
    rodada_label.config(text=f"Rodadas: {rodadas}")

    if giro:
        simbolos_label.config(
            text="   ".join(icones[s] for s in giro)
        )

def verificar_fim():
    if saldo >= 200:
        status_label.config(text="🎉 Você ganhou!", fg="green")
        return True
    if saldo <= 0:
        status_label.config(text="💀 Você perdeu!", fg="red")
        return True
    return False

# ===========================
# Ações dos botões
# ===========================
def jogar_uma():
    global saldo, rodadas
    if verificar_fim():
        return

    saldo -= 1
    rodadas += 1

    giro = girar()
    premio = calcular_premio(giro)
    saldo += premio

    atualizar_tela(giro)
    verificar_fim()

def simular_tudo():
    while saldo > 0 and saldo < 200:
        jogar_uma()

def reiniciar():
    global saldo, rodadas
    saldo = 100
    rodadas = 0
    simbolos_label.config(text="🎰 🎰 🎰")
    status_label.config(text="", fg="black")
    atualizar_tela()

# ===========================
# Interface gráfica
# ===========================
janela = tk.Tk()
janela.title("Caça-Níquel")
janela.geometry("400x350")

tk.Label(janela, text="🎰 Caça-Níquel", font=("Arial", 18)).pack(pady=10)

saldo_label = tk.Label(janela, text="Saldo: R$ 100", font=("Arial", 12))
saldo_label.pack()

rodada_label = tk.Label(janela, text="Rodadas: 0", font=("Arial", 12))
rodada_label.pack()

simbolos_label = tk.Label(janela, text="🎰 🎰 🎰", font=("Arial", 30))
simbolos_label.pack(pady=15)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text="Jogar 1 rodada", command=jogar_uma, width=15).grid(row=0, column=0, padx=5)
tk.Button(frame_botoes, text="Simular tudo", command=simular_tudo, width=15).grid(row=0, column=1, padx=5)

tk.Button(janela, text="🔄 Reiniciar", command=reiniciar).pack(pady=10)

status_label = tk.Label(janela, text="", font=("Arial", 14))
status_label.pack(pady=10)

janela.mainloop()

