import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Definir tamanho do tabuleiro
TAMANHO_TABULEIRO = 800
TAMANHO_QUADRADO = TAMANHO_TABULEIRO // 8

# Definir peças
PECAS = {
    "R": "Torre",
    "N": "Cavalo",
    "B": "Bispo",
    "Q": "Rainha",
    "K": "Rei",
    "P": "Peão"
}

# Definir movimentos válidos
MOVIMENTOS_VALIDOS = {
    "R": [(1, 0), (-1, 0), (0, 1), (0, -1)],
    "N": [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)],
    "B": [(1, 1), (-1, -1), (1, -1), (-1, 1)],
    "Q": [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)],
    "K": [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)],
    "P": [(1, 0), (-1, 0), (0, 1), (0, -1)]
}

# Definir tabuleiro
tabuleiro = [
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-", "-"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["r", "n", "b", "q", "k", "b", "n", "r"]
]

# Definir jogador atual
jogador_atual = "Branco"

# Definir verificar check
verificar_check = False

# Definir verificar checkmate
verificar_checkmate = False

# Criar janela
janela = pygame.display.set_mode((TAMANHO_TABULEIRO, TAMANHO_TABULEIRO))

# Definir fonte
fonte = pygame.font.SysFont("Arial", 24)

# Função para desenhar tabuleiro
def desenhar_tabuleiro():
    janela.fill(BRANCO)
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 1:
                pygame.draw.rect(janela, PRETO, (j * TAMANHO_QUADRADO, i * TAMANHO_QUADRADO, TAMANHO_QUADRADO, TAMANHO_QUADRADO))

# Função para desenhar peças
def desenhar_pecas():
    for i in range(8):
        for j in range(8):
            if tabuleiro[i][j] != "-":
                texto = fonte.render(tabuleiro[i][j], True, PRETO)
                janela.blit(texto, (j * TAMANHO_QUADRADO + 20, i * TAMANHO_QUADRADO + 20))

# Função para validar movimentos
def validar_movimento(x1, y1, x2, y2):
    if tabuleiro[x1][y1] == "-":
        return False
    if tabuleiro[x2][y2] != "-" and tabuleiro[x2][y2].isupper() == tabuleiro[x1][y1]:
