#include <stdlib.h>
#include <stdio.h>

void test(char *dst)
{
	memset(dst, 0x31, 20);
}

void main(void)
{
	char dst[20];
	test(dst);
}
