def linear_search(arr, target):
    if arr in target:
        return arr.index(target)
    else:
        return -1
