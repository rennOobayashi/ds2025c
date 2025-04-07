def check_parentheses(check_string : str) -> bool:
    stack = []

    for data in check_string:
        if data == '(':
            stack.append(data)
        elif data == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    return len(stack) == 0

s1 = "(Nayutan seinjin)"
s2 = ")(Nayutan seinjin)("

if check_parentheses(s1):
    print("Normal.")
else:
    print("Wrong use of parentheses.")