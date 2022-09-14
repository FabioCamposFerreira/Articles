# Códigos Comuns

## Como construir uma barra de progresso para o terminal

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



## 
Refs: [LearnAndLearn.com](https://learnandlearn.com/python-programming/python-how-to/python-function-arguments-mutable-and-immutable])
