# TO-DO: complete the helper function below to merge 2 sorted leftys
def merge(left, right):
    elements = len(left) + len(right)
    merged_arr = [0] * elements 
    # set up a counter
    index = 0
    # compare first index of each lefty
    while len(left) > 0 or len(right) > 0:
        try:
    # if a is less, overwrite current index in merged with a[0], else overwrite with b[0]
            if left[0] < right[0]:
                merged_arr[index] = left.pop(0)
    # increment counter and pop index that was added
                index += 1
            else:
                merged_arr[index] = right.pop(0)
                index += 1
    # recursively compare until all indeces shared between the two lists have been compared
        except:
    # if len(a) is 0 or len(b) is 0, overwrite the rest of merged with the remainder
            if len(left) == 0:
                for i in range(len(right)):
                    merged_arr[index] = right.pop(0)
                    index += 1
            if len(right) == 0:
                for i in range(len(left)):
                    merged_arr[index] = left.pop(0)
                    index += 1
    # return merged
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # break lefty in half, recursively until lefty lengths are 1
    if len(arr) > 1:
        mid = len(arr) // 2
        lsl = merge_sort(arr[:mid])
        rsl = merge_sort(arr[mid:])
        return merge(lsl, rsl)    
    return arr    
# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

