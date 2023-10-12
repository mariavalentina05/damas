import pygame
import sys
 
# Defina as constantes
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
 
# Defina as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
 
# Classe para representar as peças
class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.is_king = False
 
    def move(self, row, col):
        self.row = row
        self.col = col
 
    def make_king(self):
        self.is_king = True
 
    def draw(self, win):
        pass  # Implemente a lógica para desenhar a peça na tela aqui
        width=round(WIDTH / 8)
        pygame.draw.circle(win, self.color, ( self.col*width +width/2, self.row*width+width/2), width/2)

 
# Classe para representar o tabuleiro
class Board:
    def __init__(self):
        self.board = [[None] * COLS for _ in range(ROWS)]
 
    def create_pieces(self):
        pass  # Implemente a lógica para criar as peças iniciais no tabuleiro aqui
        for i in range (3): #i = y
            for j in [0, 2, 4 ,6]: # j= y
                if (i)%2==0:
                    self.board[i][j+1] = Piece(i,j+1,RED)
                else :
                    self.board[i][j] = Piece(i,j,RED)

        for i in range (3): #i = y
            for j in [0, 2, 4 ,6]: # j= y
                if (i)%2==1:
                    self.board[5+i][j+1] = Piece(5+i,j+1,BLUE)
                else :
                    self.board[5+i][j] = Piece(5+i,j,BLUE)
                    
 
    def draw_squares(self, win):
        pass  # Implemente a lógica para desenhar os quadrados do tabuleiro aqui
        width=round(WIDTH / 8)
        for i in range (8): #i = y
            for j in range (8): # j= y 
                cor= WHITE if (i+j)%2==0 else BLACK
                pygame.draw.rect(win,cor, (j*width, i*width, width, width))

    def draw_pieces(self, win):
        pass  # Implemente a lógica para desenhar as peças no tabuleiro aqui
        for rowPieces in self.board:
            for piece in rowPieces:
                if piece != None:
                    piece.draw(win)
        
    def select(self, row, col):
        pass  # Implemente a lógica para selecionar uma peça no tabuleiro aqui
 
    def move(self, piece, row, col):
        pass  # Implemente a lógica para mover uma peça no tabuleiro aqui
        #chama o valid pra ver se pode
        self.board[piece.row][piece.col] = None
        piece.move(row, col)
        self.board[row][col] = piece
 
    def is_valid_move(self, piece, row, col):
        pass  # Implemente a lógica para verificar se um movimento é válido aqui
 
    def remove(self, piece):
        pass  # Implemente a lógica para remover uma peça do tabuleiro aqui
        self.board[piece.row][piece.col] = None

    def is_winner(self, color):
        pass  # Implemente a lógica para verificar se um jogador ganhou aqui
        #validar as regras de jogo finzaliado
 
# Função principal
def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jogo de Damas")
 
    board = Board()
    board.create_pieces()
 
    selected_piece = None
 
    running = True
    movimentoRealizado = False
    playerAtualColor = RED
    ##qual player ta jogaqqndo red ou blue
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #faria um while pra esperar até o cara selecionar uma peça dele que pode jogar
            if event.type == pygame.MOUSEBUTTONDOWN:
                col = event.pos[0] // SQUARE_SIZE
                row = event.pos[1] // SQUARE_SIZE,
                #busca em board.board alguma peça com essas posições
            #     pieceTemp = board.board[col][row]
            #     if pieceTemp != None and pieceTemp.color == playerAtualColor:
            #         selected_piece = pieceTemp
            #     #jogar pra selectedPiece a peca selecioanda com o mause
            #     # Implemente a lógica de seleção de peça aqui
            # if selected_piece != None:
            #     # Implemente a lógica de movimentação da peça aqui
            #     selected_piece.move(1,1)
            #     movimentoRealizado = True
            # if movimentoRealizado:
            #     selected_piece = None
            #     board.is_winner(playerAtualColor)
            #     playerAtualColor = BLUE if playerAtualColor == RED else RED
        
        win.fill(WHITE)
        board.draw_squares(win)
        board.draw_pieces(win)
        pygame.display.update()

    pygame.quit()
    sys.exit()
 
if __name__ == "__main__":
    main()