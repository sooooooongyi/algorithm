#include <stdio.h>

int main() {
	int num;
	scanf("%d", &num);

	num = num * (num + 1) / 2;
	printf("%d", num);
}