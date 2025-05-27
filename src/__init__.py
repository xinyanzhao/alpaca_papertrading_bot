"""
Alpaca Paper Trading Bot
一个基于 Alpaca API 的自动化交易机器人，集成 Telegram 通知功能
"""

__version__ = '0.1.0'
__author__ = 'Your Name'

# 导出主要的类，方便其他模块导入
from .config import Config
from .strategy import BaseStrategy
from .telegram_bot import TelegramBot

__all__ = [
    'Config',
    'BaseStrategy',
    'TelegramBot',
]
