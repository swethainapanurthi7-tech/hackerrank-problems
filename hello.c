#include <stdio.h>

int main() {
    char s[100];

    // Read input string (including spaces)
    fgets(s, sizeof(s), stdin);

    // Print required output
    printf("Hello, World!\n");
    printf("%s", s);

    return 0;
}
