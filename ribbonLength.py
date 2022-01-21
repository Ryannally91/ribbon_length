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



