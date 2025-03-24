import array

def move_zero(ls):
    zero_ind = 0

    for i, data in enumerate(ls):
        if data != 0:
            ls[zero_ind] = data

            if zero_ind != i:
                ls[i] = 0

            zero_ind += 1

    return ls

arr = array.array("i", [0, 99, -7, 0, 5, 15])

arr = move_zero(arr)

print(arr)