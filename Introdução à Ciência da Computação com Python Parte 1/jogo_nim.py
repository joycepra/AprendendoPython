# n o número de peças inicial
# m o número máximo de peças

def computador_escolhe_jogada(n,m):
        comp = 1
        if n <= m:
                comp = n
                return (comp)
        if m == 1:
                comp = m
                return(comp)
        else:
                while comp != m:
                        if (n - comp) % (m+1) == 0:
                                return (comp)
                        else:
                                comp = comp + 1
                return (comp)
        
        
def usuario_escolhe_jogada(n,m):
        usu = int(input('Quantas peças você vai tirar? '))
        while usu > m or usu < 1 or usu > n: 
                print('Oops! Jogada inválida! Tente de novo.')  
                usu = int(input('Quantas peças você vai tirar? '))
        else:
                return (usu)
                              
def partida():
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))

        if n % (m+1) == 0:
                print("Você começa!")
                while n > 0:
                        if n > 0:
                                usu = usuario_escolhe_jogada(n,m)
                                n = n - usu
                                print ("Voce tirou", usu, "peças.")
                                print ("Agora restam", n, "peças no tabuleiro.")
                        if n > 0:
                                comp = computador_escolhe_jogada(n,m)
                                n = n - comp
                                print ("O computador tirou", comp, "peças.")
                                print ("Agora restam", n, "peças no tabuleiro.")
                else:
                        print('Fim do jogo! O computador ganhou!')
                                      
        else:
                print("Computador começa!")
                while n >0:
                        if n > 0: 
                                comp = computador_escolhe_jogada(n,m)
                                n = n - comp
                                print ("O computador tirou", comp, "peças.")
                                print ("Agora restam", n, "peças no tabuleiro.")
                        if n > 0: 
                                usu= usuario_escolhe_jogada(n,m)
                                n = n - usu
                                print ("Voce tirou", usu, "peças.")
                                print ("Agora restam", n, "peças no tabuleiro.")
                else:
                        print('Fim do jogo! O computador ganhou!')
   

def campeonato():
        nrodadas = 3
        while nrodadas <= 3 and nrodadas > 0:
                print ("**** Rodada", nrodadas, "****")
                partida()
                nrodadas = nrodadas - 1

        print ("**** Final do campeonato! ****")
        print ("Placar: Você 0 X 3 Computador")
                       

def main():

        print ("Bem-vindo ao jogo do NIM! Escolha:")
        print ("1 - para jogar uma partida isolada")
        print ("2 - para jogar um campeonato")

        op = int(input("Digite o número da opção: "))
 
        if op == 1:
            partida()
        if op == 2:
            campeonato()

main()
