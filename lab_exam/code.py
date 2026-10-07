import time
import tracemalloc

# Take transactions from userN = int(input("Enter number of transactions: "))

transactions = []

n = int(input("Enter number of transactions: "))

for i in range(n):
    amount = float(input(f"Enter transaction {i + 1}: ₹"))
    transactions.append(amount)

THRESHOLD = float(input("Enter the threshold value: ₹"))

# ---------------- LIST ----------------
tracemalloc.start()

start_time = time.perf_counter()

filtered_list = [
    amount for amount in transactions
    if amount > THRESHOLD
]

list_time = time.perf_counter() - start_time

current, list_peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

list_count = len(filtered_list)

# ---------------- GENERATOR ----------------
def transaction_generator(data, threshold):
    for amount in data:
        if amount > threshold:
            yield amount


tracemalloc.start()

start_time = time.perf_counter()

filtered_generator = transaction_generator(
    transactions, THRESHOLD
)

generator_count = 0

for transaction in filtered_generator:
    generator_count += 1

generator_time = time.perf_counter() - start_time

current, generator_peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("\nList-Based Processing")
print("Records processed :", list_count)
print("Execution time    :", list_time, "seconds")
print("Peak memory       :", list_peak_memory / (1024 * 1024), "MB")

print("\nGenerator-Based Processing")
print("Records processed :", generator_count)
print("Execution time    :", generator_time, "seconds")
print("Peak memory       :", generator_peak_memory / (1024 * 1024), "MB")

if list_peak_memory > generator_peak_memory:
    print("\nList uses more additional memory.")
else:
    print("\nGenerator uses more additional memory.")