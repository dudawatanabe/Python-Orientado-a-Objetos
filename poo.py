class Pessoa:
  def __init__(self, nome: str, idade: int, altura: float):
    self.nome = nome
    self.idade = idade
    self.altura = altura

  def dizer_ola(self):
    print(f'Olá, meu nome é {self.nome}. Tenho {self.idade} '
          f'anos e minha altura é {self.altura}m.')

  def cozinhar(self, receita: str):
    print(f'Estou cozinhando um(a): {receita}')

  def jogando(self, missões: float):
    print(f'Depois vou jogar no meu quarto. Volto quando completar {missões} missões')

  def escola(self, nome_escola: str):
    print(f'Vou à faculdade todos os dias. O nome dela é: {nome_escola}')

pessoa = Pessoa(nome='Duda', idade=20, altura=1.70)


pessoa.dizer_ola()
pessoa.cozinhar('Carbonara')
pessoa.jogando(5)
pessoa.escola('FATEC')