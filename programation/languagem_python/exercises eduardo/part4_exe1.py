#Nma classe que modela um quadrado, com um atributo lado e os métodos: mudar valor do lado, retornar valor do lado e calcular área.
class Quadrado():
    def __init__(self, lado):
        self.lado = lado
    def set_lado(self, novo_valor):
        self.lado = novo_valor
    def get_lado(self):
        return self.lado
    def area(self):
        return pow(self.lado,2)

q = Quadrado(4)
print(q.lado)
q.set_lado(25)
print(q.lado)
print(q.get_lado())
print(q.area())

