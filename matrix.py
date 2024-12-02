def get_matrix(n, m,value):
    matrix = []
    for i in range(n):
        list_ = []
        matrix.append(list_)
        for j in range(m):
            list_.append(value)
    return matrix

n = int(input('Введите кол-во строк ', ))
m = int(input('Введите кол-во столбцов ', ))
value = int(input('Введите значение ячейки ', ))

result = get_matrix(n, m, value)
print(result)