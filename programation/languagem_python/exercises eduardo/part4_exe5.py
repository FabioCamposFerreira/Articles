# Implemente um módulo com:
#   + Uma classe Ponto, com coordenadas x, y e z.
#   + Uma classe Linha, com dois pontos A e B, e que calcule o comprimento da linha.
#   + Uma classe Triangulo, com dois pontos A, B e C, que calcule o comprimento dos lados e a área.

class Ponto():
    # definição das variaveis
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    # retorna a classe
    def __repr__(self):
        return "("+str(self.x)+", "+str(self.y)+", "+str(self.z)+")"

class Linha():
    # definição das variaveis
    def __init__(self,A,B):
        self.A = A
        self.B = B
        # Linha como vetor        
        self.x = self.B.x-self.A.x
        self.y = self.B.y-self.A.y
        self.z = self.B.z-self.A.z

    # retorna a classe
    def __repr__(self):
        return "("+str(self.x)+", "+str(self.y)+", "+str(self.z)+")"

    # retorna o comprimento do triângulo
    def comprimento(self):
        return pow(pow(self.B.x-self.A.x,2)+pow(self.B.y-self.A.y,2)+pow(self.B.z-self.A.z,2),1/2)            

class Triangulo():
    # definição das variaveis
    def __init__(self,A,B,C):
        # Pontos que formam o triângulo        
        self.A = A
        self.B = B
        self.C = C
        # Lados que formam o triângulo
        self.lado_A_B = Linha(self.A,self.B)
        self.lado_B_C = Linha(self.B,self.C)
        self.lado_C_A = Linha(self.C,self.A)

    # retorna a classe
    def __repr__(self):
        return  str(self.A)+", "+str(self.B)+", "+str(self.C) 

    # retorna a área do triângulo
    def area(self):
        return pow((pow(self.lado_A_B.y*self.lado_B_C.z-self.lado_A_B.z*self.lado_B_C.y,2)+pow(self.lado_A_B.z*self.lado_B_C.x-self.lado_A_B.x*self.lado_B_C.z,2)+pow(self.lado_A_B.x*self.lado_B_C.y-self.lado_A_B.y*self.lado_B_C.x,2)),2)/2
    
    # retorna o comprimento do triângulo
    def comprimento(self):
        return self.lado_A_B.comprimento()+self.lado_B_C.comprimento()+self.lado_C_A.comprimento()

# definindo os pontos
p1 = Ponto(0,0,0)
p2 = Ponto(0,10,0)
p3 = Ponto(10,0,0)
# criando uma linha
l = Linha(p1,p2)
print("Linha A="+str(p1)+" e B="+str(p2))
print("Comprimento: "+str(l.comprimento()))
# criando um triângulo
t = Triangulo(p1,p2,p3)
print("Triângulo "+str(t))
print("Comprimento do triângulo: "+str(t.comprimento()))
print("Área do triângulo: "+str(t.area()))
