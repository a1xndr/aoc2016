#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char max(int *arr)
{
    int max = 0;
    int maxi = 0;
    for(int i=0; i< 26; i++)
    {
        if( arr[i] > max )
        {
            max = arr[i];
            maxi = i;

        }
    }
    return 'a'+maxi;
}
main()
{
    int letfreq[8][26] = {0};
    FILE * fp;
    char line[10];
    fp = fopen("input", "r");
    while(fgets(line, sizeof(line), fp))
    {
        for(int i=0; i<strlen(line)-1; i++)
        {
            letfreq[i][line[i]-'a']+=1;
        }
    }
    for(int i=0; i<8; i++)
        printf("%c", max(&letfreq[i][0]));
    printf("\n");
}

