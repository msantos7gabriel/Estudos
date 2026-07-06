def filter_list(l):
    new_list = []
    for i in l:
        if isinstance(i, int):
            if i >= 0:
                new_list.append(i)
    return new_list


list = [1, 2, 'aasf', '1', '123', 123]
print(filter_list(list))
