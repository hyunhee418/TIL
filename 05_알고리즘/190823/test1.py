N = "1+2+3-8*6"
stack = []
for i in range(len(N)):

    if N[i] == "+" or N[i] =="-" or N[i] == "/" or N[i] == "*":
        stack.append(N[i])

    else:
        print(N[i], end="")

while stack != []:
    print(stack.pop(),end = "")