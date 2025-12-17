def transpose(mat):
    if len(mat) == 0:
        return []
    elif len(mat) == 1:
        b = [[] for _ in range(len(mat[0]))]
        for i in range(len(mat[0])):
            b[i] += [mat[0][i]]
        return b
    elif all(len(mat[i]) == 1 for i in range(len(mat))):
        c = [[]]
        for k in mat:
            c[0] += k
        return c
    elif all(len(mat[i]) == len(mat[i + 1]) for i in range(len(mat[0]) - 1)):
        a = [[] for _ in range(len(mat))]
        for k in range(len(mat)):
            for i in range(len(mat[0])):
                a[k] += [mat[i][k]]
        return a
    else:
        return "ValueError"


def row_sums(mat):
    k = len(mat[0])
    ans = []
    for i in mat:
        if k == len(i):
            ans.append(sum(i))
        else:
            return "ValueError"
    return ans


def col_sums(mat):
    ans = [0] * len(mat[0])
    k = len(mat[0])
    for i in range(len(mat)):
        if k == len(mat[i]):
            for j in range(len(mat[i])):
                ans[j] += mat[i][j]
        else:
            return "ValueError"
    return ans


print("transpose")
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))

print("row_sums")
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))

print("col_sums")
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
