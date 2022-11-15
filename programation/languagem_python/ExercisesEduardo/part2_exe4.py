#split(fn, n), que quebra o arquivo fn em partes de n bytes e salva com nomes sequenciais (se fn = arq.txt, então arq_001.txt, arq_002.txt, ... )
#join(fn, fnlist) que junte os arquivos da lista fnlist em um arquivo só fn.

import os.path
from functools import reduce
import glob


def split(fn, n):
    temp = open(fn, 'r')
    size_file = os.path.getsize(fn)
    text = []
    for x in temp:
        for ch in x:
            text += [ch]
    temp.close()
    parts = int(size_file/n)
    if parts <=1:
        return 'O arquivo possui um numero menor de bytes!'
    text_split_size = int(len(text)/parts)
    for part in range(1,parts+1):
        temp = open('arq'+str(part)+'.txt','w')
        i=0
        for t in text:
            temp.write(t)
            i+=1
            if i==text_split_size:
                break
        temp.close()
        text = text[text_split_size:]
    return 'Finalizado com sucesso'
def join(fn, fnlist):
    print(fnlist)
    text = []
    for arq in fnlist:
        temp = open(arq,'r')
        for x in temp:
            for ch in x:
                text += [ch]
        temp.close()
    temp = open(fn, 'w')
    for ch in text:
        temp.write(ch)
    temp.close()
fnlist=[]
for arq in sorted(glob.glob("arq*.txt")):
    fnlist += [arq[3]]
join('arq.txt',fnlist)