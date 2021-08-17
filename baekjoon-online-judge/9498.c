#include <stdio.h>
#pragma warning(disable 4996)

int main() {
	int A;
	
	scanf("%d", &A);
	if (A >= 80) {
		if (A >= 90) printf("A");
		else printf("B");
	}
	else
	{
		if (A >= 70) printf("C");
		else {
			if (A >= 60) printf("D");
			else printf("F");
		}
	}
}