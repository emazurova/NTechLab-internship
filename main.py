def findMaxSubArray(A):
    best_sum = float('-inf')
    current_sum = 0
    start_index = 0
    stop_index = 0
    is_all_negative = True
    for i, item in enumerate(A):
        current_sum += item
        if is_all_negative and best_sum < current_sum:
            best_sum = current_sum
        if current_sum <= 0:
            current_sum = 0
            start_index = i + 1
        else:
            is_all_negative = False
            if best_sum < current_sum:
                stop_index = i
                best_sum = current_sum

    if is_all_negative:
        return [best_sum]
    else:
        return A[start_index:stop_index + 1]

