#include <iostream>

int main()
{
    // Conversão de tipo = Conversão de um valor de um tipo de dado para outro
    // Implícito = Automático
    // Explicito = Procede o valor com um novo tipo de dado (int)
    // Serve para converter valores em divisões inteiras

    int x = 3.14;

    std::cout << x << '\n'; // Implicitamente converte o valor da variável

    double y = (int)3.14;

    std::cout << y << '\n';

    int correct = 8;
    int questions = 10;
    double score = correct / (double)questions * 100;

    std::cout << score << '%' << '\n';

    return 0;
}