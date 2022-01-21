def solution(a, k):
    max_val = max(a)
    max_int= []
    for j in range(1, max_val):
        count = 0  # needs to >=k
        for item in a:
            count += int(item / j)
        if count >= k:
            max_int.append(j)
    return max(max_int)
    #last: iterate through max_int for max


print(solution([4, 4, 7, 1, 4, 9, 5, 5, 8, 4, 1, 1], 2))


#RIBBON cutting

# You are given an array of integers a, where each element a[i] represents the length of a ribbon.
# Your goal is to obtain k ribbons of the same length, by cutting the ribbons into as many pieces as you want.
# Your task is to calculate the maximum integer length L for which it is possible to obtain at least k ribbons of length L by cutting the given ones.
# Example
# For a = [5, 2, 7, 4, 9] and k = 5, the output should be solution(a, k) = 4.
