#include <stdio.h>
double different_birthdays(int n){
    return n == 1 ? 1.0 : different_birthdays(n - 1) * (365.0 - (n - 1)) / 365.0;
}

int main(void){
    int n;
    for (n = 1; n <= 365; n++)
        printf("%3d: %e\n", n, 1.0 - different_birthdays(n));
    return 0;
}