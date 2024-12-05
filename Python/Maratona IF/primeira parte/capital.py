# Chat GPT
def verificar_divisão(A):
    # Ordenando as áreas para facilitar a comparação
    A.sort()

    # Verificamos se a soma das áreas opostas é igual
    # A[0] + A[3] (primeira e última área) e A[1] + A[2] (segunda e terceira área)
    if A[0] + A[3] == A[1] + A[2]:
        return "S"
    else:
        return "N"


# Leitura da entrada
areas = list(map(int, input().split()))

# Saída do resultado
print(verificar_divisão(areas))
