from heroi import Heroi
from vilao import Vilao
import random

class Duelo:
    """
    Gerencia um embate entre heroi e vilão
    """
    def __init__(self, heroi = Heroi, vilao = Vilao):
        self.heroi = heroi
        self.vilao = vilao
        self.terminou_em_perdao = False

    
    def iniciar_confronto(self):
        print("---- O DUELO COMEÇA ----")
        print(f"{self.heroi.nome} VS {self.vilao.nome}")

        while self.heroi.vida > 0 and self.vilao.vida > 0:
            print("--- SEU TURNO ---")
            escolha = input("O que você faz? (1 - Atacar, 2 - Defender, 3 - Perdoar): ")
            if escolha == "1":
                self.heroi.ataque(self.vilao)
            elif escolha == "2":
                self.heroi.defender()
            elif escolha == "3":
                perdão_concedido = self.heroi.perdoar(self.vilao)
                if perdão_concedido == True:
                    self.terminou_em_perdao = True
                    break
                else:
                    continue
            elif escolha == "4":
                self.heroi.usar_habilidade_especial(self.vilao)

            else:
                print(f"{self.heroi.nome} não realizou nenhuma ação")

            if self.vilao.vida <= 0:
                break
            print("------------------------------")
            print(f"--- TURNO DE {self.vilao.nome} ---")
        
            if random.random() < 0.7: 
                self.vilao.ataque(self.heroi)
            else:
                self.vilao.defender()

            print("------------------------------")
        
        print("\n--- O DUELO TERMINOU! ---")
        if self.terminou_em_perdao == True:
            print(f"🕊️  O combate terminou em paz. {self.heroi.nome} poupou seu inimigo. 🕊️")
        elif self.heroi.vida > 0:
            print(f"🎉 PARABÉNS! {self.heroi.nome} foi vitorioso! 🎉")
        elif self.vilao.vida > 0:
            print(f"GAME OVER! {self.vilao.nome} venceu o combate.")
        else:
            print("INCRÍVEL! Ambos os combatentes caíram. O resultado é um empate!")