#include <iostream>

using string_t = std::string;

int main()
{
    string_t name;
    int age;

    std::cout << "Qual o seu nome?: ";
    std::getline(std::cin >> std::ws, name); // Usado para ler linas que possuem espaços
    // O std::ws serve para o caso do o get line estiver em baixo de outro input,
    // serve para não aceitar o caractere \n do enter do teclado

    std::cout << "Qual sua idade?: ";
    std::cin >> age;

    std::cout << "Oi " << name << '\n';
    std::cout << "Voce tem " << age << " anos de idade";

    return 0;
}