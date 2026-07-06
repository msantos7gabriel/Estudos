def printer_error(s):
    tam = len(s)
    for i in range(97, 110):
        s = s.replace(chr(i), '')
    return f'{len(s)}/{tam}'


s = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
print(printer_error(s))
