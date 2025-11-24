from collections import deque

class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time
        print(f"Process {self.pid} created. Burst: {self.burst_time}")

    def run(self, quantum):
        if self.remaining_time > quantum:
            self.remaining_time -= quantum
            print(f"> P{self.pid} ran for {quantum}ms. Left: {self.remaining_time}")
            return False  # Not finished yet
        else:
            time_ran = self.remaining_time
            self.remaining_time = 0
            print(f"> P{self.pid} ran for {time_ran}ms. Finished!")
            return True  # Finished

# Create processes
p1 = Process(1, 25)
p2 = Process(2, 15)
p3 = Process(3, 30)

process_list = deque([p1, p2, p3])
time_quan = 10

# Round-Robin scheduling
while process_list:
    proc = process_list.popleft()
    finished = proc.run(time_quan)
    if not finished:
        process_list.append(proc)  # Put back unfinished process
