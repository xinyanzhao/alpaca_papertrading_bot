from abc import ABC, abstractmethod
import pandas as pd

class BaseStrategy(ABC):
    def __init__(self):
        self.position = None
        self.data = None
    
    @abstractmethod
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """生成交易信号"""
        pass
    
    @abstractmethod
    def should_entry(self) -> bool:
        """入场判断"""
        pass
    
    @abstractmethod
    def should_exit(self) -> bool:
        """出场判断"""
        pass