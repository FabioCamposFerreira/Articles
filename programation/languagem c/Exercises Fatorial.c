#include <stdio.h>
#include <locale.h>
#include <conio.h>

//fatorial

int fatorial(int N)
{
	int f=1 , a ;
	for(a=1; N>=a; a++)
	{
		f = a*f;
	}
	return f;
}

void main()
{
	setlocale(LC_ALL, "Portuguese");
	int N, resultado;
	printf("Fatorial de N");
	printf("\nDigite N : ");
	scanf("%d", &N);
	resultado = fatorial(N);
	printf("O resultado é %d", resultado);
	getch();
}