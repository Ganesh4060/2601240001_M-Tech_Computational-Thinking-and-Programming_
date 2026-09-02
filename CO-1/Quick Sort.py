# Quick Sort - Product Price Sorting

def quick_sort(prices):
    # Base condition
    if len(prices) <= 1:
        return prices

    # Choose the last element as pivot
    pivot = prices[-1]

    left = []
    right = []

    # Divide the elements
    for price in prices[:-1]:
        if price <= pivot:
            left.append(price)
        else:
            right.append(price)

    # Sort left and right parts
    return quick_sort(left) + [pivot] + quick_sort(right)


# Main Program

print("========== PRODUCT PRICE SORTING ==========")

n = int(input("Enter number of products: "))

prices = []

for i in range(n):
    price = float(input(f"Enter price of product {i + 1}: ₹"))
    prices.append(price)

print("\nPrices Before Sorting:")
print(prices)

sorted_prices = quick_sort(prices)

print("\nPrices After Sorting:")
print(sorted_prices)

print("\nLowest Price  : ₹", sorted_prices[0])
print("Highest Price : ₹", sorted_prices[-1])

print("==========================================")