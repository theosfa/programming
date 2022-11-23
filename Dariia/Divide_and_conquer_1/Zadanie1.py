def findMin(a, fr, to):
    if (fr==to-1):
        return a[fr]
    a1 = findMin(a, fr, (fr+to)//2)
    a2 = findMin(a, (fr+to)//2, to)
    return a1 if a1<a2 else a2

def findMax(a, fr, to):
    if (fr==to-1):
        return a[fr]
    a1 = findMax(a, fr, (fr+to)//2)
    a2 = findMax(a, (fr+to)//2, to)
    return a1 if a1>a2 else a2

if __name__ == '__main__':
    a = [3, 2, 0, 9, 6, 2, 1, 8]
    print("Min number is : " + str(findMin(a, 0, len(a))))
    print("Max number is : " + str(findMax(a, 0, len(a))))
