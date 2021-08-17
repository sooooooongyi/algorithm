#include <stdio.h>
#pragma warning(disable 4996)

int main() {
	int year, isYear=0;

	scanf("%d", &year);
	if (year % 4 == 0)
	{
		if (year % 100 == 0)
		{
			if (year % 400 == 0) isYear = 1;
		}
		else isYear = 1;
	}
	printf("%d", isYear);
}