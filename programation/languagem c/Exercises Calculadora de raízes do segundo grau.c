#include <stdio.h>
#include <locale.h>
#include <conio.h>
#include <math.h>
void main (){//f�rmula de b�scara
	setlocale(LC_ALL, "Portuguese");
	float a, b, c, X1, X2, delta;
	printf("Calculadora de ra�zes do segundo grau.");
	printf("\nRetire da equa��o ax�+bx +c = 0 os coeficientes a, b e c:\n");
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
			printf("Essa equa��o s� tem uma ra�z que � %.2f", X1);
		}
		else {
			X1 = ((-b) - (sqrt(delta))) / (2*a);
			X2 = ((-b) + (sqrt(delta))) / (2*a);
			printf("As ra�zes desta equa��o s�o %.2f e %.2f", X1, X2);
		}
	}
	else printf("A equa��o � inv�lida ou n�o tem ra�zes!");
	getch();
}