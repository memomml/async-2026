
import asyncio
import time

async def update_cup_number(customer_name):
    print(f"{time.ctime()} | LCD: Processing for customer {customer_name}...")
    await asyncio.sleep(1)
    print(f"{time.ctime()} | LCD: Done for customer {customer_name}.")

async def make_coffee(customer_name):
    print(f"{time.ctime()} | Making coffee for {customer_name}...")
    await asyncio.sleep(1)
    print(f"{time.ctime()} | Coffee ready for {customer_name}!")

    await update_cup_number(customer_name)

async def main():
    print(f"{time.ctime()} | === Asyncio Coffee Machine ===")

    start_time = time.time()

    customers = ["A", "B", "C"]

    tasks = [make_coffee(customer) for customer in customers]
    await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"{time.ctime()} | Total time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())