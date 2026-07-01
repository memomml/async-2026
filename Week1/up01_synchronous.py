from time import sleep, ctime, time

def update_cup_number(customer_name):
<<<<<<< HEAD
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

    print(f"{ctime()} | === Synchronous Coffee Machine ===")

    start = time()

    for customer in customers:
        make_coffee(customer)

    total_time = time() - start

    print(f"{ctime()} | Total time: {total_time:.2f} seconds")
=======
    pass

def make_coffee(customer_name):
    pass

def main():
    pass
>>>>>>> upstream/main

if __name__ == "__main__":
    main()