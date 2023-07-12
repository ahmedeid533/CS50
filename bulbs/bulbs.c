#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    string message = get_string("message: ");
    int i = 0;
    int base ;

    while (message[i] != '\0')
    {
        base = 128;
        int num = message[i];
        while (base != 0)
        {
            int chk = num / base;
            if (chk)
            {
                print_bulb(1);
                num -= base;
            }
            else
            {
                print_bulb(0);
            }
            base /= 2;
        }
        printf("\n");
        i++;
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
