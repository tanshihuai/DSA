def dbs(arr, target):
    length = len(arr)
    middle = length // 2
    if arr[middle] + arr[middle - 1] == target:
        return [arr[middle-1], arr[middle]]
    if length <= 2:
        return -1
    else:
        left = arr[:middle]
        right = arr[middle:]
        if arr[middle] + arr[middle-1] < target:
            return dbs(right, target)
        else:
            return dbs(left, target)
