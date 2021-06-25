#include <stdlib.h>
#include <stdio.h>

void test(char *dst)
{
	char src[10];
	bcopy(src, dst, 20);
}

void main(void)
{
	char dst[20];
	test(dst);
}
