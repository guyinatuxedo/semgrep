#include <stdlib.h>
#include <stdio.h>

char dst[20];

void main(void)
{
	char src[50];
	bcopy(src, dst, 50);
}
