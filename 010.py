from math import sqrt

def main():

    n = 2000000

    result = [True] * n

    for x in range(2,int(sqrt(n))):
        for y in range(x * 2, n, x):
            result[y] = False

    z = sum([i for i in range(2,n) if result[i]])

    return z

if __name__ == '__main__':
    print(main())
