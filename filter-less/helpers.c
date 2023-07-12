#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int Gray = ((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0) + 0.5;
            image[i][j].rgbtRed = Gray;
            image[i][j].rgbtGreen = Gray;
            image[i][j].rgbtBlue = Gray;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int copy_rgbtRed = image[i][j].rgbtRed;
            int copy_rgbtGreen = image[i][j].rgbtGreen;
            int copy_rgbtBlue = image[i][j].rgbtBlue;
            int sepiaR = (.393 * copy_rgbtRed + .769 * copy_rgbtGreen + .189 * copy_rgbtBlue) + 0.5;
            int sepiaG = (.349 * copy_rgbtRed + .686 * copy_rgbtGreen + .168 * copy_rgbtBlue) + 0.5;
            int sepiaB = (.272 * copy_rgbtRed + .534 * copy_rgbtGreen + .131 * copy_rgbtBlue) + 0.5;
            if (sepiaR > 255)
            {
                sepiaR = 255;
            }
            if (sepiaG > 255)
            {
                sepiaG = 255;
            }
            if (sepiaB > 255)
            {
                sepiaB = 255;
            }
            image[i][j].rgbtRed = sepiaR;
            image[i][j].rgbtGreen = sepiaG;
            image[i][j].rgbtBlue = sepiaB;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE copy;
            copy.rgbtRed = image[i][j].rgbtRed;
            copy.rgbtGreen = image[i][j].rgbtGreen;
            copy.rgbtBlue = image[i][j].rgbtBlue;
            int LW = width - j - 1;
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
    RGBTRIPLE copy[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j].rgbtRed = image[i][j].rgbtRed;
            copy[i][j].rgbtGreen = image[i][j].rgbtGreen;
            copy[i][j].rgbtBlue = image[i][j].rgbtBlue;
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sumR = 0;
            int sumG = 0;
            int sumB = 0;
            int count = 0;
            for (int k = i - 1; k <= i + 1; k++)
            {
                for (int l = j - 1; l <= j + 1; l++)
                {
                    if (k < 0 || k >= height || l < 0 || l >= width)
                    {
                        continue;
                    }
                    else
                    {
                        sumR += copy[k][l].rgbtRed;
                        sumG += copy[k][l].rgbtGreen;
                        sumB += copy[k][l].rgbtBlue;
                        count++;
                    }
                }
            }
            int avgR = (((float)sumR / count)) + .5;
            int avgG = (((float)sumG / count)) + .5;
            int avgB = (((float)sumB / count)) + .5;
            image[i][j].rgbtRed = avgR;
            image[i][j].rgbtGreen = avgG;
            image[i][j].rgbtBlue = avgB;
        }
    }
    return;
}
