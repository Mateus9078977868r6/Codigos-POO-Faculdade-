# Criação do tabuleiro inicial do Sudoku (0 representa os espaços vazios)
grid = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]
def possible(y, x, n):

    # Toda vez que eu ler ou alterar algo no grid aqui dentro desta função, não crie uma cópia nova. 
    # Use exatamente aquele mesmo tabuleiro que definimos lá fora no início do programa.
    global grid

    # 1. Verifica a linha 'y'
    for i in range(0, 9): # Inicia um loop (laço) que vai se repetir 9 vezes.
        if grid[y][i] == n: # fixa a busca na linha y (onde jogaremos)
                            # como o i está mudando de 0 até 8 por causa do for, 
                            # o código vai olhar, uma por uma, para todas as colunas daquela linha y.
            return False 
            # Se o loop terminar todas as 9 voltas de 0 a 8 e nunca acionar o return False, significa que o número n não está na linha y. 
            # Aí o código passa para o próximo teste (que é verificar a coluna).
            
    # 2. Verifica a coluna 'x'
    for i in range(0, 9):
        if grid[i][x] == n:
            return False
             # Se o loop terminar todas as 9 voltas de 0 a 8 e nunca acionar o return False, significa que o número n não está na coluna x. 
            # Aí o código passa para o próximo teste (que é verificar o quadrante).
    
    # 3. Verificação do quadrante 3x3
    # O Sudoku é um grande 9x9 que é dividido em 9 blocos menores 3x3
    # Para verificar todas as posições do bloco 3x3 em que estamos, o computador precisa descobrir onde fica o
    # canto superior esquerdo (posição inicial)
    # Se a coluna atual for 0, 1 ou 2, o bloco dela começa na coluna 0...
    # A fórmula (x // 3) * 3 é como o Python força os números a "caírem" sempre no 0, no 3 ou no 6.
    # Ex: O código faz: 8 // 3 = 2. 2*3=6
    
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    
    #Verificação da "matriz" 3x3 
    for i in range(0, 3): #explorador de linhas
        for j in range(0, 3): #explorador de colunas
            if grid[y0 + i][x0 + j] == n: # Se em qualquer um desses 9 quadradinhos o número que estiver lá for igual ao nosso palpite n
                return False # Pode parar, esse número já existe dentro desse bloco 3x3!
                
    # Se passou por todas as verificações, Pode colocar o número n nessa casinha, pois ele obedece a todas as regras
    return True

def solve():
    global grid
    
    # Varre a matriz toda procurando um espaço vazio (0)
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                
                # Encontrou um vazio, tenta os números de 1 a 9
                for n in range(1, 10):
                    if possible(y, x, n): # chama a função de verificação
                        
                        # Na Casinha A, os números 1 e 2 são movimentos válidos (a função possible retorna True).
                        # Na Casinha B, apenas o número 1 é um movimento válido. Mas lembre-se: no Sudoku, não podemos ter números repetidos 
                        
                        grid[y][x] = n # O programa faz o palpite a lápis: grid[y][x] = 1.
                        
                        # Chama a si mesma para o próximo espaço vazio
                        solve() # Ele testa o n = 1. A função possible diz False (pois a Casinha A já está 
                                # usando o 1 e elas estão no mesmo bloco).
                        
                        # BACKTRACKING: Se a chamada acima não resolveu até o fim 
                        # e retornou para cá, o palpite 'n' estava errado.
                        # Então, resetamos a casa para 0 e o loop for tenta o próximo 'n'.
                        grid[y][x] = 0 # O programa executa: grid[y][x] = 0. Ele apaga o '1' da Casinha A.
                
                # Se tentou de 1 a 9 e nenhum deu certo, volta um passo atrás (retorna)
                return
                
    # Se os loops terminarem sem achar nenhum 0, o Sudoku está resolvido
    print("Sudoku Resolvido:")
    for row in grid:
        print(row)

# Inicia a execução do programa
solve()