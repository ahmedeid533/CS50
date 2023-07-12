#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for(int j = 0; j < width; j++)
        {
            BYTE Gray = (image[i][j].rgbtRed+image[i][j].rgbtGreen+image[i][j].rgbtBlue)/3;
            image[i][j].rgbtRed = Gray;
            image[i][j].rgbtGreen = Gray;
            image[i][j].rgbtBlue = Gray;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for(int j = 0; j < width/2; j++)
        {
            RGBTRIPLE copy;
            copy.rgbtRed = image[i][j].rgbtRed;
            copy.rgbtGreen = image[i][j].rgbtGreen;
            copy.rgbtBlue = image[i][j].rgbtBlue;
            int LW = width - j;
            image[i][j].rgbtRed = image[i][LW].rgbtRed;
            image[i][j].rgbtGreen = image[i][LW].rgbtGreen;
            image[i][j].rgbtBlue = image[i][LW].rgbtBlue;
            ///////
            image[i][LW].rgbtRed = copy.rgbtRed;
            image[i][LW].rgbtGreen = copy.rgbtGreen;
            image[i][LW].rgbtBlue = copy.rgbtBlue;
        }
        //width--;
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
