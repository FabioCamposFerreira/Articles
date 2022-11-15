# Implementar uma classe Vetor:
#   + Com coordenadas x, y e z.
#   + Que suporte soma, subtração, produto escalar e produto vetorial.
#   + Que calcule o módulo (valor absoluto) do vetor.

class Vetor():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def soma(self,outro_vetor):
        return Vetor(self.x+outro_vetor.x,self.y+outro_vetor.y, self.z+outro_vetor.z)
    def subtracao(self,outro_vetor):
        return Vetor(self.x-outro_vetor.x,self.y-outro_vetor.y, self.z-outro_vetor.z)
    def produto_escalar(self,outro_vetor):
        return self.x*outro_vetor.x+self.y*outro_vetor.y+self.z*outro_vetor.z
    def produto_vetorial(self,outro_vetor):
        return Vetor(self.y*outro_vetor.z-self.z*outro_vetor.y,self.z*outro_vetor.x-self.x*outro_vetor.z,self.x*outro_vetor.y-self.y*outro_vetor.x)
    def modulo(self):
        return pow(pow(self.x,2)+pow(self.y,2)+pow(self.z,2),1/2)

v= Vetor(1,2,3)
print("v = "+"("+str(v.x)+", "+str(v.y)+", "+str(v.z)+")")
v2= Vetor(4,5,6)
v3 = v.soma(v2)
print("Soma de v é "+"("+str(v3.x)+", "+str(v3.y)+", "+str(v3.z)+")")
v4 = v.subtracao(v2)
print("Subtração de v é "+"("+str(v4.x)+", "+str(v4.y)+", "+str(v4.z)+")")
print("Produto Escalar de v é "+str(v.produto_escalar(v2)))
print("Modulo de v : "+str(v.modulo()))
v5 = v.produto_vetorial(v2) 
print("Produto Vetorial de v e v2 é "+"("+str(v5.x)+", "+str(v5.y)+", "+str(v5.z)+")")

