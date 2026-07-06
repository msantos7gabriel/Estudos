#include <iostream>

int main()
{
    // Operador Ternário ?: = Trica o if/else
    // Condição ? Expressão 1 : Expressão 2;

    double grade = 7.5;
    grade >= 6 ? std::cout << "Voce passou" : std::cout << "Voce perdeu";

    std::cout << "\n";

    int number = 9;
    9 % 2 == 0 ? std::cout << "Par" : std::cout << "Impar";
    // Não precisaria do Igual a zero pois o 1 é Igual a True e 0 Igual a false

    std::cout << "\n";

    bool hungry = true;
    hungry ? std::cout << "Voce esta com fome" : std::cout << "Voce esta cheio";
    // Outra maneira de escrever isso seria (Achei melhor)
    // std::cout << (hungry ? : "Voce esta com fome" : "Voce esta cheio");

    return 0;
}