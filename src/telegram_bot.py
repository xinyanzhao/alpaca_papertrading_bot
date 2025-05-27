import requests
import logging

class TelegramBot:
    def __init__(self, token, chat_id):
        """初始化 Telegram Bot"""
        self.token = token
        self.chat_id = chat_id
        self.base_url = f"https://api.telegram.org/bot{token}"
        
    def send_message(self, text):
        """发送消息到 Telegram"""
        try:
            url = f"{self.base_url}/sendMessage"
            data = {
                "chat_id": self.chat_id,
                "text": text,
                "parse_mode": "HTML"
            }
            response = requests.post(url, data=data)
            if response.status_code == 200:
                logging.info(f"消息发送成功: {text[:50]}...")
            else:
                logging.error(f"消息发送失败: {response.status_code}, {response.text}")
            return response.json()
        except Exception as e:
            logging.error(f"发送 Telegram 消息时出错: {str(e)}")
            return None

    def send_trade_alert(self, symbol, side, quantity, price, time):
        """发送交易提醒"""
        emoji = "🟢" if side == "BUY" else "🔴"
        action = "买入" if side == "BUY" else "卖出"
        
        message = (
            f"{emoji} {action}信号\n"
            f"股票: {symbol}\n"
            f"数量: {quantity}\n"
            f"价格: {price}\n"
            f"时间: {time}"
        )
        return self.send_message(message)