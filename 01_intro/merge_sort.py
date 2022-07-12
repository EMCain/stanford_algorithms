def merge(a, b):
    """
    a: first array
    b: second array
    returns: sorted array
    """
    print(f"A: {a}, B: {b}]")
    n = len(a + b)
    # make an array of that length
    c = [None] * n
    # pseudocode example uses 1-indexed arrays
    i = 0
    j = 0
    # what happens if the length is different?
    for k in range(0, n):
        print(f"i: {i}, j: {j}, k: {k}")

        if i > len(a) - 1 or j > len(b) - 1:
            print("done merging {a} and {b}")
            break
        print(f"Comparing A[{i}] {a[i]} and B[{j}] {b[j]}")
        if a[i] < b[j]:
            print(f"A[i] {a[i]} is less than B[j] {b[j]}")
            c[k] = a[i]
            i += 1
        else:
            print(f"B[j] {b[j]} is less than A[i] {a[i]}")
            c[k] = b[j]
            j += 1
        print(f"C is now {c}")
    if k < len(c):
        if i < len(a):
            result = c[:k] + a[i:]
        elif j < len(b):
            result = c[:k] + b[j:]
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    midpoint = len(arr) // 2
    a = arr[:midpoint]
    b = arr[midpoint:]

    a_sorted = merge_sort(a)
    b_sorted = merge_sort(b)

    return merge(a_sorted, b_sorted)


if __name__ == "__main__":
    # merge([1, 6], [5, 3])
    # res = merge([1, 66, 2], [5, 12, 42])
    # print(f"Final result is {res}")
    l10 = [3, 1, 6, 4, 5, 0, 7, 2, 8, 9]
    res = merge_sort(l10)
    print(f"Final result is {res}")
    l1_to_20 = [10, 8, 4, 13, 12, 2, 15, 16, 3, 17, 11, 18, 14, 5, 19, 1, 6, 9, 7]
    res = merge_sort(l1_to_20)
    print(f"Final result is {res}")
