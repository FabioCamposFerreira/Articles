#include <stdio.h>
#include <locale.h>
#include <conio.h>

//x^y

int potencia(int x, int y)
{
	setlocale(LC_ALL, "Portuguese");
	int a=0, p=1;
	for(a=1;a<=y;a++)
	{
		p = x * p;
	}
	return p;	
}

void main()
{
	setlocale(LC_ALL, "Portuguese");
	int x, y, resultado;
	printf("Para x^y, digite x e y não negativos : ");       scanf("%d, %d", &x, &y);
	resultado = potencia(x, y);
	printf("x^y = %d", resultado); 
	getch();
}