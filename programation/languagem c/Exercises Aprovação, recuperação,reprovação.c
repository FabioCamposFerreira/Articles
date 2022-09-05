#include <stdio.h>
#include <conio.h>
#include <locale.h>
void main() {//media aritimetica de duas notas e a cituação de aprovado, reprovado ou recuperação
	setlocale(LC_ALL, "Portuguese");
	float N1, N2, Ma;
	printf("\nNota 1:");
	scanf("%f ", &N1);
	printf("\nNota 2:");
	scanf("%f", &N2);
	Ma = (N1 + N2) / 2;
	if( Ma < 7.0 ) {
		if (Ma <3.0) printf("\n Reprovado");
		else printf("\nRecuperação");
	}
 	else printf("\n Aprovado");
	getch();
}