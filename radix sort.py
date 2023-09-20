# Returns the maximum length, in number of digits, out of all list elements
def radix_get_max_length(numbers):
    max_digits = 0
    for num in numbers:
        digit_count = radix_get_length(num)
        if digit_count > max_digits:
            max_digits = digit_count
    return max_digits


# Returns the length, in number of digits, of value
def radix_get_length(value):
    if value == 0:
        return 1

    digits = 0
    while value != 0:
        digits += 1
        value = int(value / 10)
    return digits


def radix_sort(numbers):
    buckets = []
    for i in range(10):
        buckets.append([])
    max_digits = radix_get_max_length(numbers)
    pow10 = 1
    for digitIndex in range(max_digits):
        for num in numbers:
            bucketIndex = (abs(num) // pow10) % 10
            buckets[bucketIndex].append(num)
        numbers.clear()
        for bucket in buckets:
            numbers.extend(bucket)
            bucket.clear()
        pow10 = 10 * pow10

    # Add your code here
    negatives = []
    non_negatives = []
    for num in numbers:
        if num < 0:
            negatives.append(num)
        else:
            non_negatives.append(num)
    negatives.reverse()
    numbers.clear()
    numbers.extend(negatives + non_negatives)
    return numbers

# Create a list of unsorted values
numbers = [-9, 47, 81, 101, -5, 38, -99, 96, 51, -999, -11, 64]

# Print unsorted list
print('UNSORTED:', numbers)

# Call radix_sort to sort the list
radix_sort(numbers)

# Print sorted list
print('SORTED:', numbers)
