#Le um arquivo texto
#Conta as ocorrências de cada palavra.
#Mostra os resultados ordenados pelo número de ocorrências
import sys
import time
import re
from operator import itemgetter, attrgetter, methodcaller

def read_text(arq):
    temp = open(arq)
    text = ''
    for x in temp:
        text += x
    return text


def count_words(words, list_words):
    if len(words)!=0:
        word = words[0]
        count=0
        i=0
        for w in words:
            if w==word:
                count+=1
                words.pop(i)
            i+=1            
        list_words+= [(word,count)]
        count_words(words,list_words)
    else:
        list_words = sorted(list_words, key=itemgetter(1), reverse=True)
        j=0
        for l in list_words:
            if l[0] =='':
                list_words.pop(j)
            j+=1
        for l in list_words:
            print(l)

text = read_text('text.txt')
words = re.split('[ ,.?!();:\n]', text)
count_words(words, [])
print(time.perf_counter(), 'segundos')
