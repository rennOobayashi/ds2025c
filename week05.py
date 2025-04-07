def check_parentheses(check_string : str) -> str:
    stack = []

    for data in check_string:
        if data == '(':
            stack.append(data)
        elif data == ')':
            if len(stack) == 0:
                return ("Wrong use of parentheses\r\n"
                        "(The closing parentheses must apper after the opening parentheses)")
            else:
                stack.pop()
    if len(stack) == 0:
        return "Normal"
    else:
        return ("Wrong use of parentheses\r\n"
                "(Need closing parentheses)")

s1 = "(Nayutan seijin)"
s2 = ")(Nayutan seijin)("

print(check_parentheses(s1))
print(check_parentheses(s2))