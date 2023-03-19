## This server/code belongs to Rohit
import socket
from threading import Thread
import webbrowser
import sys
import os
import socketserver
import http.server

# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print('Welcome to my Server!!')
        print("Enter 'exit' to shutdown!!")
        print("[+] New server socket thread started for Client IP:" + ip + " Port: " + str(port))

    def run(self):
        while True:
            data = conn.recv(2048)
            info = 'info'
            send = 'send'
            help = 'help'
            webpage = 'html'
            google = 'google'
            local_host = 'localhost'
            received = str(data.decode())
            delimit_num = received.find('#')
            if delimit_num != -1:
                c_hostname = received[:delimit_num-1]
                received = received[delimit_num+1:]
            if c_hostname:
                print('Client Hostname: ',c_hostname)
                c_hostname = None

            print("Client " + str(port) + " message: ", received)
            if help in received:
                response = "Instructions:\nType 'help' to get the commands\nType 'info' to get Server info\nType 'google' to access Google\nType 'send' with filename to request a file\nType 'send index.html' to access local webpage\nType 'exit' to shutdown\n"
                conn.send(response.encode())
                continue
            elif received == info:
                var1 = str(sock_family) +'#'+ str(sock_type) +'#'+str(sock_proto)+'#'+str(sock_timeout)
                conn.send(bytes(var1.encode()))
                continue
            # Localhost access to client (Not working)
            #elif local_host in received:
            #    PORT2 = 8080
            #    Handler = http.server.SimpleHTTPRequestHandler
            #    httpd = socketserver.TCPServer(("", PORT2), Handler)
            #    print("Server at PORT : ", PORT2)
            #    try:
            #        httpd.settimeout(10)  # timout for 20 secs coz server running in same thread
            #        httpd.serve_forever()

            #    except:
            #        print('Timeout!')
            #        break

            elif send in received:
                filename = received[5:]
                if webpage in filename:
                    # Open the html file requested by client
                    try:
                        webbrowser.open('file://' + os.path.realpath(filename))
                        response = 'HTTP/1.0 200 OK\n\n'

                    except FileNotFoundError:
                        response = 'HTTP/1.0 404 NOT FOUND\nFile Not Found'

                    conn.send(response.encode())
                    continue
                # Read file from server and display on the client
                else:
                    try:
                        fin = open('./' + filename)
                        content = fin.read()
                        fin.close()

                        response = 'HTTP/1.0 200 OK\n\n' + content
                    except FileNotFoundError:
                        response = 'HTTP/1.0 404 NOT FOUND\nFile Not Found'
                    conn.send(response.encode())
                    continue
            elif received == google:
                try:
                    webbrowser.open('http:google.com')  # Go to google.com
                    response = 'HTTP/1.0 200 OK\n\n'

                except FileNotFoundError:
                    response = 'HTTP/1.0 404 NOT FOUND\nFile Not Found'

                conn.send(response.encode())
                continue
            

            MESSAGE = input("Server : Enter Response from Server:")
            if MESSAGE == 'exit':
                break
                sys.exit(0)
            conn.send(MESSAGE.encode())  # echo


# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '0.0.0.0'
TCP_PORT = 8000
BUFFER_SIZE = 20  # Usually 1024, but we need quick response

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
sock_family = tcpServer.family
sock_type = tcpServer.type
sock_proto = tcpServer.proto
sock_timeout = tcpServer.timeout
threads = []
s_hostname = socket.gethostname()

print("Server : Waiting for connections from TCP clients...")
while True:
    try:
        tcpServer.settimeout(300)     #Server will run for 5 minutes
        tcpServer.listen(5)
        (conn, (ip, port)) = tcpServer.accept()
        newthread = ClientThread(ip, port)
        newthread.start()
        threads.append(newthread)
    # Exception for timeout
    except:
        print('Timeout!')
        break

for t in threads:
    t.join()


