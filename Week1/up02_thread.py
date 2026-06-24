from time import sleep, ctime, time
import threading

def update_cup_number(customer_name):
    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    sleep(1)
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")

def make_coffee(customer_name):
    print(f"{ctime()} | Making coffee for {customer_name}...")
    sleep(1)
    print(f"{ctime()} | Coffee ready for {customer_name}!")

    update_cup_number(customer_name)

def main():
    customers = ["A", "B", "C"]
    threads = []

    print(f"{ctime()} | === Multi-threading Coffee Machine ===")

    start = time()

    for customer in customers:
        t = threading.Thread(
            target=make_coffee,
            args=(customer,)
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total_time = time() - start

    print(f"{ctime()} | Total time: {total_time:.2f} seconds")

if __name__ == "__main__":
    main()