



def stack(test):
    stack = []
    for idx in range(len(test)):
        if test[idx] == "(":
            stack.append(test[idx])

        elif test[idx] == ")":
            if (len(stack)):
                stack.pop(len(stack)-1)
            else:
                return False
    if len(stack):
        return False
    else:
        return True

print(stack("()()((()))"))
print(stack("((()((((()()((()())((())))))"))