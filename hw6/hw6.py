from asyncio import run, gather

from aiohttp import ClientSession
from aiopath import AsyncPath


async def save_page(url: str, name: str):
    path = AsyncPath(name)

    if await path.exists():
        return

    async with ClientSession() as session:
        response = await session.get(url)
        content: bytes = await response.read()

    await path.write_bytes(content)


async def main():
    urls = [
    'https://example.com',
    'https://github.com/alexdelorenzo/aiopath',
    'https://alexdelorenzo.dev',
    'https://dupebot.firstbyte.dev']

    scrapers = (save_page(url, f'{index}.html') for index, url in enumerate(urls))

    await gather(*scrapers)


run(main())