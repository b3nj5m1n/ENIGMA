#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct rotor {
    // "VIII", "UKW B", ...
    char kind[10];
    // "1939", "15.12.1938", ...
    char date[10];
    // "Enigma I", "M3", ...
    char model[20];
    // "ETW", "NORMAL", ...
    char wer[15];
    int *wiring;
    int *notch;
};

typedef struct rotor Rotor;

/*
Returns a rotor
*/
Rotor getRotor(char *kind, char *date, char *model, char *wer, int *wiring, int *notch)
{
    Rotor *result = malloc(sizeof(Rotor));
    strcpy(kind, kind );
    strcpy(date, date );
    strcpy(model, model );
    strcpy(wer, wer );
    wiring = wiring;
    notch = notch;
}

int main()
{
    int wiring[5] = { 3, 4, 2, 1, 0 };
    int notch[2] = {2, 1};
    struct rotor r = getRotor("VIII", "1969", "M3", "ETW", wiring, notch);
    printf("Moin");
}
