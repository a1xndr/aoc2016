#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
typedef unsigned __int128 uint128_t;
char input[] = "^.^^^..^^...^.^..^^^^^.....^...^^^..^^^^.^^.^^^^^^^^.^^.^^^^...^^...^^^^.^.^..^^..^..^.^^.^.^.......";
int rows=400000-1;
int bitcount(uint128_t n)
{
	int c =0;
	while(n) {
		c += n & 1;
		n>>=1;
	}
	return c;
}
int main()
{
	int trows=rows+1;
	int count;
	uint128_t prevrow = 0;
	int len = strlen(input);
	uint128_t lenones = 0;
	for(int i =0; i < len; i++)
	{
		prevrow<<=1;
		prevrow |= ((input[i] == '^')&1);
		printf("%d", input[i]=='^');
		lenones<<=1;
		lenones |=1;
	}
	count += bitcount(prevrow);
	while(rows)
	{
		rows--;	
		uint128_t  row=0;
		row = prevrow>>1;
		row = lenones;
		row = (prevrow & ((prevrow << 1) ^ (prevrow >> 1))) | ( ~ prevrow & ((prevrow << 1) ^ (prevrow >> 1)));
		prevrow = (row)&lenones;
		count += bitcount(prevrow);
	}
	printf("\n%d\n", len*trows-count);
}

