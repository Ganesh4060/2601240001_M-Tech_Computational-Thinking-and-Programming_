import heapq

# Create an empty priority queue
hospital_queue = []

# Number of patients
n = int(input("Enter number of patients: "))

# Add patients to the priority queue
for i in range(n):
    name = input("Enter patient name: ")
    severity = int(input("Enter severity (1-10): "))

    # Negative severity makes heapq work as a max-priority queue
    heapq.heappush(hospital_queue, (-severity, name))

print("\n--- Emergency Treatment Order ---")

# Serve patients according to severity
while hospital_queue:
    priority, name = heapq.heappop(hospital_queue)

    severity = -priority

    print("Serving:", name, "| Severity:", severity)
