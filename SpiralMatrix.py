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
    flag = False
    while not flag:
        try:
            n = int(input("N = "))
        except ValueError:
            print("Oops, wrong type value of N! Try again...")
            continue
        if n <= 0:
            print("N must be positive! Try again...")
        else:
            flag = True
    flag = False
    while not flag:
        try:
            m = int(input("M = "))
        except ValueError:
            print("Oops, wrong type value of M! Try again...")
            continue
        if m <= 0:
            print("M must be positive! Try again...")
        else:
            flag = True
    print("="*32)
    print_m(spiral(n, m))


if __name__ == "__main__":
    main()

