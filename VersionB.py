def insertionSort(Shrits):
    for i in range(1, len(Shrits)):

        key = Shrits[i]
        j = i - 1
        while j >= 0 and key < Shrits[j]:
            Shrits[j + 1] = Shrits[j]
            j -= 1
        Shrits[j + 1] = key


ShritSize = [12, 11, 13, 5, 6]
insertionSort(ShritSize)
for i in range(len(ShritSize)):
    print("% d" % ShritSize[i])

