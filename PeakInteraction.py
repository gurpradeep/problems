def peak_interaction_times(interaction, hours):
    sums = [] 
    curr_sum = 0
    for i, x in enumerate(interaction):
        curr_sum += x
        if i >= hours: 
            curr_sum -= interaction[i - hours]
        if i >= hours - 1: 
            sums.append(curr_sum)

    left = [0] * len(sums)
    best = 0
    for i in range(len(sums)):
        if sums[i] > sums[best]:
            best = i
        left[i] = best

    right = [0] * len(sums)
    best = len(sums) - 1
    for i in range(len(sums) - 1, -1, -1):
        if sums[i] >= sums[best]:
            best = i
        right[i] = best

    output = None
    for j in range(hours, len(sums) - hours):
        i = left[j - hours]
        l = right[j + hours]
        if output is None or (sums[i] + sums[j] + sums[l] > sums[output[0]] + sums[output[1]] + sums[output[2]]):
            output = [i, j, l]
    return output

# Driver code
interaction = [0, 2, 1, 3, 1, 7, 11, 5, 5]
hours = 2
print(peak_interaction_times(interaction, hours))