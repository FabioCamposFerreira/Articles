# Uma classe Carro que tem as seguintes propriedades:
#   + Um veículo tem um certo consumo de combustível (medidos em km /litro) e uma certa quantidade de combustível no tanque.
#   + O consumo é especificado no construtor e o nível de combustível inicial é 0.
#   + Forneça um método mover(km) que receba a distância em quilômetros e reduza o nível de combustível no tanque de gasolina.
#   + Forneça um método gasolina(), que retorna o nível atual de combustível.
#   + Forneça um método abastecer(litros), para abastecer o tanque

class Carro():
    def __init__(self,consumo ):
        self.consumo = consumo
        self.nivel_tanque = 0
    def mover(self,km):
        self.nivel_tanque = self.nivel_tanque - km*self.consumo
        if self.nivel_tanque<0:
            self.nivel_tanque = 0
    def gasolina(self):
        return self.nivel_tanque
    def abastecer(self, litros):
        self.nivel_tanque += litros

c = Carro(5)
print(c.gasolina())
c.abastecer(100)
print(c.gasolina())
c.mover(10)
print(c.gasolina())
