#A = [2, 2, 4, 5, 5, 5, 7, 7, 7, 7]
#i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#l = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
#len(A) == 10

def binsearch_left_boundary(array, x):
    left = -1
    right = len(array)
    while right - left > 1:
        middle = (left + right) // 2
        if array[middle] < x:
            left = middle
        else:
            right = middle
    return left


def binsearch_right_boundary(array, x):
    left = -1
    right = len(array)
    while right - left > 1:
        middle = (left + right) // 2
        if array[middle] <= x:
            left = middle
        else:
            right = middle
    return right


def main():
    A = [2, 2, 4, 5, 5, 5, 7, 7, 7, 7]
    x = int(input('Enter what to find x: '))
    print(binsearch_left_boundary(A, x))
    print(binsearch_right_boundary(A, x))


if __name__ == '__main__':
    main()

