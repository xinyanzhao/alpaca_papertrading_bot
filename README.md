# Alpaca Paper Trading Bot

基于 Alpaca API 的自动化交易机器人，集成 Telegram 通知功能。

## 功能特点

- 基于策略模式的交易系统
- 支持模拟交易测试
- Telegram 实时交易提醒
- PM2 进程管理

## 安装步骤

1. 克隆仓库：
```bash
git clone <your-repository-url>
cd alpaca_paperoder
```

2. 创建虚拟环境：
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 配置环境变量：
```bash
cp .env.example .env
# 编辑 .env 文件，填入你的配置信息
```

## PM2 使用说明

1. 安装 PM2：
```bash
npm install pm2 -g
```

2. 启动应用：
```bash
pm2 start ecosystem.config.js
```

3. 常用 PM2 命令：
```bash
# 查看应用状态
pm2 status

# 查看日志
pm2 logs

# 停止应用
pm2 stop quant-trading

# 重启应用
pm2 restart quant-trading

# 删除应用
pm2 delete quant-trading

# 保存当前进程列表
pm2 save

# 开机自启动
pm2 startup

# 监控
pm2 monit
```

4. 环境变量配置：
- development: `pm2 start ecosystem.config.js --env development`
- production: `pm2 start ecosystem.config.js --env production`

## 配置说明

在 `.env` 文件中配置：
- Alpaca API 密钥
- Telegram Bot Token 和 Chat ID
- 交易品种
- 交易数量等参数

## 注意事项

- 请确保在纸面交易模式下充分测试
- 实盘交易前请仔细检查策略逻辑
- 请妥善保管 API 密钥和 Telegram Token
