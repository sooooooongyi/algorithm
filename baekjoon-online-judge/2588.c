#include <stdio.h>
#pragma warning(disable 4996)

int main() {
	int A, B;
	int n1, n2, n3;

	scanf("%d %d", &A, &B);
	n1 = B/100;
	B = B%100;
	n2 = B/10;
	B = B%10;
	n3 = B;

	printf("%d\n%d\n%d\n%d", A*n3, A*n2, A*n1, A*n3+ A * n2 * 10+ A * n1 * 100);
}