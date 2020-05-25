#! /usr/bin/env python3
"""Note: This server uses 8080 as default port"""
import http.server, sys, socketserver, socket, re

args = sys.argv
args.pop(0)
args = " ".join(args)
port_pattern, address_pattern = r"([0-9]+)", r"(^[a-zA-Z][0-9a-zA-Z\.\-_]+)"
# searching for patterns in args (argv) list
server_address = re.search(address_pattern, args)
port = re.search(port_pattern, args)
# default values
default_port = 8080
address = ""
# change values if needed
if server_address != None:
    address = server_address.group(1)
if port != None:
    default_port = int(port.group(1).strip())
print("Listening on port", default_port)
# defining a simple HTTP request handler, handles requests over HTTP
handler = http.server.SimpleHTTPRequestHandler
try:
    tcp_server = socketserver.TCPServer((address, default_port), handler, bind_and_activate=True) # deploying server
except Exception as error:
    message = str(error)
    if "already in use" in message:
        print("\nServer failed to start, please ensure that the website is not opened on your machine or any other, if so, close the tabs and try again\n")
    else:
        print("Error message:", message)
    sys.exit(1)

def get_ip_address():
    ip = socket.gethostbyname(socket.gethostname())
    return ip

def main(): # main function does all required things to bring our new tcp_server on track and running
    print("Website: http://{}:{}/".format(get_ip_address(), default_port))
    print("Server active")
    serve_forever = tcp_server.serve_forever() # runs the server
    print(serve_forever)
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt: # saves screen from filling with a long stderr message due to pressing of ctrl-c
        print("\nServer closed\n")
