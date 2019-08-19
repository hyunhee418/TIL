pattern = "test"
text = "This is a text to test."
i = 0
j = 0
while j != len(pattern) and j < len(pattern) and i < len(text):
    if pattern[j] != text[i]:
        i = i-j
        j = -1
    i += 1
    j += 1
    else:
        print(i)
