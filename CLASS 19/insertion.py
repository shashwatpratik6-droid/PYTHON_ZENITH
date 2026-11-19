def insertion_sort(a):
    n = len(a)
    i = 1
    while i < n:
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        i += 1
words = ["Banana","apple","fig","cherry"]
nums = [5, 2, 9, 1, 5, 6]
insertion_sort(words)
print(words)

# Output:

# [1, 2, 5, 5, 6, 9]
