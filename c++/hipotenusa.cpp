#include <iostream>
#include <math.h>

int main()
{
    double a;
    double b;
    double c;

    std::cout << "Qual o valor do Lado A: ";
    std::cin >> a;

    std::cout << "Qual o valor do Lado B: ";
    std::cin >> b;

    c = sqrt(pow(a, 2) + pow(b, 3));
    std::cout << "A Hipotenusa desse triangulo e: " << c;
    

    return 0;
}