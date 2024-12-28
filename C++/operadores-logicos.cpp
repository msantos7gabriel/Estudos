#include <iostream>

int main()
{

    // && - Checa se as duas condições são verdadeiras (AND)
    // !! - Checa se pelo menos uma das das condições é verdade (OR)
    // ! - Inverte o valor logico de seu operador

    int temp;

    std::cout << "Escreva a temperatura: ";
    std::cin >> temp;

    if (temp > 0 && temp < 30)
    {
        std::cout << "A temperatura esta boa!";
    }
    else
    {
        std::cout << "A temperatura esta ruim!";
    }
}


