#include <stdio.h>

int main() {
    char ch;
    char s[100];
    char sen[100];

    // Read a single character
    scanf("%c", &ch);

    // Read a string (no spaces)
    scanf("%s", s);

    // Clear the newline left by previous scanf
    scanf("\n");

    // Read a full sentence (with spaces)
    scanf("%[^\n]%*c", sen);

    // Print outputs
    printf("%c\n", ch);
    printf("%s\n", s);
    printf("%s\n", sen);

    return 0;
}
