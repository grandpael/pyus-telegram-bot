import config
from settings import *

# import l
import sqlite3
import asyncio

# import external
import subprocess
import traceback

# import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.filters import CommandObject
from aiogram.types import FSInputFile
from loguru import logger

logger.debug('Bot pyus.')

# Объект бота
bot = Bot(token=config.token)

# Диспетчер для бота
dp = Dispatcher()