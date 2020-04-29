def partition(Holder, low, high):
    Shirt = (low - 1)
    pivot = Holder[high]

    for j in range(low, high):
        if Holder[j] <= pivot:
            Shirt = Shirt + 1
            Holder[Shirt], Holder[j] = Holder[j], Holder[Shirt]

    Holder[Shirt + 1], Holder[high] = Holder[high], Holder[Shirt + 1]
    return Shirt + 1


def quickSort(Holder, low, high):
    if low < high:
        pi = partition(Holder, low, high)

        quickSort(Holder, low, pi - 1)
        quickSort(Holder, pi + 1, high)


ShirtSize = [10, 7, 8, 9, 1, 5]
n = len(ShirtSize)
quickSort(ShirtSize, 0, n - 1)
print("Sorted Card values are:")
for i in range(n):
    print("%d" % ShirtSize[i]),
