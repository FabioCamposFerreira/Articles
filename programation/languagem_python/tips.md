# Dicas

## Contenação
Usar python .join é mais eficiente que +

## Cuidado com objetos mutaveis

```python
def sort_x(list_X):
    list_X.sort()
    return list_X


list_1 = [2, 1, 3]
list_2 = sort_x(list_1)
print("list_1 = "+str(list_1))
print("list_2 = "+str(list_2))
```
## Otimize seu codigo
Ref:![Speed Up Python Code](https://www.loginradius.com/blog/engineering/speed-up-python-code/)
## Rode codigos de forma mas rápida
Veja: ![Multiprocessing](https://urban-institute.medium.com/using-multiprocessing-to-make-python-code-faster-23ea5ef996ba)
