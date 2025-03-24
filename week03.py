import array

arr = array.array("f", [99, -7, 1, 5, 15, 1])

for i in range(len(arr)):
    print(f"{arr[i]:4} {id(arr[i])}")
