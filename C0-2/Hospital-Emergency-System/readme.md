# Heaps and Priority Queues

## 1. Hospital Emergency System

A hospital maintains a queue of patients according to their **severity**. A newly arriving critical patient must be served before patients with lower severity.

### Question

A hospital maintains a queue of patients according to severity.

**(a)** Explain why a heap is appropriate for this problem. **[2 Marks]**

**(b)** Design a Python priority queue using `heapq`. **[4 Marks]**

**(c)** Explain how the implementation differs from a normal FIFO queue. **[2 Marks]**

---

# Solution

According to the scenario, the hospital needs to serve patients based on their **severity**, not simply based on their arrival time.

Therefore, a **priority queue** is suitable for this problem.

A **heap** can efficiently maintain the patient with the highest priority so that the most critical patient can be served first.

---

# 1. Why is a Heap Appropriate?

A heap is appropriate because the hospital requires a **priority-based queue**.

In a normal queue, patients are served according to their arrival time.

However, in an emergency system:

* Each patient has a **severity level**.
* A patient with higher severity must be served first.
* A newly arriving critical patient can be served before patients who arrived earlier.
* A heap allows efficient insertion and removal of the highest-priority patient.

### Example

Suppose the hospital has the following patients:

| Patient | Severity |
| ------- | -------: |
| Ravi    |        2 |
| Arun    |        5 |
| Kiran   |        3 |

The treatment order should be:

```text
Arun → Kiran → Ravi
 5       3       2
```

Even though Ravi may have arrived first, Arun is served first because his severity is higher.

---

# 2. Priority Queue Using `heapq`

Python provides the built-in `heapq` module for implementing heaps.

`heapq` normally implements a **min-heap**, where the smallest value has the highest priority.

Since the hospital needs the **highest severity first**, we store the severity as a negative value.

## Python Implementation

See `hospital_emergency.py.py` in this folder.

---

# 3. How the Code Works

### Step 1: Import `heapq`

```python
import heapq
```

The `heapq` module provides functions for creating and manipulating heaps.

### Step 2: Create the Priority Queue

```python
hospital_queue = []
```

An empty Python list is used as the heap.

### Step 3: Get the Number of Patients

```python
n = int(input("Enter number of patients: "))
```

The user enters how many patients are waiting.

### Step 4: Get Patient Information

For every patient, the program asks for the patient name and severity level.

### Step 5: Insert Patient into the Heap

```python
heapq.heappush(hospital_queue, (-severity, name))
```

The negative severity makes Python's min-heap behave like a max-priority queue.

### Step 6: Serve Patients

```python
priority, name = heapq.heappop(hospital_queue)
```

The highest-severity patient is removed first.

---

# 4. Difference Between Priority Queue and FIFO Queue

A normal queue follows the **FIFO** principle:

> First In, First Out

The hospital emergency priority queue follows:

> Highest Priority First

| Normal FIFO Queue | Hospital Priority Queue |
| --- | --- |
| First patient is served first | Highest-severity patient is served first |
| Based on arrival time | Based on severity |
| Follows FIFO | Follows priority |

For example:

```text
Ravi   → Severity 2
Arun   → Severity 9
Kiran  → Severity 5
Rahul  → Severity 7
```

FIFO order:

```text
Ravi → Arun → Kiran → Rahul
```

Priority order:

```text
Arun → Rahul → Kiran → Ravi
 9       7       5       2
```

---

# 5. Time Complexity

### Insertion

`heapq.heappush()` takes **O(log n)**.

### Deletion

`heapq.heappop()` takes **O(log n)**.

### Access Highest Priority

The root can be accessed using `hospital_queue[0]` in **O(1)**.

### Space Complexity

The heap requires **O(n)** space for `n` patients.

---

# Algorithm

1. Import the `heapq` module.
2. Create an empty priority queue.
3. Read the number of patients.
4. Read each patient's name and severity.
5. Store negative severity in the heap.
6. Insert each patient using `heapq.heappush()`.
7. Remove patients using `heapq.heappop()`.
8. Convert the negative priority back to severity.
9. Display the treatment order.
10. Continue until all patients are served.
