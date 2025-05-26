import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class Config:
    # Alpaca配置
    ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
    ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
    ALPACA_PAPER = os.getenv("ALPACA_PAPER", "True").lower() == "true"
    
    # Telegram配置
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
    
    # 交易参数
    SYMBOLS = eval(os.getenv("SYMBOLS", '["QQQ"]'))
    TIMEFRAME = os.getenv("TIMEFRAME", "1D")
    QUANTITY = int(os.getenv("QUANTITY", "100"))