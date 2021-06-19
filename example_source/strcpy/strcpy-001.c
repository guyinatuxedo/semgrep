#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main(void) {
	char src[20];
	char dst;

	dst = malloc(0x100);
	strcpy(dst, src);
}
