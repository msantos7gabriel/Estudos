#include <iostream>
#include <math.h>

int main()
{
    char operador;
    double v1, v2;

    std::cout << "********** CALCULADORA **********\n";

    std::cout << "Escreva a operação que deseja ( + - * / ): ";
    std::cin >> operador;

    std::cout << "Escreva o Valor 1: ";
    std::cin >> v1;

    std::cout << "Escreva o Valor 2: ";
    std::cin >> v2;

    switch (operador)
    {
    case '+':
        std::cout << "A Soma entre: " << v1 << " Mais " << v2 << " e igual a = " << v1 + v2;
        break;
    case '-':
        std::cout << "A Subtração entre: " << v1 << " Menos " << v2 << " e igual a = " << v1 - v2;
        break;

    case '*':
        std::cout << "O Produto de: " << v1 << " Vezes " << v2 << " e igual a = " << v1 * v2;
        break;

    case '/':
        std::cout << "A Divisão entre: " << v1 << " Dividido Por " << v2 << " e igual a = " << (v1 / v2);
        break;
    default:
        std::cout << "Por favor insira uma operação valida ( + - * / )";
        break;
    }
    std::cout<< "\n*********************************";
    return 0;
}