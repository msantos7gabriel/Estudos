def is_triangle(a, b, c):
    return False if (a+b+c - max([a, b, c])) <= max([a, b, c]) else True


a = b = c = -1

print(is_triangle(a, b, c))
