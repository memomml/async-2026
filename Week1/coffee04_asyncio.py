<<<<<<< HEAD
from time import ctime, time
import asyncio

# ฟังก์ชันจำลองการทำกาแฟแบบ Asynchronous
async def make_coffee(customer_name):
    print(f"{ctime()} กำลังชงกาแฟให้ ลูกค้า {customer_name}...")
    await asyncio.sleep(1) # จำลองเวลาชงกาแฟ 1 วินาที (แทน 1 นาที)
    print(f"{ctime()} ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!")

async def main():
    # คิวลูกค้า
    queue = ['A', 'B', 'C']
    print(f"{ctime()} === เริ่มระบบจำลองตู้กาแฟแบบ Asynchronous ===")
    start_time = time()
    
    # รวบรวมงาน (Task Gathering): ใช้ asyncio.gather เพื่อมัดรวมออเดอร์ของทุกคนแล้วโยนให้ Event Loop บริหาร
    tasks = [asyncio.create_task(make_coffee(customer)) for customer in queue]
    await asyncio.gather(*tasks)
    
    duration = time() - start_time
    print(f"{ctime()} ลูกค้า {len(queue)} คน ได้รับกาแฟครบแล้ว! ใช้เวลารวมทั้งหมด: {duration:0.2f} วินาที")

# สั่งให้ระบบ Async เริ่มทำงาน
if __name__ == "__main__":
    # ใช้ asyncio.run เพื่อเปิด Event Loop หลักของโปรแกรม
    asyncio.run(main())
=======
from time import ctime, time
import asyncio

# ฟังก์ชันจำลองการทำกาแฟแบบ Asynchronous
async def make_coffee(customer_name):
    pass

async def main():
    pass

# สั่งให้ระบบ Async เริ่มทำงาน
if __name__ == "__main__":
    # ใช้ asyncio.run เพื่อเปิด Event Loop หลักของโปรแกรม
    asyncio.run(main())
>>>>>>> upstream/main
