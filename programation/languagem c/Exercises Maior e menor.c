#include <stdio.h>
#include <locale.h>
#include <conio.h>

//o maior e menor de cinco valores

void maiormenor(int a, int b, int c, int d, int f)
{
	setlocale(LC_ALL, "Portuguese");
	if(a>b && a>c && a>d && a>f) printf("O maior é %d", a);
	if(b>a && b>c && b>d && b>f) printf("O maior é %d", b);
	if(c>a && c>b && c>d && c>f) printf("O maior é %d", c);
	if(d>a && d>b && d>c && d>f) printf("O maior é %d", d);
	if(f>a && f>b && f>c && f>d) printf("O maior é %d", f);
	if(a<b && a<c && a<d && a<f) printf(" e o menor é %d", a);
	if(b<a && b<c && b<d && b<f) printf(" e o menor é %d", b);
	if(c<a && c<b && c<d && c<f) printf(" e o menor é %d", c);
	if(d<a && d<b && d<c && d<f) printf(" e o menor é %d", d);
	if(f<a && f<b && f<c && f<d) printf(" e o maior é %d", f);
	
}

void main()
{
	setlocale(LC_ALL, "Portuguese");
	int a, b, c, d, f;
	printf("Digite 5 numeros distintos : ");                 scanf("%d,%d,%d,%d,%d", &a, &b, &c, &d, &f);
	maiormenor(a, b, c, d, f);
	getch();
}