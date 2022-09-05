#include <stdio.h>
#include <locale.h>
#include <conio.h>
void main(){
	setlocale(LC_ALL, "Portuguese");
	int N, a, n;
	printf("Número:");
	scanf("%d", &N);
	for(n=1;n<N;n++){
	a = 1 +(n-1)*2;
	printf("%d, ", a);
	}
	a = 1 +(N-1)*2;
	printf("%d.", a);
	getch();
}