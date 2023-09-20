def merge(numbers, i, j, k):
    merged_size = k - i + 1  # Size of merged partition
    merged_numbers = [0] * merged_size  # Dynamically allocates temporary array
    # for merged numbers
    merge_pos = 0  # Position to insert merged number
    left_pos = i  # Initialize left partition position
    right_pos = j + 1  # Initialize right partition position
    merge_pos = 0
    # Add smallest element from left or right partition to merged numbers
    
    # Add your code here
    while left_pos <= j and right_pos <= k:
        if numbers[left_pos] <= numbers[right_pos]:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos +=1
        else:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos +=1

        merge_pos +=1
    # If left partition is not empty, add remaining elements to merged numbers
    
    # Add your code here
    while left_pos <= j:
        merged_numbers[merge_pos]= numbers[left_pos]
        left_pos +=1
        merge_pos +=1

    # If right partition is not empty, add remaining elements to merged numbers

    # Add your code here
    while right_pos <= k:
        merged_numbers[merge_pos]= numbers[right_pos]
        right_pos +=1
        merge_pos +=1
    # Copy merge number back to numbers

    # Add your code here
    for merge_pos in range(merged_size):
        numbers[i+merge_pos] = merged_numbers[merge_pos]

def merge_sort(numbers, i, k):
    j = 0

    if i < k:
        j = (i + k) // 2  # Find the midpoint in the partition

        # Recursively sort left and right partitions
        merge_sort(numbers, i, j)
        merge_sort(numbers, j + 1, k)

        # Merge left and right partition in sorted order
        merge(numbers, i, j, k)


# Create a list of unsorted values
numbers = [61, 76, 19, 4, 94, 32, 27, 83, 58]

# Print unsorted list
print('UNSORTED:', numbers)

# Initial call to merge_sort
merge_sort(numbers, 0, len(numbers) - 1)

# Print sorted list
print('SORTED:', numbers)
