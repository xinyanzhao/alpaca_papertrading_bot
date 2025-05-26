# Alpaca Paper Trading Bot

一个基于 Alpaca API 的自动化交易机器人。

## 功能特点

- 基于策略模式的交易系统
- 支持纸面交易测试
- PM2 进程管理

## 安装步骤

1. 克隆仓库
2. 安装依赖: `pip install -r requirements.txt`
3. 复制 `.env.example` 到 `.env` 并填写配置
4. 使用 PM2 启动: `pm2 start ecosystem.config.js`

## 配置说明

在 `.env` 文件中配置:
- Alpaca API 密钥
- 交易品种
- 交易数量等参数

## 注意事项

- 请确保在纸面交易模式下充分测试
- 实盘交易前请仔细检查策略逻辑