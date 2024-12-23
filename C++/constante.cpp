#include <iostream>

int main()
{
    // A contante especifica que o valor da variável é contante
    // Fala para o compilador para prefinir qualquer coisa de modificar ele
    // (Apenas leia)

    const double PI = 3.14159;
    const int LIGHT_SPEED = 299792458;
    double radius = 10;
    double circumference = 2 * PI * radius;

    std::cout << circumference << "cm";

    return 0;
}