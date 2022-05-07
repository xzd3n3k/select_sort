def select_sort(numbers):
    for x in range(len(numbers)):
        min_index = x

        for i in range(x+1, len(numbers)):
            if numbers[i] < numbers[min_index]:
                min_index = i

        numbers[x], numbers[min_index] = numbers[min_index], numbers[x]

    return numbers
# comment