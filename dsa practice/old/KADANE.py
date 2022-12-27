arr = [-1, -4, 5, -15, 3]


def kadane(arr):
    current_max = arr[0]
    global_max = arr[0]
    for i in arr[1:]:
        if i > current_max + i:
            current_max = i
        else:
            current_max += i
        if current_max > global_max:
            global_max = current_max
    return global_max


print(kadane(arr))

cur = 5
gob = 5
