# Gerador que lê um arquivo e retorne uma lista de tuplas com os dados (o separador de campo do arquivo é vírgula), eliminando as linhas vazias. Caso ocorra algum problema, imprime uma mensagem de aviso e encerra o programa.
# minha resposta
import time

def my_aswer():
    def file_tuple_out(file):
        try:
            temp = open(file, 'r')
            for linhe in temp:
                linhe_ = linhe[0:-1]
                if len(linhe_) > 0:
                    list_ = linhe_.split(',')
                    yield tuple(list_)
        except expression as identifier:
            print('Ocorreu um erro ao ler o arquivo', file)
            print(Exception)
    a = file_tuple_out('part3_exe4.txt')
    print(type(a))
    print(list(a))


def book_aswer():
    def load_csv(fn):
        try:
            file = open(fn, 'r')
            for line in file:
                new_line = line.strip()
                if new_line:
                    yield tuple(new_line.split(','))
        except:
            print('Ocorreu um erro ao ler o arquivo', fn)
            raise SystemExit
    # Teste
    for line in load_csv('part3_exe4.txt'):
        print(line)


my_aswer()
# book_aswer()
print(print(time.perf_counter(), 'segundos'))
