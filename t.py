import os
from m import add, sub, mul
import signal
import asyncio

async def main():
    task = [
        asyncio.create_task(add(10, 5)),
        asyncio.create_task(sub(10, 5)),
        asyncio.create_task(mul(10, 5))
    ]
    await asyncio.gather(*task)


if __name__ == "__main__":
    asyncio.run(main())
#pid= os.getpid()
#print("Process ID is :",pid)

# add(10, 5)
# sub(10, 5)
# mul(10, 5)


