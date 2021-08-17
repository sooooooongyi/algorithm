#include <stdio.h>
#pragma warning(disable 4996)

int main() {
	double A, B;
	while (1) {
		scanf("%d %d", &A, &B);
		if (A > 0 && B < 10) { break; }
	}
	printf("%lf", A / B);
}