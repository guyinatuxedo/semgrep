#include <stdlib.h>
#include <stdio.h>

void main(void) {
	char inp = malloc(0x400);
	fgets(inp, 0x400, stdin);
}
