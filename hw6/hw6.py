import asyncio
from asyncio import run, gather

from aiohttp import ClientSession
from aiopath import AsyncPath

text = 'example'


async def save_page(name, text):
    path = AsyncPath(name)
    print(path)

    if await path.exists():
        return

    async with path.open(mode='w') as file:
        await file.write(text)

    # async with ClientSession() as session:
    #     response = await session.get(url)
    #     content = await response.read()

    # await path.write_bytes(content)


async def main():
    # urls = [
    # 'https://example.com',
    # 'https://github.com/alexdelorenzo/aiopath',
    # 'https://alexdelorenzo.dev',
    # 'https://dupebot.firstbyte.dev']

    # scrapers = (save_page(url, f'{index}.html') for index, url in enumerate(urls))

    await asyncio.gather(save_page('test.py', text))

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # Обход 
asyncio.run(main())