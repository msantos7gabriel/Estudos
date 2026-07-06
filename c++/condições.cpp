#include <iostream>

int main()
{
    // Condições = faça uma coisa se a condição estabelecida é verdadeira
    //             Se não, não faça isso.

    int age;
    std::cout << "Escreva sua idade: ";
    std::cin >> age;

    if (age >= 100)
    {
        std::cout << "Voce e muito velho para entrar nesse site";
    }
    else if (age < 0)
    {
        std::cout << "Voce ainda nem nasceu";
    }
    else if (age >= 18)
    {
        std::cout << "Bem Vindo ao site! ";
    }
    else
    {
        std::cout << "Voce nao e velho o suficiente para entrar!";
    }

    return 0;
}