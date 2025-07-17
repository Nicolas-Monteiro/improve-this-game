from classes_heroi import Guerreiro, Mago, Arqueiro

class IniciarJornada:
    """
    Gerencia o processo de criação do personagem no início do jogo.
    """
    def __init__(self):
        pass

    def escolher_classe(self):
        """
        Guia o jogador na escolha de uma classe e na criação do seu herói.
        Este método retorna o objeto do herói criado.
        """
        print("="*40)
        print(" Bem-vindo(a) à sua jornada, aventureiro(a)!")
        print("="*40)
        
        
        while True:
            nome_heroi = input("Primeiro, diga-nos seu nome: ")
            if nome_heroi: 
                break
            print("O nome não pode ser vazio.")

        print(f"\nBelo nome, {nome_heroi}! Agora, escolha sua vocação.")

        
        print("\n--- CLASSES DISPONÍVEIS ---")
        print("1 - Guerreiro (Vida: 120, Força: 18)")
        print("2 - Mago      (Vida: 80,  Força: 25)")
        print("3 - Arqueiro  (Vida: 100, Força: 20)")
        
        heroi_criado = None

        
        while True:
            escolha = input("\nDigite o número da classe desejada: ")
            
            if escolha == '1': # Guerreiro
                heroi_criado = Guerreiro(
                    nome=nome_heroi, 
                    idade=25, 
                    vida=120, 
                    bondade='Média', 
                    força=18
                )
                break 
            
            elif escolha == '2': # Mago
                heroi_criado = Mago(
                    nome=nome_heroi, 
                    idade=35, 
                    vida=80, 
                    bondade='Alta', 
                    força=25
                )
                break
            
            elif escolha == '3': # Arqueiro
                heroi_criado = Arqueiro(
                    nome=nome_heroi, 
                    idade=22, 
                    vida=100, 
                    bondade='Média', 
                    força=20
                )
                break
            
            else:
                print("Opção inválida! Por favor, digite 1, 2 ou 3.")

        print("\n" + "="*40)
        print("      Herói Criado com Sucesso!      ")
        print("="*40)
        print(heroi_criado) 
        print("="*40)

        return heroi_criado