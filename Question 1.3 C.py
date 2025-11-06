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

                print(f"Machine: {self.machine_id} has been assigned Job: {job.job_id}")
                print(f"Machine: {self.machine_id} started Job {job.job_id}")
                time.sleep(job.processing_time)
                print(f"Machine: {self.machine_id} finished Job: {job.job_id}")

                lock.acquire()
                self.active_jobs.remove(job)
                lock.release()
            else:
                lock.release()
                time.sleep(0.1)
        print(f"Machine {self.machine_id} has completed all jobs.")

jobs_list = [Job(i, random.randint(1, 9)) for i in range(1, 11)]

m1 = Machine(1, 3, jobs_list)
m2 = Machine(2, 3, jobs_list)
m3 = Machine(3, 3, jobs_list)

m1.start()
m2.start()
m3.start()

m1.join()
m2.join()
m3.join()

print("\nAll jobs have been processed with capacity limits!\n")