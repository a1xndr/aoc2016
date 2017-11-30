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
char min(int *arr)
{
    int min = 30;
    int mini = 0;
    for(int i=0; i< 26; i++)
    {
        if( arr[i] < min )
        {
            min = arr[i];
            mini = i;

        }
    }
    return 'a'+mini;
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
    for(int i=0; i<8; i++)
        printf("%c", min(&letfreq[i][0]));
    printf("\n");
}

