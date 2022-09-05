#Implementar uma função que leia um arquivo e retorne uma lista de tuplas com os dados (o separador de campo do arquivo é vírgula), eliminando as linhas vazias. Caso ocorra algum problema, imprima uma mensagem de aviso e encerre o programa.

import csv
def reader_csv():
    try:
        arq = csv.reader(file('date.csv'))
        list = []
        for line in arq:
            if line!='':
                for word in line:
                    trup = (word)
                    list.append(trup)
        return list
    except:
        return 'Erro!!'

print (reader_csv())
