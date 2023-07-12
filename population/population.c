#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start;
    do
    {
        start = get_int("Start size: ");
    }
    while (start < 9);

    // TODO: Prompt for end size
    int End;
    do
    {
        End = get_int("End size: ");
    }
    while (End < start);

    // TODO: Calculate number of years until we reach threshold
    int years = start;
    int counter = 0;
    while (years < End)
    {
        int this_year = years;
        years += (this_year / 3);
        years -= (this_year / 4);
        counter++;
    }

    // TODO: Print number of years
      printf("Years: %i\n", counter);
}
