import time
import tracemalloc


N = 1_000_000


# -------------------------------
# List-based processing
# -------------------------------

tracemalloc.start()

start = time.perf_counter()

data = [i * 2 for i in range(N)]
total_list = sum(data)

list_time = time.perf_counter() - start

current, list_peak = tracemalloc.get_traced_memory()

tracemalloc.stop()


# -------------------------------
# Generator-based processing
# -------------------------------

tracemalloc.start()

start = time.perf_counter()

data_generator = (i * 2 for i in range(N))
total_generator = sum(data_generator)

generator_time = time.perf_counter() - start

current, generator_peak = tracemalloc.get_traced_memory()

tracemalloc.stop()


# -------------------------------
# Results
# -------------------------------

print("List Total:", total_list)
print("Generator Total:", total_generator)

print("\nList Processing Time:",
      round(list_time, 4), "seconds")

print("Generator Processing Time:",
      round(generator_time, 4), "seconds")

print("\nList Peak Memory:",
      round(list_peak / (1024 * 1024), 2), "MB")

print("Generator Peak Memory:",
      round(generator_peak / (1024 * 1024), 2), "MB")