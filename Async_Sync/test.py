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
        await asyncio.sleep(0.25)


async def print_my_name(): # sou bué egocêntrico
    my_name = ["Simao", "Pedro", "Batista", "Caridade", "Quintela"]

    for name in my_name:
        print(name)
        await asyncio.sleep(1)
        


# Question: What's happening here?
# Answer: With the create_task method, I'm adding the tasks to the event pool. In the event pool the
# tasks are being executed asynchronously and with the await function I'm saying "wait for this function to end" before moving forward
async def main():
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(print_vowels())
    task3 = asyncio.create_task(print_my_name())
    
    await task1
    await task2
    await task3 

    print("Finished")

asyncio.run(main())