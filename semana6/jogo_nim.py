# Funções principais:
def computador_escolhe_jogada(n, m):
    # A jogada ideal consiste no maior número menor
    # ou igual a m e múltiplo de m+1. Caso contrário
    # escolher o maior número possível.
    jogada = m
    # Escolher múltiplo:
    while jogada > 0:
        if (n-jogada) % (m+1) == 0:
            return jogada
        else:
            jogada -= 1
    # Escolher maior número:
    if m < n:
        return m
    else:
        return n

def usuario_escolhe_jogada(n, m):
    jogada = int(input("\nQuantas peças você vai tirar? "))
    while jogada > m or jogada > n or jogada <= 0:
        print("\nOops! Jogada inválida! Tente de novo.")
        jogada = int(input("\nQuantas peças você vai tirar? "))
    return jogada

def partida():
    # Leitura dos parâmetros:
    n = int(input("\nQuantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    # Jogada inicial:
    ## Usuário: 1 ; Computador: 0
    if n % (m+1) == 0:
        print("\nVocê começa!")
        jogador_atual = 1
    else:
        print("\nComputador começa!")
        jogador_atual = 0
    # Restante da partida:
    while n != 0:
        if jogador_atual == 0:
            jogada = computador_escolhe_jogada(n, m)
            if jogada == 1:
                print("\nO computador tirou uma peça.")
            else:
                print("\nO computador tirou", jogada, "peças")
            n -= jogada
            jogador_atual = 1
        else:
            jogada = usuario_escolhe_jogada(n, m)
            if jogada == 1:
                print("\nVocê tirou uma peça.")
            else:
                print("\nVoce tirou", jogada, "peças.")
            n -= jogada
            jogador_atual = 0
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            if n != 0:
                print("Agora restam", n, "peças no tabuleiro.")
    # Fim de jogo:
    if jogador_atual == 1:
        print("Fim do jogo! O computador ganhou!")
        return 0
    else:
        print("Fim do jogo! Voce ganhou!")
        return 1

def campeonato():
    rodada = 1
    pontos_computador = 0
    pontos_usuario = 0
    while rodada <= 3:
        print("\n**** Rodada", rodada, "****")
        vencedor = partida()
        if vencedor == 0:
            pontos_computador += 1
        else:
            pontos_usuario += 1
        rodada += 1
    print("\n**** Final do campeonato! ****")
    print("\nPlacar: Você", pontos_usuario, "X", pontos_computador, "Computador")
    return
    
# Main:
def main():
    print("\nBem-vindo ao jogo do NIM! Escolha:")
    print("\n1 - para jogar uma partida isolada")
    modo = int(input("2 - para jogar um campeonato "))
    if modo == 2:
        print("\nVoce escolheu um campeonato!")
        campeonato()
    else:
        print("\nVoce escolheu uma partida!")
        partida()
    return


# Guard:
if __name__ == '__main__':
    main()