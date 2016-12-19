#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
typedef unsigned __int128 uint128_t;
char input[] = "^.^^^..^^...^.^..^^^^^.....^...^^^..^^^^.^^.^^^^^^^^.^^.^^^^...^^...^^^^.^.^..^^..^..^.^^.^.^.......";
int rows=400000-1;
int popcount(uint128_t v)
{
		return __builtin_popcountll((uint64_t)(v >> 64u))
				       + __builtin_popcountll((uint64_t)(v));
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
	count += popcount(prevrow);
	while(rows)
	{
		rows--;	
		uint128_t  row=0;
		row = prevrow>>1;
		row = lenones;
		row = (prevrow & ((prevrow << 1) ^ (prevrow >> 1))) | ( ~ prevrow & ((prevrow << 1) ^ (prevrow >> 1)));
		prevrow = (row)&lenones;
		count += popcount(prevrow);
	}
	printf("\n%d\n", len*trows-count);
}

