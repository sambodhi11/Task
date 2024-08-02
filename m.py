import os
import asyncio

async def add(m, n):
    print(f"PID 1: {os.getpid()}")
    print(f"Addition: {m + n}")
    await asyncio.sleep(30)
       
async def sub(m,n):
    print(f"PID 2: {os.getpid()}")
    print(f"Subtraction: {m -n}")
    await asyncio.sleep(30)
    
async def mul(m,n):
    print(f"PID 3: {os.getpid()}")
    print(f"Multiplication: {m*n}")
    await asyncio.sleep(30)

