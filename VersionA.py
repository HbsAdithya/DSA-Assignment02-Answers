def insertionSort(Hand):
    for CardValue in range(1, len(Hand)):

        key = Hand[CardValue]

        j = CardValue - 1
        while j >= 0 and key < Hand[j]:
            Hand[j + 1] = Hand[j]
            j -= 1
        Hand[j + 1] = key


CardValuesArray = [12, 11, 13, 5, 6]
insertionSort(CardValuesArray)
for i in range(len(CardValuesArray)):
    print("% d" % CardValuesArray[i])
