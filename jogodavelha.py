
import numpy as np
jogador = 2
vit = 0

jogo_da_velha =[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]


def tela():
    print(   "   0  "  " 1  "   "  2 " )
    print ("0: " + jogo_da_velha[0][0] + " | " + jogo_da_velha[0][1]+ " | " + jogo_da_velha[0][2]+ " | ")
    print(   "-----------")
    print ("1: " + jogo_da_velha[1][0] + " | " + jogo_da_velha[1][1]+ " | " + jogo_da_velha[1][2]+ " | ")
    print(   "-----------")
    print ("2: " + jogo_da_velha[2][0] + " | " + jogo_da_velha[2][1]+ " | " + jogo_da_velha[2][2]+ " | ")
    print(   "-----------")


def jogador1(jogador):
    
    if jogador ==1 :
        print("Jogada do jogador X")
        print("--------")
        l= int(input("Digite a linha: "))
        c= int(input("Digite a coluna: "))
    try:
        while jogo_da_velha[l][c] != " ":
            print("Linha e/ou coluna preenchida")
            l= int(input("Digite a linha: "))
            c= int(input("Digite a coluna: "))
        jogo_da_velha[l][c]="X"
    except:
        print("Linha e/ou coluna invalida")

def jogador2(jogador):
    
    if jogador ==2 :
        print("Jogada do jogador O")
        print("--------")
        l= int(input("Digite a linha: "))
        c= int(input("Digite a coluna: "))
    try:
        while jogo_da_velha[l][c] != " ":
            print("Linha e/ou coluna preenchida")
            l= int(input("Digite a linha: "))
            c= int(input("Digite a coluna: "))
        jogo_da_velha[l][c]= "O"
    except:
        print("Linha e/ou coluna invalida")

def vitoria():
    if jogo_da_velha[0][0] == "X" and jogo_da_velha[0][1]== "X" and jogo_da_velha [0][2] == "X":
        print("Jogador X ganhou!!")
        vit+=1

    if jogo_da_velha[0][0] == "O" and jogo_da_velha[0][1]== "O" and jogo_da_velha [0][2] == "O":
        print("Jogador O ganhou!!")
        vit+=2
    
    if jogo_da_velha[1][0] == "X" and jogo_da_velha[1][1]== "X" and jogo_da_velha [1][2] == "X":
        print("Jogador X ganhou!!")
        vit+=1

    if jogo_da_velha[1][0] == "O" and jogo_da_velha[1][1]== "O" and jogo_da_velha [1][2] == "O":
        print("Jogador O ganhou!!")
        vit+=2
    
    if jogo_da_velha[2][0] == "X" and jogo_da_velha[2][1]== "X" and jogo_da_velha [2][2] == "X":
        print("Jogador X ganhou!!")
        vit+=1

    if jogo_da_velha[2][0] == "O" and jogo_da_velha[2][1]== "O" and jogo_da_velha [2][2] == "O":
        print("Jogador O ganhou!!")
        vit+=2

    if jogo_da_velha[0][0] == "X" and jogo_da_velha[1][1]== "X" and jogo_da_velha [2][2] == "X":
        print("Jogador X ganhou!!")
        vit+=1
    
    if jogo_da_velha[0][0] == "O" and jogo_da_velha[1][1]== "O" and jogo_da_velha [2][2] == "O":
        print("Jogador O ganhou!!")
        vit+=2 
    
    if jogo_da_velha[0][2] == "X" and jogo_da_velha[1][1]== "X" and jogo_da_velha [2][0] == "X":
        print("Jogador X ganhou!!")
        vit+=1
    
    if jogo_da_velha[0][2] == "O" and jogo_da_velha[1][1]== "O" and jogo_da_velha [2][0] == "O":
        print("Jogador O ganhou!!")
        vit+=2

while True:
    tela()
    jogador1(1)
    jogador2(2)
    vit = vitoria()
    if(vit==1) or(vit==2):
        break
    
