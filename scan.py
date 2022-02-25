import socket


def Scan(ip):
    ports = [443, 80, 8080, 8000, 3000, 445, 9050, 21, 19, 23, 22, 8081]
    open_ports = []
    open_ports.clear()
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                s.connect((ip, port))
                open_ports.append(port)
        except:
            pass
    if len(open_ports) == 0:
        return 'All ports are closed :('
    else:
        return open_ports
