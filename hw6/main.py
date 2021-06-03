from aiopath import AsyncPath
import asyncio
import os
from pathlib import Path
import sys
import shutil
from time import sleep, time
from uuid import uuid4


try:
    from helpers import *
except ModuleNotFoundError:
    from .helpers import *

path = root_path_dir

async def sort_files(path):
    futures = [rename_files(file) for file in path.iterdir() if file.is_file()]
    await asyncio.gather(*futures)

    futures = [moving_files(file) for file in path.iterdir() if file.is_file()]
    await asyncio.gather(*futures)


async def main(path):
    await sort_files(path)
    for item in path.iterdir():
        if item.is_dir() and item.name not in ignore_dir:
            await sort_files(item)
            await main(item)
            
            # Удаление пустых директорий
            try:
                item = AsyncPath(item)
                await AsyncPath.rmdir(item)
            except OSError:
                continue


try:
    if Path(path).exists():
        asyncio.run(main(path))
        show_result()
    else:    
        raise OSError
except OSError:
    print('You entered wrong path! Please, try again!')


