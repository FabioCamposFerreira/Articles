#include <stdio.h>
#include <locale.h>
int main() { //dado um ano, informa se ele é bissexto
	setlocale(LC_ALL, "Portuguese");
	int ano, x, y;
	printf("Qual é o ano?\n");
	scanf("%d", &ano);
	x = ano%4;
	y = ano%100;
	if (x == 0) {
		if (y == 0) printf ("O ano %d não é bissexto.", ano);
		else printf ("O ano %d é bissexto.", ano);
	}
	else printf("O ano %d não é bissexto.", ano);
	system("pause");
	return 0;
}
