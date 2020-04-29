import http.server
import socketserver

handler = http.server.SimpleRequestHandler
tcp_server = socketserver.TCPServer(("", 8000), handler)

tcp_server.server_forever()
