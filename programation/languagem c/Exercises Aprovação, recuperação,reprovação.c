#include <stdio.h>
#include <conio.h>
#include <locale.h>
void main() {//media aritimetica de duas notas e a citua��o de aprovado, reprovado ou recupera��o
	setlocale(LC_ALL, "Portuguese");
	float N1, N2, Ma;
	printf("\nNota 1:");
	scanf("%f ", &N1);
	printf("\nNota 2:");
	scanf("%f", &N2);
	Ma = (N1 + N2) / 2;
	if( Ma < 7.0 ) {
		if (Ma <3.0) printf("\n Reprovado");
		else printf("\nRecupera��o");
	}
 	else printf("\n Aprovado");
	getch();
}