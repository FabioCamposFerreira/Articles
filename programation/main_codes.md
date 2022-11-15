# Principais funções

## Como pegar o texto digitado pelo terminal?

```python
name = input("What is yout name? ")
# What is yout name? Fabio
print(name)
# Fabio
```
  
##   Como imprimir textos coloridos?
  
```python
text = "Text red"
print("\033[91m {}\033[00m".format(text))
# Text red
text = "Text green"
print("\033[92m {}\033[00m".format(text))
# Text green
```

 
