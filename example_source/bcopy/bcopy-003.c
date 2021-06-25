#include <stdlib.h>
#include <stdio.h>

void main(void)
{
	char src[50];
	char dst;

	dst = malloc(0x100);

	bcopy(src, dst, 50);
}
