class Carro:
    def __init__(self,marca,ano ,cor):
        self.marca = marca
        self.ano = ano
        self.cor = cor
    
    def infos(self):
        print(f"O carro e da Marca: ",self.marca, "ano ",self.ano, "cor",self.cor)

    
carro1 = Carro(input('marca 1 '),input('ano 1 '),input('cor 1 '))
carro2 = Carro(input('marca 2 '),input('ano 2 '),input('cor 2 '))

carro1.infos()
carro2.infos()