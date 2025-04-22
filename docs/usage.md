## 使用说明

后端部署完成后，可通过 REST API 调用以下功能：
- GET `/bbr/status` 查看 BBR 状态
- POST `/bbr/enable` 启用 BBR
- POST `/sysctl/optimize` 自动优化网络参数
- GET `/speedtest` 执行网速测试

如需前端支持，可使用 Vue3 创建 Web UI 并调用上述接口。