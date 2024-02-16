# Input: [3, 5, 2, 1, 7], k=2
# Output: 8
# The subarray [1, 7] is the sum of the maximum sum.
def find_maximum_sum_subarray(data, k ):
    window_sum = 0
    start = 0
    sum = 0
    for i in range(len(data)):
        window_sum += data[i]
        if (i - start + 1 == k):
            sum = max(sum, window_sum) 
            window_sum -= data[start]
            start += 1
    return sum    
    

data = [3, 5, 2, 1, 7]
k = 4
print(find_maximum_sum_subarray(data, k))