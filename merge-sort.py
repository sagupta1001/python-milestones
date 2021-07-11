def merge(numbers, start_index, middle_index, end_index):
    sorted_numbers = []
    array_one_start = start_index
    array_two_start = middle_index + 1
    array_one_end = middle_index
    array_two_end = end_index

    i = array_one_start
    j = array_two_start
    while (i <= array_one_end and j <= array_two_end):
        if numbers[i] < numbers[j]:
            sorted_numbers.append(numbers[i])
            i += 1
        else:
            sorted_numbers.append(numbers[j])
            j += 1

    while (i <= array_one_end):
        sorted_numbers.append(numbers[i])
        i += 1

    while(j <= array_two_end):
        sorted_numbers.append(numbers[j])
        j += 1

    return sorted_numbers

def merge_sort(numbers, start_index, end_index):
    if start_index < end_index:
        middle_index = int((start_index + end_index ) / 2)
        merge_sort(numbers, start_index, middle_index)
        merge_sort(numbers, middle_index + 1, end_index)
        numbers[start_index: end_index+1] = merge(numbers, start_index, middle_index, end_index)

    return numbers

if __name__ == "__main__":
    numbers = [3, 1, 2, 4, 5, -1]
    print(f"Input numbers {numbers}")
    sorted_numbers = merge_sort(numbers.copy(), 0, len(numbers) - 1)
    print(f"Sorted numbers {sorted_numbers}")
