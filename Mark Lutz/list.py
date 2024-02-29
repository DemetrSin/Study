matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print([matrix[i][i] for i in range(3).__reversed__()])
sum_gen = (sum(row * 2) for row in matrix)
print([i for i in sum_gen])
print(list(map(sum, matrix)))


l = list('spam and param')
l[4: 8] = []  # deletion
print(l)
