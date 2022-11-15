def list_ordn(dados, chave, reverso, x, y):
         if(reverso):
                  if(len(dados)>y):
                           if(dados[x][-chave]<dados[y][-chave]):
                                    a = dados[x]
                                    dados[x] = dados[y]
                                    dados[y] = a
                                    list_ordn(dados, chave, reverso, 0, 1)
                           
                           else: list_ordn(dados, chave, reverso, x+1, y+1)
                  else:
                           print ('Lista ordenada: ', dados)
         else:
                  if(len(dados)>y):
                           if(dados[x][-chave]>dados[y][-chave]):
                                    a = dados[x]
                                    dados[x] = dados[y]
                                    dados[y] = a
                                    list_ordn(dados, chave, reverso, 0, 1)
                           
                           else: list_ordn(dados, chave, reverso, x+1, y+1)
                  else:
                           print ('Lista ordenada: ', dados)
                           
         
dados = [(1,2),(10,0),(5,9),(4,4),(7,6), (99, -3)]
chave = 2
reverso = False
list_ordn(dados,chave,reverso, 0, 1)

