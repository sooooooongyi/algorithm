#include <stdio.h>

int main() {
	int A, B;
	char ch;
	
	while (1) {
		scanf("%d %d", &A, &B);
		if ((ch = getchar()) == EOF) break;
		printf("%d\n", A + B);
	}
}