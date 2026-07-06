n = int(input())
numeros = list(map(int, input().split()))
estoque = set()  
contador = 0

for n in numeros:
    if n not in estoque:
        estoque.add(n)  
        contador += 2   
    else:
        estoque.remove(n)  

print(contador)

# O Set é mais rápido que uma lista
# https://www.youtube.com/watch?v=MGGGgrtlu4o

# # Vantagens ao usar set nesse caso:
# Busca rápida: A operação n in estoque agora ocorre em O(1) em vez de O(n), o que acelera muito o algoritmo.
# Inserção e remoção rápidas: Tanto a inserção (add) quanto a remoção (remove) também ocorrem em tempo constante O(1) em média.
# Portanto, usar um set é a melhor opção quando você precisa evitar duplicatas e realizar operações frequentes de busca e remoção, como no seu problema.