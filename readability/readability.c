#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main(void)
{
    string text = get_string("Text: ");
    int chars = 0;
    int words = 0;
    int sentence = 0;

    for (int i = 0; text[i] != '\0'; i++)
    {
        if ((text[i] >= 'a' && text[i] <= 'z') || (text[i] >= 'A' && text[i] <= 'Z'))
        {
            chars++;
        }
        if (text[i] == ' ')
        {
            words++;
        }
        if (text[i] == '?' || text[i] == '.' || text[i] == '!')
        {
            sentence++;
            if (text[i + 1] == ' ')
            {
                i++;
            }
            words++;
        }
    }
    double L = ((float)chars / words) * 100;
    double S = ((float)sentence / words) * 100;
    printf("Letters %i\n", chars);
    printf("Words %i\n", words);
    printf("Sentence %i\n", sentence);

    double index = (0.0588 * L) - (0.296 * S) - 15.8;
    int Idx = index;
    if ((index - Idx) > 0.5)
    {
        Idx++;
    }
    if (Idx >= 2 && Idx < 16)
    {
            printf("Grade %i\n", Idx);
    }
    else if (Idx > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Before Grade 1\n");
    }

}