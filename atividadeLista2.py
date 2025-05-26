class Pessoa:
    def __init__(self,nome,idade,cpf):
        self.nome = nome
        self.idade = idade
        self.cpf  = cpf

    def infos(self):
        print(f'Meu nome é {self.nome}idade {self.idade} CPF: {self.cpf}')

user1 = Pessoa(input('nome 1 '),input('idade 1 '),input('CPF 1 '))
user2 = Pessoa(input('nome 2 '),input('idade 2 '),input('cpf 2 '))

user1.infos()
user2.infos()
