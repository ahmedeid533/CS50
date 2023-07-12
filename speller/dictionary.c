// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cs50.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;
void free_node(node *p);
int strcicmp(char const *a, char const *b);

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int hashed = hash(&word[0]);
    node *head = table[hashed];
    while(head != NULL)
    {
        if (strcicmp(head->word, word) == 0)
        {
            return true;
        }
        head = head->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 65;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }
    char text[100];
    bool chk = true;
    while(chk)
    {
        if (fscanf(file, "%s", text) == EOF)
        {
            break;
        }

        int hashed = hash(text);
        node *new_node =  malloc(sizeof(node));
        new_node->next = table[hashed];
        table[hashed] = new_node;
        strcpy(new_node->word, text);

    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    int size = 0;
    for (int i = 0; i <= 25; i++)
    {
        node *head = table[i];
        while (head != NULL)
        {
            head = head->next;
            size++;
        }
    }
    return size;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i <= 25; i++)
    {
        node *head = table[i];
        free_node(head);
    }
    return true;
}

void free_node(node *p)
{
    if(p == NULL)
        return;
    free_node(p->next);
    free(p);
}
int strcicmp(char const *a, char const *b)
{
    for (;; a++, b++) {
        int d = tolower((unsigned char)*a) - tolower((unsigned char)*b);
        if (d != 0 || !*a)
            return d;
    }
}