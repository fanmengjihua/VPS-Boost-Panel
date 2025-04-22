import subprocess

def enable_bbr():
    cmds = [
        "modprobe tcp_bbr",
        "echo 'tcp_bbr' >> /etc/modules-load.d/modules.conf",
        "sysctl -w net.core.default_qdisc=fq",
        "sysctl -w net.ipv4.tcp_congestion_control=bbr",
        "sysctl -p"
    ]
    for cmd in cmds:
        subprocess.run(cmd, shell=True)

def check_bbr_status():
    return subprocess.getoutput("sysctl net.ipv4.tcp_congestion_control")