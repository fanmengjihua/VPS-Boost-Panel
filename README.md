 VPS-Boost-Panel 🚀

VPS-Boost-Panel 是一款用于优化 VPS 网络性能的开源工具，支持 BBR/BBRv3、TCP 调优、测速等功能。它能够帮助用户提升网络吞吐量、降低延迟，并提供实时网速测试，方便评估网络性能. 🌐⚡

---

 特性 ✨

- 启用 BBR/BBRv3 🚀：通过启用 BBR 或 BBRv3，显著提升网络吞吐量和降低延迟。
- TCP 系统优化 ⚙️：自动调整系统的 TCP 参数，优化网络连接，提升数据传输效率。
- Speedtest 网速测试 📊：提供实时的网速测试，帮助用户实时了解网络性能。
- REST API 支持 🔗：提供完整的 API 接口，便于与前端框架（如 Vue）集成，构建自定义管理界面。
- 跨平台支持 💻：支持在各种 Linux 发行版上运行，包括 Ubuntu、CentOS 和 Debian。

---

 技术栈 🛠️

- 后端：Python（主要用于逻辑处理和功能实现）
- 脚本：Shell（用于系统配置和自动化任务）
- 前端：支持 Vue.js 集成，通过 REST API 构建自定义面板

---

 安装步骤 🔧

1. 克隆项目代码：

    ```bash
    git clone https://github.com/fanmengjihua/VPS-Boost-Panel.git
    cd VPS-Boost-Panel
    ```

2. 运行安装脚本：

    ```bash
    bash install.sh
    ```

3. 安装完成后，您可以访问 `http://your-server-ip:8000/docs` 查看 API 文档 📖。

---

 配置与使用 ⚙️

- 启用 BBR/BBRv3 🚀：默认情况下，系统将自动启用 BBR 或 BBRv3，您可以根据需求选择相应的版本。
- TCP 参数优化 🔧：安装完成后，工具将自动优化 TCP 系统设置，您可以通过 `vps-boost --status` 查看当前设置。
- Speedtest 测试 🌐：通过 `vps-boost --speedtest` 命令，您可以实时查看网络速度和延迟。

---

 贡献 💡

欢迎任何形式的贡献！如果您发现了 bug 🐛 或有功能建议 💬，请提交 Issue 或 Pull Request。

---

 开源协议 📜

该项目采用 [MIT License](LICENSE)，您可以自由使用、修改和分发。

---

 联系我们 📬

如果您有任何问题或建议，欢迎通过 GitHub Issues 或电子邮件与我们联系。

---

感谢使用 VPS-Boost-Panel，祝您网络性能飞跃提升！ 🌟
