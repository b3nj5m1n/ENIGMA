#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int steckerPairsCount;
int **steckerPairs;

/* 
   Takes an array of intergers as input and parses them into stecker pairs
   2 integers will get grouped together
   */
int setStecker(int *pairsValues, int individualCount)
{
    // Make sure there is an even number of integers
    if (individualCount % 2 != 0)
    {
        printf("Cannot initialize stecker pairs with uneven number of integers.");
        exit(1);
    }
    // Allocate memory for steckerPairs variable
    steckerPairs = malloc(individualCount / 2 * sizeof( int* ));
    // Loop over values, 2 at a time
    for (int i = 0; i < individualCount; i+=2)
    {
        // Allocate memory and insert pair into steckerPairs
        int index = i/2;
        steckerPairs[index] = malloc(sizeof( int )*2);
        steckerPairs[index][0] = pairsValues[i];
        steckerPairs[index][1] = pairsValues[i+1];
        // Test if we just inserted a duplicate
        for (int j = 0; j < steckerPairsCount; j++)
        {
            if (steckerPairs[j][0] == steckerPairs[index][0]
                    || steckerPairs[j][1] == steckerPairs[index][0] 
                    || steckerPairs[j][0] == steckerPairs[index][1] 
                    || steckerPairs[j][1] == steckerPairs[index][1]) {
                printf("Duplicate in stecker pairs.");
                exit(2);

            }
        }
        // Increase pair count
        steckerPairsCount += 1;
        // Print the pair
        printf("%d:%d\n", steckerPairs[index][0], steckerPairs[index][1]);
    }
    return 0;
}

/*
   Takes a single integer as intput and passes it through the steckbrett
   */
int steckerEncode(int input)
{
    // Loop over all pairs and try to find a match
    for (int i = 0; i < steckerPairsCount; i++)
    {
        if (steckerPairs[i][0] == input)
        {
            return steckerPairs[i][1];
        }
        else if (steckerPairs[i][1] == input)
        {
            return steckerPairs[i][0];
        }
    }
    // The input is not mapped to anything on the steckbrett, just return it
    return input;
}

/*
   Free all resources used by the steckbrett
   */
int removeStecker()
{
    for (int i = 0; i < steckerPairsCount; i++)
    {
        free(steckerPairs[i]);
    }
    free(steckerPairs);
}

int main() {
    int test[6] = { 2, 15, 1, 4, 5, 12 };
    setStecker(test, 6);

    for (int i = 0; i < 10; i++)
    {
        printf("Testing %d, result: %d\n", i, steckerEncode(i));
    }

    removeStecker();

    return 0;
}
