def partition(numbers, start_index, end_index):
    # Select the middle value as the pivot.
    midpoint = start_index + (end_index - start_index) // 2
    pivot = numbers[midpoint]

    # "low" and "high" start at the ends of the list segment
    # and move towards each other.
    low = start_index
    high = end_index
    done = False
    # Add your code here
    while not done:
        # Move "low" to the right until you find a value greater than or equal to the pivot.
        while numbers[low] < pivot:
            low += 1

        # Move "high" to the left until you find a value less than or equal to the pivot.
        while numbers[high] > pivot:
            high -= 1

         
        # If there are no elements to swap, we're done.
        if low >= high:
            done = True

        else:

            # Swap the elements at "low" and "high".
            numbers[low], numbers[high] = numbers[high], numbers[low]

            # Move "low" and "high" one step further.
            low += 1
            high -= 1
    return high

def quicksort(numbers, start_index, end_index):
    # Only attempt to sort the list segment if there are
    # at least 2 elements
    if end_index <= start_index:
        return

    # Partition the list segment
    high = partition(numbers, start_index, end_index)

    # Recursively sort the left segment
    quicksort(numbers, start_index, high)

    # Recursively sort the right segment
    quicksort(numbers, high + 1, end_index)


# Main program to test the quicksort algorithm.
numbers = [12, 18, 3, 7, 32, 14, 91, 16, 8, 57]
print('UNSORTED:', numbers)

quicksort(numbers, 0, len(numbers) - 1)
print('SORTED:', numbers)
