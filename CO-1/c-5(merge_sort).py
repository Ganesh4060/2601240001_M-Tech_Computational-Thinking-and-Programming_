def merge_lists(a, b):
    result = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])

    return result


# Two sorted employee lists
a = [101, 105, 120, 150]
b = [103, 110, 130, 140]

result = merge_lists(a, b)

print(result)