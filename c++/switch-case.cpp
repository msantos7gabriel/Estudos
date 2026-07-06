#include <iostream>

int main()
{
    int month;
    std::cout << "Escreva um Mes (1-12): ";
    std::cin >> month;

    switch (month)
    {
    case 1:
        std::cout << "E Janeiro";
        break;
    case 2:
        std::cout << "E Fevereiro";
        break;
    case 3:
        std::cout << "E Marco";
        break;
    case 4:
        std::cout << "E Abril";
        break;
    case 5:
        std::cout << "E Maio";
        break;
    case 6:
        std::cout << "E Junho";
        break;
    case 7:
        std::cout << "E Julho";
        break;
    case 8:
        std::cout << "E Agosto";
        break;
    case 9:
        std::cout << "E Setembro";
        break;
    case 10:
        std::cout << "E Outubro";
        break;
    case 11:
        std::cout << "E Novembro";
        break;
    case 12:
        std::cout << "E Dezembro";
        break;
    default:
        std::cout << "Por Favor escreva apenas numeros (1-12)";
        break;
    }

    return 0;
}