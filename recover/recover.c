#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cs50.h>
#include <stdint.h>

#define BLOCK_SIZE 512
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover [image disk]\n");
        return 1;
    }
    FILE *file = fopen(argv[1], "r");
    char filename[9];
    BYTE buffer[BLOCK_SIZE];
    int i = 0;
    FILE *img = NULL;

    while (fread(buffer, 1, BLOCK_SIZE, file) == BLOCK_SIZE)
    {
        bool good = false;
        bool newF = false;
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff)
        {
            good = true;
        }
        if (good == true && (buffer[3] & 0xf0) == 0xe0)
        {
            newF = true;
        }
        if (newF)
        {
            if (i > 0)
            {
                fclose(img);
            }
            sprintf(filename, "%03i.jpg", i);
            img = fopen(filename, "w");
            i++;
        }
        if (i > 0)
        {
            fwrite(buffer, 1, BLOCK_SIZE, img);
        }
    }
    fclose(img);
    fclose(file);
}