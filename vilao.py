from personagem import Personagem  # Importa a classe Personagem
from heroi import Heroi

class Vilao(Personagem):
    """
    A classe Vilao representa as características de um vilão no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, idade, vida, maldade, força):
        super().__init__(nome, idade, vida)
        niveis_validos = ['Baixa', 'Média', 'Alta']
        if maldade not in niveis_validos:
            raise ValueError(f"Nível de maldade inválido! Escolha entre {niveis_validos}")
        self.maldade = maldade
        self.força = força

    def manipular_personagem(self, personagem):
        if personagem is not Heroi:
            if self.maldade == "Alta":
                print(f"{personagem.nome} foi enganado por {self.nome}, e agora está do seu lado")
            elif self.maldade == "Média":
                print(f"{personagem.nome} está se questionando de que lado ele está")
            else:
                print(f"{personagem.nome} não caira nesses truques")
        else:
            print("Um heroi não pode ser manipulado facilmente")
        

            
    def __str__(self):
        return f'Vilão: {self.nome}, Idade: {self.idade}, Vida: {self.vida}, Maldade: {self.maldade}'
