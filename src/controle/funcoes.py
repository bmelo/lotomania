def find(lista,item):
    pos = 0
    for index in lista:
        if index == item:
            return pos
        pos = pos +1
    return -1
