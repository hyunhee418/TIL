def stack(test):
    stack = []
    for idx in range(len(test)):
        if test[idx] == "(" or test[idx] == "{":
            stack.append(test[idx])

        elif test[idx] == ")":
            if (len(stack)):
                if stack.pop(len(stack)-1) != "(":
                    return False
            else:
                return False

        elif test[idx] == "}":
            if (len(stack)):
                if stack.pop(len(stack)-1) != "{":
                    return False
            else:
                return False

    if len(stack):
        return False
    else:
        return True

T = int(input())
for tc in range(1, T+1):
    S = str(input())
    print("#%d %d" %(tc, stack(S)))