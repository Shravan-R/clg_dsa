import asyncio
import random
import time
from collections import deque

class Printer:
    def _init_(self, name, delay_per_page=1):
        self.name = name
        self.delay_per_page = delay_per_page
        self.printing = False
        print(f"Printer '{self.name}' initialized (delay: {self.delay_per_page}s/page).")

    async def print_job(self, job):
        self.printing = True
        print(f"[{self.name}] Starting to print job '{job['name']}' ({job['pages']} pages).")
        for page_num in range(1, job['pages'] + 1):
            print(f"[{self.name}] Printing page {page_num} of '{job['name']}'...")
            await asyncio.sleep(self.delay_per_page)
        print(f"[{self.name}] Finished printing job '{job['name']}'.")
        self.printing = False


class Spooler:
    def _init_(self, printer_queue):
        self.printer_queue = printer_queue  # A list of available printers
        self.job_queue = deque()
        self.processing_task = None
        print("Spooler initialized.")

    def add_job(self, job_name, num_pages):
        job = {'name': job_name, 'pages': num_pages, 'status': 'queued'}
        self.job_queue.append(job)
        print(f"Spooler: Added job '{job_name}' to queue ({num_pages} pages).")

    async def _process_queue(self):
        while True:
            if self.job_queue:
                # Find an idle printer
                for printer in self.printer_queue:
                    if not printer.printing:
                        job = self.job_queue.popleft()
                        job['status'] = 'printing'
                        print(f"Spooler: Assigning job '{job['name']}' to '{printer.name}'.")
                        # Start printing in the background
                        asyncio.create_task(printer.print_job(job))
                        break
            await asyncio.sleep(0.5) # Check for new jobs/idle printers periodically

    async def start(self):
        if not self.processing_task:
            print("Spooler: Starting background processing.")
            self.processing_task = asyncio.create_task(self._process_queue())

    async def stop(self):
        if self.processing_task:
            print("Spooler: Stopping background processing.")
            self.processing_task.cancel()
            try:
                await self.processing_task
            except asyncio.CancelledError:
                pass
            self.processing_task = None

async def main():
    # Setup printers
    printer1 = Printer('HP_LaserJet', delay_per_page=1)
    printer2 = Printer('Epson_InkJet', delay_per_page=2)
    printers = [printer1, printer2]

    # Setup spooler with printers
    spooler = Spooler(printers)
    await spooler.start()

    # Simulate adding jobs asynchronously
    spooler.add_job('Report_A', 3)
    await asyncio.sleep(0.1)
    spooler.add_job('Invoice_B', 2)
    await asyncio.sleep(0.1)
    spooler.add_job('Document_C', 5)
    await asyncio.sleep(0.1)
    spooler.add_job('Photo_D', 1)

    print("\n--- Application continues while spooling... ---\n")
    # Simulate other application work
    for _ in range(3):
        print("Application: Doing other work...")
        await asyncio.sleep(random.uniform(0.5, 1.5))

    spooler.add_job('Presentation_E', 4)

    # Allow time for all jobs to complete
    print("\n--- Waiting for all printing to finish... ---\n")
    # A simple way to wait: wait until job queue is empty and no printer is active
    while spooler.job_queue or any(p.printing for p in printers):
        await asyncio.sleep(1)

    await spooler.stop()
    print("Simulator finished.")

# To run the simulator:
# In a Jupyter/Colab environment, you might need to use await main() directly if it's top-level.
# If running as a script, use asyncio.run(main()).

# Run the main asynchronous function
await main()