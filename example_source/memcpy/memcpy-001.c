#include <stdlib.h>
#include <stdio.h>

void test(char *dst)
{
	char src[10];
	memcpy(dst, src, 20);
}

void main(void)
{
	char dst[20];
	test(dst);
}
