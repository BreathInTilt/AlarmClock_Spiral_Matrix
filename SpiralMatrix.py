def print_m(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print("%3s"% a[i][j], end = ' ')
        print()
    print("="*32)



def spiral(n, m):
    a = [[0] * m for i in range(n)]

    i, j, d = 0, 0, 0
    moves = ((0, 1,), (1, 0,), (0, -1,), (-1, 0,),)
    for k in range(1, n * m + 1):
        a[i][j] = k
        for l in range(4):
            newD = (d + l) % 4
            di, dj = moves[newD]
            newI, newJ = i + di, j + dj
            if 0 <= newI < n and 0 <= newJ < m and a[newI][newJ] == 0:
                i, j, d = newI, newJ, newD
                break
    return a


def main():
    n = int(input("N = "))
    m = int(input("M = "))
    print("="*32)
    print_m(spiral(n, m))


if __name__ == "__main__":
    main()
