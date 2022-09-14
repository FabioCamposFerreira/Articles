# Dicas

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
