#include <stdio.h>
#include <locale.h>
#include <conio.h>
#include <math.h>
void main (){//fórmula de báscara
	setlocale(LC_ALL, "Portuguese");
	float a, b, c, X1, X2, delta;
	printf("Calculadora de raízes do segundo grau.");
	printf("\nRetire da equação ax²+bx +c = 0 os coeficientes a, b e c:\n");
	printf("a =");
	scanf("%f", &a);
	printf("b =");
	scanf("%f", &b);
	printf("c =");
	scanf("%f", &c);
	delta = (b*b) - (4*a*c);
	if ((a != 0) && (delta >= 0)) {
		if (delta == 0) {
			X1 = (-b) / (2*a);
			printf("Essa equação só tem uma raíz que é %.2f", X1);
		}
		else {
			X1 = ((-b) - (sqrt(delta))) / (2*a);
			X2 = ((-b) + (sqrt(delta))) / (2*a);
			printf("As raízes desta equação são %.2f e %.2f", X1, X2);
		}
	}
	else printf("A equação é inválida ou não tem raízes!");
	getch();
}