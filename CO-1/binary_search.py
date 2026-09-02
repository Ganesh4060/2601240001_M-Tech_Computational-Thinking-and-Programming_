books = list(range(1, 1000001))

target = int(input("Enter the book number to search: "))

low = 0
high = len(books) - 1

while low <= high:

    mid = (low + high) // 2

    if books[mid] == target:
        print("Book is available")
        print("Book Number:", target)
        break

    elif books[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

else:
    print("Book is not available")