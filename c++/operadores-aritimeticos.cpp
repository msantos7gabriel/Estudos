#include <iostream>

int main()
{
    // Operadores aritméticos = retornam o resultado especifico de uma operação aritmética (+ - * /)
    // Ordem de execução:
    /*
        Parêntesis
        Multiplicação e Divisão
        Adição e Subtração
    */

    int students = 20;
    students += 2;
    students++;

    students -= 2;
    students--;

    students /= 3;

    int remainder = students % 3;

    students *= 10;

    std::cout << students;

    return 0;
}