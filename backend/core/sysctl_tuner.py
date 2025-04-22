import subprocess

def optimize():
    conf = """
net.core.rmem_max=67108864
net.core.wmem_max=67108864
net.ipv4.tcp_rmem=4096 87380 67108864
net.ipv4.tcp_wmem=4096 65536 67108864
net.core.netdev_max_backlog=250000
net.core.somaxconn=65535
    """
    with open("/etc/sysctl.d/99-vps-boost.conf", "w") as f:
        f.write(conf)
    subprocess.run("sysctl --system", shell=True)