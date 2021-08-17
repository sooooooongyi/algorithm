#include <stdio.h>
#pragma warning(disable 4996)

int main() {
	int H, M;

	scanf("%d %d", &H, &M);
	M = H * 60 + M - 45;

	H = M / 60;
	M = M % 60;

	printf("%d %d", H, M);
}