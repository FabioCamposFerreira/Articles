# Uma classe derivada de lista com um método que retorna os elementos da lista sem repetição.

class Lista_repetida(list):
    def sem_repetir(self):
        lista_nao_repetida = []        
        for i in range(0,len(self)):
            repetido = False
            for i2 in range(0,len(lista_nao_repetida)):
                if self[i] == lista_nao_repetida[i2]:
                    repetido = True
            if repetido == False:            
                lista_nao_repetida+=[self[i]]    
                    
            
        return lista_nao_repetida


lista = [1,2,34,5,5,5,6,7,8,9,1,3,5,7,4567,456745,4567]
l_r = Lista_repetida(lista)
print(l_r.sem_repetir())

