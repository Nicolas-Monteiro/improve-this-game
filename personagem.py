class Personagem:
    """
    A classe Personagem representa um personagem genérico em um jogo.
    """
    def __init__(self, nome, idade, vida):
        self.nome = nome
        self.idade = idade
        self.vida = vida
        self.vida_maxima = vida
        self.esta_defendendo = False

    def upgrade_vida(self, incremento=10):
        """
        Aumenta a vida do personagem. O valor padrão de incremento é 10.
        """
        self.vida += incremento
        print(f'Vida de {self.nome} após upgrade: {self.vida}')


    def downgrade_vida(self, dano_recebido):
        dano_final = 0 # Variável para guardar o dano que será aplicado

        if self.esta_defendendo:
            dano_final = dano_recebido / 2
            print(f"{self.nome} defendeu o ataque e reduziu o dano para {dano_final}!")
            self.esta_defendendo = False # Sai da postura defensiva
        else:
            # Se não está defendendo, o dano final é o dano total
            dano_final = dano_recebido

        if self.vida > dano_final:
            self.vida -= dano_final
        else:
            # Se o dano for maior que a vida, a vida vai para 0
            self.vida = 0
    
        print(f'Vida de {self.nome} agora é: {int(self.vida)}/{int(self.vida_maxima)}')


    def update_nome(self, nome_editado):
        """
        Atualiza o nome do personagem.
        """
        self.nome = nome_editado

    def ataque(self, personagem):
        """
        Reduz a vida de outro personagem atacado per outro personagem.
        """
        print(f'{self.nome} atacou {personagem.nome}!')
        personagem.downgrade_vida(self.força)

    def defender(self):
        """
        Deixa o personagem em modo de defesa, reduzindo pela metade o valor do proximo ataque
        """
        self.esta_defendendo = True
        print(f"{self.nome} vai se defender do próximo ataque")

    def __str__(self):
        return f'Personagem: {self.nome}, Idade: {self.idade}, Vida: {self.vida}'
