from config import Config
from strategy import BaseStrategy
from telegram_bot import TelegramBot
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
import time

def main():
    # 初始化组件
    config = Config()
    strategy = BaseStrategy()
    trading_client = TradingClient(config.ALPACA_API_KEY, config.ALPACA_SECRET_KEY, paper=True)
    telegram_bot = TelegramBot(config.TELEGRAM_BOT_TOKEN, config.TELEGRAM_CHAT_ID)
    
    try:
        while True:
            for symbol in config.SYMBOLS:
                # 获取数据
                data = trading_client.get_bars(symbol)
                
                # 生成信号
                signals = strategy.generate_signals(data)
                
                # 执行交易
                if strategy.should_entry():
                    # 创建买入订单
                    market_order_data = MarketOrderRequest(
                        symbol=symbol,
                        qty=config.QUANTITY,
                        side=OrderSide.BUY,
                        time_in_force=TimeInForce.DAY
                    )
                    order = trading_client.submit_order(market_order_data)
                    
                    # 发送 Telegram 通知
                    telegram_bot.send_message(
                        f"🟢 买入信号\n"
                        f"股票: {symbol}\n"
                        f"数量: {config.QUANTITY}\n"
                        f"价格: {order.filled_avg_price}\n"
                        f"时间: {order.filled_at}"
                    )
                    
                elif strategy.should_exit():
                    # 创建卖出订单
                    market_order_data = MarketOrderRequest(
                        symbol=symbol,
                        qty=config.QUANTITY,
                        side=OrderSide.SELL,
                        time_in_force=TimeInForce.DAY
                    )
                    order = trading_client.submit_order(market_order_data)
                    
                    # 发送 Telegram 通知
                    telegram_bot.send_message(
                        f"🔴 卖出信号\n"
                        f"股票: {symbol}\n"
                        f"数量: {config.QUANTITY}\n"
                        f"价格: {order.filled_avg_price}\n"
                        f"时间: {order.filled_at}"
                    )
                
            time.sleep(60)  # 每分钟检查一次
                    
    except KeyboardInterrupt:
        print("程序正常退出")
        
if __name__ == "__main__":
    main()