import threading
import time
import random

lock = threading.Lock()

class Job:
    def __init__(self, job_id, processing_time):
        self.job_id = job_id
        self.processing_time = processing_time

class Machine(threading.Thread):
    def __init__(self, machine_id, capacity, job_pool):
        super().__init__()
        self.machine_id = machine_id
        self.capacity = capacity
        self.job_pool = job_pool
        self.active_jobs = []

    def run(self):
        while True:
            lock.acquire()
            if not self.job_pool:
                lock.release()
                break

            if len(self.active_jobs) < self.capacity:
                job = self.job_pool.pop(0)
                self.active_jobs.append(job)
                lock.release()

                print(f"Machine {self.machine_id} assigned Job-{job.job_id}")
                time.sleep(job.processing_time)
                print(f"Machine {self.machine_id} completed Job-{job.job_id}")

                lock.acquire()
                self.active_jobs.remove(job)
                lock.release()
            else:
                lock.release()
                time.sleep(0.1)

jobs_list = [Job(i, random.randint(1, 9)) for i in range(1, 11)]

machines = [Machine(i, 5, jobs_list) for i in range(1, 4)]

for m in machines:
    m.start()

for m in machines:
    m.join()

print("\nAll jobs have been processed.\n")