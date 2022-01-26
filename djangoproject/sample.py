def countDuplicate(numbers):
    dup = []
    for i in numbers:
        if i not in dup and numbers.count(i) > 1:
            dup.append(i)
    return dup


print(countDuplicate([1, 2, 2, 3, 3]))
