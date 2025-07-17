from vilao import Vilao
from heroi import Heroi
from duelo import Duelo
import time 
from iniciar_jornada import IniciarJornada
from duelo import Duelo

def main():
    """
    Função principal que orquestra o fluxo do jogo.
    """
    print("*"*45)
    print("      BEM-VINDO A 'A ÚLTIMA BATALHA'      ")
    print("*"*45)
    time.sleep(2) 
    jornada = IniciarJornada()
    heroi_jogador = jornada.escolher_classe() 
    
    time.sleep(1)
    print(f"\nPrepare-se, {heroi_jogador.nome}! Um grande desafio se aproxima...")
    time.sleep(2)

    # --- FASE 2: PREPARAÇÃO DO DESAFIO ---
    # Criamos o inimigo que o jogador irá enfrentar.
    chefe_final = Vilao('Malakor, o Devorador', 100, 150, 'Alta', 35)
    print("\n" + "="*45)
    print("      Um inimigo poderoso surge das sombras!      ")
    print("="*45)
    print(chefe_final)
    print("="*45)
    time.sleep(2)

    # --- FASE 3: O CONFRONTO FINAL ---
    # A classe Duelo recebe os dois combatentes e gerencia a batalha.
    duelo_decisivo = Duelo(heroi_jogador, chefe_final)
    duelo_decisivo.iniciar_confronto()
    
    # --- FIM DO JOGO ---
    print("\nObrigado por jogar!")


# Ponto de entrada padrão para um script Python
if __name__ == "__main__":
    main()