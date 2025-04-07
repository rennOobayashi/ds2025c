def check_parentheses(check_string : str) -> str:
    stack = dict()
    stack["("] = []
    stack["{"] = []
    stack["["] = []

    for data in check_string:
        if data in stack.keys():
            stack[data].append(data)
        elif data == ')'  or data == '}' or data == ']':
            d = ''
            if data == ')': d = '('
            elif data == '}': d = '{'
            elif data == ']': d = '['

            if len(stack[d]) == 0:
                return ("Wrong use of parentheses\r\n"
                        "(The closing parentheses must apper after the opening parentheses)")
            else:
                stack[d].pop()

    if (len(stack["("]) + len(stack["{"]) + len(stack["["])) == 0:
        return "Normal"
    else:
        return ("Wrong use of parentheses\r\n"
                "(Need closing parentheses)")

s1 = "[{(Nayutan seijin)}]"
s2 = "}[(Nayutan seijin)[}"
s3 = "[((Nayutan seijin)]}"

print(check_parentheses(s1))
print(check_parentheses(s2))
print(check_parentheses(s3))