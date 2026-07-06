def solution(s):
    x = []
    for l in s:
        if l.isupper():
            x.append(' '+l)
        else:
            x.append(l)
    return ''.join(x)


print(solution("camelCasing"))
