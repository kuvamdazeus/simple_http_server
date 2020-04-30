#! /usr/bin/env python3
import subprocess as sb
import http.server
import socketserver
import sys

default_port = 8080
# defining a simple HTTP request handler, handles requests over HTTP
handler = http.server.SimpleHTTPRequestHandler
try:
    tcp_server = socketserver.TCPServer(("", default_port), handler) # deploying server
except Exception:
    print("\nServer failed to start, please ensure that the website is not opened on your machine or any other, if so, close the tabs and try again\n")
    sys.exit(1)

def get_ip_address(): # gets ip address but the command runs only in unix based OS's (hope so!)
    try:
        result = sb.run(["ipconfig", "getifaddr", "en0"], capture_output = True)
        return result.stdout.decode().strip() # extracts text from the captured ip address
    except Exception: # if command failed to run, this exception is the life saver
        return "localhost:8080/home.html"

def main(): # main function does all required things to bring our new tcp_server on track and running
    print("Website: http://{}:{}/home.html".format(get_ip_address(), default_port))
    print("Server active")
    tcp_server.serve_forever() # runs the server

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt: # saves screen from filling with a long stderr message due to pressing of ctrl-c
        print("\nServer closed\n")
