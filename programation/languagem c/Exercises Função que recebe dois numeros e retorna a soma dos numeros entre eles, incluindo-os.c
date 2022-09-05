#include <stdio.h>
#include <locale.h>
#include <conio.h>

//Função que recebe dois numeros e retorna a soma dos numeros entre eles, incluindo-os

int soma(int N1, int N2)
{
	int soma=0, a;
	for ( a=N1 ; a<=N2 ; a++)
	{
		soma = a + soma;
	}
	return soma;	
}

void main ()
{
	setlocale(LC_ALL, "Portuguese");
	int N1, N2, S;
	printf(" Digite dois numeros para saber a soma dos numeros inteiros entre eles, incluindo-os.\n");
	scanf("%d, %d", &N1, &N2);
	S = soma(N1, N2);
	printf("\nA soma é %d", S);
	getch();
}