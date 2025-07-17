from personagem import Personagem

class Heroi(Personagem):
    """
    A classe heroi, representa um heroi no jogo e herda da classe personagem
    """
    def __init__(self, nome, idade, vida, bondade, força):
        super().__init__(nome, idade, vida)
        niveis_validos = ['Baixa', 'Média', 'Alta']
        if bondade not in niveis_validos:
            raise ValueError(f"Nível de bondade inválido! Escolha entre {niveis_validos}")
        self.bondade = bondade
        self.força = força

    def perdoar(self, personagem):
        self.perdão = False
        if personagem.vida < personagem.vida_maxima/2:
            if self.bondade == "Alta":
                print(f"Mesmo com seus atos de tirania eu lhe perdoarei {personagem.nome}")
                return True
            elif self.bondade == "Média":
                print(f"Eu deixarei você passar, mas não cruze meu caminho de novo")
                return True
            else:
                print(f"{personagem.nome}, você não merece o meu perdão")
                return False
        else:
            print(f"{personagem.nome} ainda não pode ser perdoado")
            return False
            
        
    

        

