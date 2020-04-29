def partition(Holder, low, high):
    Card = (low - 1)
    pivot = Holder[high]

    for j in range(low, high):
        if Holder[j] <= pivot:
            Card = Card + 1
            Holder[Card], Holder[j] = Holder[j], Holder[Card]

    Holder[Card + 1], Holder[high] = Holder[high], Holder[Card + 1]
    return Card + 1


def quickSort(Holder, low, high):
    if low < high:
        pi = partition(Holder, low, high)

        quickSort(Holder, low, pi - 1)
        quickSort(Holder, pi + 1, high)


CardValues = [10, 7, 8, 9, 1, 5]
n = len(CardValues)
quickSort(CardValues, 0, n - 1)
print("Sorted Card values are:")
for i in range(n):
    print("%d" % CardValues[i]),
