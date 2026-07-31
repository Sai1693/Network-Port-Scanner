import socket
from datetime import datetime
import os


def validate_ip(ip):
    """
    Validate whether the given IP address is valid.
    """
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


def get_current_time():
    """
    Return current date and time.
    """
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def save_results(target, open_ports):
    """
    Save scan results to output/scan_results.txt
    """
    os.makedirs("output", exist_ok=True)

    filename = "output/scan_results.txt"

    with open(filename, "w") as file:
        file.write("NETWORK PORT SCANNER REPORT\n")
        file.write("=" * 40 + "\n")
        file.write(f"Target IP : {target}\n")
        file.write(f"Scan Time : {get_current_time()}\n\n")

        if open_ports:
            file.write("Open Ports:\n")
            for port in open_ports:
                file.write(f"Port {port} - OPEN\n")
        else:
            file.write("No open ports found.\n")

    return filename
