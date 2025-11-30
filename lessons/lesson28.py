# lessons/lesson28.py
import asyncio
import time
import utils

utils.show_base_name(__file__, True)
# --- Part 1: Coroutines and Event Loop ---

async def say_hello():
    """A simple coroutine function."""
    print("Hello...")
    # 'await asyncio.sleep(1)' simulates an I/O operation (e.g., a network request).
    # It pauses this coroutine and allows the event loop to run other tasks.
    await asyncio.sleep(1)
    print("...World!")

async def count(name, limit):
    """A coroutine that counts up to a limit with delays."""
    print(f"Counter '{name}' started.")
    for i in range(1, limit + 1):
        print(f"Counter '{name}': {i}")
        await asyncio.sleep(0.5)
    print(f"Counter '{name}' finished.")

# --- Part 2: Running Tasks Concurrently ---

async def fetch_data(source_name, delay):
    """Simulates fetching data from a source after a delay."""
    print(f"Fetching data from {source_name}...")
    await asyncio.sleep(delay)
    print(f"Data from {source_name} received.")
    return {"source": source_name, "data": f"some data from {source_name}"}

async def main_async():
    """The main entry point for our asyncio lesson."""
    print("--- Lesson 28: asyncio, Coroutines, and Tasks ---")

    # 1. What is asyncio?
    # asyncio is a library to write concurrent code using the async/await syntax.
    # It's ideal for I/O-bound operations (like network requests, database access, file I/O)
    # where the program would otherwise spend a lot of time waiting.

    # 2. Coroutines and `await`
    # An 'async def' function defines a coroutine. Calling it returns a coroutine object.
    # The 'await' keyword passes control back to the event loop, pausing the
    # current coroutine until the awaited operation is complete.

    print("\n--- Running a single coroutine ---")
    start_time = time.time()
    # Calling a coroutine doesn't run it. It creates an object.
    coro = say_hello()
    print(f"Created a coroutine object: {coro}")
    # asyncio.run() starts the event loop and runs the coroutine until it's done.
    await coro
    print(f"Single coroutine finished in {time.time() - start_time:.2f} seconds.")
    print("-" * 20)

    # 3. Running multiple coroutines sequentially
    print("\n--- Running coroutines sequentially (using await) ---")
    start_time = time.time()
    await count("A", 2)
    await count("B", 2)
    print(f"Sequential execution finished in {time.time() - start_time:.2f} seconds.")
    print("-" * 20)

    # 4. Running multiple coroutines concurrently
    # To run tasks truly at the same time (concurrently), we need to schedule
    # them on the event loop using asyncio.create_task() or asyncio.gather().

    print("\n--- Running coroutines concurrently (using asyncio.gather) ---")
    start_time = time.time()
    # asyncio.gather() runs multiple awaitables concurrently.
    await asyncio.gather(
        count("Concurrent-A", 2),
        count("Concurrent-B", 2)
    )
    print(f"Concurrent execution finished in {time.time() - start_time:.2f} seconds.")
    print("-" * 20)

    # 5. Using asyncio.create_task()
    # asyncio.create_task() schedules the coroutine to run on the event loop as a "Task".
    # This gives more control over the task (e.g., you can cancel it).

    print("\n--- Running coroutines concurrently (using asyncio.create_task) ---")
    task1 = asyncio.create_task(count("Task-A", 3))
    task2 = asyncio.create_task(count("Task-B", 3))

    # 'await' on the tasks to ensure they complete before the main program exits.
    await task1
    await task2
    print("All tasks finished.")
    print("-" * 20)

    # 6. Practical Example: Gathering results from concurrent tasks
    print("\n--- Gathering results from concurrent API calls ---")
    start_time = time.time()

    results = await asyncio.gather(
        fetch_data("API 1", 1),
        fetch_data("Database", 2),
        fetch_data("File System", 0.5)
    )

    print(f"\nConcurrent data fetching finished in {time.time() - start_time:.2f} seconds.")
    print("Results:")
    for result in results:
        print(f"  - {result}")

    print("-" * 20)

if __name__ == "__main__":
    # To run an async function, we use asyncio.run().
    # This creates a new event loop and runs the main_async() coroutine.
    try:
        asyncio.run(main_async())
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    finally:
        utils.show_base_name(__file__, False)
else:
    utils.show_base_name(__file__, False)