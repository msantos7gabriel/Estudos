#include <iostream>
#include <vector>

// typedef std::vector<std::pair<std::string, int>> pairlist_t;
// typedef std::string text_t;
// typedef int number_t;

using text_t = std::string;
using number_t = int;
using pairlist_t = std::vector<std::pair<std::string, int>>;

int main()
{
    // Typedef = teclado reservado para criar um nome adicional para outro tipo de dado
    //  Novo identificador para um tipo existente
    //  Que te ajuda em reduzir os tipos
    // Usado quando é um beneficio claro
    // Trocado pelo 'Using' (Funciona melhor com Templates)

    pairlist_t pairlist;
    text_t first_name = "Bro";
    number_t age = 21;

    std::cout << first_name << '\n';
    std::cout << age << '\n';

    return 0;
}