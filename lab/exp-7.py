import threading
import multiprocessing
import queue
import time


# ---------------- THREADING ----------------

def threaded_producer(q, lock, count):
    for i in range(1, count + 1):
        time.sleep(0.2)

        with lock:
            q.put(i)
            print(f"Thread Producer: Produced {i}")


def threaded_consumer(q, lock, count):
    for _ in range(count):
        item = q.get()

        with lock:
            print(f"Thread Consumer: Consumed {item}")

        q.task_done()


def run_threading():
    print("\n--- Threading Producer-Consumer ---")

    q = queue.Queue(maxsize=3)
    lock = threading.Lock()

    producer = threading.Thread(
        target=threaded_producer,
        args=(q, lock, 5)
    )

    consumer = threading.Thread(
        target=threaded_consumer,
        args=(q, lock, 5)
    )

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    print("Threading execution completed.")


# ---------------- MULTIPROCESSING ----------------

def multiprocessing_producer(q, event, count):
    for i in range(1, count + 1):
        time.sleep(0.2)
        q.put(i)
        print(f"Process Producer: Produced {i}")

    event.set()


def multiprocessing_consumer(q, event):
    while True:
        try:
            item = q.get(timeout=1)
            print(f"Process Consumer: Consumed {item}")
        except queue.Empty:
            if event.is_set():
                break


def run_multiprocessing():
    print("\n--- Multiprocessing Producer-Consumer ---")

    q = multiprocessing.Queue(maxsize=3)
    event = multiprocessing.Event()

    producer = multiprocessing.Process(
        target=multiprocessing_producer,
        args=(q, event, 5)
    )

    consumer = multiprocessing.Process(
        target=multiprocessing_consumer,
        args=(q, event)
    )

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    print("Multiprocessing execution completed.")


if __name__ == "__main__":

    print("PRODUCER-CONSUMER APPLICATION")

    run_threading()
    run_multiprocessing()

    print("\nProgram completed successfully.")