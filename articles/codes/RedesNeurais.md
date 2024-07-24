# Deep Learn (Aprendizado profundo)
## Perceptron

O modelo perceptron foi construido com base no que se entendia do funcionamento dos neuronios do cerebro.

Um neuronio é apresenta um necleu, dendritios e axionio (conecta o nucle nos dentritios dos outros neuronios)

![Neuronio](??)

No perceptron, os dentritios recebem a informação (valores), o nucle processa eles (realiza uma soma ponderada, com pesos diferentes para cada valor, onde o resultado passa por um limiarizador), o axionio transmite a resposta do gerada pelo nucleo 

**Exemplo**: Tendo a entrada ($x_1$ e $x_2$) e saída desejada($y$) apresentada na tabela abaixo:
|$X_1$|	$X_2$|	$y$|
|----|----|-----|
|0|	0|	0|
|0|	1|	0|
|1|	0|	0|
|1|	1|	1|

Podemos construir o perceptron definindo ps pessos para cada entrada ($\omega_1$ e $\omega_2$) e o valor  do limiarizador ($t$).

![Perceptron usado para contruir uma porta AND](perceptron.jpg)

A equação que descreve o perceptron é 


$
y_0(x_1\times\omega_1+x_2\times\omega_2) \qquad 1 \text{ se } y_0\ge 1,5
\qquad 0 \text{ se } y_0 \leq 1,5
$

Acompanhe o processo para cada uma das quatro entradas.

|Equação|Limiarizar para 1,5|
|-----|:--------:|
|$0*1+0*1 = 0$|0|
|$0*1+1*1 = 1$|0|
|$1*1+0*1 = 1$|0|
|$1*1+1*1 = 2$|1|

# Modelo classico de Rosenblatt's

![Perceptron de Rosenblatt](rosenblatt.gif)

Este modelo é formado por:
- Entrada: $x_1, x_2, \dots, x_m$
- Pesos: $\omega_1,\omega_1, \omega_2, \dots, \omega_m$
- Função de ativação (ou threshold): $\sigma(z)$
- Bias: $\theta$
- Saida: $\hat y$

Este modelo equivale a equação

$\sigma\left(\sum^m_{i=0}x_i\omega_i\right) = \hat y$

|||
|----|------|
|$\sigma(z) =$|$0, z-\theta \leq 0$|
||$1, z-\theta > 0$|

O código em python equivalente a equação acima é

<spam id="codes/redes_neurais.py/Perceptron using for loop"></spam>

A equação pode ser reescrevida em forma de multiplicação vetorial

$
\sigma\left(\sum^m_{i=0}x_i\omega_i\right) = \sigma\left(X^TW\right) = \hat y
$

O código em python equivalente a equação acima é

<spam id="codes/redes_neurais.py/Perceptron using vector"></spam>

A GPU permite fazer executar estes caculos (for loop e vetorizado) de forma paralela, aumentando a velocidade do código.

# Regra de aprendizado Perceptron 

O objetivo do aprendizado profundo é acha a melhor reta que separa os pontos

A reta é construída fazendo uma interação para cada ponto, onde se o ponto desta do lado correto da reta, ela não é modificada, caso contrario, a reta é modificada para que o ponto fique no lado correto

|![Perceptron de Rosenblatt](perceptron_linha.gif)|
|:--:|
|*Achando melhor linha de separação*|

Este processo é dado pelo seguinte algoritmo
````
for each point (x_1,x_2):
    if prediction==target:
        Do nothing
    else:
        if prediction==0 and target==1:
            Add (x_1,x_2) to weight vector
        if prediction==1 and target==0:
            Subtract (x_1,x_2) to weight vector
````

**Exemplo**: Construindo o perceptron para a entrada ($x_1$, $x_2$ e $x_3$) e saida desejada ($y$) da tabela abaixo.
|$x_1$|	$x_2$|	$x_3$|	$y$|
|----|----|-----|---|
|1|	0|	0|0|
|1|	0|	1|0|
|1|	1|	0|0|
|1|	1|	1|1|

As tabelas abaixo mostra o processo executado para cada epoch. 

* Epoch 1


|Entrada|	$\hat{y}=\sigma(\vec{x}^T\vec{w})$  | Erro	$err=y-\hat{y}$|$\vec{w}=(w_1+err\cdot x_1,w_2+err\cdot x_2, w_3+err\cdot x_3)$ |
|----|----|-----|----|
|-        |	-|	-|$\vec{w}=(0,0)$|
|1        |	$\hat{y}=\sigma(1\times 0+0\times 0 + 0\times 0)=\sigma(0)=0$|	$err = 0-0=0$      |$\vec{w}=(0+0\times 1,0+0\times 0,0+0\times 0)=(0,0,0)$|
|2        |	$\hat{y}=\sigma(1\times 0+0\times 0 + 1\times 0)=\sigma(0)=0$|	$err = 0-0=0$      |$\vec{w}=(0+0\times 1,0+0\times 1,0+0\times 1)=(0,0,0)$|
|3        |	$\hat{y}=\sigma(1\times 0+1\times 0 + 0\times 0)=\sigma(0)=0$|	$err = 0-0=0$      |$\vec{w}=(0+0\times 1,0+0\times 1,0+0\times 0)=(0,0,0)$|
|4        |	$\hat{y}=\sigma(1\times 0+1\times 0 + 1\times 0)=\sigma(0)=0$|	$err = 1-0=1$      |$\vec{w}=(0+1\times 1,0+1\times 1,0+1\times 1)=(1,1,1)$|

* Epoch 2

|Entrada|	$\hat{y}=\sigma(\vec{x}^T\vec{w})$  | Erro	$err=y-\hat{y}$|$\vec{w}=(w_1+err\cdot x_1,w_2+err\cdot x_2, w_3+err\cdot x_3)$ |
|----|----|-----|----|
|1|	$\hat{y}=\sigma(1\times 1+0\times 1 + 0\times 1)=\sigma(1)=1$|	$err = 0-1=-1$|$\vec{w}=(1-1\times 1,1-1\times 0,1-1\times 0)=(0,1,1)$|
|2| $\hat{y}=\sigma(1\times 0+0\times 1 + 1\times 1)=\sigma(1)=1$|	$err = 0-1=-1$|$\vec{w}=(0-1\times 1,1-1\times 0,1-1\times 1)=(-1,1,0)$|
|3| $\hat{y}=\sigma(1\times (-1)+1\times 1 + 0\times 0)=\sigma(0)=0$|	$err = 0-0=0$|$\vec{w}=((-1)+0\times 1,1+0\times 1,0+0\times 0)=(-1,1,0)$|
|4| $\hat{y}=\sigma(1\times (-1)+1\times 1 + 1\times 0)=\sigma(0)=0$|	$err = 1-0=1$|$\vec{w}=((-1)+1\times 1,1+1\times 1,0+1\times 1)=(0,2,1)$|

* ...

* Após a Epoch 5
    * $w_0 = -2$
    * $w_1 = 2$
    * $w_2 = 1$

Normalizando para 1 tem-se $w_0=-1$,$w_1=1$ e $w_2=0,5$. A imagem abaixo mostra a divisão de decissão do classificador.

|![Região de Decisão](região_de_decisão.gif)|
|:--:|
|*Região de decisão obtida*|

A superficie de decisão é obtida atraves da equalção da reta $y=ax+b$ ou $y-ax-b=0$ para representar a operação $\hat{w}^T\hat{x}=0$. Se o vetor peso for $\hat{w}=(-b,-a,1)$ e o vetor entrada $\hat{x}=(1,x,y)$ pode-se repesentar a operação vetorial como uma equação de reta. (nesta equação $y$ da equação não é o resultado do perceptron)

$\hat{w}^T\hat{x}=-b\times 1+(-a)\times x + 1\times y$

$\hat{w}^T\hat{x}=-b+(-a)x+y$

Para o exemplo (lembrando que $w_0=\theta$)

$\hat{w}=(w_0,w_1,w_2)=(-b,1,-a)=(-1;1;0,5)$

$\hat{x}=(x_1,x_2,x_3)=(1,x,y)=(1,x_2,x_3)$

então a equação da reta é 

$-b+(-a)x+y=0$

$1+(0,5)x_2+x_3=0$

$\dfrac{x_2}{2}+x_3=1$

Segue o código do perceptron

<spam id="codes/redes_neurais.py/Code full Perceptron"></spam>

* **Theorema Convergencia do Perceptron**: se os dados forem linearmente separáveis, o perceptron sempre vai convergir, ou seja, construir uma reta que consiga separar os dados.

O objetivo do perceptron não é obter a magnitude do vetor $\hat{w}$, mas sim seu angulo. Assim, a escala de $\hat{w}$ não é importante, mas se for utilizado valores muito grandes, a convergência ira demorar. Por isso, é preferível escalar $\hat{w}$ e $\hat{x}$ para valores próximos de 0.

Desvantagens do perceptron:

*  Classificar linear (so pode separar conjunto usando uma reta);
*  Classificar binário (so pode classificar entradas para duas classes);
*  Não ira convergir se as classes não forem linearmente separáveis;
*  Ele pode achar uma região de decisão que não é uma "ótima" solução;

O perceptron tem os seguintes modos:
* *"online"* apresenta uma amostra e atualiza os pesos. 
* *"batch"* apresenta varias amostras e depois atualiza os pesos. Para melhorar o resultado no modo "online" é necessário misturar as amostra, mas no modo "batch" não necessita desta etapa. O "bath" é mais otimizado mas precisa de muitas épocas para convergir;
* *"minibatch"* onde não é apresentado todos mas sim uma pequena parcela das amostras para depois atualizar os pesos. Ele é o mais usado, pois existe a possibilidade  vetorização, apresenta menos atualização de pesos que o "online" e menor ruido.

# Algebra Linear para Aprendizado Profundo

Tensor é um vetor que tensiona a região de decisão.
* **Escalar**: qualquer numero real, ex: $x=1$, é um tensor de rank 0;
* **Vetor**: conjunto de $n$ números reais ex: $\hat{x}=(x_1,x_2,...,x_n)$, é um tensor de rank 1;
* **Matriz**: conjunto de $m\times n$ numero reais dispostos en linhas e colunas, ex: 

$**X**=\left[x_{1,1} x_{1,2} ... x_{1,n}
x_{2,1} x_{2,2} ... x_{2,n}
... ... ... ...
x_{m,1} x_{m,2} ... x_{m,n}
\right]$

,é tensor de rank 2;

* **Matriz design**: é nome dado a matriz contendo  $n$ caracteristicas de $m$ amostras;

* **3D Tensor**: são varias matrizes, por exemplo uma imagem com tres canais de cores, é importante para usar o paralelismo de processamento e quacionamento vetorial;

# Pytorch vs Numpy

Os dois são bibliotecas do python usados para criação e manipulação de vetores. Mas é preferível usar o Pytorch porque PyTorch tem suporte a GPU (permite carregar dados e modelos usando a memoria da GPU) (GPU permite o melhor paralelismo), também apresenta diferenciação automática (faz regra da cadeia de forma automática), ja apresenta multiplas função de Deep Learn

# Vetores

Para obtermos a resposta escalar z , que é um número real é preciso realizar a equação

$\hat{w}^T\hat{x}+b=z$

em que:

$\hat{x} = \left[x_1,x_2,\dots,x_m\right]$,

$\hat{w} = \left[w_1,w_2,\dots,w_m\right]$


são vetores. Os operações básicas entre vetores são:
* Adição;
  
$[1,2,3]+[4,5,6] = []$
```python
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b)
# array([5, 7, 9])
```
* Produto interno;
```python
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a*b)
# array([ 4, 10, 18])
```
* Multiplicação escalar.
  
# Gradiente Dessedente

É possível melhorar o perceptron usando o gradiente descendente para:
* resolver um problema não linearmente separável;
* usar mais de duas classes;
* trabalhar com imagens e textos.

Modo estocástico é ruidoso.

|![Gradiente Descendente Ruidoso](gradiente_descedente_ruidoso.gif)|
|:--:|
|*Gradiente Descendente Ruidoso*|


Para evitar que os pesos se afastem do menor error é preciso normalizar as entradas.


|![Normalizar Entradas](normalizar_entradas.gif)|
|:--:|
|*Normalizar Entradas*|


A perda minima não é zero.
|![Perda Minima](perda_minima.gif)|
|:--:|
|*Perda Minima*|

A equação de perca da soma do erro quadratico (SSE - Sum Square Error) é 

$L(\vet{w},b) = \sum_{i}(\hat{y}^i-y^i)^2$

Fazendo a derivada parcial em relação aos pesos para encontrar a equação de perca minima obten-se:

$\dfrac{\partial L}{\partial \italic{w}_j}  =\dfrac{\partial }{\partial \italic{w}_j} \sum_{i}(\hat{y}^i-y^i)^2$

.

.

.

$\dfrac{\partial L}{\partial \italic{w}_j}  = \sum_{i}2(\sigma(\vet{w}^T\vet{x}^i)-y^i)x_j^i$

# Adaline 
Foi desenvolvido em 1960. Usado para classificar classes

|![Adaline VS Perceptron](adaline_vs_Perceptron.gif)|
|:--:|
|*Adaline VS Perceptron*|

**Forward**: Com a entrada X, usa os pesos para achar a saida y_hat
**Backward**: Com a saida y_hat, calcula o erro, calcula as derivadas parciais e atualiza os pesos 

The loss function is MSE, giben by:

$MSE = 1/n\sum_i(a^i-y^i)^^2$

É igual ao perceptron, mas após o envio do erro existe uma função de limiarização.

Código do Adaline usando *minibatch*
minibatch_mode.png
|![Minibacth Mode](minibatch_mode.gif)|
|:--:|
|*Minibacth Mode*|
```python


```
# Regreção linear 
|![Regreção Linear](linear_regretion.gif)|
|:--:|
|*Regreção Linear*|
Usado para prever valores numericos
Código da Regreção Linear
```python


```
# Solução Analitica 

|![Analytical Solution](analytical_solution.gif)|
|:--:|
|*Analytical Solution*|

The weights vector also is given by:

$\vet{w} = (\vet{X}^T\vet{X})^{-1}\vet{X}^Ty$

The code to use alalytic solution is:

```python


```

# PyToch
A automatica diferenciação faz a derivada parcial altomatica
|![Computation Graphs](computationGraphs.gif)|
|:--:|
|*Computation Graphs*|
Automatic diferentiation.
See the code
```python


```

# Funções de Ativação 

## step
 : ou é o ou é 1
## Linear
 f(x)=x

## Relu (Rectified Linear Unit)
Most used in Deep Learning

relu(x)= x if x>0

       = 0 therwise

The derivate of the relu is

f'(x)=x  x>0

     =0  x<=0


|![Relu](relu.gif)|
|:--:|
|*relu*|

# Logistic Regression
Equal Adaline, the diference is the activation funcion ($\sigma(z)$). The logistic regression use the logistic sigmoid:

$\sigma(z) = \dfrac{1}{1+\euler^(-z)}$

The respose this function is

|![Logistic Sigmoid](logistic_sigmoid.gif)|
|:--:|
|*Logistic Sigmoid*|

The response of $\sigma(z)$ is the probability 

# Entropya cruzada
* É uma função de perca melhor que a MSE para classificação de classes

# Classificação multiclasse
* Usandop entropia cruzada e softmax

# Outras
 A bliblioteca Keras é mais facil que o Pytorcy e o tensorflow. Mas ela tem menos recursos

# Adaline com Keras, Regreção Logistica com Keras, Regreção Linear com Keras

Do adaline para a regrção ligistica muda a função de ativação e a de perca (loss)

Da regreção logistica para a linear muda a saida de ao inves de ser 0s e 1s são numeros reais

# Funções de ativação

## Degrau 0 1
|![Degrau 0 1](Degrau 0 1.gif)|
|:--:|
|*Logistic Sigmoid*|
## Degrau -1 1
|![Degrau -1 1d](Degrau -1 1.gif)|
|:--:|
|*Degrau -1 1*|
## Linear
|![Linear](Linear.gif)|
|:--:|
|*Linear*|
## Logistica (Sigmoid)
|![Logistica (Sigmoid)](Logistica (Sigmoid).gif)|
|:--:|
|*Logistica (Sigmoid)*|
## Tangente Hiperbolica (Sigmoid)
|![Tangente Hiperbolica (Sigmoid)](Tangente Hiperbolica (Sigmoid).gif)|
|:--:|
|*Tangente Hiperbolica (Sigmoid)*|

# Perceptron vs Adaline vs Regreção logistica

O perceptron para de atializar quando acha qualquer reta que separe as classes.

|![Logistic Sigmoid](logistic_sigmoid.gif)|
|:--:|
|*Logistic Sigmoid*|

O Adaline ele consegue achar a melhor reta que separe as duas classes, mas o hiperplano se aproxima mais da classe com mais vetores de caracteristicas.

|![Logistic Sigmoid](logistic_sigmoid.gif)|
|:--:|
|*Logistic Sigmoid*|

A regreção linear acha o melhor hiperplano e não e influenciada pela quantidade de objetos em cada classe.

# MultiLayers Perceptron
 Usado para resolver problames XOR

 |![Problemas não lineares](xor.gif)|
|:--:|
|*Problemas não lineares*|

Na historia os marcos hitoricos forma:

    * 1957: Perceptron;
    * 1960: Adaline;
    * ??: Regreção Logistica;
    * 1986: Multilayer Perceptron e Backpropagation;
    * 1995: SVM;
    * 2006: Rede neural profunda.

