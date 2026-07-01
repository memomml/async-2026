import asyncio
import time

def log(msg):
    """พิมพ์ข้อความพร้อม timestamp แบบเดียวกับ time.ctime()"""
    print(f"{time.ctime()} {msg}")

async def greet_customer(name):
    log(f"Greeting for Customer-{name} ...")
    await asyncio.sleep(1)
    log(f"Greeting for Customer-{name} ...Done!")

async def serve_table(name):
    log(f"  [Task-{name}] Taking Order ...")
    await asyncio.sleep(1)
    log(f"  [Task-{name}] Taking Order ...Done!")

    log(f"  [Task-{name}] Cooking Spaghetti ...")
    await asyncio.sleep(1)
    log(f"  [Task-{name}] Cooking Spaghetti ...Done!")

    log(f"  [Task-{name}] Manage Bar for Drink ...")
    await asyncio.sleep(1)
    log(f"  [Task-{name}] Manage Bar for Drink ...Done!")

    log(f"  [Task-{name}] All served!")
    print()  # บรรทัดว่างหลัง "All served!" ของแต่ละโต๊ะ

async def main():
    start = time.time()

    # ช่วงที่ 1: ทักทายลูกค้าทีละคน (sequential)
    for name in ["A", "B", "C"]:
        await greet_customer(name)

    print()
    log("--- All customers greeted. Scheduling independent Async Tasks! ---")
    print()

    # ช่วงที่ 2: เสิร์ฟทุกโต๊ะพร้อมกัน (concurrent)
    tasks = [asyncio.create_task(serve_table(name)) for name in ["A", "B", "C"]]
    await asyncio.gather(*tasks)

    elapsed = time.time() - start
    log(f"Finished Entire Restaurant Operation in {elapsed:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())