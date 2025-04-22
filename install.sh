#!/bin/bash

# 安装依赖
apt update && apt install -y python3 python3-pip curl
pip3 install -r backend/requirements.txt

# 安装 Speedtest CLI
curl -s https://install.speedtest.net/app/cli/install.deb.sh | bash
apt install -y speedtest

# 启动服务
cd backend
nohup uvicorn app:app --host 0.0.0.0 --port 8000 &

echo "VPS Boost Panel 已启动：http://<your-ip>:8000/docs"