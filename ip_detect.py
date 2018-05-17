# coding=utf-8
def detect_ip():
    """获取内外网ip和获取时间"""
    # 获取内网IP
    import socket
    localIP = socket.gethostbyname(socket.gethostname())

    # 获取外网IP
    from urllib.request import urlopen
    externalIP = urlopen('http://ip.42.pl/raw').read()
    externalIP = externalIP.decode()

    # 获取系统时间
    import time
    localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    filename = "C:/Users/DA/Desktop/IP监控.txt"
    with open(filename, 'a') as fj:
        fj.write("DetectTime: %s, localIP: %s, ExternalIP: %s\n" %
                 (localtime, localIP, externalIP))


detect_ip()
