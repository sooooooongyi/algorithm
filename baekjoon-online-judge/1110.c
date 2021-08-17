#include <stdio.h>

int main() {
	int num, storeNum, N=0;

	scanf("%d", &num);
	storeNum = num;

	while (1) {
		num = storeNum % 10 + (storeNum/10+storeNum%10) % 10;
		if (num == storeNum) break;
		N++;
	}
	printf("%d", N);
}