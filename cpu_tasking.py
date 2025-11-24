from collections import deque
import random

class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time
        print(f"Process {self.pid} created. Burst: {self.burst_time}ms")

    def run(self, quantum):
        if self.remaining_time > quantum:
            self.remaining_time -= quantum
            print(f" > P{self.pid} ran for {quantum}ms. Left: {self.remaining_time}ms")
            return True  # Still has remaining time
        else:
            time_ran = self.remaining_time
            self.remaining_time = 0
            print(f" > P{self.pid} ran for {time_ran}ms. Finished!")
            return False  # Finished

# Create p1, p2, p3 with random burst times between 5 and 25ms
p1 = Process(1, random.randint(5, 25))
p2 = Process(2, random.randint(5, 25))
p3 = Process(3, random.randint(5, 25))

# Round Robin Scheduling
time_quantum = 10
queue = deque([p1, p2, p3])

while queue:
    current = queue.popleft()
    still_remaining = current.run(time_quantum)
    if still_remaining:
        queue.append(current)
