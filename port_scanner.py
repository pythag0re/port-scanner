#!/usr/bin/env python3

import socket
import argparse

def scan_port(target, port, timeout):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0
    except Exception:
        return False

def main():
    parser = argparse.ArgumentParser(description="Port scanner by pythag0re")
    parser.add_argument("target", help="ip ou ndd")
    parser.add_argument("--start", type=int, default=1, help="port de debut")
    parser.add_argument("--end", type=int, default=1024, help="port de fin")
    parser.add_argument("--timeout", type=float, default=0.5, help="timeout")

    args = parser.parse_args()

    print(f"Scan de {args.target} ({args.start}-{args.end})")

    open_ports = []
    for port in range(args.start, args.end + 1):
        if scan_port(args.target, port, args.timeout):
            print(f"OPEN Port {port}")
            open_ports.append(port)

    print("\nINFO terminé")
    print(f"ports ouverts : {open_ports}")

if __name__ == "__main__":
    main()
