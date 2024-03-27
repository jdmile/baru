import socket
import common_ports

def get_open_ports(target, port_range, verbose=False):
    try:
        ip_address = socket.gethostbyname(target)
    except socket.gaierror:
        return "Error: Invalid hostname"
    except ValueError:
        try:
            socket.inet_aton(target)
            ip_address = target
        except socket.error:
            return "Error: Invalid IP address"

    open_ports = []

    for port in range(port_range[0], port_range[1]+1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((ip_address, port))
            if result == 0:
                open_ports.append(port)

    if verbose:
        output = f"Open ports for {target} ({ip_address})\nPORT     SERVICE\n"
        for port in open_ports:
            service = common_ports.ports_and_services.get(port, "unknown")
            output += f"{port:<9}{service}\n"
        return output
    else:
        return open_ports
