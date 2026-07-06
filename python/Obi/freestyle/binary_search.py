"""
Returns either the index of the location in the array,
 or -1 if the array did not contain the targetValue 
"""


def do_search(array, targetValue):
    min_val = 0
    max_val = len(array) - 1
    guess = 0

    while min_val <= max_val:
        guess = (max_val + min_val) // 2
        if array[guess] > targetValue:
            max_val = guess - 1
        else:
            min_val = guess + 1

    return guess


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
          41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# A linha abaixo foi comentada para evitar que o programa trave em um loop infinito.
result = do_search(primes, 73)
print("Found prime at index " + str(result))

assert result == 20
