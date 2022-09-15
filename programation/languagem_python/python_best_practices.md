# Python

## Dicas de otimização
Ao inves de utilizar list e dic, use arrays da biblioteca numpy. Isso torna o codigo mais rapido e usa menos memoria, além  de ser mais prático
 \section{Boas práticas}
![Numpy](https://numpy.org/devdocs/user/absolute_beginners.html)
 Para o nome de classes use ClassName e para nomes de funções use function_name

## Fazendo quebra de linhas
```python
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```
```python
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```
See:![Peps](https://peps.python.org/pep-0008/#maximum-line-length)

## É Mais Fácil Pedir Perdão do que Permissão
<table>
<tr>
<td>
Wrong
</td>
 
 <td>
Correct
 </td>
 </tr>
 <tr>
<td>

<tr>
<td>
  
  
```python
import os
file_path ="text.txt"
if os.path.exists(file_path ):
    with open(file_path ,"r") as file:
        print(file)
        # <_io.TextIOWrapper name='text.txt' mode='r' encoding='UTF-8'>
else:
    print("File not exists!")
# File not exists!
``` 
 </td>
 <td>

```python
file_path = "text.txt"
try:
    with open(file_path, "r") as file:
        print(file)
        # <_io.TextIOWrapper name='text.txt' mode='r' encoding='UTF-8'>
except:
    print("File not exists!")

```
</td>
</tr>
![Agus Richard](https://medium.com/nerd-for-tech/look-before-you-leap-vs-easier-to-ask-for-forgiveness-than-permission-in-programming-85d17a5f48c8)
## Referencias
![Peps](https://peps.python.org/pep-0008)
![Osantana](https://osantana.me/dicas-para-um-om-programa-em-python/)
