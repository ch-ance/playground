def hourglassSum(arr):
    hourglasses = []
    # go down to the fourth row
    for i in range(len(arr) - 2):
        # go to the right to the fourth column
        for j in range(len(arr) - 2):
            hourglasses.append([
            arr[i][j],
            arr[i][j + 1],
            arr[i][j + 2],
            arr[i + 1][j + 1],
            arr[i + 2][j],
            arr[i + 2][j + 1],
            arr[i + 2][j + 2]
            ])

    greatestSum = sum(hourglasses[0])
    for arr in hourglasses:
        currentSum = sum(arr)
        print(arr)
        print(currentSum)
        if currentSum > greatestSum:
            greatestSum = currentSum

    return greatestSum