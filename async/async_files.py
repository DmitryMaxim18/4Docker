# PPEPARE FILES!
'''import random
for i in range(1000):
    oper = random.choice(range(1, 4))
    x = round(float(random.random()), 1)
    y = round(float(random.random()), 2)
    z = round(float(random.random()), 3)
    a = f'{oper}\n{x} {y} {z}'
    with open(f"in_{i}.dat", 'w') as file:
        file.write(a)'''


import asyncio
from functools import reduce
from time import time
import aiofiles


async def open_files():
    data = []
    try:
        for i in range(1, 1000):
            async with aiofiles.open(f"in_{i}.dat", 'r') as file:
                data.append(await file.read())
    except FileNotFoundError:
        pass
    return data


async def create_dict_data(data):
    dicts_data = []
    for x in data:
        file_dict = {'operation': (x.split('\n')[0]), 'nums': (x.split('\n')[1]).split(' ')}
        dicts_data.append(file_dict)
    return dicts_data


async def calculate_data(dict_data):
    final_sum = []
    for i in dict_data:
        if i['operation'] == '1':
            final_sum.append(round(sum([float(x) for x in i['nums']]), 1))
        if i['operation'] == '2':
            final_sum.append(round(reduce(lambda x, y: float(x)*float(y), i['nums']), 1))
        if i['operation'] == '3':
            final_sum.append(round(sum([(float(x)**2) for x in i['nums']]), 1))
    async with aiofiles.open('out.dat', 'w') as f:
        await f.write(str(sum(final_sum)))
    return sum(final_sum)


async def main():
    data = await open_files()
    dict_data = await create_dict_data(data)
    tasks = []
    for i in range(5):
        tasks.append(asyncio.ensure_future(calculate_data(dict_data)))

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = time()
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
    print(time() - t0)