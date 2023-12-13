def maximum_value(array):
    Max = array[0]
    for num in array:
        if num > Max:
            Max = num
    return Max


def counting_sort(array, maxv):
    sorted = [0 for i in range(len(array))]
    count = [0 for r in range(maxv + 2)]

    for num in array:
        count[num] += 1
    for i in range(maxv + 1):
        count[i] += count[i - 1]
    for num in array:
        sorted[count[num] - 1] = num
        count[num] -= 1
    return sorted

# hello main
# mostmár jó


#valami ke

#mégegy comment