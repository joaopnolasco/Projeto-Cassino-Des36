# 🎰 Desafio 36 – Cassino “A casa sempre ganha”

**Disciplina:** BI679 – Processamento de Informação  
**Período:** 2025.2  

---

## 📌 Descrição do Projeto

Este projeto consiste na simulação de um **caça-níquel de 3 símbolos**, desenvolvido em **Python**, com o objetivo de aplicar conceitos de **probabilidade, processamento de informação e simulação computacional**.

O jogo possui uma **interface gráfica**, permitindo que o usuário jogue rodada por rodada ou simule automaticamente todas as rodadas até o encerramento do jogo.

O título do desafio reflete o comportamento estatístico do sistema: no longo prazo, **a casa tende a ganhar**, embora o jogador possa eventualmente atingir o prêmio máximo.

---

## 🎰 Símbolos e Probabilidades

O caça-níquel utiliza cinco símbolos, cada um com uma probabilidade específica de ocorrência:

| Símbolo | Probabilidade |
|-------|---------------|
| 🪙 Moeda | 50% |
| 💀 Caveira | 20% |
| 7️⃣ Número 7 | 10% |
| 🍒 Cereja | 10% |
| ✖️2 Símbolo 2X | 10% |

Cada rodada sorteia **3 símbolos aleatórios**, respeitando essas probabilidades.

---

## 💰 Regras do Jogo

### 🎲 Custo e saldo inicial
- Cada giro custa **R$ 1**
- O jogador inicia com **R$ 100**

---

### 🏆 Premiações

| Combinação | Prêmio |
|----------|--------|
| 3 Moedas | R$ 3 |
| 3 números 7 | R$ 7 |
| 3 Cerejas | R$ 30 |
| Par + 1 símbolo 2X | Dobra o prêmio da trinca correspondente |
| Par de cerejas ou par de 7 | R$ 1 (jogada free) |

**Exemplo:**  
2 Moedas + 1 símbolo 2X → prêmio de **R$ 6**

---

### ⚠️ Observações

- A presença de **qualquer caveira** resulta em perda da rodada
- Se ocorrerem **dois símbolos 2X**, a rodada é automaticamente perdida
- Rodadas perdidas não geram prêmio

---

## 🛑 Condições de Encerramento

O jogo é encerrado quando:

- O saldo do jogador chega a **R$ 0**, ou
- O saldo do jogador atinge **R$ 200 ou mais**

Ao final, o sistema informa:
- Total de rodadas jogadas
- Saldo final
- Resultado do jogo (vitória ou derrota)

---

## 🖥️ Interface Gráfica

A interface gráfica foi desenvolvida com **Tkinter** e apresenta:

- Exibição visual dos símbolos do giro
- Saldo atual do jogador
- Contador de rodadas
- Botão para jogar uma rodada
- Botão para simular todas as rodadas automaticamente
- Botão para reiniciar o jogo

---

## 🧠 Objetivo Acadêmico

O projeto busca:

- Aplicar conceitos de probabilidade
- Simular sistemas aleatórios
- Utilizar estruturas condicionais e laços de repetição
- Analisar o comportamento estatístico de jogos de azar
- Demonstrar, por meio de simulação, que a casa possui vantagem no longo prazo

---

## ▶️ Execução do Projeto

1. Certifique-se de ter o **Python 3** instalado
2. Salve o arquivo do jogo (exemplo: `cassino.py`)
3. Execute no terminal:

```bash
python cassino.py
