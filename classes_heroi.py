from heroi import Heroi
import random

class Guerreiro(Heroi):
    def __init__(self, nome, idade, vida, bondade, força):
        super().__init__(nome, idade, vida, bondade, força)
    
    def usar_habilidade_especial(self, alvo):
        dano = self.força * 2
        print(f"⚔️ {self.nome} usa GOLPE FURIOSO em {alvo.nome}, causando {dano} de dano!")
        alvo.downgrade_vida(dano)

class Mago(Heroi):
    def __init__(self, nome, idade, vida, bondade, força):
        super().__init__(nome, idade, vida, bondade, força)
    
    def usar_habilidade_especial(self, alvo):
        cura = self.força * 1.5
        self.vida = min(self.vida_maxima, self.vida + cura)
        print(f"✨ {self.nome} conjura uma LUZ CURATIVA, recuperando {int(cura)} pontos de vida!")


class Arqueiro(Heroi):
    def __init__(self, nome, idade, vida, bondade, força):
        super().__init__(nome, idade, vida, bondade, força)

    def usar_habilidade_especial(self, alvo):
        print(f"🎯 {self.nome} dispara uma FLECHA PRECISA em {alvo.nome}!")
        if random.random() < 0.5:
            dano = self.força * 2.5 
            print(f"ACERTO CRÍTICO! O dano é de {int(dano)}!")
        else:
            dano = self.força 
            print(f"A flecha atinge seu alvo, causando {dano} de dano.")
        
        alvo.downgrade_vida(dano)