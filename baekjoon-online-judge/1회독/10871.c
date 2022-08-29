#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main() {
	int N, X;
	int * arr;
	scanf("%d %d", &N, &X);

	arr = (int *)malloc(N * sizeof(int));
	for (int i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
	}
	for (int i = 0; i < arr.length; i++) {
		if (arr[i] < X) {
			printf("%d", arr[i]);
		}
	}
}