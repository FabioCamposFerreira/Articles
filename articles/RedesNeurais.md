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

![Perceptron usado para contruir uma porta AND](imgs/perceptron.jpg)

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

![Perceptron de Rosenblatt](imgs/rosenblatt.gif)

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

|![Perceptron de Rosenblatt](imgs/perceptron_linha.gif)|
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


|Interação|	$\hat{y}=\sigma(\vec{x}^T\vec{w})$  | Erro	$err=y-\hat{y}$|$\vec{w}=(w_1+err\times x_1,w_2+err\times x_2, w_3+err\times x_3)$ |
|----|----|-----|----|
|-        |	-|	-|$\vec{w}=(0,0)$|
|0        |	$\hat{y}=\sigma(1\times 0+0\times 0 + 0\times 0)=\sigma(0)=0$|	$err = 0-0=0$      |$\vec{w}=(0+0\times 1,0+0\times 0,0+0\times 0)=(0,0,0)$|
|1        |	$\hat{y}=\sigma(1\times 0+0\times 0 + 1\times 0)=\sigma(0)=0$|	$err = 0-0=0$      |$\vec{w}=(0+0\times 1,0+0\times 1,0+0\times 1)=(0,0,0)$|
|2        |	$\hat{y}=\sigma(1\times 0+1\times 0 + 0\times 0)=\sigma(0)=0$|	$err = 0-0=0$      |$\vec{w}=(0+0\times 1,0+0\times 1,0+0\times 0)=(0,0,0)$|
|3        |	$\hat{y}=\sigma(1\times 0+1\times 0 + 1\times 0)=\sigma(0)=0$|	$err = 1-0=1$      |$\vec{w}=(0+1\times 1,0+1\times 1,0+1\times 1)=(1,1,1)$|

* Epoch 2


|||||
|----|----|-----|----|
|0|	$\hat{y}=\sigma(1\times 1+0\times 1 + 0\times 1)=\sigma(1)=1$|	$err = 0-1=-1$|$\vec{w}=(1-1\times 1,1-1\times 0,1-1\times 0)=(0,1,1)$|
|1| $\hat{y}=\sigma(1\times 0+0\times 1 + 1\times 1)=\sigma(2)=1$|	$err = 0-1=-1$|$\vec{w}=(0-1\times 0,1-1\times 1,1-1\times 1)=(0,-1,-1)$|
