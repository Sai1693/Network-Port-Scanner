import socket
import threading

from banner import show_banner
from utils import validate_ip, save_results

open_ports = []
lock = threading.Lock()


def scan_port(target, port):
    """
    Scan a single TCP port.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target, port))

        if result == 0:
            with lock:
                print(f"[OPEN] Port {port}")
                open_ports.append(port)

        sock.close()

    except:
        pass


def main():

    show_banner()

    target = input("Enter Target IP Address: ").strip()

    if not validate_ip(target):
        print("\nInvalid IP Address!")
        return

    print("\nScanning ports 1 - 1024 ...\n")

    threads = []

    for port in range(1, 1025):
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("\n==============================")
    print("Scan Completed")
    print("==============================")

    if open_ports:
        print(f"\nTotal Open Ports : {len(open_ports)}")
    else:
        print("\nNo Open Ports Found.")

    filename = save_results(target, sorted(open_ports))

    print(f"\nReport Saved : {filename}")


if __name__ == "__main__":
    main()
