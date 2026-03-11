import tkinter as tk # interfaces gráficas padrão do Python (ele que desenha a janela, as caixas de texto e os botões).
from tkinter import messagebox # responsavel pelos pop-ups, 
# No Python, alguns submódulos não são carregados automaticamente quando você importa a biblioteca "mãe" 
# para poupar recursos. Por isso, precisamos ser explícitos

# uma matriz (tabela) de 9 linhas por 9 colunas, totalmente preenchida com zeros (Tabuleiro SUDOKU)
grid = [[0 for _ in range(9)] for _ in range(9)] 

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

def solve(): # Preenche todos os espaços do nosso tabuleiro
    global grid
    
    # Varre a matriz toda procurando um espaço vazio (0)
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                
                # Encontrou um vazio, tenta os números de 1 a 9
                for n in range(1, 10):
                    if possible(y, x, n): # chama a função de verificação
                                                
                        grid[y][x] = n # O programa faz o palpite a lápis: grid[y][x] = z.
                        
                        if solve(): # Aqui o programa "pausa" a execução atual e cria uma cópia de si mesmo (uma nova chamada de solve).
                                    # Essa nova chamada vai olhar para o tabuleiro atualizado e tentar preencher a PRÓXIMA casa vazia.
                                    # Se essa nova chamada (e todas as outras depois dela) conseguirem preencher o tabuleiro até o fim,
                                    # ela retornará True. Se recebermos True de volta, repassamos esse True para cima.
                            return True
                        
                        
                        grid[y][x] = 0 # Se o código chegou nesta linha, significa que o 'if solve():' logo acima falhou (retornou False).
                                       # Ou seja: o nosso palpite 'n' até parecia certo no começo, mas gerou um beco sem saída lá na frente.
                                       # Então, pegamos a borracha e desfazemos a nossa ação lá em cima. A casa volta a ser zero (vazia).
                                       # O laço 'for n in range(1, 10)' vai girar novamente para tentar o próximo número possível.
                
                return False # Este return fica FORA do laço de 1 a 9.
                             # Se o programa tentou colocar o 1 (apagou), o 2 (apagou), até o 9 (apagou)... 
                             # Significa que é impossível preencher esta casa com a configuração atual do tabuleiro.
                
    # Se passou por todos os loops e não encontrou nenhum 0, está resolvido!
    return True
                
def resolver_clicado():
    # Passo A: Ler os dados para a matriz 'grid'
    for y in range(9):
        for x in range(9): # Visitar as 81 posições possiveis
            valor = celulas_gui[y][x].get() # Extrai o que o usuário digitou na interface
            if valor.isdigit() and valor != "": # Tratamento de erros para verificar se é número
                grid[y][x] = int(valor) # Armazena e converte para inteiro o que o usuario digitou
            else:
                grid[y][x] = 0 # Considera o resto como vazio, para depois ser completado pelo nosso algoritmo

    # Passo B: Chamar o algoritmo
    if solve(): # "Execute o algoritmo. Se a resposta final dele for Verdadeira (resolvido), entre no bloco abaixo".
        for y in range(9):
            for x in range(9): # Usamos fors para visitar as 81 caixinhas novamente da interface
                # Limpa a caixinha atual
                celulas_gui[y][x].delete(0, tk.END) # Apaga o que o usuário digitou para depois o algoritmo escrever
                                                    # de "caneta" e evitar que fique "55"
                # Insere o número descoberto pelo algoritmo
                celulas_gui[y][x].insert(0, str(grid[y][x])) # Coloca o número na interface
    else:
        # Se retornar False, avisa o utilizador
        messagebox.showerror("Erro", "Este Sudoku não tem solução possível!")

# 1. Cria a janela principal do aplicativo
janela = tk.Tk()
janela.title("Sudoku Solver")
janela.geometry("400x450") # Largura x Altura

# 2. Criamos uma matriz vazia para guardar as "caixinhas de texto"
# Atenção: Esta matriz guarda os elementos visuais, NÃO os números do jogo!
celulas_gui = [[None for _ in range(9)] for _ in range(9)]

# 3. Desenhando as 81 caixinhas na tela
for y in range(9):
    for x in range(9):
        # Cria uma caixa de entrada (Entry) na janela
        # width=2 deixa a caixa estreita, ideal para 1 número
        caixa = tk.Entry(janela, width=2, font=('Arial', 18), justify='center')
        
        # O sistema .grid() do Tkinter é perfeito para o Sudoku
        # Ele posiciona cada caixa exatamente na linha 'y' e coluna 'x'
        caixa.grid(row=y, column=x, pady=2, padx=2)
        
        # Guarda essa caixinha na nossa matriz visual para podermos acessá-la depois
        celulas_gui[y][x] = caixa

# Criar o botão que dispara tudo
botao_resolver = tk.Button(janela, text="Resolver Sudoku", command=resolver_clicado, font=('Arial', 14))
botao_resolver.grid(row=9, column=0, columnspan=9, pady=20) # Fica na linha abaixo do tabuleiro

# 4. Mantém a janela aberta rodando em loop
janela.mainloop()