// Is it is a visa
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int check = 0;
    // Get the Visa Number From the User
    const long long VISA = get_long_long("Number: ");
    long long Visa = VISA;
    int i = 0;
    while (Visa != 0)
    {
        Visa /= 10;
        i++;
    }
    Visa = VISA;
    // Vaildation if its card or not

    if (i != 13 && i != 15 && i != 16)
    {
        printf("INVALID\n");
    }
    int one_use = Visa / 10000000000000;
    int one_use2 = Visa / 100000000000000;
    int one_use1 = Visa / 1000000000000000;
    int one_use0 = Visa / 1000000000000;
    // Check AMEX Card
    if (i == 15 && (one_use == 34 || one_use == 37))
    {
        printf("AMEX\n");
    }
    else if (i == 15)
    {
        printf("INVALID\n");
    }
    // Check Master Card
    if (i == 16 && (one_use2 > 50 && one_use2 <= 55))
    {
        printf("MASTERCARD\n");
        return 0;
    }

    int sum = 0;
    if ((i == 16  && one_use1 == 4) || (i == 13 && one_use0 == 4))
    {
        for (int j = 0; j < i; j++)
        {
            int visa = Visa % 10;
            Visa /= 10;
            if (j % 2)
            {
                visa *= 2;
                sum += visa % 10;
                sum += visa / 10;

            }
            else
            {
                sum += visa;
            }
        }
        if (sum % 10)
        {
            printf("INVALID\n");
        }
        else
        {
            printf("VISA\n");
        }
    }
    else if (i == 16)
    {
        printf("INVALID\n");
    }
    return 0;
}
