#include <stdio.h>
#include <locale.h>
#include <conio.h>

//M�dia Aritimetica e Ponderada de tr�s constantes

float media(char letra, int n1, int n2, int n3)
{
	setlocale(LC_ALL, "Portuguese");
	float M;
printf("%c, %d, %d, %d", letra, n1, n2, n3);
	if (letra == 'A')
	{
		M = (float) (n1+n2+n3)/3;
	}
	else
	{
		M = (float) (n1*5 + n2*3 + n3*2)/10;
	}
	return M;
}

void main()
{
	setlocale(LC_ALL, "Portuguese");
	char letra;
	int n1, n2, n3; 
	float resultado;
	printf("Para calcular a m�dia de tr�s notas, digite-as e tamb�m A para m�dia aritim�tica e outro car�ctere para ponderada.");
	printf("\nDigite o car�ctere : ");                 scanf("%c", &letra);
	printf("\nNota 1 : ");                       scanf("%d", &n1);
	printf("\nNota 2 : ");                       scanf("%d", &n2);
	printf("\nNota 3 : ");                       scanf("%d", &n3);
	resultado = media(letra, n1, n2, n3);
	printf("\nA media final � %.2f", resultado);
	getch();
}