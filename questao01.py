class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def dizer_ola(self):
        print(f"Olá, meu nome é {self.nome}. Tenho {self.idade} anos e minha altura é {self.altura}m.")

    def cozinhar(self, receita):
        print(f"Estou cozinhando um(a): {receita}.")

    def andar(self, distancia):
        print(f"Sai para andar. Volto quando completar {distancia} metros.")


nome = "Ana"
idade = 25
altura = 1.68

ana = Pessoa(nome, idade, altura)

ana.dizer_ola()
ana.cozinhar("lasanha")
ana.andar(1000)
