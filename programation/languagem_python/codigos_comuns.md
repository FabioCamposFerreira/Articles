
# Códigos Comuns
## Trabalhando com Strings
### Como imprir textos coloridos?
  
```python
text = "Text red"
print("\033[91m {}\033[00m".format(text))
# Text red
text = "Text green"
print("\033[92m {}\033[00m".format(text))
# Text green
```
## Trabalhando com Listas
### Como colocar em ordem alfabetica
```python
names = ['Romeu', 'Mario', 'Patricia', ]
names.sort()
print(names)
# ['Mario', 'Patricia', 'Romeu']
digits = [1, -2, 0]
digits.sort()
print(digits)
# [-2, 0, 1]
```


## Trabalhando com o Terminal
### Como pegar o texto digitado pelo terminal?

```python
name = input("What is yout name? ")
# What is yout name? Fabio
print(name)
# Fabio
```

### Como construir uma barra de progresso para o terminal

```python
import subprocess
from time import sleep


def progress_bar(actual,total):
    """Print progress bar to accompanying processing"""
    line_width = int(subprocess.check_output("tput cols", shell=True))
    line_structure = "[] 100%"
    bar_len = (line_width-len(line_structure))
    hash_quantity = int(actual/total*bar_len)
    hyphen_quantity = bar_len-hash_quantity
    line = "[{}] {}%".format("#"*hash_quantity+"-"*hyphen_quantity,int(actual/total*100))
    print(line,end="\r")
    if(actual==total):
            print(end='\x1b[2K')


for i in range(10):
    sleep(.1)
    progress_bar(i,9)
````
## Como verificar se um arquivo exste

```python
from os.path import exists
print(exists("image.pgn"))
# False
````
## Usando com o Numpy
### Como obter a uma coluna de um array (matriz)


## 
Refs: [LearnAndLearn.com](https://learnandlearn.com/python-programming/python-how-to/python-function-arguments-mutable-and-immutable])
