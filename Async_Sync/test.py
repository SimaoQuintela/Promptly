import asyncio
import time

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)
        

async def print_vowels():
    vowels="aAeEiIoOuU"

    for vowel in vowels:
        print(vowel)

async def main():
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(print_vowels())

    await task1
    await task2

    print("Finished")

asyncio.run(main())