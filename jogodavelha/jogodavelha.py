
import numpy as np

def verificador_X(array,jogador_X):
    if array.all == jogador_X :
        return True
    else:
        return False
    
def verificador_O(array,jogador_O):
    if array.all == jogador_O:
        return True
    else:
        return False
    
def update(pos_linha,pos_coluna,valor):
    jogo_da_velha[pos_linha,pos_coluna] = valor
    return jogo_da_velha


jogador_X = 'X'
jogador_O = 'O'
jogo = True


jogo_da_velha = np.array([
    ['a','b','c'],
    ['d','e','f'],
    ['g','h','i']
])
qtd_linhas, qtd_colunas = jogo_da_velha.shape



while(jogo):
    linha = int(input("Digite a linha: "))
    coluna = int(input("Digite a coluna: "))
    valor = input("Digite X ou O: ")
    jogo_da_velha = update(linha,coluna,valor)
    print(jogo_da_velha)
    for linha in range(0, qtd_linhas):
        array= jogo_da_velha [linha, :]
        if verificador_X(array, jogador_X):
                print(f"Linha {linha}")
                print("Jogador X ganhou!!!")
                jogo = False
        else:
            print(jogo_da_velha)
    for coluna in range(0,qtd_colunas):
        array= jogo_da_velha[:, coluna]
        if verificador_X(array,jogador_X):
            print(f"Coluna {coluna}")
            jogo = False
        else:
            print("")
    for linha in range(0, qtd_linhas):
        array = jogo_da_velha[linha, :]
        if verificador_O(array, jogador_O):
            print(f"Linha {linha}")
            print("Jogador O ganhou!!!")
            print(jogo_da_velha)
            jogo = False
        else:
            print(jogo_da_velha)
    for coluna in range(0,qtd_colunas):
        array = jogo_da_velha[:, coluna]
        if verificador_O(array,jogador_O):
            print(f"Coluna {coluna}")
        else:
            print(jogo_da_velha)

