#! /usr/bin/env python3
import subprocess as sb
import http.server
import socketserver

default_port = 8080
handler = http.server.SimpleHTTPRequestHandler
tcp_server = socketserver.TCPServer(("", default_port), handler)

def get_ip_address():
    try:
        result = sb.run(["ipconfig", "getifaddr", "en0"], capture_output = True)
        return result.stdout.decode().strip()
    except Exception:
        return "localhost:8080/home.html"

def main():
    print("Website: http://{}:{}/home.html".format(get_ip_address(), default_port))
    print("Server active")
    tcp_server.serve_forever()

if __name__ == "__main__":
    main()
