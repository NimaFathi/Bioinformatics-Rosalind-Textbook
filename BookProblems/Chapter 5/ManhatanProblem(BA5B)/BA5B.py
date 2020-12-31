def manhatan_tourist(n,m,down,right):
    array = [[0 for _ in range(m+1)]for _ in range(n+1)]
    for i in range(1, m+1):
        array[0][i] = array[0][i-1] + right[0][i-1]
    for i in range(1, n+1):
        array[i][0] = array[i-1][0] + down[i-1][0]
    for i in range(1, n+1):
        for j in range(1,m+1):
            array[i][j] = max(array[i-1][j] + down[i-1][j], array[i][j-1] + right[i][j-1])
    return array[n][m]



if __name__ == '__main__':
    n, m = map(int, input().split())
    down = [[0 for i in range(m+1)] for j in range(n)]
    right = [[0 for i in range(m)] for j in range(n+1)]
    for i in range(n):
        mylist = list(map(int, input().split()))
        down[i] = mylist
    _ = input()
    for i in range(n+1):
        mylist1 = list(map(int, input().split()))
        right[i] = mylist1
    print(manhatan_tourist(n,m,down,right))