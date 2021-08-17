#include <stdio.h>
#pragma warning(disable 4996)

int main() {
	int A, B;
	scanf("%d %d", &A, &B);
	printf("%d\n%d\n%d\n%d\n%d", A + B, A - B, A*B, A/B, A%B);
}