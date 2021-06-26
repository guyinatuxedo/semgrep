#include <stdlib.h>
#include <stdio.h>

void main(void)
{
	char dst;

	dst = malloc(0x100);

	memset(dst, 0x34, 50);
}
