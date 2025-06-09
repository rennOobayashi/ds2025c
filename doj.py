ls = []

cnt = int(input())

for _ in range(cnt):
    s = input().split()

    if "push" in s and len(s) > 1:
        ls.append(s[-1])
    elif "pop" in s:
        if len(ls) == 0:
            print(-1)
            continue

        print(ls[-1])
        ls.pop()
    elif "top" in s:
        if len(ls) == 0:
            print(-1)
            continue
        print(ls[-1])
    elif "size" in s:
        print(len(ls))
    elif "empty" in s:
        if len(ls) == 0:
            print(1)
        else:
            print(0)
    else:
        print("error")
        continue
