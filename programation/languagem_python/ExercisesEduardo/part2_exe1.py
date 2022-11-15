#Implementar um programa que receba um nome de arquivo e gere estatísticas sobre o arquivo (número de caracteres, número de linhas e número de palavras)

def count_clw(file):
                temp = open(file)
                count_line = 0
                count_char = 0
                count_word = 0
                for line in temp:
                                count_line+=1
                                for ch in line:
                                                if(ch!=' '): count_char +=1
                                                else: count_word+=1
                print('Número de caracteres: ', count_char)
                print('Número de lihas: ', count_line)
                print('Número de palavras: ', count_word+1)
