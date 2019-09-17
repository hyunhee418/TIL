def SelectionSort(A, min, i, s):
    if i >= len(A)-1:
        return
    else:
        if s >= len(A):
            A[min], A[i] = A[i], A[min]
            SelectionSort(A, i+1, i + 1, i + 2)
        else:
            if A[min] > A[s]:
                min = s
            SelectionSort(A, min, i, s+1)


li = [1, 5, 6, 2, 4, 7, 9, 5]
SelectionSort(li, 0, 0, 1)
print(li)