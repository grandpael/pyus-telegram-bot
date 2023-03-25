import config
from settings import *

# import l
import sqlite3
import asyncio

# import external
#

# import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.filters import CommandObject
from aiogram.types import FSInputFile
from loguru import logger

logger.debug('Bot QIWI Yes.')

# Объект бота
bot = Bot(token=config.token, parse_mode='HTML')

# Диспетчер для бота
dp = Dispatcher()