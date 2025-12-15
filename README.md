🎰 Desafio 36 – Cassino “A casa sempre ganha”

Disciplina: BI679 – Processamento de Informação
Período: 2025.2

📌 Descrição do Projeto

Este projeto consiste na simulação de um caça-níquel de 3 símbolos, desenvolvido em Python, com o objetivo de demonstrar conceitos de probabilidade, processamento de informação e simulação computacional.

O jogo foi implementado com interface gráfica, permitindo ao usuário jogar rodada por rodada ou simular todas as rodadas automaticamente até o encerramento do jogo.

O nome do desafio reflete o comportamento estatístico do sistema: na maioria das simulações, a casa tende a ganhar, embora o jogador possa eventualmente atingir o prêmio máximo.

🎰 Símbolos do Jogo e Probabilidades

O caça-níquel possui 5 símbolos, cada um com uma probabilidade específica de ocorrência:

Símbolo	Probabilidade
🪙 Moeda	50%
💀 Caveira	20%
7️⃣ Número 7	10%
🍒 Cereja	10%
✖️2 Símbolo 2X	10%

Cada rodada sorteia 3 símbolos de forma aleatória, respeitando essas probabilidades.

💰 Regras do Jogo
🎲 Custo e saldo inicial

Cada giro custa R$ 1

O jogador inicia o jogo com R$ 100

🏆 Premiações
Combinação	Prêmio
3 Moedas	R$ 3
3 números 7	R$ 7
3 Cerejas	R$ 30
Par + 1 símbolo 2X	Dobra o prêmio da trinca correspondente
Par de cerejas ou par de 7	R$ 1 (jogada free)

Exemplo:

2 Moedas + 1 símbolo 2X → prêmio de R$ 6

⚠️ Observações Importantes

Qualquer símbolo de caveira na rodada resulta em perda da rodada

Se ocorrerem 2 símbolos 2X, a rodada é automaticamente perdida

Rodadas perdidas não geram prêmio

🛑 Condições de Encerramento do Jogo

O jogo é encerrado automaticamente quando:

O saldo do jogador chega a R$ 0 (jogador perde), ou

O saldo do jogador atinge R$ 200 ou mais (jogador vence)

Ao final, o sistema informa:

Quantidade total de rodadas jogadas

Saldo final

Resultado do jogo (vitória ou derrota)

🖥️ Interface Gráfica

O projeto possui uma interface gráfica desenvolvida com Tkinter, contendo:

Exibição visual dos símbolos do giro (emojis)

Saldo atual do jogador

Contador de rodadas

Botão para jogar uma rodada

Botão para simular todas as rodadas automaticamente

Botão para reiniciar o jogo

A interface permite tanto o uso interativo quanto a análise estatística do comportamento do jogo.

🧠 Objetivo Acadêmico

Este projeto tem como objetivos principais:

Aplicar conceitos de probabilidade

Simular sistemas aleatórios

Trabalhar lógica condicional e controle de fluxo

Analisar o comportamento estatístico de jogos de azar

Demonstrar por simulação o conceito de que, no longo prazo, a casa tende a ganhar

▶️ Execução do Projeto

Certifique-se de ter o Python 3 instalado

Salve o arquivo do jogo (ex: cassino.py)

Execute no terminal:

python cassino.py

📊 Considerações Finais

Apesar de o jogador poder ganhar em algumas simulações, a estrutura de probabilidades e regras favorece o cassino, validando o conceito central do desafio. O projeto demonstra de forma prática como sistemas probabilísticos podem ser analisados através de simulação computacional.
