''' This version of the function works only for sorted data vector
'''
def has_pair_with_sum(data, sum):
    low = 0
    high = len(data) - 1

    while low < high:
        s = data[low] + data[high]
        if s == sum:
            return True
        elif s > sum:
            high -= 1
        else:
            low += 1
    return False
        
