#include <stdio.h>
#pragma warning(disable 4996)

int main() {
	int A, B, C;
	while (1) {
		scanf("%d %d %d", &A, &B, &C);
		if (A >= 2 && B >= 2 && C <= 10000) { break; }
	}
	printf("%d\n%d\n%d\n%d", (A + B) % C, (A%C + B % C) % C, (A*B) % C, (A%C * B%C) % C);
}