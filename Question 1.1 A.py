import threading
import time
import random

class Job:
    def __init__(self,job_id,processing_time):
        self.job_id = job_id
        self.processing_time = processing_time

class Machine(threading.Thread):
    def __init__(self, machine_id, jobs):
        super().__init__()
        self.machine_id = machine_id
        self.jobs = jobs

    def run(self):
        self.process_job()

    def process_job(self):
        for job in self.jobs:
            print(f"Machine: {self.machine_id} has been assigned Job: {job.job_id}")
            print(f"Machine: {self.machine_id} started Job: {job.job_id}")
            time.sleep(job.processing_time)
            print(f"Machine: {self.machine_id} finished Job: {job.job_id}")

jobs_list = [Job(i, random.randint(1,9)) for i in range(1,11)]

machine1 = jobs_list[:5]
machine2 = jobs_list[5:10]
machine3 = jobs_list[10:]

m1 = Machine(1, machine1)
m2 = Machine(2, machine2)
m3 = Machine(3, machine3)

m1.start()
m2.start()
m3.start()

m1.join()
m2.join()
m3.join()

print("\nAll jobs have been processed!\n")